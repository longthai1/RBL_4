# **PROPOSAL**

# **Slide 1 – Title & Group**

## **Research Proposal**

### **Evaluating GPT-4o Zero-Shot Prompting for Automated Behavior-Driven Development Acceptance Test Generation from Agile User Stories**

**Thành viên**

* Đào Thiên Thành  
* Lương Thiện Nhất  
* Thái Thành Long

### **Script**

Kính chào Thầy/Cô và các bạn.

Nhóm em xin trình bày đề cương nghiên cứu với đề tài **"Evaluating GPT-4o Zero-Shot Prompting for Automated Behavior-Driven Development Acceptance Test Generation from Agile User Stories."**

Nghiên cứu được xây dựng dựa trên phương pháp của **Karpurapu et al. (IEEE Access, 2024\)** và mở rộng bằng việc đánh giá **GPT-4o sử dụng Zero-Shot Prompting**, đồng thời bổ sung **BLEU Score** để đo mức độ tương đồng giữa Gherkin được sinh và Gherkin tham chiếu.

---

# **Slide 2 – Problem Statement**

## **Background**

Behavior-Driven Development (BDD) là phương pháp kiểm thử Agile giúp tăng sự cộng tác giữa

* Business Analyst  
* Developer  
* Tester

thông qua các Acceptance Test được viết bằng ngôn ngữ **Gherkin (Given – When – Then).**

---

## **Problem**

Theo **Karpurapu et al. (2024)**,

việc xây dựng BDD Acceptance Test thủ công:

* tốn nhiều thời gian,  
* phụ thuộc vào kinh nghiệm của Tester,  
* khó chuẩn hóa giữa các nhóm Agile.

Do đó cần sử dụng **Large Language Models (LLMs)** để tự động sinh Acceptance Test.

---

## **State of the Art**

Karpurapu et al. đánh giá

* GPT-3.5  
* GPT-4  
* Llama-2-13B  
* PaLM-2

kết hợp

* Zero-shot Prompting  
* Few-shot Prompting

để sinh BDD Acceptance Test.

Kết quả:

* GPT-3.5 và GPT-4 đạt Validation Accuracy cao nhất.  
* Few-shot tốt hơn Zero-shot.

---

## **GAP-T (Technology Gap)**

Nghiên cứu **chưa đánh giá GPT-4o**.

Chưa biết GPT-4o Zero-Shot có thể sinh BDD Acceptance Test với chất lượng tương đương hoặc tốt hơn GPT-4 hay không.

---

## **GAP-M (Method Gap)**

Paper chỉ sử dụng

* Validation Accuracy  
* Syntax Errors

để đánh giá.

Chưa sử dụng **BLEU Score** để đo mức độ tương đồng giữa Gherkin được sinh và Gherkin tham chiếu.

---

### **Script**

BDD đang được sử dụng rộng rãi trong phát triển phần mềm Agile, tuy nhiên việc xây dựng Acceptance Test thủ công vẫn mất nhiều thời gian và phụ thuộc vào kinh nghiệm của người kiểm thử.

Karpurapu và cộng sự đã chứng minh LLM có khả năng hỗ trợ sinh BDD Acceptance Test tự động nhưng mới chỉ đánh giá GPT-3.5, GPT-4, Llama-2 và PaLM-2.

Ngoài ra, nghiên cứu chưa đánh giá GPT-4o và chưa sử dụng BLEU Score để đo mức độ tương đồng giữa kết quả sinh và Gherkin tham chiếu. Đây chính là khoảng trống nghiên cứu mà đề tài hướng tới.

---

# **Slide 3 – Related Work (Evidence Table)**

| Paper | LLM / Phương pháp | Metric | Kết quả chính |
| ----- | ----- | ----- | ----- |
| **Karpurapu et al. (2024)** | GPT-3.5, GPT-4, Llama-2, PaLM-2 | Validation Accuracy, Syntax Errors | GPT-3.5 và GPT-4 tốt nhất; Few-shot vượt Zero-shot |
| Ferreira et al. (2025) | GPT-4 Turbo | Acceptance Test Quality | Đánh giá bằng chuyên gia |
| Fonseca et al. (2025) | AToMIC \+ LLM | Syntax Correctness | Khoảng 93% đúng cú pháp |
| Fernandes et al. (2025) | GPT-4o Mini, Gemini, Llama | Correctness, Consistency | So sánh nhiều LLM nhưng dataset nhỏ |
| Mathur et al. (2023) | GPT-3 \+ T5 | Test Generation Accuracy | Tự động sinh test nhưng còn lỗi |
| Lafi et al. (2021) | NLP \+ CFG | Test Path Coverage | Coverage còn hạn chế |
| Guo et al. (2022) | WGAN-GP | Test Coverage | Cải thiện Unit Test Coverage |
| Utting et al. (2020) | Machine Learning | Test Identification | Nghiên cứu sơ bộ |
| Potuzak & Lipka (2023) | Literature Survey | Review | Tổng quan Automated Test Generation |
| Farooq et al. (2023) | Systematic Review | Qualitative Analysis | Tổng quan BDD |

