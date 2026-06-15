# VLU Project Instructions (Claude)

> Luật gốc nằm ở `AGENTS.md` + `_foundation/` (Claude và Codex dùng CHUNG một nguồn luật).
> File này chỉ trỏ về đó để không lệch giữa hai tool.

## BƯỚC 0 — BẮT BUỘC
Đọc `_foundation/00-START-HERE.md` trước mọi task, rồi `_foundation/RULES.md` và các file luật
liên quan (BRAND / STRUCTURE / TONE-OF-VOICE / GLOSSARY / DATA-SSOT).

Thứ tự ưu tiên: **lệnh user > _foundation/RULES.md > context dự án > mặc định AI.**
Không tự ý lệch brand/thuật ngữ/cấu trúc; khác chuẩn → hỏi confirm trước.

## Dữ liệu Airtable (central-line)
Task cần dữ liệu sống → lấy từ Airtable, không bịa/không copy tay/không token qua chat:

```bash
python3 scripts/airtable_inspect.py "<AIRTABLE_URL>" --max-records 100 --format json
```

Quy tắc đầy đủ: `_foundation/DATA-SSOT.md`. Token để ở `VLU/.env` (scope
`schema.bases:read` + `data.records:read`).
