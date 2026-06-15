# STRUCTURE — Cấu trúc folder & đặt tên

## Sơ đồ workspace

```
VLU/
├── _foundation/            ← tầng luật (file này nằm đây). KHÔNG để deliverable ở đây.
│   ├── 00-START-HERE.md
│   ├── RULES.md  BRAND.md  STRUCTURE.md  TONE-OF-VOICE.md  GLOSSARY.md  DATA-SSOT.md
│   └── init/               ← quy trình init + template tạo dự án
├── AGENTS.md  CLAUDE.md    ← shim trỏ về _foundation (cả Claude + Codex đọc)
├── .env  .env.example  .gitignore
├── scripts/                ← script dùng chung (vd. airtable_inspect.py)
│
├── <dự-án-A>/              ← MỖI DỰ ÁN = 1 FOLDER
│   ├── README.md           ← context riêng của dự án (kế thừa foundation)
│   ├── scripts/            ← script build deliverable của dự án
│   ├── assets/             ← ảnh, logo, tài nguyên
│   └── <deliverables>      ← .html / .xlsx / .pptx kết xuất
└── <dự-án-B>/ ...
```

## Quy ước đặt tên file (deliverable)
Mẫu: `<loại>-<chủ-đề>-<phạm-vi>-<yyyy-mm-dd>.<ext>`

| Loại      | Tiền tố   | Ví dụ |
|-----------|-----------|-------|
| Nghiên cứu thị trường | `market-`    | `market-vlu-postgrad-china-2026-05-21.md` |
| Báo cáo    | `report-`   | `report-vlu-postgrad-final-2026-05-30.html` |
| Memo/quyết định | `decision-` | `decision-vlu-seo-2026-06-02.html` |
| Chiến lược | `strategy-` | `strategy-vlu-seo-tuyensinh-2026-06-02.md` |
| Dữ liệu tổng hợp | `data-` | `data-vlu-postgrad-synthesis-2026.xlsx` |

Quy tắc: chữ thường, gạch nối, không dấu, không khoảng trắng; ngày `yyyy-mm-dd` để sort được.

## Quy ước folder
- Tiền tố `_` cho folder hệ thống/foundation (sort lên đầu, dễ nhận biết).
- Mỗi dự án tự chứa: README + scripts + assets + deliverables. Không rải file dự án ra gốc `VLU/`.
- File tạm/khóa (`~$*.pptx`, `.DS_Store`, `__pycache__/`) → gitignore, không commit.

## Tạo dự án mới
Copy `_foundation/init/project-template/` → `<tên-dự-án>/`, rồi điền `README.md`.