---

## **Kết luận**

* Phần lớn nghiên cứu tập trung vào tự động sinh Test Case bằng Machine Learning hoặc LLM.  
* GPT-3.5 và GPT-4 đạt kết quả tốt nhất.  
* Few-shot Prompting thường hiệu quả hơn Zero-shot.  
* Các nghiên cứu chủ yếu sử dụng Validation Accuracy hoặc Syntax Errors.  
* **Chưa có nghiên cứu đánh giá GPT-4o Zero-Shot bằng BLEU Score**, đây là khoảng trống nghiên cứu của đề tài.

---

## **Slide 4 – Research Questions & Hypotheses**

**Main RQ:**  

Liệu GPT-4o sử dụng chiến lược **Zero-Shot Prompting** có sinh được Gherkin Acceptance Test từ User Stories đạt chất lượng ngữ nghĩa và cú pháp theo ngưỡng chuẩn hay không?

**RQ1 (Semantic):**  

GPT-4o Zero-Shot có đạt BLEU Score ≥ 0.70 so với Ground Truth không?

* H01:μBLEU\<0.70  
* H11:μBLEU≥0.70  
* **Test:** One-Sample Wilcoxon Signed-Rank Test (α \= 0.05)

**RQ2 (Syntax):**  

GPT-4o Zero-Shot có đạt Syntax Correctness ≥ 90% không?

* H02:psyntax\<0.90  
* H12:psyntax≥0.90  
* **Test:** Binomial Exact Test (α \= 0.05)

**RQ3 (Comparison – Optional Extension):**  

Nếu mở rộng thêm Few-Shot hoặc Chain-of-Thought, có sự khác biệt có ý nghĩa thống kê không?

* *Ngữ nghĩa:* Paired Wilcoxon Test (H03:Median(ΔBLEU)=0)  
* *Cú pháp:* McNemar’s Test (H04:Kho^ngcoˊsựkhaˊcbiệttỷlệ)

**Script (60 giây):**  

"Chúng em đặt ra 3 câu hỏi nghiên cứu. RQ1 đánh giá BLEU Score của GPT-4o Zero-Shot với ngưỡng 0.70 bằng phép kiểm Wilcoxon một mẫu. RQ2 đánh giá tỷ lệ đúng cú pháp với ngưỡng 90% bằng Binomial Exact Test. RQ3, nếu mở rộng thêm các kỹ thuật khác, sẽ tiến hành so sánh đối chứng bằng Paired Wilcoxon cho ngữ nghĩa và McNemar cho cú pháp. Nhóm cũng báo cáo kích cỡ hiệu ứng để minh họa sự khác biệt thực tế."

---

## **✅ Slide 5 – Experimental Pipeline** 

**Experimental Pipeline**  

Agile User Stories (\~50)

→ GPT-4o Zero-Shot Prompting (Temp \= 0, Top\_p \= 1\)

→ Generated Gherkin (.feature)

→ Gherkin-Lint \+ Behave Parser → Syntax Correctness (%)

→ BLEU Score (NLTK)

→ One-Sample Wilcoxon \+ Binomial Exact Test (α \= 0.05)

→ Research Conclusion

**Dataset**

* **Nguồn:**  
  * Mendeley Requirement Dataset  
  * Public Agile User Stories (Parabol Blog)  
* **Quy mô:** \~50 User Stories, đa miền (Healthcare, Banking, E-commerce, Education, …)

**Model Configuration**

* **Model:** GPT-4o (OpenAI)  
* **Prompt Strategy:** Zero-Shot Prompting  
* **Generation Parameters:**  
  * Temperature \= 0  
  * Top\_p \= 1  
  * Max Tokens \= 1024  
* **Output:** Gherkin Acceptance Test (.feature)  
* **Execution:** Deterministic (1 User Story → 1 Gherkin Scenario)

**Evaluation Metrics**

* BLEU Score ≥ 0.70  
* Syntax Correctness ≥ 90%

**Statistical Tests**

* One-Sample Wilcoxon Signed-Rank Test  
* Binomial Exact Test  
* α \= 0.05

**Script (60 giây)**  

