# 🏗️ Phase 3 — DEEP-DIVE (Nhóm)
## Quyết định lựa chọn Bài toán & Lý do đánh giá
Trong quá trình họp hội ý kỹ thuật (Deep-Dive Analysis), nhóm đã chọn ra được 1 bài toán có tính khả thi, hiệu quả vận hành và khả năng demo prototype trong khuôn khổ dự án:
**Bài toán 2:** Tự động phân tích camera thời gian thực phát hiện sự cố an ninh.
---

* **Lý do lựa chọn:**
  * **Tính thực tiễn & Cấp thiết thời gian thực (Real-time Value):** Việc giám sát camera an ninh đại đô thị đòi hỏi tốc độ phản ứng tính bằng giây. Chuyển từ giám sát bị động (con người trực màn hình dễ xao nhãng) sang cảnh báo chủ động thời gian thực giải quyết đúng điểm đau lớn nhất của BQL Vinhomes.
  * **Kiểm soát rủi ro triệt để qua HITL:** AI chỉ thực hiện nhiệm vụ khoanh vùng bất thường và bắn Popup cảnh báo về phòng trực; nhân viên an ninh con người luôn xác thực (Verify) trước khi điều động lực lượng.

---

### ❌ Lý do loại bỏ các bài toán còn lại:

* **Loại bỏ Bài toán 1 (Tự động phân tích camera thời gian thực phát hiện sự cố an ninh):** Mặc dù tra cứu tài liệu tốn thời gian nhưng rủi ro LLM bị ảo giác (hallucination) trích xuất sai quy trình an toàn điện/PCCC có thể dẫn đến sự cố kỹ thuật nghiêm trọng hoặc tai nạn lao động. Bài toán đòi hỏi khâu số hóa/parsing bản vẽ CAD/BIM phức tạp, cần gom thêm dữ liệu chuẩn hóa và thử nghiệm kỹ cơ chế RAG trước khi triển khai.
* **Loại bỏ Bài toán 3 (Lập lịch bảo dưỡng & Sức khỏe Pin Xanh SM):**  Đây là tác vụ phân tích batch/offline (back-office background job) phụ thuộc nặng vào dữ liệu lịch sử telemetry dài hạn, không ảnh hưởng trực tiếp đến hiệu suất vận hành thời gian thực (real-time) như việc phát hiện nguy cơ an ninh hay ứng cứu sự cố tức thì tại khu đô thị.

---
## 3.1. Current-State Workflow Mapping
Sơ đồ: Tự động phân tích camera thời gian thực phát hiện sự cố an ninh
Đơn vị: Vinhomes (Khối An ninh & An toàn KĐT)
```
┌──────────────┐      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│ Bước 1       │      │ Bước 2       │      │ Bước 3       │      │ Bước 4       │
│ Giám sát màn │      │ Quan sát &   │ 🔄  │ Truy xuất vị │ 🔄   │ Gọi bộ đàm   │
│ hình camera  │ ───► │ xác định bất │ ───► │ trí camera & │ ───► │ điều động    │
│ 24/7         │      │ thường       │      │ bản đồ khu   │      │ tuần tra     │
│ Ai: Bảo vệ   │      │ Ai: Bảo vệ   │      │ Ai: Bảo vệ   │      │ Ai: Bảo vệ   │
│ ⏱ 5 phút 🔴 │      │ ⏱ 3 phút 🔴 │      │ ⏱ 2 phút    │      │ ⏱ 2 phút     │
│ In: Luồng TV │      │ In: Hình ảnh │      │ In: Mã Cam   │      │ In: Vị trí   │
│ Out: Phát hiện│     │ Out: Xác nhận│      │ Out: Tọa độ  │      │ Out: Lệnh đàm│
└──────────────┘      └──────────────┘      └──────────────┘      └──────────────┘
                                                                         │
                                                                         ▼
                                                                  ┌──────────────┐
                                                                  │ Bước 5       │
                                                                  │ Tiếp cận     │
                                                                  │ hiện trường  │
                                                                  │ Ai: Tuần tra │
                                                                  │ ⏱ 3 phút     │
                                                                  └──────────────┘

🔴 = Bottlenecks (Tắc nghẽn / Bỏ sót cao)
🔄 = Handoff (Điểm chuyển giao giữa Bảo vệ trực màn hình và Đội tuần tra)
⏱ Tổng thời gian xử lý thủ công: 15 phút/lượt sự cố.
```
## 3.2. Problem Statement (6-field) & Metrics

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Nhân viên an ninh trực phòng trung tâm (Monitoring Guard) và Đội tuần tra cơ động ngoại khu Vinhomes. |
| **2. Current Workflow** | Giám sát hàng chục đến hàng trăm màn hình camera 24/7 bằng mắt thường $\rightarrow$ Phát hiện sự cố thủ công (đột nhập hàng rào, té ngã, tụ tập gây rối, khói lửa) $\rightarrow$ Dùng bộ đàm gọi báo cho đội tuần tra $\rightarrow$ Đội tuần tra di chuyển tới hiện trường xác minh. |
| **3. Bottleneck** | **Bước giám sát và phát hiện sự cố thủ công:** Con người dễ bị suy giảm tập trung sau 20-30 phút giám sát liên tục, dẫn đến độ trễ phát hiện sự cố lớn (từ 5 đến 10 phút), dễ bỏ sót các góc khuất hoặc sự cố diễn ra chớp nhoáng ban đêm. |
| **4. Business Impact** | Thời gian phản ứng với sự cố an ninh khẩn cấp chậm; rủi ro mất cắp tài sản, tai nạn hoặc sự cố cháy nổ lan rộng; ảnh hưởng trực tiếp đến cam kết chất lượng dịch vụ (SLA) an toàn và uy tín thương hiệu Vinhomes. |
| **5. Success Metric** | • Rút ngắn thời gian phát hiện cảnh báo từ 10 phút xuống **dưới 15 giây** (Real-time alert).<br>• Giảm **90%** các sự cố an ninh bị bỏ sót do yếu tố con người mệt mỏi.<br>• Kiểm soát tỷ lệ cảnh báo giả (False Positive Rate) dưới 15% nhờ thuật toán lọc nhiễu. |
| **6. Operational Boundary** | **AI ĐƯỢC PHÉP:** Phân tích luồng video thời gian thực (Computer Vision), tự động khoanh vùng đối tượng (Bounding Box), phát hiện bất thường và bắn popup cảnh báo kèm âm thanh về màn hình phòng trực an ninh.<br>**TUYỆT ĐỐI KHÔNG:** Tự động phát loa phóng thanh toàn khu đô thị gây hoảng loạn khi chưa xác thực, hoặc tự động kích hoạt các biện pháp khóa cổng/vũ lực tự động.<br>**ĐIỂM CẦN DUYỆT:** Nhân viên an ninh tại phòng trực bắt buộc phải quan sát video xác thực (Verify Alert) trước khi bấm nút điều phối đội tuần tra xử lý. |

