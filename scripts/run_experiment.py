import pandas as pd
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

def main():
    model_name = "google/flan-t5-small"  # nhẹ hơn base
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    df = pd.read_csv("data/raw/pilot_sample.csv")

    outputs = []
    for story in df["story"]:
        print("Đang xử lý:", story)
        inputs = tokenizer(
            f"Hãy viết Gherkin Scenario cho user story sau:\n{story}",
            return_tensors="pt"
        )
        outputs_ids = model.generate(**inputs, max_new_tokens=200)
        text = tokenizer.decode(outputs_ids[0], skip_special_tokens=True)
        outputs.append(text)

    df["GeneratedScenario"] = outputs
    df.to_csv("results/pilot_llm_output.csv", index=False, encoding="utf-8")
    print("✅ Đã lưu kết quả vào results/pilot_llm_output.csv")

if __name__ == "__main__":
    main()
