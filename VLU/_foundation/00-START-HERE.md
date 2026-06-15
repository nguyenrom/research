# 00 — START HERE (AI đọc file này ĐẦU TIÊN)

> Đây là điểm vào của tầng Foundation. Bất kỳ AI nào (Claude, Codex, hoặc tool khác)
> làm việc trong `VLU/` **phải đọc hết file này trước khi tạo/sửa bất cứ thứ gì**.

## BƯỚC 0 — Bắt buộc trước mọi task

1. Đọc các file luật trong thứ tự sau:
   - `_foundation/RULES.md` — luật cứng + checklist trước khi giao việc
   - `_foundation/BRAND.md` — màu, font, logo, format số/ngày
   - `_foundation/STRUCTURE.md` — quy ước folder + đặt tên file
   - `_foundation/TONE-OF-VOICE.md` — ngữ điệu, văn phong
   - `_foundation/GLOSSARY.md` — thuật ngữ chuẩn (dùng đúng từ, không tự chế)
   - `_foundation/DATA-SSOT.md`: quy tắc kênh dữ liệu đồng bộ (tùy chọn)
2. Đọc context riêng của dự án đang làm: `<tên-dự-án>/README.md`.
3. Nếu task cần **dữ liệu cập nhật** (danh sách, records, nội dung) và workspace có kênh đồng bộ:
   KHÔNG tự tạo, KHÔNG hỏi user copy tay, chạy connector theo `DATA-SSOT.md`.

## Thứ tự ưu tiên khi có mâu thuẫn

```
Lệnh trực tiếp của user  >  _foundation/RULES.md  >  context dự án  >  mặc định của AI
```

Nếu lệnh user nghịch với foundation → **làm theo user, nhưng nói rõ một câu** rằng điều này
lệch chuẩn để user biết.

## Quy tắc vàng

- **Không tự ý lệch concept/brand/term.** Khác chuẩn → hỏi 1 câu confirm trước khi làm.
- **Một nguồn sự thật.** Dữ liệu sống ở Airtable; file chỉ là bản kết xuất (snapshot) tại 1 thời điểm.
- **Tái lập được.** Mọi deliverable phải kèm script/nguồn để người khác chạy lại ra cùng kết quả.

---
*Foundation version: v0.1 · cập nhật: chạy `_foundation/init/INIT-GUIDE.md` để chốt các mục `<CẦN CHỐT>`.*
