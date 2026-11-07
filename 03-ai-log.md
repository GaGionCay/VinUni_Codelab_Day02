# NHẬT KÝ TƯƠNG TÁC AI (AI INTERACTION LOG)
---

## 1. Tổng quan quá trình tương tác

Trong quá trình thực hiện bài tập tôi đã sử dụng AI làm người đồng hành để tư vấn kiến trúc hệ thống, debug lập trình và đóng gói hồ sơ dự án.

Quá trình tương tác của tôi trải qua các bước chính:
1. Đánh giá và lựa chọn 1 trong 3 đề tài bài toán.
2. Xây dựng sơ đồ quy trình hiện tại (Current-State Flow) và đề xuất Problem Statement (6-field).
3. Lập trình script `prompt_prototype.py` với thư viện Google GenAI SDK mới.
4. Đóng gói báo cáo kỹ thuật và nhật ký làm việc dưới dạng Markdown.

---

## 2. AI đã giúp ích gì cho tôi?

* **Định hướng chiến lược & Ra quyết định:** AI hỗ trợ tôi phân tích ưu/nhược điểm vận hành giữa các đề tài, giúp tôi chốt bài toán **Camera AI An ninh** nhờ tính thời gian thực (Real-time alert < 15 giây) và tác động trực tiếp đến an toàn khu đô thị.
* **Chuẩn hóa hồ sơ kỹ thuật:** AI giúp tôi dựng sơ đồ quy trình thủ công với các ký hiệu trực quan (🔴 Bottleneck, 🔄 Handoff, ⏱ Thời gian) và hoàn thiện 6 trường thông tin Problem Statement chuẩn báo cáo doanh nghiệp.
* **Tự động hóa & Sửa lỗi Code:** AI hướng dẫn tôi chuyển đổi sang SDK mới nhất (`google-genai`), thiết lập `types.GenerateContentConfig` và xử lý các lỗi runtime khi kết nối API.

---

## 3. Lỗi sai của AI và Cách tôi khắc phục

### a. AI nhầm lẫn vai trò khi đưa ra câu trả lời
* **Hiện tượng:** Khi yêu cầu phân tích lý do loại bỏ các đề tài, AI đã nhầm lẫn vai trò khi trả lời từ góc nhìn hạn chế nguồn lực của sinh viên ("do sinh viên không đủ thời gian", "do độ khó sinh viên chưa làm được") thay vì đánh giá chiến lược kỹ thuật.
* **Cách khắc phục của tôi:** Tôi đã khắc phục bằng cách **ghi rõ và siết chặt vai trò (Role Assignment) ngay trong câu lệnh (Prompt)**. Tôi yêu cầu AI phải đóng vai một **Trưởng nhóm AI Engineer / Software Architect chuyên nghiệp**, phân tích dựa trên rủi ro ảo giác (Hallucination), tính chất xử lý Real-time vs Offline và rủi ro vận hành của doanh nghiệp.

### b. Nhầm lẫn về mặt logic mốc thời gian (24/7 vs 5 phút)
* **Hiện tượng:** Tôi phát hiện điểm bất hợp lý khi hệ thống giám sát 24/7 nhưng Bước 1 trong sơ đồ lại tốn ⏱ 5 phút.
* **Cách xử lý:** Tôi đã đặt câu hỏi chất vấn AI. AI sau đó giải thích rõ sự khác biệt giữa **Thời gian túc trực hệ thống (24/7)** và **Độ trễ phát hiện sự cố của con người (5 phút)** do suy giảm tập trung, giúp tôi làm rõ bản chất Bottleneck trong báo cáo.

---

## 4. Cách tôi tinh chỉnh Prompt & Ranh giới an toàn (Guardrails)

1. **Gán vai trò rõ ràng (Role Prompting):** Luôn bắt đầu prompt bằng việc quy định rõ góc nhìn và chuyên môn của AI (ví dụ: *"Hãy đóng vai trò là Trưởng nhóm AI Engineer..."*).
2. **Cung cấp mẫu chuẩn (Few-Shot Prompting):** Tôi đã đưa ra các đoạn văn mẫu (Card #4, Card #6) để định hình cho AI viết lại lý do chọn/bỏ bài toán theo phong cách cô đọng, đi thẳng vào rủi ro và giá trị vận hành.
---

## 5. Bài học cá nhân rút ra

* Việc đặt vai trò (Role) và bối cảnh (Context) rõ ràng ở đầu prompt là yếu tố quyết định để AI trả về câu trả lời đúng tầm vóc và tư duy kỹ thuật.
* Không thụ động tiếp nhận kết quả của AI; việc đặt câu hỏi chất vấn khi phát hiện điểm vô lý giúp hoàn thiện sản phẩm chuẩn xác hơn.
* Luôn sàng lọc và kiểm chứng thông tin do AI đưa ra.