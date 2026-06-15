# Onboarding thành viên mới (~10 phút)

Chào mừng. Làm đúng 5 bước này là bạn đóng góp được mà không phá chuẩn chung.

### 1. Lấy workspace
- Có quyền vào repo `research/` (hoặc nhận folder `VLU/`).
- Cài Python 3 (script chỉ dùng standard library, không cần `pip install`).

### 2. Kết nối Airtable (dữ liệu sống)
```bash
cd VLU
cp .env.example .env          # rồi điền AIRTABLE_TOKEN=pat_xxx (xin lead, KHÔNG dán vào chat)
python3 scripts/airtable_inspect.py "<AIRTABLE_URL>" --max-records 5 --format markdown
```
Token cần scope `schema.bases:read` + `data.records:read`.

### 3. Bảo AI đọc luật trước
Mở Claude hoặc Codex **tại folder `VLU/`**. AI sẽ tự đọc `AGENTS.md` → `_foundation/`.
Để chắc chắn, mở đầu phiên hãy nói:
> "Đọc `_foundation/00-START-HERE.md` trước khi làm. Tuân RULES/BRAND/GLOSSARY/TONE."

### 4. Quy tắc bất di bất dịch
- **Dữ liệu sống ở Airtable**, không sửa Excel rời rồi gửi qua lại.
- **Không tự đổi** màu/thuật ngữ/cấu trúc — khác chuẩn thì hỏi trước.
- **Mỗi dự án 1 folder**; tạo mới từ `_foundation/init/project-template/`.
- **Không commit secret** (`.env`, token).

### 5. Khi bí
Đọc `_foundation/RULES.md` (có checklist) hoặc hỏi lead. Gặp thuật ngữ mới → thêm vào
`_foundation/GLOSSARY.md` rồi commit.
