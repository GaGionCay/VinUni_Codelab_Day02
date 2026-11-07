# Lab 02 · Problem Scan và Quick Problem Cards

Bối cảnh bài lab là Vin Smart Future. Các pain point là giả thuyết để khảo sát, các ngưỡng là mục tiêu đề xuất. Nhóm chưa xác minh quy trình nội bộ hoặc hiệu năng thực tế của các đơn vị.

## Phase 1 · SCAN

| **#** | **Đơn vị** | **Lens** | **Bài toán và tác động cần kiểm chứng** |
|---|---|---|---|
| 1 | Xanh SM | Tốn thời gian | Khi tài xế báo xe sắp hết pin hoặc gặp sự cố trên đường, nhân viên điều phối phải tổng hợp mức pin, vị trí và khoảng cách đến trạm sạc để lựa chọn phương án hỗ trợ. Việc kiểm tra nhiều điều kiện thủ công có thể kéo dài thời gian phản hồi, đặc biệt với tình huống khẩn cấp. |
| 2 | VinFast | AI có thể tốt hơn | Kỹ thuật viên tại xưởng dịch vụ phải tra cứu tài liệu kỹ thuật, mã lỗi và lịch sử sửa chữa để xác định hướng kiểm tra khi xe xuất hiện triệu chứng bất thường. Thông tin phân tán ở nhiều tài liệu và cách mô tả triệu chứng không thống nhất có thể khiến việc tìm đúng hướng dẫn mất thời gian hoặc bỏ sót bước kiểm tra. |
| 3 | Vinschool | Pain từ người khác | Khi phụ huynh thay đổi người đón, lịch xe buýt hoặc đăng ký người đón thay, thông tin có thể được gửi qua nhiều kênh khác nhau. Bộ phận phụ trách phải đối chiếu và xác nhận lại để tránh sai lệch trong danh sách bàn giao học sinh cuối ngày. |
| 4 | Vinhomes | Lặp lại | Nhân viên chăm sóc cư dân phải đọc và phân loại các phản ánh về vệ sinh, an ninh, kỹ thuật, tiện ích và dịch vụ trước khi chuyển đến bộ phận phụ trách. Một phản ánh có thể chứa nhiều vấn đề hoặc không nêu rõ địa điểm, khiến nhân viên phải xác minh và phân loại lại. |
| 5 | Vinpearl | Pain từ người khác | Khách hàng thường cần xác nhận các điều kiện sử dụng dịch vụ như thời hạn vé, quyền lợi đi kèm, điều kiện đổi lịch hoặc quy định của từng khu vui chơi. Khi thông tin nằm ở nhiều chính sách và loại vé khác nhau, khách hàng có thể phải liên hệ nhân viên nhiều lần để xác nhận trước khi sử dụng dịch vụ. |

## Phase 2 · Card 1 · Hỗ trợ điều phối xử lý tình huống xe điện pin yếu tại Xanh SM

- **Actor** — Nhân viên điều phối vận hành Xanh SM.
- **Thành phần nhận kết quả** — Nhân viên điều phối và tài xế đang cần hỗ trợ.
- **Current workflow** — Tiếp nhận thông tin từ tài xế → kiểm tra mức pin và vị trí → xác định trạm sạc hoặc phương án hỗ trợ → đánh giá điều kiện an toàn → phản hồi phương án cho tài xế.
- **Bottleneck** — Nhân viên phải tổng hợp nhiều thông tin trước khi đưa ra phương án. Trường hợp pin quá thấp nhưng trạm sạc ở xa có thể cần chuyển sang phương án hỗ trợ khác. Thời gian xử lý từng bước cần được đo để xác định công đoạn gây chậm.
- **Điểm can thiệp** — AI phân tích mô tả sự cố, tổng hợp thông tin và đề xuất phương án xử lý. Các điều kiện an toàn quan trọng, chẳng hạn pin dưới 5% và trạm sạc cách trên 5 km, phải được kiểm tra bằng Rule-based. AI chỉ tạo bản nháp đề xuất, nhân viên điều phối phê duyệt trước khi thực hiện.
- **Metric đề xuất** — Giảm ≥30% thời gian xử lý trung bình mỗi tình huống; ≥90% đề xuất phân loại đúng trên bộ tình huống có nhãn; 100% tình huống vi phạm điều kiện pin và khoảng cách được chuyển sang phương án hỗ trợ phù hợp trong bộ kiểm thử.
- **Quick architecture** — LLM Feature kết hợp Rule-based Safety Check và Human-in-the-loop.

## Phase 2 · Card 2 · Trợ lý tra cứu và đề xuất quy trình chẩn đoán lỗi xe tại VinFast

