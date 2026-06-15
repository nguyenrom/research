# -*- coding: utf-8 -*-
"""
Blue Coral — Brand Kit for office documents.
Single source of truth: _brand/brand-tokens.json

Reads the token file and applies the Blue Coral house brand to:
  - Excel  (openpyxl)        -> run with: python3            (system, openpyxl 3.1.5)
  - Word   (python-docx)     -> run with: .venv-docx/bin/python
  - PPTX   (python-pptx)     -> run with: .venv-pptx/bin/python

Library imports are LAZY so this module loads in any venv; you only need the
library for the format you actually use.

Usage:
    from brandkit import T, hexrgb, excel, docx, pptx   # import what you need
    print(T["company"]["brand"])
"""
import json, os

_HERE = os.path.dirname(os.path.abspath(__file__))
TOKENS_PATH = os.path.join(_HERE, "brand-tokens.json")

with open(TOKENS_PATH, encoding="utf-8") as _f:
    T = json.load(_f)

C        = T["color"]
PRIMARY  = C["primary"]
ACCENT   = C["accent"]
NEUTRAL  = C["neutral"]
SEM      = C["semantic"]
COMPANY  = T["company"]
XL       = T["excel"]
FONT_OFF = T["font"]["office"]
PT       = T["office_type_pt"]


# ---------- color helpers ----------
def hex6(c):
    """'#1428A0' -> '1428A0' (uppercase, no hash)."""
    return c.lstrip("#").upper()

def argb(c, alpha="FF"):
    """'#1428A0' -> 'FF1428A0' for openpyxl fills."""
    return (alpha + hex6(c)).upper()

def rgbtuple(c):
    """'#1428A0' -> (20, 40, 160)."""
    h = hex6(c)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