---

## 3.3. Future-State Flow & AI Fit

- **Xác định mức AI Fit (AI-Fit Matrix):** `[x] Edge AI / Computer Vision Pipeline (YOLO Architecture)`
- **Sơ đồ Future-State Flow:**

```text
[Luồng Video Camera 24/7 (RTSP Stream)]
                   │
                   ▼
┌──────────────────────────────────────────────────────────────┐
│ 🔵 AI Step: Edge AI Server / CV Pipeline                     │
│ • Object Detection & Behavior Analysis (Xâm nhập, Khói lửa)  │
│ • Lọc nhiễu môi trường (lá cây rơi, ánh sáng thay đổi)        │
└──────────────────────────────────────────────────────────────┘
                   │
                   ├──────────────────────────────────────────┐
                   │ (Confidence Score ≥ 85%)                 │ (Score thấp / Nhiễu)
                   ▼                                          ▼
┌──────────────────────────────────────┐   ┌─────────────────────────────────────┐
│ 🟢 Human Step (HITL - Dashboard):    │   │ ↩️ Fallback:                        │
│ • Popup cảnh báo hiển thị tại phòng  │   │ • Hệ thống ghi nhận vào log ẩn,     │
│   trực trung tâm kèm video snippet   │   │   không làm phiền nhân viên trực    │
│ • Nhân viên an ninh bấm "Xác nhận"   │   │   để tránh tình trạng "Alert Fatigue"│
└──────────────────────────────────────┘   ┌─────────────────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│ 🟢 Human Step: Tự động điều phối     │
│ • Hệ thống ghim tọa độ GPS lên App   │
│   của Đội tuần tra cơ động gần nhất  │
└──────────────────────────────────────┘
```

---

# 🏁 Phase 5 — EVALUATE

### AI Readiness Checklist:
1. `[x]` **Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test?** *(Sử dụng các open-source dataset về an ninh/khói lửa như UCF-Crime, Roboflow Security datasets kết hợp dựng video mô phỏng môi trường đô thị cho đồ án).*
2. `[x]` **Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)?** *(Hoàn toàn kiểm soát được nhờ lớp nhân viên an ninh xác thực trước khi điều động lực lượng, tránh việc còi hú liên tục gây phiền toái).*
3. `[x]` **Stakeholders sẵn sàng thay đổi quy trình làm việc cũ?** *(Đội ngũ an ninh rất hoan nghênh vì giảm tải áp lực trực màn hình liên tục và hỗ trợ bảo vệ tài sản tốt hơn).*

---

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:

`[x] GO (Bắt đầu xây dựng Prototype)`

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
> **1. Bằng chứng Kỹ thuật (Technical Feasibility):** Các mô hình thị giác máy tính hiện đại như YOLO (v8/v10) kết hợp với các framework xử lý luồng video thời gian thực (như OpenCV / DeepStream) cho tốc độ xử lý khung hình (FPS) cực kỳ ấn tượng, hoàn toàn đáp ứng chạy mượt mà trên phần cứng cơ bản hoặc Google Colab / Local GPU cho mục đích dựng mô hình demo (Prototype).
> 
> **2. Hiệu quả Chi phí & Năng lực triển khai (Cost & Feasibility):** Đối với nhóm sinh viên, việc chọn 2 kịch bản trọng tâm (Ví dụ: **Phát hiện xâm nhập khu vực cấm ban đêm** và **Phát hiện khói lửa sớm**) giúp thu hẹp scope gọn gàng, dễ huấn luyện/tinh chỉnh mô hình (fine-tune) trong vòng 3-4 tuần, tạo ra sản phẩm trực quan có độ tương tác cao khi bảo vệ đề tài.
> 
> **3. Phạm vi PoC:** Xây dựng hệ thống Prototype nhận diện qua web app (Streamlit kết hợp OpenCV Stream) mô phỏng phòng trực an ninh thông minh của Vinhomes.
---