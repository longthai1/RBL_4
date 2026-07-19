import pandas as pd
import numpy as np
from collections import Counter

def main():
    # Đọc file output
    df_output = pd.read_csv("results/pilot_llm_output.csv")

    outputs = df_output["GeneratedScenario"].astype(str).tolist()

    # Độ dài (số từ) của từng output
    lengths = [len(o.split()) for o in outputs]

    # Thống kê cơ bản
    avg_length = np.mean(lengths)
    min_length = np.min(lengths)
    max_length = np.max(lengths)
    median_length = np.median(lengths)
    std_length = np.std(lengths)

    # Token duy nhất
    all_tokens = []
    for o in outputs:
        all_tokens.extend(o.lower().split())
    vocab = set(all_tokens)
    vocab_size = len(vocab)

    # Tần suất token
    token_counts = Counter(all_tokens)
    most_common_tokens = token_counts.most_common(10)

    print("📊 Output Analysis")
    print("------------------")
    print(f"Total samples: {len(outputs)}")
    print(f"Average length (words): {avg_length:.2f}")
    print(f"Median length (words): {median_length:.2f}")
    print(f"Min length (words): {min_length}")
    print(f"Max length (words): {max_length}")
    print(f"Std deviation length: {std_length:.2f}")
    print(f"Unique tokens across outputs: {vocab_size}")
    print("\n🔝 Top 10 most frequent tokens:")
    for tok, freq in most_common_tokens:
        print(f"- {tok}: {freq}")

if __name__ == "__main__":
    main()
