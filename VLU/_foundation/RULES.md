# RULES — Luật cứng của workspace VLU

> Nguồn luật gốc. `AGENTS.md` và `CLAUDE.md` ở gốc `VLU/` chỉ trỏ về đây.
> Sửa luật = sửa file này, rồi commit. Không rải luật ra nhiều nơi.

## R1. Đọc Foundation trước (BƯỚC 0)
Trước mọi task tạo/sửa tài liệu hoặc phân tích, AI phải đã đọc `_foundation/00-START-HERE.md`
và các file luật liên quan. Không bỏ qua vì task "trông đơn giản".

## R2. Kênh dữ liệu đồng bộ (tùy chọn)
- Bảng dữ liệu chung là **tùy chọn**. Nếu workspace có dùng, mọi danh sách/records/nội dung lấy từ
  kênh đồng bộ online (**Google Sheets** hoặc **Airtable**), không từ file Excel rời.
- Ưu tiên Airtable nếu cần chèn ảnh vào ô và theo dõi cập nhật chặt; Google Sheets nếu đã quen.
- Không hỏi user copy-paste dữ liệu thủ công. Không nhận token qua chat.
- Cách lấy dữ liệu và quy trình cập nhật content giữa các team: xem `_foundation/DATA-SSOT.md`.
- File Excel/slide/report chỉ là **snapshot kết xuất**: ghi rõ ngày lấy dữ liệu và số bản ghi.

## R3. Brand & format
- Tuân `_foundation/BRAND.md`. Không hard-code màu/hex tùy tiện.
- Tiền VND: `#,##0`. Ngày: `dd/mm/yyyy`. Ngôn ngữ tài liệu: tiếng Việt (trừ khi yêu cầu khác).

## R4. Thuật ngữ & ngữ điệu
- Dùng đúng từ trong `_foundation/GLOSSARY.md`. Gặp thuật ngữ mới → thêm vào glossary, đừng tự chế biến thể.
- Văn phong theo `_foundation/TONE-OF-VOICE.md`.

## R5. Cấu trúc & đặt tên
- Mỗi dự án = 1 folder. Tạo dự án mới từ `_foundation/init/project-template/`.
- Đặt tên file theo `_foundation/STRUCTURE.md`. Không để file rác ở gốc.

## R6. Tái lập (reproducibility)
- Excel → `python3` (openpyxl); Word → `.venv-docx`; PPTX → `.venv-pptx`.
- Mỗi deliverable build bằng script lưu trong `<dự-án>/scripts/`, không chỉnh tay sản phẩm cuối.

## R7. Bảo mật
- Secret (token, .env) **không bao giờ** vào Git, Markdown, hay chat. Đã gitignore `.env`, `token.md`.
- Token lộ ra (kể cả trong chat/log) thì **rotate ngay** ở dịch vụ tương ứng.

## Checklist TRƯỚC KHI giao deliverable
- [ ] Đã đọc foundation liên quan
- [ ] Nếu dùng kênh đồng bộ: dữ liệu lấy từ Sheets/Airtable (ghi rõ ngày + số bản ghi), không chép tay
- [ ] Đúng brand: màu/font/format số/ngày
- [ ] Đúng thuật ngữ (glossary) + ngữ điệu
- [ ] File đặt đúng folder, đúng quy ước tên
- [ ] Có script tái lập trong `scripts/`
- [ ] Không lộ secret
- [ ] Khuyến nghị (nếu có) trình bày: 2 phương án + 1 đề xuất