"Quy trình thực nghiệm bắt đầu bằng việc thu thập khoảng 50 Agile User Stories từ Mendeley Requirement Dataset và bộ User Stories công khai của Parabol. Các User Stories này được đưa vào GPT-4o với Zero-Shot Prompting để sinh Gherkin Scenario. Sau đó, nhóm kiểm tra cú pháp bằng Gherkin-Lint và Behave Parser để tính Syntax Correctness. Tiếp theo, BLEU Score được tính bằng thư viện NLTK để đo mức độ tương đồng ngữ nghĩa với Gherkin tham chiếu. Cuối cùng, nhóm sử dụng One-Sample Wilcoxon và Binomial Exact Test để trả lời các câu hỏi nghiên cứu."

## **✅ Slide 6 – Dataset & Model Configuration** 

**Dataset**

* **Nguồn:**  
  * Mendeley Requirement Dataset (User Stories)  
  * 45 User Story Examples (Parabol Blog)  
* **Dataset thực nghiệm:**  
  * Khoảng 50 Agile User Stories  
  * Đa miền: Healthcare, Banking, E-commerce, Education,…  
  * Theo phương pháp của Karpurapu et al. (2024)

**Model Configuration**

* **Model:** GPT-4o (OpenAI)  
* **Prompting Strategy:** Zero-Shot Prompting  
* **Generation Parameters:**  
  * Temperature \= 0  
  * Top\_p \= 1  
  * Max\_tokens \= 1024

**Evaluation Configuration**

* **Output:** Gherkin Scenario (.feature)  
* **Metrics:** BLEU Score (NLTK), Syntax Correctness (Gherkin-Lint \+ Behave Parser)

**Script trình bày (30 giây):**  

"Để đảm bảo tính khách quan và khả năng tái lập của nghiên cứu, nhóm sử dụng khoảng 50 Agile User Stories được tổng hợp từ Mendeley Requirement Dataset và bộ 45 User Story Examples của Parabol, tương tự phương pháp của Karpurapu và cộng sự năm 2024\. Mô hình thực nghiệm là GPT-4o kết hợp với Zero-Shot Prompting. Nhóm cấu hình Temperature bằng 0, Top\_p bằng 1 và Max Tokens là 1024 nhằm tạo ra kết quả sinh tất định và ổn định. Các Gherkin Scenario được sinh sẽ được đánh giá bằng BLEU Score và kiểm tra cú pháp bằng Gherkin-Lint cùng Behave Parser."

## **Slide 7 – Statistical Plan** 

**Bảng kiểm định thống kê:**

| Mục tiêu | Ngưỡng | Phép kiểm | Rationale |
| :---: | ----- | ----- | ----- |
| **Tương đồng ngữ nghĩa (RQ1)** | ≥ 0.70 | One-sample Wilcoxon | So sánh trung vị BLEU với ngưỡng chất lượng |
| **Cú pháp khả thi (RQ2)** | ≥ 90% | Binomial Exact Test | Kiểm định tỷ lệ PASS/FAIL trên tập Gherkin |
| **So sánh cặp ngữ nghĩa (RQ3)** | Đối chứng | Paired Wilcoxon | So sánh BLEU giữa các kỹ thuật prompt |
| **So sánh cặp cú pháp (RQ3)** | Đối chứng | McNemar’s Test | So sánh tỷ lệ cú pháp giữa các kỹ thuật |

**Kích cỡ hiệu ứng (Effect Size):**

* Rank-Biserial Correlation cho các phép kiểm Wilcoxon.  
* Tỷ lệ PASS/FAIL minh họa cho McNemar.

**Script (30 giây):**  

"Về kế hoạch phân tích thống kê, nhóm sử dụng phép kiểm Wilcoxon một mẫu để so sánh BLEU Score của GPT-4o với ngưỡng 0.70, và phép kiểm Binomial Exact Test để so sánh tỷ lệ cú pháp với ngưỡng 90%. Để so sánh chéo giữa các kỹ thuật prompt, nhóm áp dụng Paired Wilcoxon cho ngữ nghĩa và McNemar cho cú pháp. Ngoài ra, nhóm cũng báo cáo chỉ số Rank-Biserial Correlation để đo kích cỡ hiệu ứng thực tế."

## **✅ Slide 8 – Threats to Validity** 

**Bảng Threats to Validity:**

