# BÁO CÁO CHUYÊN SÂU (DEEP DIVE REPORT)

**Dự án:** Tự động hóa phân loại và định tuyến phản ánh cư dân tại Vinhomes qua ứng dụng di động.

**Phạm vi báo cáo:** Chỉ tập trung phân tích quy trình tiếp nhận, phân loại và định tuyến các ticket dạng văn bản tiếng Việt được gửi từ ứng dụng cư dân Vinhomes. Các kênh tiếp nhận khác như tổng đài thoại và phản ánh trực tiếp nằm ngoài phạm vi dự án.

---

## 1. Phát biểu bài toán 6 trường (Six-Field Problem Statement)

### 1.1. Actor / Operator (Tác nhân / Vận hành)

- **Cư dân:** Người gửi phản ánh thông qua ứng dụng di động.
- **Nhân viên CSKH trực ca:** Người tiếp nhận, kiểm tra nội dung và chuyển tiếp ticket đến bộ phận phụ trách theo quy trình thủ công.
- **Đội ngũ Kỹ thuật / Ban Quản lý khu đô thị:** Bộ phận tiếp nhận ticket cuối cùng để xử lý các sự cố được phản ánh.

### 1.2. Current Workflow (Quy trình hiện tại)

- **Bước 1:** Cư dân nhập nội dung phản ánh và gửi ticket thông qua ứng dụng di động.
- **Bước 2:** Hệ thống lưu ticket vào cơ sở dữ liệu CRM. Nhân viên CSKH định kỳ kiểm tra danh sách ticket mới (thời gian chờ: 15–30 phút).
- **Bước 3:** Nhân viên CSKH đọc và phân tích thủ công nội dung để xác định nhóm sự cố như Điện, Nước, Vệ sinh, An ninh... (thời gian xử lý: 3–5 phút/ticket).
- **Bước 4:** Nhân viên thực hiện thao tác định tuyến (routing) ticket đến phòng ban chuyên trách trên hệ thống CRM (thời gian xử lý: khoảng 2 phút/ticket).
- **Bước 5:** Bộ phận chuyên trách tiếp nhận ticket và bắt đầu xử lý sự cố (thời gian chờ: 1–2 giờ).

### 1.3. Bottleneck (Điểm nghẽn)

Điểm nghẽn chính nằm ở khâu tiếp nhận, đọc hiểu, phân loại và định tuyến ticket thủ công (Bước 2, 3 và 4).

Vào giờ cao điểm, lượng ticket tăng đột biến khiến nhân viên CSKH bị quá tải, dẫn đến thời gian chuyển tiếp kéo dài. Bên cạnh đó, tỷ lệ phân loại sai phòng ban ước tính khoảng 15–20% do quy trình phụ thuộc nhiều vào kinh nghiệm và đánh giá chủ quan của từng nhân viên.

### 1.4. Business Impact (Tác động kinh doanh)

- Gia tăng áp lực công việc và chi phí nhân sự cho đội ngũ CSKH trực ca.
- Kéo dài thời gian phản hồi ban đầu và chuyển tiếp thông tin đến bộ phận chuyên trách.
- Ảnh hưởng tiêu cực đến chỉ số hài lòng của cư dân (CSAT), đặc biệt đối với các sự cố hạ tầng quan trọng cần được xử lý kịp thời.

### 1.5. Success Metric (Chỉ số đo lường thành công)

**Baseline – Hiện trạng (số liệu ước tính, cần kiểm định qua PoC):**

- Thời gian từ khi gửi ticket đến khi hoàn tất định tuyến: khoảng 120 phút/ticket.
- Độ chính xác phân loại hiện tại: khoảng 80%.

**Target – Mục tiêu PoC:**

- Đối với ticket có confidence score ≥ 85% và không thuộc nhóm nhạy cảm: AI tự động phân loại và định tuyến đến bộ phận chuyên trách trong vòng dưới 2 phút kể từ khi hệ thống tiếp nhận ticket.
- Độ chính xác phân loại tự động đạt trên 90%, được đánh giá riêng trên nhóm ticket được AI tự động định tuyến.
- Ticket có confidence score < 85% hoặc thuộc nhóm nhạy cảm phải được chuyển qua hàng đợi kiểm duyệt thủ công. Các ticket này không thuộc phạm vi đo chỉ tiêu định tuyến tự động dưới 2 phút.

