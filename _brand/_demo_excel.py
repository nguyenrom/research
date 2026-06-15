# -*- coding: utf-8 -*-
"""Demo: brand-compliant quotation sheet. Run: python3 _brand/_demo_excel.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openpyxl import Workbook
from brandkit import excel, COMPANY

wb = Workbook(); ws = wb.active; ws.title = "Báo giá"
ncols = 4
r = 1
r = excel.title_row(ws, r, "Blue Coral — Báo giá triển khai", ncols,
                    subtitle=COMPANY["footer"])
r += 0
r = excel.header_row(ws, r, ["Hạng mục", "Mô tả", "Ngày công", "Chi phí (VND)"], num_cols={3, 4})
r = excel.phase_row(ws, r, "Giai đoạn 1 — Nền tảng (Foundation)", ncols)
r = excel.data_row(ws, r, ["Khảo sát & setup", "Thu thập yêu cầu, dựng môi trường", 5, 12000000], num_cols={3}, money_cols={4})
r = excel.data_row(ws, r, ["Kiến trúc dữ liệu", "Mô hình hoá, chuẩn hoá nguồn", 8, 20000000], num_cols={3}, money_cols={4}, zebra=True)
r = excel.phase_row(ws, r, "Giai đoạn 2 — Triển khai", ncols)
r = excel.data_row(ws, r, ["Pipeline & dashboard", "Tự động hoá + báo cáo", 12, 30000000], num_cols={3}, money_cols={4})
r = excel.total_row(ws, r, ["Tổng cộng", "", 25, 62000000], num_cols={3}, money_cols={4})

excel.autofit(ws, {1: 26, 2: 42, 3: 12, 4: 18})
excel.freeze_header(ws, 3)  # freeze below header row

out = os.path.join(os.path.dirname(__file__), "templates", "demo-quotation.xlsx")
os.makedirs(os.path.dirname(out), exist_ok=True)
wb.save(out)
print("OK Excel ->", out)
