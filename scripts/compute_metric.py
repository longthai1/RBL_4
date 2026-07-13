import pandas as pd

def main():
    df_truth = pd.read_csv("data/raw/pilot_sample.csv")
    df_output = pd.read_csv("results/pilot_llm_output.csv")

    # Kiểm tra cột ground truth
    print("Các cột trong pilot_sample.csv:", df_truth.columns.tolist())

    # Nếu có cột 'scenario' thì dùng, nếu không thì bỏ qua
    if "scenario" in df_truth.columns:
        y_true = df_truth["scenario"].astype(str).tolist()
        y_pred = df_output["GeneratedScenario"].astype(str).tolist()

        exact_matches = sum([1 for t, p in zip(y_true, y_pred) if t.strip() == p.strip()])
        accuracy = exact_matches / len(y_true)

        print("📊 Evaluation Results")
        print("---------------------")
        print(f"Total samples: {len(y_true)}")
        print(f"Exact matches: {exact_matches}")
        print(f"Accuracy: {accuracy:.2f}")
    else:
        print("⚠️ File pilot_sample.csv không có cột 'scenario'.")
        print("Chỉ có thể xem output model trong results/pilot_llm_output.csv.")
        print("Bạn cần thêm ground truth (ví dụ cột 'scenario') để tính metric.")

if __name__ == "__main__":
    main()


import pandas as pd

def main():
    df_output = pd.read_csv("results/pilot_llm_output.csv")

    outputs = df_output["GeneratedScenario"].astype(str).tolist()

    # Độ dài trung bình
    lengths = [len(o.split()) for o in outputs]
    avg_length = sum(lengths) / len(lengths)

    print("📊 Output Analysis")
    print("------------------")
    print(f"Total samples: {len(outputs)}")
    print(f"Average length (words): {avg_length:.2f}")

    # Độ đa dạng token
    all_tokens = set()
    for o in outputs:
        all_tokens.update(o.lower().split())
    print(f"Unique tokens across outputs: {len(all_tokens)}")

if __name__ == "__main__":
    main()
