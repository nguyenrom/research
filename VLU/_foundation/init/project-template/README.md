# <TÊN DỰ ÁN>

> Template tạo dự án mới. Copy cả folder `project-template/` → `VLU/<tên-dự-án>/`, rồi điền các mục dưới.
> Dự án này **kế thừa** toàn bộ luật ở `VLU/_foundation/` — chỉ ghi ở đây cái RIÊNG của dự án.

## 1. Mục tiêu
<Một câu: dự án này giải quyết vấn đề gì, cho ai.>

## 2. Phạm vi & deliverable chính
- <vd. report HTML, deck PPTX, file Excel synthesis>

## 3. Nguồn dữ liệu (Airtable)
- Base/Table/View: `<điền — theo DATA-SSOT.md>`
- Dữ liệu sống ở Airtable; file trong folder này là snapshot có ngày.

## 4. Thuật ngữ riêng (nếu có)
- <thuật ngữ chỉ thuộc dự án này; thuật ngữ dùng chung → để ở _foundation/GLOSSARY.md>

## 5. Quy ước riêng (nếu lệch foundation)
- <ghi rõ chỗ lệch + lý do; mặc định KHÔNG lệch>

## 6. Cách build deliverable
```bash
# vd: python3 scripts/build_xxx.py
```

## Cấu trúc folder
```
<tên-dự-án>/
├── README.md      (file này)
├── scripts/       (script build deliverable)
├── assets/        (ảnh, tài nguyên)
└── <deliverables> (.html/.xlsx/.pptx — đặt tên theo STRUCTURE.md)
```
