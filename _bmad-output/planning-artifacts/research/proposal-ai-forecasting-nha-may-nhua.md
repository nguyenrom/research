# AI Forecasting cho Nhà máy Sản xuất Nhựa

**Đề xuất Giải pháp Tổng quan**

---

## Bối cảnh

Nhà máy nhựa đang vận hành trên SAP nhưng phần lớn vẫn dự báo bằng spreadsheet và điều chỉnh tay. Kết quả: tồn kho resin dư khi giá giảm, thiếu hàng khi đơn tăng đột biến, phế phẩm phát hiện muộn, và downtime ngoài kế hoạch ảnh hưởng trực tiếp đến biên lợi nhuận.

Thị trường AI trong manufacturing đang bùng nổ ($7.6B năm 2025 → $128B năm 2034), 98% nhà sản xuất đang khám phá AI nhưng chỉ 20% sẵn sàng triển khai. **Hiện không có giải pháp AI demand forecasting nào chuyên biệt cho nhà máy nhựa trên SAP** — đây là khoảng trống thị trường lớn nhất.

---

## Giải pháp AI Forecasting — 8 Trụ cột

### 1. Dự báo Nhu cầu (Demand Forecasting)

Xây dựng mô hình dự báo sản lượng cần sản xuất dựa trên **biến số đặc thù ngành nhựa** — không chỉ dữ liệu bán hàng đơn thuần:

- **Khách hàng:** Lịch sử đơn hàng, hợp đồng dài hạn vs đơn lẻ, lead time yêu cầu
- **Mùa vụ:** Chu kỳ tiêu thụ bao bì, mùa xây dựng (ống nhựa), Tết
- **Khả năng sản xuất:** Công suất máy, lịch bảo trì, tỷ lệ phế phẩm
- **Thị trường:** Xu hướng ngành, chính sách môi trường, cạnh tranh

| Chỉ số | Kỳ vọng |
|--------|---------|
| Cải thiện forecast accuracy | 20-50% |
| ROI | 150-250% |
| Payback | 6-14 tháng |

---

### 2. Dự đoán Chất lượng & Giảm Phế phẩm

Tỷ lệ phế phẩm (scrap) trong nhà máy nhựa có thể vượt 20%. AI phân tích real-time nhiệt độ, áp suất, độ nhớt vật liệu để **cảnh báo trước khi tạo batch lỗi**, thay vì phát hiện khi đã sản xuất xong.

| Chỉ số | Kỳ vọng |
|--------|---------|
| Giảm scrap | 25% |
| Tiết kiệm | 6 chữ số/năm |
| Thời gian thấy kết quả | **2-4 tháng** (nhanh nhất trong tất cả use cases) |

---

### 3. Tối ưu Lịch trình Sản xuất (Production Scheduling)

Injection molding và extrusion có dependencies phức tạp: thay khuôn, chuyển vật liệu, nhiệt độ chuyển đổi. AI tối ưu scheduling để tránh:

- Máy idle chờ nguyên liệu hoặc khuôn
- Changeover kéo dài không cần thiết
- Giao hàng trễ do lập lịch thủ công

| Chỉ số | Kỳ vọng |
|--------|---------|
| Cải thiện OEE | 15% |
| Giảm unplanned downtime | 30% |
| Giảm lead times | 10% |

---

### 4. Dự báo Giá Nguyên liệu

Giá resin (PE, PP, PS, PVC, PET) biến động mạnh theo giá dầu và supply chain toàn cầu. Mua sai thời điểm có thể tốn hàng triệu đô. AI dự báo xu hướng giá để **tối ưu thời điểm mua hàng và quản lý hợp đồng**.

| Chỉ số | Kỳ vọng |
|--------|---------|
| Giảm chi phí mua hàng | ~20% |
| Cải thiện quản lý tồn kho nguyên liệu | 30% |

---

### 5. Bảo trì Dự đoán (Predictive Maintenance)

Downtime ngoài kế hoạch trên máy injection molding, extruder gây thiệt hại trung bình **$2,500/giờ**. Một sự cố lớn có thể tốn $45,000. AI phân tích dữ liệu vận hành máy để dự đoán hỏng hóc **trước khi xảy ra**.

| Chỉ số | Kỳ vọng |
|--------|---------|
| Giảm unplanned downtime | 50% trong 6 tháng |
| ROI | Ngăn 2 sự cố lớn/năm = cover toàn bộ chi phí hệ thống |

---

### 6. Tối ưu Tồn kho (Inventory Optimization)

AI cân bằng giữa đủ hàng giao và không giữ tồn kho dư thừa, giải phóng vốn lưu động bị đọng trong kho.

| Chỉ số | Kỳ vọng |
|--------|---------|
| Giảm mức tồn kho | 10-25% |
| Giảm chi phí lưu kho | 15-30% |
| Giảm stockouts | 20-50% |

---

### 7. Tối ưu Năng lượng (Energy Optimization)

Sản xuất nhựa tiêu tốn nhiều năng lượng cho gia nhiệt, làm mát, khí nén, thủy lực — chiếm 5-10% chi phí sản xuất. AI dynamic adjustments giúp giảm tiêu thụ mà không ảnh hưởng chất lượng.

| Chỉ số | Kỳ vọng |
|--------|---------|
| Giảm chi phí năng lượng | 25-30% |

---