**Measurement Method & Pilot Period (Phương pháp đo lường và thời gian thử nghiệm):**

- Thu thập và phân tích dữ liệu thông qua hệ thống log CRM.
- Theo dõi các chỉ số hiệu suất hàng tuần trong suốt giai đoạn thử nghiệm 4 tuần tại một khu đô thị mẫu.

### 1.6. Operational Boundary (Ranh giới vận hành)

**AI được phép thực hiện:**

- Đọc hiểu nội dung phản ánh bằng tiếng Việt.
- Đề xuất nhãn phân loại phù hợp với nội dung ticket.
- Xác định mức độ ưu tiên xử lý (Khẩn cấp / Thông thường).
- Tự động định tuyến ticket đến bộ phận chuyên trách nếu điểm tin cậy đạt ngưỡng cho phép.

**AI không được phép thực hiện:**

- Tự động đóng hoặc từ chối ticket của cư dân.
- Đưa ra các cam kết liên quan đến bồi thường hoặc đền bù tài chính.
- Tự ý đưa ra quyết định xử lý đối với các trường hợp nhạy cảm vượt ngoài phạm vi được phê duyệt.

**Điểm bắt buộc có sự phê duyệt của con người:**

- Ticket có điểm tin cậy (confidence score) thấp hơn ngưỡng cấu hình phải được nhân viên CSKH kiểm duyệt trước khi định tuyến.
- Ticket liên quan đến an ninh khẩn cấp hoặc các trường hợp nhạy cảm phải được chuyển qua quy trình kiểm duyệt của nhân viên CSKH.

---

## 2. Đánh giá giải pháp AI và lý do lựa chọn (AI Fit and Rationale)

Ba phương án công nghệ đã được đưa ra để đánh giá mức độ phù hợp với bài toán:

### 2.1. Rules / State-Machine (Dựa trên từ khóa và luật cố định)

**Đánh giá: Không phù hợp để sử dụng làm giải pháp chính.**

Phương pháp này dựa trên các từ khóa và điều kiện được thiết lập trước. Tuy nhiên, nội dung phản ánh của cư dân thường đa dạng, sử dụng nhiều cách diễn đạt, tiếng lóng, từ viết tắt và không tuân theo một cấu trúc ngôn ngữ cố định.

Do đó, hệ thống dễ bỏ sót ngữ cảnh hoặc phân loại sai khi gặp những trường hợp diễn đạt không nằm trong bộ quy tắc đã định nghĩa.

### 2.2. Agentic Loop (Tác nhân AI tự trị nhiều bước)

**Đánh giá: Chưa phù hợp trong giai đoạn triển khai ban đầu.**

Mô hình Agentic Loop cho phép AI tự thực hiện nhiều bước suy luận và hành động liên tiếp. Tuy nhiên, việc trao quyền tự chủ quá lớn cho AI trong bài toán định tuyến ticket có thể làm gia tăng độ phức tạp và rủi ro vận hành, đặc biệt đối với các quyết định liên quan đến an ninh hoặc khiếu nại nhạy cảm.

Vì vậy, giải pháp này chưa thực sự cần thiết đối với phạm vi tự động hóa phân loại và định tuyến hiện tại.

### 2.3. LLM Feature / Text Classification (Mô hình ngôn ngữ lớn kết hợp phân loại văn bản)

**Đánh giá: Được lựa chọn làm giải pháp chính thức.**

Đây là phương án phù hợp nhất với bài toán nhờ khả năng xử lý ngôn ngữ tự nhiên (NLP), hiểu ngữ cảnh và nhận diện ý định phản ánh bằng tiếng Việt.

LLM có thể phân tích nội dung ticket và trả về kết quả có cấu trúc, bao gồm nhãn phân loại, mức độ ưu tiên và điểm tin cậy (confidence score). Những thông tin này là cơ sở để hệ thống quyết định tự động định tuyến hoặc chuyển ticket sang hàng đợi kiểm duyệt thủ công.

Giải pháp này vừa tận dụng được khả năng hiểu ngôn ngữ của AI, vừa duy trì cơ chế kiểm soát của con người đối với các quyết định quan trọng.

---

## 3. Quy trình tương lai, kiểm duyệt và dự phòng (Future-State Workflow, Review & Fallback)

### 3.1. Future-State Flow (Quy trình xử lý trong tương lai)