| Loại | Câu hỏi cốt lõi | Ví dụ Threat | Mitigation (hành động cụ thể) |
| :---: | ----- | ----- | ----- |
| **Internal Validity** | Kết quả có thực sự do intervention không? | Model version drift (cloud LLM), annotation bias | Pin version GPT-4o, log model version; double annotation \+ tính IAA Kappa ≥ 0.7 |
| **External Validity** | Kết quả có generalize ra ngoài dataset không? | Dataset chỉ 1 domain, không đại diện | Dùng nhiều domain (Healthcare, Banking, E-commerce, Education); pilot \+ full run |
| **Construct Validity** | Metric có đo đúng cái muốn đo không? | BLEU không đo semantic meaning đầy đủ | Kết hợp BLEU với Syntax Correctness; báo cáo hạn chế metric trong §7 |
| **Conclusion Validity** | Statistical power có đủ không? | N nhỏ, sub-group thiếu power | Tối thiểu 50 User Stories; pilot kiểm tra power; báo cáo effect size (Rank-Biserial) |

**Script (30 giây):**  

"Trong phần Threats to Validity, nhóm phân tích bốn loại chính. Internal Validity có thể bị ảnh hưởng bởi việc OpenAI cập nhật model, do đó nhóm pin version và log lại. External Validity được xử lý bằng cách chọn dataset đa miền thay vì một domain duy nhất. Construct Validity được giảm thiểu bằng cách kết hợp BLEU với Syntax Correctness và ghi rõ hạn chế metric. Cuối cùng, Conclusion Validity được đảm bảo bằng cách dùng tối thiểu 50 User Stories, kiểm tra power qua pilot và báo cáo thêm effect size."

## **Slide 9 – Timeline & Resources** 

**Phân công vai trò (Roles):**

| Role | Trách nhiệm |
| :---: | ----- |
| **long** | Điều phối tiến độ, review, submit GV |
| **long** | Thu thập dataset, tạo ground truth, viết §3 |
| **thanh** | Setup API, chạy experiment, log output |
| **Thanh** | Implement metric, chạy statistical tests, tính effect size |
| **Nhat** | Viết intro/conclusion/threats, tạo figures, format document |

**Resource Inventory:**

* ✅ Dataset: Mendeley \+ Parabol (đã tải thử, đa miền)  
* ✅ API key: GPT-4o (free tier, log calls/day)  
* ✅ Compute: Colab T4 / Kaggle P100 / local backup  
* ⚠️ Ground Truth: cần annotation thủ công (ước tính X giờ × Y người)

**Timeline (Tuần 5–10):**

| Tuần | Hoạt động | Output |
| :---: | ----- | ----- |
| **5–6** | Viết proposal \+ chuẩn bị dataset | Draft §2–§7, `data/raw/` |
| **7** | Pilot run (10–20% sample) | `pilot_ground_truth.csv`, `pilot_llm_output.csv` |
| **8** | Full run | `full_llm_output.csv`, `full_analysis.ipynb` |
| **9–10** | Viết paper \+ present | Final report, figures |

**Script (30 giây):**  

"Trong phần Timeline & Resources, nhóm phân công rõ vai trò: PL điều phối, DG xử lý dataset và ground truth, LR chạy LLM, MS phân tích thống kê, RW viết báo cáo. Dataset đã được tải thử từ Mendeley và Parabol, API key GPT-4o và compute Colab/Kaggle đã sẵn sàng. Tuần 7 nhóm chạy pilot 10–20% sample để kiểm tra pipeline, tuần 8 chạy full run, và tuần 9–10 hoàn thiện báo cáo cùng phần trình bày."

## **✅ Slide 10 – Expected Contribution (20–30 giây)**

**Đóng góp dự kiến của nghiên cứu:**

* **Khoa học (Academic):**  
  * Bổ sung đánh giá **GPT-4o Zero-Shot Prompting** cho bài toán User Story → Gherkin Scenario.  
  * Đưa vào **BLEU Score** như một metric ngữ nghĩa mới, chưa từng được dùng trong các nghiên cứu trước.  
  * Cung cấp pipeline chuẩn hóa, có thể tái lập cho cộng đồng nghiên cứu.  
* **Thực tiễn (Practical):**  
  * Giảm thời gian viết Acceptance Test thủ công trong Agile.  
  * Chuẩn hóa cú pháp Gherkin, giảm lỗi syntax.  
  * Tăng khả năng áp dụng LLM vào quy trình BDD thực tế.

**Script (20–30 giây):**  

"Đề tài của chúng em kỳ vọng đóng góp hai mặt. Về khoa học, nghiên cứu sẽ là đánh giá đầu tiên về GPT-4o Zero-Shot Prompting trong bài toán User Story sang Gherkin, đồng thời bổ sung BLEU Score như một metric ngữ nghĩa mới. Về thực tiễn, nghiên cứu giúp giảm thời gian viết Acceptance Test thủ công, chuẩn hóa cú pháp Gherkin và mở rộng khả năng ứng dụng LLM trong quy trình Agile BDD."

