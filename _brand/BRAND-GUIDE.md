# Blue Coral — Brand & Document Guide

**Version 1.0.0 · Cập nhật 10/06/2026**
Mô hình: **House brand thống nhất** — một identity Blue Coral áp lên *mọi* deliverable (HTML, Excel, Word, PPTX), cho cả tài liệu nội bộ lẫn bàn giao client.

> **Nguyên tắc số 1:** Không bao giờ hard-code màu/hex hay thông tin công ty trong từng tài liệu. Mọi thứ đọc từ **`_brand/brand-tokens.json`** (single source of truth). Đổi 1 chỗ → tái sinh → mọi tài liệu đồng nhất.

---

## 1. Nhận diện công ty

| Trường | Giá trị |
|---|---|
| Brand (mặt tiền) | **Blue Coral** |
| Pháp nhân | CÔNG TY TNHH ADNS |
| MST | 0313209465 |
| Email | nguyen@bluecoral.vn |
| Footer chuẩn | `Blue Coral · CÔNG TY TNHH ADNS · MST 0313209465 · nguyen@bluecoral.vn` |
| Tagline (DRAFT) | "Triển khai Dữ liệu & Marketing" — *xác nhận hoặc thay* |

Blue Coral là tên client-facing; ADNS là pháp nhân trên hợp đồng/báo giá. Logo placeholder hiện tại là chữ **"BC"** trên nền trắng bo góc — thay bằng file logo thật khi có.

---

## 2. Bảng màu — "Trust Blue + Coral"

**Primary (Trust Blue — Royal, hướng Samsung Blue `#1428A0`)** — màu chủ đạo: tin cậy, hiện đại, premium.
`900 #060B3D · 800 #0B1566 · 700 #0E1E78 (dark) · 600 #1428A0 (base) · 500 #2540BE · 300 #8094E0 · 200 #AEBCEC · 100 #DCE3F7 · 50 #EFF2FC`

> **Blue sâu = đơn giản:** `600 #1428A0` phục vụ **mọi vai trò ở mức AAA** — nền chữ trắng (11.41), chữ trên nền sáng / link / KPI (11.41), badge trên `100` (8.89). **Không cần** phân vai shade. `700/800` cho gradient sâu & nền đậm; `500` vivid cho điểm nhấn lớn; `100` cho nền chip/badge.

**Accent (Coral)** — điểm nhấn, phase divider, badge nổi bật. Dùng **tiết chế** (~10% diện tích).
`700 #D8463A · 600 #FF6B5C (base) · 400 #FF8E82 · 100 #FFE7E3 · ink #97271C`

> **Luật cứng về coral** (đã đo WCAG):
> 1. **KHÔNG** đặt chữ trắng lên coral đặc — tương phản chỉ 2.80 (fail). Coral chỉ dùng *trang trí*.
> 2. **KHÔNG** dùng coral cho trạng thái/status — `danger` giữ `bad #C0392B` để tách khỏi họ đỏ (tránh badge accent bị đọc nhầm là lỗi).
> 3. Chữ trên nền `coral-100` phải dùng **`accent-ink #97271C`** (AA 6.78), không dùng `700` (3.66, fail chữ nhỏ).

**Neutral** (cool slate ngả indigo, tối giản kiểu Samsung) — `ink #15192B · ink2 #2E3447 · muted #5B6173 · line #DEE1EA · bg #F6F7FC · card #FFFFFF · fill #EFF1F8`

**Semantic** — `good #1F8A5B · warn #B47514 · bad #C0392B · info #1C6FB8` (mỗi màu có biến `_bg` nhạt + `_ink` đậm).

**Extra** — `gold #C9A227` cho nhãn premium/highlight, dùng rất hạn chế.

**Tỷ lệ dùng màu (60-30-10):** 60% neutral (bg/card/ink) · 30% primary · 10% accent + semantic.

---

## 3. Typography

- **Web:** system stack `-apple-system, "Segoe UI", Inter, Roboto, …` (sans). Mono: `ui-monospace, "SF Mono", Menlo, …`.
- **Office (docx/pptx/xlsx):** **Calibri** (đồng nhất cross-platform, khớp pipeline hiện có).
- **Thang cỡ (web px):** display 32 · h1 26 · h2 21 · h3 17 · h4 13(uppercase) · body 15.5 · small 13.5 · caption 11.5.
- **Office (pt):** title 22 · h1 16 · h2 13 · h3 11.5 · body 11 · small 9.5.

---

## 4. Components chuẩn (HTML — xem `style-guide.html`)

