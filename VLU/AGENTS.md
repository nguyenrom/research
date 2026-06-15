# Agent Instructions — VLU

## BƯỚC 0 — BẮT BUỘC trước mọi task

Đọc `_foundation/00-START-HERE.md` TRƯỚC khi tạo/sửa/phân tích bất cứ thứ gì.
Nó dẫn tới toàn bộ luật: `_foundation/RULES.md`, `BRAND.md`, `STRUCTURE.md`,
`TONE-OF-VOICE.md`, `GLOSSARY.md`, `DATA-SSOT.md`.

Thứ tự ưu tiên: **lệnh user > _foundation/RULES.md > context dự án > mặc định AI.**
Không tự ý lệch brand/thuật ngữ/cấu trúc — khác chuẩn thì hỏi 1 câu confirm trước.

## Dữ liệu Airtable

Khi message có Airtable URL (`https://airtable.com/app...`) và task cần dữ liệu, inspect trước
khi trả lời nghiệp vụ. Chạy từ folder `VLU/`:

```bash
python3 scripts/airtable_inspect.py "<AIRTABLE_URL>" --max-records 100 --format json
```

- Không bịa dữ liệu, không hỏi user copy rows tay, không nhận token qua chat.
- Token scope tối thiểu `schema.bases:read` + `data.records:read`, để ở `VLU/.env`.
- Chi tiết quy tắc central-line: `_foundation/DATA-SSOT.md`.