# =====================================================================
#  EXCEL  (openpyxl)  —  run with system python3
# =====================================================================
class _Excel:
    """Brand helpers for openpyxl worksheets. Follows client_facing_excel_preferences:
       no icons, no row-2 descriptions, phase divider rows, M1=foundation, Vietnamese,
       2-option recommendations, freeze header, right-align numbers."""

    def _imp(self):
        from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
        return Font, PatternFill, Alignment, Border, Side

    def _fill(self, hexc):
        _, PatternFill, *_ = self._imp()
        return PatternFill("solid", fgColor=argb(hexc))

    def _side(self, hexc):
        *_, Side = self._imp()
        return Side(style="thin", color=argb(hexc))

    def thin_border(self):
        _, _, _, Border, Side = self._imp()
        s = self._side(XL["border"])
        return Border(left=s, right=s, top=s, bottom=s)

    def title_row(self, ws, row, text, ncols, subtitle=None):
        """Merged brand title bar across ncols. Optional subtitle row below."""
        Font, PatternFill, Alignment, *_ = self._imp()
        st = XL["title"]
        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=ncols)
        c = ws.cell(row=row, column=1, value=text)
        c.fill = self._fill(st["fill"])
        c.font = Font(name=FONT_OFF["heading"], bold=True, size=st["size"], color=argb(st["font"]))
        c.alignment = Alignment(vertical="center", horizontal="left", indent=1)
        ws.row_dimensions[row].height = 30
        nxt = row + 1
        if subtitle:
            ss = XL["subtitle"]
            ws.merge_cells(start_row=nxt, start_column=1, end_row=nxt, end_column=ncols)
            c2 = ws.cell(row=nxt, column=1, value=subtitle)
            c2.fill = self._fill(ss["fill"])
            c2.font = Font(name=FONT_OFF["body"], size=ss["size"], color=argb(ss["font"]), italic=True)
            c2.alignment = Alignment(vertical="center", horizontal="left", indent=1)
            nxt += 1
        return nxt

    def header_row(self, ws, row, headers, num_cols=()):
        """Column header row. num_cols = set of 1-based indexes to right-align."""
        Font, PatternFill, Alignment, Border, Side = self._imp()
        st = XL["header"]
        bottom = Side(style="medium", color=argb(st["border_bottom"]))
        thin = self._side(XL["border"])
        for i, h in enumerate(headers, start=1):
            c = ws.cell(row=row, column=i, value=h)
            c.fill = self._fill(st["fill"])
            c.font = Font(name=FONT_OFF["heading"], bold=True, size=st["size"], color=argb(st["font"]))
            c.alignment = Alignment(horizontal="right" if i in num_cols else "left",
                                    vertical="center", wrap_text=True)
            c.border = Border(left=thin, right=thin, top=thin, bottom=bottom)
        ws.row_dimensions[row].height = 24
        return row + 1

    def phase_row(self, ws, row, text, ncols):
        """Coral phase-divider row, merged across all columns. e.g. 'Giai đoạn 1 — Nền tảng'."""
        Font, PatternFill, Alignment, *_ = self._imp()
        st = XL["phase_divider"]
        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=ncols)
        c = ws.cell(row=row, column=1, value=text)
        c.fill = self._fill(st["fill"])
        c.font = Font(name=FONT_OFF["heading"], bold=True, size=st["size"], color=argb(st["font"]))
        c.alignment = Alignment(vertical="center", horizontal="left", indent=1)
        ws.row_dimensions[row].height = 22
        return row + 1

    def data_row(self, ws, row, values, num_cols=(), money_cols=(), zebra=False):
        """Body row. num_cols/money_cols = 1-based indexes; money uses #,##0 format."""
        Font, PatternFill, Alignment, *_ = self._imp()
        st = XL["body"]
        border = self.thin_border()
        fill = self._fill(XL["zebra"]["fill"]) if zebra else self._fill(st["fill"])
        for i, v in enumerate(values, start=1):
            c = ws.cell(row=row, column=i, value=v)
            c.fill = fill
            c.font = Font(name=FONT_OFF["body"], size=st["size"], color=argb(st["font"]))
            c.border = border
            right = i in num_cols or i in money_cols
            c.alignment = Alignment(horizontal="right" if right else "left",
                                    vertical="center", wrap_text=True)
            if i in money_cols:
                c.number_format = '#,##0'
        return row + 1

    def total_row(self, ws, row, values, num_cols=(), money_cols=()):
        Font, PatternFill, Alignment, Border, Side = self._imp()
        st = XL["total"]
        top = Side(style="medium", color=argb(st["border_top"]))
        thin = self._side(XL["border"])
        for i, v in enumerate(values, start=1):
            c = ws.cell(row=row, column=i, value=v)
            c.fill = self._fill(st["fill"])
            c.font = Font(name=FONT_OFF["heading"], bold=True, size=st["size"], color=argb(st["font"]))
            c.border = Border(left=thin, right=thin, top=top, bottom=thin)
            right = i in num_cols or i in money_cols
            c.alignment = Alignment(horizontal="right" if right else "left", vertical="center")
            if i in money_cols:
                c.number_format = '#,##0'
        return row + 1

    def autofit(self, ws, widths):
        """widths: dict {col_index: width} or list aligned to columns."""
        items = widths.items() if isinstance(widths, dict) else enumerate(widths, start=1)
        from openpyxl.utils import get_column_letter
        for idx, w in items:
            ws.column_dimensions[get_column_letter(idx)].width = w

    def freeze_header(self, ws, row):
        ws.freeze_panes = ws.cell(row=row, column=1)

excel = _Excel()