Quy trình tự động hóa dự kiến được triển khai theo luồng sau:

**Cư dân gửi ticket qua ứng dụng di động**

↓

**API Gateway tiếp nhận ticket và thực hiện kiểm tra, làm sạch dữ liệu cá nhân (PII)**

↓

**AI phân tích nội dung (Intent Classification & Priority Detection)**

↓

**Hệ thống đánh giá điểm tin cậy (Confidence Score)**

↓

**Kiểm tra điều kiện định tuyến và chuyển sang luồng xử lý tương ứng**

### 3.2. Human-in-the-Loop (Cơ chế kiểm duyệt có sự tham gia của con người)

Hệ thống áp dụng cơ chế Human-in-the-Loop nhằm đảm bảo các quyết định phân loại và định tuyến được kiểm soát phù hợp.

**Ngưỡng confidence score mặc định: 85%.**

**Trường hợp 1: Điểm tin cậy ≥ 85%**

- Hệ thống tự động gán nhãn phân loại và mức độ ưu tiên.
- Ticket được định tuyến trực tiếp đến bộ phận hoặc kỹ thuật viên chuyên trách.
- Mục tiêu hoàn tất định tuyến trong vòng dưới 2 phút kể từ thời điểm tiếp nhận ticket.

**Trường hợp 2: Điểm tin cậy < 85% hoặc thuộc nhóm nhạy cảm**

- Ticket được chuyển vào hàng đợi kiểm duyệt trực tuyến.
- Nhân viên CSKH kiểm tra nội dung, xác nhận hoặc ghi đè (override) kết quả phân loại của AI.
- Ticket chỉ được định tuyến sau khi có sự xác nhận của nhân viên CSKH.

Các trường hợp liên quan đến an ninh khẩn cấp và khiếu nại tài chính luôn phải được kiểm duyệt thủ công, không phụ thuộc vào confidence score.

**Cơ chế lưu trữ và cải tiến dữ liệu:**

Mọi thao tác xác nhận, chỉnh sửa hoặc ghi đè kết quả của nhân viên CSKH đều được lưu lại dưới dạng log vận hành. Đội ngũ kỹ thuật có thể sử dụng dữ liệu này để đánh giá các trường hợp AI phân loại sai, chuẩn hóa dữ liệu và cải tiến prompt hoặc mô hình định kỳ theo quy trình quản trị dữ liệu của công ty.

### 3.3. Operational Fallback (Phương án dự phòng vận hành)

Trong trường hợp API mô hình AI gặp sự cố như timeout, lỗi HTTP 500 hoặc mất kết nối, hệ thống sẽ kích hoạt cơ chế dự phòng:

- Tạm ngừng luồng xử lý tự động bằng AI.
- Tự động chuyển toàn bộ ticket mới sang hàng đợi tiếp nhận thủ công theo quy trình truyền thống.
- Gửi cảnh báo sự cố đến kênh giám sát nội bộ của đội ngũ DevOps để kịp thời xử lý.
- Đảm bảo ticket vẫn được lưu trữ đầy đủ trong CRM, tránh thất lạc hoặc xử lý trùng lặp trong thời gian hệ thống AI gián đoạn.

---

## 4. Bảng kiểm độ sẵn sàng và quyết định (Readiness Checklist & Decision)

### 4.1. Readiness Checklist (Đánh giá mức độ sẵn sàng)

| Tiêu chí đánh giá | Trạng thái | Ghi chú và căn cứ thực tế |
|---|---|---|
| **Dữ liệu (Data Readiness)** | Sẵn sàng (Có điều kiện) | Đã có kho lưu trữ lịch sử ticket phản ánh trong 2 năm qua. Tuy nhiên, dữ liệu cần được rà soát, chuẩn hóa và gán nhãn lại trong giai đoạn chuẩn bị PoC. |
| **Hạ tầng (Infrastructure)** | Sẵn sàng | Hạ tầng Cloud tập trung của Vinhomes được giả định là đáp ứng yêu cầu triển khai mô hình dưới dạng Microservice API. Cần xác nhận năng lực tích hợp và tài nguyên thực tế trước khi triển khai. |
| **Quy trình và con người (Process & People)** | Chưa sẵn sàng | Đội ngũ CSKH chưa quen với giao diện kiểm duyệt ticket tích hợp AI. Cần tổ chức đào tạo và hướng dẫn sử dụng trước khi chạy thử nghiệm. |
| **Chi phí và hiệu quả đầu tư (Cost & ROI)** | Chưa kiểm chứng | Kỳ vọng giảm thời gian xử lý thủ công và tối ưu nguồn lực nhân sự. Tuy nhiên, chi phí triển khai, vận hành và ROI hiện vẫn là giả định, cần được đo lường thực tế sau giai đoạn thử nghiệm. |