### 8. Trợ lý AI Tương tác (AI Assistant)

Bên cạnh các mô hình dự báo chạy nền, hệ thống cung cấp một lớp **tương tác chủ động** cho đội ngũ quản lý:

- **Tra cứu nhanh** về tiến độ sản xuất, trạng thái đơn hàng, mức tồn kho — bằng ngôn ngữ tự nhiên
- **Trợ lý xử lý thông tin** quản lý trên hệ thống: tổng hợp báo cáo, cảnh báo bất thường, đề xuất hành động
- **What-if scenarios** — "Nếu đơn hàng X tăng 30% tháng sau thì cần bao nhiêu resin PP?"

---

## Tuân thủ Quy định & EPR

Giải pháp tích hợp sẵn khả năng hỗ trợ tuân thủ:

| Quy định | Tác động | Cách AI hỗ trợ |
|----------|----------|----------------|
| **EPR nhựa Việt Nam** (từ 2026) | Quota tái chế, cấm túi nhựa không phân hủy | Tích hợp EPR cost tracking, dự báo chuyển đổi vật liệu |
| **Luật BVDLCN** (Luật 91/2025) | Bảo vệ dữ liệu cá nhân, phạt đến 5% doanh thu | Tách biệt dữ liệu cá nhân vs vận hành trong kiến trúc |
| **EU AI Act** (8/2026) | Phân loại AI theo rủi ro | Thiết kế AI dạng advisory (đề xuất cho người, không tự quyết định) |

**Biến compliance thành lợi thế cạnh tranh** — vendor nào tích hợp EPR vào forecast sẽ giúp nhà máy chủ động thay vì bị động trước quy định.

---

## Nguyên tắc Triển khai

- **Bổ sung, không thay thế** — AI layer nằm trên hệ thống SAP hiện tại, tiêu thụ dữ liệu đã có, không cần rip-and-replace
- **Bắt đầu nhỏ, chứng minh giá trị** — Pilot trên phạm vi hẹp với KPI rõ ràng trước khi mở rộng
- **Chạy song song** — AI forecast chạy cạnh quy trình hiện tại trong giai đoạn đầu, không disrupt vận hành
- **Augment con người** — AI đề xuất, con người quyết định. Đội planning dùng giao diện quen thuộc trên SAP

---

## Lộ trình Triển khai

### Phase 1: Discovery & Pilot (Tuần 1-12)

| Tuần | Hoạt động |
|------|-----------|
| 1-2 | Xác định mục tiêu, khảo sát dữ liệu hiện có trên SAP |
| 3-6 | Thu thập & chuẩn bị dữ liệu, kết nối hệ thống |
| 7-8 | Triển khai mô hình dự báo đầu tiên cho 5-10 SKU trọng điểm |
| 9-12 | Chạy song song, đo lường kết quả, báo cáo go/no-go |

**Chi phí pilot:** $25,000 - $75,000
**KPI go/no-go:** Forecast accuracy cải thiện ≥15%, tồn kho giảm ≥10%

### Phase 2: Model Development & Mở rộng (Tuần 13-24)

- Phát triển & tinh chỉnh model cho toàn bộ SKU portfolio
- Tích hợp thêm use cases: giảm scrap, bảo trì dự đoán
- Kết nối biến số nhựa (giá resin, scrap rates, mold cycles)

### Phase 3: Validation (Tuần 25-30)

- Validation toàn diện trên nhiều dây chuyền
- Đào tạo đội ngũ vận hành
- Compliance review

### Phase 4: Deployment (Tuần 31-36)

- Go-live tích hợp đầy đủ vào SAP
- Triển khai AI Assistant cho đội quản lý
- Monitoring & support

### Phase 5: Scale (Liên tục)

- Mở rộng sang các nhà máy/dây chuyền khác
- Thêm module: tối ưu năng lượng, EPR tracking
- Continuous model improvement

---

## Tổng quan ROI

| Use Case | Thời gian thấy kết quả | Impact chính |
|----------|------------------------|-------------|
| Giảm phế phẩm | 2-4 tháng | Giảm 25% scrap |
| Dự báo nhu cầu + Tồn kho | 3-6 tháng | ROI 150-250% |
| Bảo trì dự đoán | 3-6 tháng | Tự cover chi phí hệ thống |
| Tối ưu năng lượng | 3-6 tháng | Giảm 25-30% chi phí năng lượng |
| Dự báo giá nguyên liệu | 6-12 tháng | Giảm ~20% chi phí mua hàng |
| Tối ưu scheduling | 6-12 tháng | Cải thiện 15% OEE |

**Benchmark ngành:** Manufacturing AI đạt ROI trung bình 200% — cao nhất mọi ngành. Payback trung bình 6-14 tháng.

Mỗi 1 điểm OEE cải thiện trên dây chuyền $50M revenue = **$500K+/năm**.

---

## Bước tiếp theo

1. **Workshop khảo sát** (1 buổi) — Tìm hiểu dữ liệu SAP hiện có, pain points ưu tiên, KPI mong muốn
2. **Đề xuất Pilot chi tiết** — Phạm vi, SKU mục tiêu, timeline, chi phí, KPI go/no-go
3. **Kick-off Pilot** — Bắt đầu trong 2 tuần sau khi đồng ý

---

*Tài liệu đề xuất — Ngày 16/04/2026*