- **Actor** — Kỹ thuật viên tại xưởng dịch vụ VinFast.
- **Thành phần nhận kết quả** — Kỹ thuật viên trực tiếp kiểm tra và sửa chữa xe.
- **Current workflow** — Tiếp nhận mô tả triệu chứng hoặc mã lỗi → xác định dòng xe và hệ thống liên quan → tra cứu tài liệu kỹ thuật → tìm quy trình kiểm tra tương ứng → thực hiện kiểm tra và ghi nhận kết quả.
- **Bottleneck** — Kỹ thuật viên có thể phải tìm kiếm qua nhiều tài liệu để xác định hướng dẫn phù hợp với dòng xe và mã lỗi. Triệu chứng do khách hàng mô tả cũng có thể không trùng với thuật ngữ trong tài liệu kỹ thuật, làm tăng thời gian tra cứu và nguy cơ chọn nhầm hướng dẫn.
- **Điểm can thiệp** — Xây dựng hệ thống RAG để tìm kiếm tài liệu kỹ thuật dựa trên mã lỗi, dòng xe và mô tả triệu chứng. LLM tổng hợp các bước kiểm tra liên quan, giải thích hướng dẫn và trích dẫn nguồn tài liệu. Kỹ thuật viên kiểm tra nội dung trước khi thực hiện, AI không tự kết luận nguyên nhân hỏng hóc hoặc chỉ định thay thế linh kiện.
- **Metric đề xuất** — ≥90% câu trả lời có trích dẫn đúng tài liệu tham chiếu trên bộ câu hỏi kiểm thử; giảm ≥25% thời gian tra cứu trung bình; 100% câu trả lời không tìm được nguồn phù hợp phải thông báo chưa đủ căn cứ thay vì tự suy đoán.
- **Quick architecture** — RAG kết hợp LLM Feature và Human-in-the-loop.

## Phase 2 · Card 3 · Đối chiếu thông tin thay đổi người đón và lịch xe buýt tại Vinschool

- **Actor** — Nhân viên phụ trách đưa đón học sinh và giáo viên chủ nhiệm.
- **Thành phần nhận kết quả** — Bộ phận quản lý đưa đón và nhân viên bàn giao học sinh cuối ngày.
- **Current workflow** — Tiếp nhận yêu cầu thay đổi từ phụ huynh → xác định học sinh và nội dung thay đổi → kiểm tra thông tin người đón hoặc tuyến xe → đối chiếu với danh sách hiện tại → xác nhận và cập nhật danh sách bàn giao.
- **Bottleneck** — Yêu cầu thay đổi có thể được gửi qua nhiều kênh và ở dạng nội dung tự do. Nhân viên phải xác định đúng học sinh, thời gian áp dụng và người được phép đón. Nếu thông tin thiếu hoặc mâu thuẫn với danh sách hiện tại, cần liên hệ xác minh lại trước khi cập nhật.
- **Điểm can thiệp** — LLM trích xuất thông tin từ nội dung yêu cầu thành các trường có cấu trúc như mã học sinh, ngày áp dụng, người đón và nội dung thay đổi. Rule-based kiểm tra trường bắt buộc, đối chiếu với danh sách được phê duyệt và phát hiện thông tin không khớp. Mọi thay đổi liên quan đến người đón phải được nhân viên có thẩm quyền xác minh và phê duyệt trước khi cập nhật.
- **Metric đề xuất** — ≥95% trường thông tin được trích xuất chính xác trên bộ yêu cầu có nhãn; giảm ≥25% thời gian đối chiếu mỗi yêu cầu; 100% yêu cầu thiếu xác nhận hoặc có thông tin không khớp được chuyển sang xử lý thủ công, không tự động cập nhật danh sách bàn giao.
- **Quick architecture** — LLM Information Extraction kết hợp Rule-based Validation và Human-in-the-loop.

## Đề xuất cá nhân trước buổi họp

Chọn Card 1 – Hỗ trợ điều phối xử lý tình huống xe điện pin yếu tại Xanh SM làm đề tài ưu tiên để phát triển sâu.

Lý do:

- Bài toán có quy trình vận hành tương đối rõ, đầu vào và đầu ra có thể mô tả cụ thể.
- Có thể kết hợp LLM với Rule-based để thể hiện rõ giới hạn của AI trong tình huống có ràng buộc an toàn.
- Có các tình huống kiểm thử đối kháng cụ thể, chẳng hạn pin dưới 5% nhưng trạm sạc gần nhất cách 8 km, hoặc người dùng yêu cầu bỏ qua quy tắc an toàn.
- Có thể triển khai prototype bằng Gemini 2.5 Flash theo starter code được cung cấp.
- Human-in-the-loop giúp phân định rõ AI chỉ đề xuất phương án, còn nhân viên điều phối chịu trách nhiệm phê duyệt và thực hiện.

Card 2 có tiềm năng phát triển thành hệ thống RAG chuyên ngành, có chiều sâu về truy xuất tài liệu và độ tin cậy của câu trả lời. Tuy nhiên, tính khả thi phụ thuộc nhiều vào việc có được tài liệu kỹ thuật và dữ liệu mã lỗi phù hợp hay không.

Card 3 có quy trình kiểm tra rõ ràng và có thể kết hợp LLM với Rule-based. Tuy nhiên, đây là bài toán liên quan đến an toàn học sinh và thông tin người được phép đón, do đó cần ranh giới phê duyệt của con người rất chặt chẽ.

Cả ba đề tài đều cần dữ liệu thực tế hoặc bộ dữ liệu mô phỏng có nhãn để đánh giá. Các chỉ số trên chỉ là mục tiêu đề xuất, chưa phải kết quả đo được của các đơn vị.