| Component | Class | Dùng khi |
|---|---|---|
| Masthead | `.bc-masthead` | Header gradient mọi tài liệu |
| Card | `.bc-card` | Khối nội dung gom nhóm |
| Table | `.bc-table` + `tr.bc-phase` / `tr.bc-total` | Bảng dữ liệu, báo giá, timeline |
| Callout | `.bc-callout .info/.good/.warn/.bad` | Lưu ý, khuyến nghị, rủi ro |
| Badge | `.bc-badge .primary/.accent/.good/...` | Trạng thái, nhãn |
| KPI card | `.bc-kpis > .bc-kpi` | Chỉ số nổi bật |
| Phase band | `.bc-phase-band` | Phân chia giai đoạn |
| Recommendation | `.bc-options > .bc-option.bc-pick` + `.bc-recommend` | **2 phương án + 1 khuyến nghị** (chuẩn house) |
| Footer | `.bc-footer` | Cuối mọi tài liệu |

---

## 5. Quy ước nội dung (house rules)

1. **Tiếng Việt** cho tài liệu client-facing (trừ thuật ngữ kỹ thuật).
2. **Khuyến nghị = đúng 2 phương án + 1 lựa chọn đề xuất** kèm lý do ngắn.
3. **M1 (mốc đầu) = Nền tảng/Foundation** trong mọi timeline/lộ trình.
4. **Họp tinh gọn** — không nhồi nhét nội dung thừa.
5. **Không icon/emoji** trong bảng Excel client-facing.
6. **Không hàng mô tả ở row 2** của Excel — vào thẳng dữ liệu.
7. Mọi tài liệu kết bằng **footer chuẩn** (mục 1).

---

## 6. Quy ước Excel (xem `excel` trong brandkit.py)

- Title row: nền `primary-600 #1428A0`, chữ trắng đậm size 14, merge full width.
- Header row: nền `primary-100`, viền dưới `primary-600`, freeze panes.
- **Phase divider row:** nền coral `#FFE7E3`, chữ `#97271C` đậm, merge full width.
- Body: viền `line`, số/tiền canh phải, format `#,##0`.
- Total row: nền `fill`, viền trên `primary-600`, đậm.

---

## 7. Cách dùng → xem `README.md`

Mọi format đọc chung `brand-tokens.json`. HTML qua `brand.css`; Office qua `brandkit.py`.
Đổi brand: sửa token → chạy lại script sinh tài liệu.

---

## 8. Quy ước sản xuất tài liệu (đủ để làm báo giá / Excel / Word)

**Ngôn ngữ & định dạng**
- Ngôn ngữ: **tiếng Việt** (client-facing). Tiền tệ mặc định **VND**, format `#,##0` (vd `62.000.000`); nếu USD ghi rõ `$` và tỷ giá quy đổi (mặc định 27.000 VND/USD).
- Ngày: **dd/mm/yyyy**. Khoảng thời gian: `dd/mm – dd/mm/yyyy`.
- Số %: 1 chữ số thập phân khi cần (vd `3.2×`, `67%`).

**Đặt tên file** — `[Client] - [Loại tài liệu] - vX.Y.[ext]`
vd `Ambrosia - Bao gia trien khai - v1.0.xlsx`, `VLU - De xuat SEO - v2.1.docx`.

**Cấu trúc báo giá / đề xuất chuẩn** (Excel hoặc Word)
1. Masthead/Title (brand + tên client + ngày + version)
2. Tóm tắt phạm vi (1 đoạn)
3. Bảng hạng mục theo **phase** (M1 = Nền tảng), cột: Hạng mục · Mô tả · Ngày công · Chi phí
4. Dòng **Tổng cộng**
5. Khối **2 phương án + 1 khuyến nghị** (nếu có lựa chọn)
6. Điều khoản/giả định ngắn gọn
7. **Footer chuẩn** (brand + pháp nhân + MST + email)

**Checklist trước khi bàn giao**
- [ ] Màu/format lấy từ token (không hard-code)
- [ ] Footer chuẩn có đủ pháp nhân + MST
- [ ] Tiền VND `#,##0`, canh phải · Ngày dd/mm/yyyy
- [ ] M1 = Nền tảng · phase chia rõ
- [ ] Khuyến nghị đúng 2 phương án
- [ ] Không icon/emoji trong Excel · không hàng mô tả row 2

---

## 9. Lịch sử phiên bản

- **v1.2.1** (15/06/2026) — Đổi email liên hệ sang **nguyen@bluecoral.vn** (bỏ admin@valotech.org). Giữ nguyên pháp nhân ADNS + MST.
- **v1.2.0** (11/06/2026) — Primary đổi sang **Trust Blue (Royal #1428A0, hướng Samsung)**: tin cậy/hiện đại/premium; base phục vụ mọi vai trò AAA. Neutral chuyển cool slate ngả indigo. Thêm mục Quy ước sản xuất.
- **v1.1.0** (11/06/2026) — Primary Azure Ocean Blue (đã thay).
- **v1.0.1** (10/06/2026) — Luật cứng về coral + accent-ink #97271C.
- **v1.0.0** (10/06/2026) — Khởi tạo (teal Deep Ocean + Coral).
