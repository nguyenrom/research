# `_brand/` — Nền tảng thương hiệu Blue Coral

Thư mục này là **single source of truth** cho màu sắc, typography, layout và thông tin công ty
dùng cho **mọi** deliverable về sau (HTML, Excel, Word, PPTX). Mục tiêu: tài liệu đồng nhất về
brand và thông tin, không lặp lại / lệch chuẩn.

## Cấu trúc

```
_brand/
├── brand-tokens.json     ← SOURCE OF TRUTH (màu, font, info công ty, chuẩn Excel)
├── brand.css             ← Design system cho HTML (import vào mọi mockup/deck)
├── brandkit.py           ← Module Python áp brand vào Excel / Word / PPTX
├── BRAND-GUIDE.md        ← Hướng dẫn brand đầy đủ (đọc cái này trước)
├── style-guide.html      ← Style guide trực quan — mở bằng trình duyệt để xem component
├── README.md             ← File này
└── templates/
    ├── _template-doc.html   ← Starter HTML rỗng để copy
    ├── demo-quotation.xlsx  ← Demo Excel đúng chuẩn
    ├── demo-proposal.docx   ← Demo Word đúng chuẩn
    └── demo-deck.pptx       ← Demo PPTX đúng chuẩn
```

## Dùng cho HTML mockup / deck

1. Copy `templates/_template-doc.html` ra vị trí tài liệu mới.
2. Sửa đường dẫn `<link rel="stylesheet" href="../brand.css">` cho đúng độ sâu thư mục.
3. Dùng các class trong `style-guide.html` (mở file đó để xem trực quan + copy markup).

## Dùng cho Excel / Word / PPTX

Mỗi format chạy bằng môi trường Python tương ứng (lib đã cài sẵn):

```bash
# Excel  (openpyxl — system python)
python3 _brand/_demo_excel.py

# Word   (python-docx)
.venv-docx/bin/python _brand/_demo_docx.py

# PPTX   (python-pptx)
.venv-pptx/bin/python _brand/_demo_pptx.py
```

Trong script của bạn:

```python
import sys; sys.path.insert(0, "_brand")
from brandkit import excel, docx, pptx, T, COMPANY, PRIMARY, ACCENT
# excel.title_row / header_row / phase_row / data_row / total_row
# docx.apply_base / cover_title / brand_table / footer
# pptx.title_slide / _text
```

## Đổi brand / cập nhật thông tin

Sửa **`brand-tokens.json`** (ví dụ đổi accent, sửa tagline, thêm website) → chạy lại script sinh
tài liệu. HTML tự cập nhật qua `brand.css` (nếu đổi màu, cập nhật cả biến `--bc-*` trong `brand.css`
cho khớp — hoặc dùng JSON làm chuẩn và regenerate CSS sau này).

## Việc còn để ngỏ (cần bạn xác nhận)

- [ ] **Tagline** — hiện đặt tạm "Triển khai Dữ liệu & Marketing". Xác nhận hoặc thay.
- [ ] **Website** — đang để trống trong token.
- [ ] **Logo** — đang dùng placeholder chữ "BC". Thay bằng file logo thật khi có.
- [ ] **Migrate tài liệu cũ** — các deck/Excel hiện có (VLU, HAWEE, AmCham…) đang dùng hệ màu riêng;
      quyết định có chuyển sang chuẩn Blue Coral hay giữ nguyên (xem ghi chú trong BRAND-GUIDE).