# =====================================================================
#  WORD  (python-docx)  —  run with .venv-docx/bin/python
# =====================================================================
class _Docx:
    def apply_base(self, doc):
        """Set Normal + Heading styles to the Blue Coral brand."""
        from docx.shared import Pt, RGBColor
        normal = doc.styles["Normal"]
        normal.font.name = FONT_OFF["body"]
        normal.font.size = Pt(PT["body"]["size"])
        normal.font.color.rgb = RGBColor(*rgbtuple(NEUTRAL["ink"]))
        heads = {"Heading 1": ("h1", PRIMARY["700"]),
                 "Heading 2": ("h2", PRIMARY["600"]),
                 "Heading 3": ("h3", NEUTRAL["ink2"])}
        for name, (key, col) in heads.items():
            if name in doc.styles:
                s = doc.styles[name]
                s.font.name = FONT_OFF["heading"]
                s.font.size = Pt(PT[key]["size"])
                s.font.bold = True
                s.font.color.rgb = RGBColor(*rgbtuple(col))
        return doc

    def cover_title(self, doc, title, subtitle=None, date=None):
        from docx.shared import Pt, RGBColor
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        bp = doc.add_paragraph()
        br = bp.add_run("BLUE CORAL")
        br.bold = True
        br.font.size = Pt(11)
        br.font.color.rgb = RGBColor(*rgbtuple(PRIMARY["600"]))
        h = doc.add_heading(title, level=0)
        if subtitle:
            sp = doc.add_paragraph(subtitle)
            sp.runs[0].italic = True
            sp.runs[0].font.color.rgb = RGBColor(*rgbtuple(NEUTRAL["muted"]))
        if date:
            doc.add_paragraph("Ngày: " + date)
        return doc

    def footer(self, doc):
        from docx.shared import Pt, RGBColor
        sec = doc.sections[0]
        p = sec.footer.paragraphs[0]
        r = p.add_run(COMPANY["footer"])
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(*rgbtuple(NEUTRAL["muted"]))
        return doc

    def brand_table(self, doc, headers, rows):
        """Header-shaded table in brand colors. rows = list of row-lists."""
        from docx.shared import Pt, RGBColor
        from docx.oxml.ns import qn
        from docx.oxml import OxmlElement
        tbl = doc.add_table(rows=1, cols=len(headers))
        tbl.style = "Table Grid"
        def shade(cell, hexc):
            tcPr = cell._tc.get_or_add_tcPr()
            sh = OxmlElement("w:shd")
            sh.set(qn("w:fill"), hex6(hexc))
            tcPr.append(sh)
        for i, h in enumerate(headers):
            cell = tbl.rows[0].cells[i]
            cell.text = h
            shade(cell, PRIMARY["100"])
            run = cell.paragraphs[0].runs[0]
            run.bold = True
            run.font.color.rgb = RGBColor(*rgbtuple(NEUTRAL["ink"]))
        for r in rows:
            cells = tbl.add_row().cells
            for i, v in enumerate(r):
                cells[i].text = str(v)
        return tbl

docx = _Docx()


# =====================================================================
#  PPTX  (python-pptx)  —  run with .venv-pptx/bin/python
# =====================================================================
class _Pptx:
    def color(self, hexc):
        from pptx.dml.color import RGBColor
        return RGBColor(*rgbtuple(hexc))

    def title_slide(self, prs, title, subtitle=None):
        """Brand cover slide: deep-ocean background, white title, coral accent bar."""
        from pptx.util import Inches, Pt
        from pptx.enum.shapes import MSO_SHAPE
        from pptx.enum.text import PP_ALIGN
        slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
        W, H = prs.slide_width, prs.slide_height
        # background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, H)
        bg.fill.solid(); bg.fill.fore_color.rgb = self.color(PRIMARY["800"])
        bg.line.fill.background()
        bg.shadow.inherit = False
        # coral accent bar
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(2.2), Inches(1.4), Inches(0.12))
        bar.fill.solid(); bar.fill.fore_color.rgb = self.color(ACCENT["600"]); bar.line.fill.background()
        # brand label
        self._text(slide, "BLUE CORAL", Inches(0.6), Inches(1.4), Inches(8), Inches(0.5),
                   size=14, bold=True, color="#FFFFFF")
        # title
        self._text(slide, title, Inches(0.6), Inches(2.5), W - Inches(1.2), Inches(2),
                   size=40, bold=True, color="#FFFFFF")
        if subtitle:
            self._text(slide, subtitle, Inches(0.6), Inches(4.3), W - Inches(1.2), Inches(1.2),
                       size=18, bold=False, color=PRIMARY["100"])
        return slide

    def _text(self, slide, text, l, t, w, h, size=18, bold=False, color=None, align=None):
        if color is None:
            color = NEUTRAL["ink"]
        from pptx.util import Pt
        from pptx.enum.text import PP_ALIGN
        tb = slide.shapes.add_textbox(l, t, w, h)
        tf = tb.text_frame; tf.word_wrap = True
        p = tf.paragraphs[0]
        if align:
            p.alignment = PP_ALIGN.LEFT
        r = p.add_run(); r.text = text
        r.font.size = Pt(size); r.font.bold = bold
        r.font.name = FONT_OFF["heading"]
        r.font.color.rgb = self.color(color)
        return tb

pptx = _Pptx()


if __name__ == "__main__":
    print("Blue Coral brand kit loaded.")
    print("  brand   :", COMPANY["brand"])
    print("  legal   :", COMPANY["legal_name"], "· MST", COMPANY["tax_id"])
    print("  primary :", PRIMARY["600"], "| accent:", ACCENT["600"])
    print("  tokens  :", TOKENS_PATH)
