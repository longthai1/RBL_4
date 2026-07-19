#!/usr/bin/env python3
"""Run the FLAN-T5 experiment with improved prompt and validation."""
from __future__ import annotations
import argparse, json, re, time
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

def strip_fences(text: str) -> str:
    if not text:
        return ""
    value = text.strip()
    value = re.sub(r"^```(?:gherkin|feature)?\s*", "", value, flags=re.IGNORECASE)
    value = re.sub(r"```$", "", value)
    return value.strip()

def validate_gherkin(text: str) -> tuple[bool, str]:
    if not isinstance(text, str) or not text.strip():
        return False, "empty_output"
    parser_note = "official_parser_pass"
    try:
        from gherkin.parser import Parser
        from gherkin.token_scanner import TokenScanner
        Parser().parse(TokenScanner(text))
    except ImportError:
        parser_note = "fallback_keyword_check_no_gherkin_package"
    except Exception as exc:
        return False, f"parser_error:{exc}"
    lines = [x.strip() for x in text.splitlines() if x.strip()]
    feature = sum(x.startswith("Feature:") for x in lines)
    scenario = sum(x.startswith("Scenario:") for x in lines)
    missing = [k for k in ("Given ", "When ", "Then ") if not any(x.startswith(k) for x in lines)]
    if feature != 1 or scenario != 1 or missing:
        return False, f"contract_error:feature={feature},scenario={scenario},missing={','.join(missing)}"
    return True, parser_note + "_and_contract_pass"

def call_flan_t5(prompt: str, model, tokenizer, max_new_tokens: int = 200) -> str:
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs_ids = model.generate(**inputs, max_new_tokens=max_new_tokens)
    return strip_fences(tokenizer.decode(outputs_ids[0], skip_special_tokens=True))

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--log", required=True)
    p.add_argument("--checkpoint-every", type=int, default=1)
    args = p.parse_args()

    model_name = "google/flan-t5-base"   # dùng bản base thay vì small
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    data = pd.read_csv(args.input)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.log).parent.mkdir(parents=True, exist_ok=True)
    Path("results/checkpoints").mkdir(parents=True, exist_ok=True)

    rows = []
    with Path(args.log).open("w", encoding="utf-8") as log:
        log.write(json.dumps({
            "event": "run_started",
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "provider": "flan_t5",
            "requested_model": model_name,
            "n": len(data),
            "input": args.input
        }, ensure_ascii=False) + "\n")

        for i, (_, row) in enumerate(data.iterrows(), start=1):
            started = time.perf_counter()
            ts = datetime.now(timezone.utc).isoformat()
            story = str(row.get("story", ""))

            # Prompt có ví dụ mẫu
            prompt = f"""Viết kịch bản Gherkin cho user story sau:
{story}

Ví dụ format:
Feature: Shopping Cart
  Scenario: Add item to cart
    Given the customer is logged in
    When the customer adds a product
    Then the product appears in the cart
"""

            try:
                generated = call_flan_t5(prompt, model, tokenizer)
                error = ""
            except Exception as exc:
                generated = ""
                error = str(exc)

            if not generated.strip() and not error:
                error = "empty_response"
            status = "INVALID" if not generated.strip() or error else "VALID"
            syntax_pass, syntax_detail = validate_gherkin(generated)

            result = {
                "story_id": row.get("story_id"),
                "story": story,
                "generated_gherkin": generated,
                "record_status": status,
                "syntax_pass": syntax_pass,
                "syntax_detail": syntax_detail,
                "run_mode": "FLAN_T5_LOCAL_RUN",
                "timestamp_utc": ts,
                "elapsed_ms": round((time.perf_counter() - started) * 1000, 2),
                "requested_model": model_name,
                "error": error
            }
            rows.append(result)
            log.write(json.dumps({"event": "call", **result}, ensure_ascii=False) + "\n")

            if i % args.checkpoint_every == 0:
                pd.DataFrame(rows).to_csv(args.output, index=False, encoding="utf-8-sig")
                pd.DataFrame(rows).to_csv(
                    Path("results/checkpoints") / (Path(args.output).stem + "_checkpoint.csv"),
                    index=False, encoding="utf-8-sig"
                )

        pd.DataFrame(rows).to_csv(args.output, index=False, encoding="utf-8-sig")
        log.write(json.dumps({
            "event": "run_finished",
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "rows": len(rows),
            "valid_rows": sum(r["record_status"] == "VALID" for r in rows),
            "invalid_rows": sum(r["record_status"] == "INVALID" for r in rows)
        }, ensure_ascii=False) + "\n")

    print(f"Completed {len(rows)} rows -> {args.output}")
    print(f"Run mode: {rows[0]['run_mode'] if rows else 'NO_ROWS'}")

if __name__ == "__main__":
    main()