### 4.2. Final Decision (Quyết định cuối cùng)

**Kết luận: NOT YET – Chưa sẵn sàng triển khai diện rộng.**

Đề xuất chuyển sang giai đoạn phê duyệt và triển khai thử nghiệm trong phạm vi hẹp (Proof of Concept – PoC).

**Lý do đưa ra quyết định:**

- Tiêu chí về quy trình và con người chưa đáp ứng yêu cầu triển khai thực tế.
- Các chỉ số về chi phí và hiệu quả đầu tư (ROI) vẫn đang ở mức giả định, chưa có dữ liệu thực nghiệm để xác nhận.
- Việc triển khai diện rộng ngay lập tức có thể tạo ra rủi ro vận hành nếu AI phân loại sai hoặc nhân viên CSKH chưa thích nghi với quy trình mới.

### 4.3. PoC Scope (Phạm vi thử nghiệm)

- **Thời gian:** 4 tuần.
- **Địa điểm:** 1 khu đô thị mẫu thuộc Vinhomes.
- **Phạm vi nghiệp vụ:** Tiếp nhận, phân loại và định tuyến ticket dạng văn bản tiếng Việt gửi từ ứng dụng cư dân.
- **Phương thức vận hành:** Kết hợp tự động hóa bằng AI và kiểm duyệt thủ công theo cơ chế Human-in-the-Loop.

### 4.4. Success Criteria (Tiêu chí đánh giá thành công)

PoC được xem là đạt yêu cầu khi đáp ứng các tiêu chí sau:

- Độ chính xác phân loại tự động đạt từ 90% trở lên đối với nhóm ticket đủ điều kiện tự động định tuyến.
- Thời gian hoàn tất định tuyến dưới 2 phút đối với ticket có confidence score ≥ 85% và không thuộc nhóm nhạy cảm.
- Ticket có confidence score < 85% hoặc thuộc nhóm nhạy cảm được chuyển đến hàng đợi kiểm duyệt thủ công trước khi định tuyến.
- Duy trì khả năng tiếp nhận và xử lý ticket ổn định trong suốt 4 tuần thử nghiệm.
- Ghi nhận riêng kết quả của luồng tự động và luồng kiểm duyệt thủ công để đánh giá hiệu quả PoC.

### 4.5. Stop / Expand Thresholds (Ngưỡng dừng hoặc mở rộng)

**Điều kiện dừng và đánh giá lại:**

- Tỷ lệ phân loại sai vượt quá 15%.
- Nhân viên CSKH không chấp nhận hoặc không thể sử dụng hiệu quả giao diện kiểm duyệt mới.
- Phát sinh các lỗi vận hành nghiêm trọng liên quan đến thất lạc ticket hoặc định tuyến sai các trường hợp nhạy cảm.

Trong trường hợp này, dự án sẽ tạm dừng để rà soát dữ liệu, điều chỉnh prompt hoặc mô hình và cải thiện quy trình vận hành.

**Điều kiện mở rộng:**

Nếu PoC đáp ứng các tiêu chí thành công, đảm bảo tính ổn định và nhận được sự chấp thuận từ đội ngũ vận hành, dự án sẽ được đề xuất mở rộng triển khai sang các khu đô thị khác trong hệ thống Vinhomes.

---

**Kết luận chung:**

Giải pháp ứng dụng LLM vào quy trình phân loại và định tuyến phản ánh cư dân có tiềm năng cải thiện đáng kể tốc độ xử lý ticket, giảm tải công việc thủ công cho đội ngũ CSKH và nâng cao chất lượng dịch vụ. Tuy nhiên, thay vì triển khai diện rộng ngay từ đầu, phương án phù hợp là thực hiện PoC có kiểm soát, đánh giá hiệu quả thực tế và hoàn thiện cơ chế Human-in-the-Loop trước khi mở rộng hệ thống.