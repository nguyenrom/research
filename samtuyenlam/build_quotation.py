"""
SAM TUYEN LAM — Website Consolidation Programme
Enterprise Proposal & Quotation
Prepared by Blue Coral (Powered by ADNS)
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.page import PageMargins

# ============================================================
# BRAND SYSTEM
# ============================================================
C_PRIMARY      = '1F3A5F'  # Deep navy — primary
C_PRIMARY_DARK = '0F1F3D'  # Cover navy
C_ACCENT       = 'C19A5B'  # Warm gold — Swiss-Bel feel
C_ACCENT_LITE  = 'F5EEE0'  # Cream highlight
C_GREY_DARK    = '2C3E50'  # Charcoal
C_GREY_MID     = '6B7280'
C_GREY_LITE    = 'F4F6F8'
C_GREY_LINE    = 'D5DBE0'
C_TEXT         = '1F2937'
C_WHITE        = 'FFFFFF'
C_SUCCESS      = '2D6A4F'
C_DANGER       = 'A93226'

FONT_NAME      = 'Calibri'

# Pricing economics
RATE_USD_HOUR  = 19.25
FX_VND_USD     = 26000

# ============================================================
# STYLE HELPERS
# ============================================================
def fill(color):
    return PatternFill('solid', fgColor=color)

def font(size=10, bold=False, color=C_TEXT, italic=False, name=FONT_NAME):
    return Font(name=name, size=size, bold=bold, color=color, italic=italic)

def align(h='left', v='center', wrap=True, indent=0):
    return Alignment(horizontal=h, vertical=v, wrap_text=wrap, indent=indent)

THIN = Side(border_style='thin', color=C_GREY_LINE)
MED  = Side(border_style='medium', color=C_PRIMARY)
NO   = Side(border_style=None)
BORDER_BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
BORDER_TOP_ACCENT = Border(top=Side(border_style='medium', color=C_ACCENT),
                            left=THIN, right=THIN, bottom=THIN)

def style_cell(cell, *, bg=None, fnt=None, alg=None, border=BORDER_BOX, fmt=None):
    if bg: cell.fill = fill(bg)
    if fnt: cell.font = fnt
    if alg: cell.alignment = alg
    if border is not None: cell.border = border
    if fmt: cell.number_format = fmt

def set_widths(ws, widths_dict):
    for col, w in widths_dict.items():
        ws.column_dimensions[col].width = w

def set_row_heights(ws, heights_dict):
    for r, h in heights_dict.items():
        ws.row_dimensions[r].height = h

def section_header(ws, row, cols, text, *, bg=C_PRIMARY, fg=C_WHITE,
                    height=28, size=12):
    """Render a full-width section banner."""
    start, end = cols
    ws.merge_cells(start_row=row, start_column=start,
                    end_row=row, end_column=end)
    c = ws.cell(row=row, column=start, value=text)
    c.fill = fill(bg)
    c.font = font(size=size, bold=True, color=fg)
    c.alignment = align('left', 'center', indent=1)
    ws.row_dimensions[row].height = height

def repeat_brand_header(ws, cols=('B', 'L'), title=None):
    """Top brand strip — repeats on every operational sheet."""
    start, end = cols
    s_idx = openpyxl.utils.column_index_from_string(start)
    e_idx = openpyxl.utils.column_index_from_string(end)

    # Row 1: Blue Coral / address bar
    ws.merge_cells(start_row=1, start_column=s_idx, end_row=1, end_column=e_idx)
    c = ws.cell(row=1, column=s_idx,
                 value='  BLUE CORAL   ▍ Powered by ADNS  '
                       '·  8/7D Phan Huy Ich, Tan Binh, Ho Chi Minh City  '
                       '·  +84 979 477 101  ·  hello@bluecoral.vn')
    c.fill = fill(C_PRIMARY_DARK)
    c.font = font(size=10, bold=True, color=C_WHITE)
    c.alignment = align('left', 'center')
    ws.row_dimensions[1].height = 24

    # Row 2: gold accent strip
    ws.merge_cells(start_row=2, start_column=s_idx, end_row=2, end_column=e_idx)
    c = ws.cell(row=2, column=s_idx, value='')
    c.fill = fill(C_ACCENT)
    ws.row_dimensions[2].height = 4

    # Row 3: sheet title strip
    if title:
        ws.merge_cells(start_row=3, start_column=s_idx, end_row=3, end_column=e_idx)
        c = ws.cell(row=3, column=s_idx, value=f'  {title}')
        c.fill = fill(C_GREY_LITE)
        c.font = font(size=14, bold=True, color=C_PRIMARY)
        c.alignment = align('left', 'center')
        ws.row_dimensions[3].height = 32

# ============================================================
# SHEET 1 — COVER
# ============================================================
def build_cover(wb):
    ws = wb.create_sheet('1. Cover')
    ws.sheet_view.showGridLines = False
    ws.sheet_properties.tabColor = C_PRIMARY_DARK

    set_widths(ws, {'A': 2, 'B': 14, 'C': 14, 'D': 14, 'E': 14, 'F': 14,
                     'G': 14, 'H': 14, 'I': 14, 'J': 14, 'K': 2})

    # Navy background block — rows 1 to 18
    for r in range(1, 19):
        for col_idx in range(1, 12):
            ws.cell(row=r, column=col_idx).fill = fill(C_PRIMARY_DARK)

    # Brand bar (rows 2-3)
    ws.merge_cells('B2:J2')
    c = ws['B2']
    c.value = '  BLUE CORAL'
    c.fill = fill(C_PRIMARY_DARK)
    c.font = font(size=20, bold=True, color=C_WHITE)
    c.alignment = align('left', 'center')
    ws.row_dimensions[2].height = 32

    ws.merge_cells('B3:J3')
    c = ws['B3']
    c.value = '  Powered by ADNS  ·  Enterprise web & digital experience studio'
    c.fill = fill(C_PRIMARY_DARK)
    c.font = font(size=10, color=C_ACCENT, italic=True)
    c.alignment = align('left', 'top')
    ws.row_dimensions[3].height = 18

    # Gold divider
    for col_idx in range(2, 11):
        ws.cell(row=5, column=col_idx).fill = fill(C_ACCENT)
    ws.row_dimensions[5].height = 4

    # Document type
    ws.merge_cells('B7:J7')
    c = ws['B7']
    c.value = '  PROPOSAL  &  QUOTATION'
    c.fill = fill(C_PRIMARY_DARK)
    c.font = font(size=12, bold=True, color=C_ACCENT)
    c.alignment = align('left', 'center')
    ws.row_dimensions[7].height = 22

    # Project title
    ws.merge_cells('B8:J10')
    c = ws['B8']
    c.value = '  SAM Tuyen Lam\n  Website Consolidation Programme'
    c.fill = fill(C_PRIMARY_DARK)
    c.font = font(size=28, bold=True, color=C_WHITE)
    c.alignment = align('left', 'center', wrap=True)
    ws.row_dimensions[8].height = 36
    ws.row_dimensions[9].height = 36
    ws.row_dimensions[10].height = 14

    # Subtitle
    ws.merge_cells('B12:J12')
    c = ws['B12']
    c.value = ('  One master brand · three properties · three languages · '
                'three booking flows')
    c.fill = fill(C_PRIMARY_DARK)
    c.font = font(size=11, color=C_GREY_LINE, italic=True)
    c.alignment = align('left', 'center')
    ws.row_dimensions[12].height = 22

    # Client / project block at bottom of navy
    ws.merge_cells('B15:E16')
    c = ws['B15']
    c.value = '  PREPARED FOR\n  SAM Tuyen Lam Hospitality Group'
    c.fill = fill(C_PRIMARY_DARK)
    c.font = font(size=11, bold=True, color=C_WHITE)
    c.alignment = align('left', 'center')

    ws.merge_cells('F15:J16')
    c = ws['F15']
    c.value = ('  REFERENCE\n  BC-2026-0526-SAM  ·  Issued 26 May 2026  '
                '·  Valid until 25 June 2026')
    c.fill = fill(C_PRIMARY_DARK)
    c.font = font(size=11, color=C_WHITE)
    c.alignment = align('left', 'center')

    # ===== Bottom white area =====
    # Investment headline card
    ws.merge_cells('B20:J21')
    c = ws['B20']
    c.value = 'PROGRAMME INVESTMENT AT A GLANCE'
    c.font = font(size=11, bold=True, color=C_PRIMARY)
    c.alignment = align('center', 'center')
    c.fill = fill(C_GREY_LITE)
    ws.row_dimensions[20].height = 22
    ws.row_dimensions[21].height = 6

    # Three-card layout
    ws.row_dimensions[22].height = 22
    ws.row_dimensions[23].height = 42
    ws.row_dimensions[24].height = 22

    # 3-row cards: row22=label, row23=price, row24=footer
    card_specs = [
        ((2, 4), 'PHASE 1 — DESIGN & BUILD',
         "='4. Pricing — Build'!I_GRAND",
         "='4. Pricing — Build'!J_GRAND",
         'One-time · VAT included'),
        ((5, 7), 'PHASE 2 — HOSTING & SUPPORT (Y1)',
         "='5. Pricing — Hosting'!D_GRAND",
         None,
         '12 months · VAT included'),
        ((8, 10), 'TOTAL PROGRAMME — Year 1',
         '=SUM_GRAND_VND',
         '=SUM_GRAND_USD',
         '4-5 month build + 12-month support'),
    ]
    for (cs, ce), lbl, vnd, usd, ftr in card_specs:
        # Label row 22
        ws.merge_cells(start_row=22, start_column=cs, end_row=22, end_column=ce)
        c = ws.cell(row=22, column=cs, value=lbl)
        c.fill = fill(C_PRIMARY)
        c.font = font(size=10, bold=True, color=C_WHITE)
        c.alignment = align('center', 'center')
        # Price row 23
        ws.merge_cells(start_row=23, start_column=cs, end_row=23, end_column=ce)
        c = ws.cell(row=23, column=cs, value=vnd)
        c.fill = fill(C_ACCENT_LITE)
        c.font = font(size=14, bold=True, color=C_PRIMARY_DARK)
        c.alignment = align('center', 'center')
        c.number_format = '#,##0 [$₫-vi-VN]'
        # USD line (overlay) — render in footer row instead if usd present
        # Footer row 24
        ws.merge_cells(start_row=24, start_column=cs, end_row=24, end_column=ce)
        if usd:
            c = ws.cell(row=24, column=cs, value=usd)
            c.number_format = '"~ $"#,##0"   ·   VAT included"'
        else:
            c = ws.cell(row=24, column=cs, value=ftr)
        c.fill = fill(C_ACCENT_LITE)
        c.font = font(size=9, color=C_GREY_DARK, italic=True)
        c.alignment = align('center', 'center')

    # Engagement context
    ws.merge_cells('B27:J27')
    c = ws['B27']
    c.value = 'ENGAGEMENT CONTEXT'
    c.font = font(size=11, bold=True, color=C_PRIMARY)
    c.alignment = align('left', 'center')
    ws.row_dimensions[27].height = 22

    context_lines = [
        ('B28:J28', 'Client',          'SAM Tuyen Lam Hospitality Group — Golf Course, Swiss-Belresort, Villa'),
        ('B29:J29', 'Primary Domain',  'samtuyenlam.com.vn  (consolidation of 4 legacy domains)'),
        ('B30:J30', 'Reference Style', 'Hoiana.com (multi-property architecture) × NamiaRiverRetreat.com (emotional, healing tone)'),
        ('B31:J31', 'Languages',       'Vietnamese · English · Korean'),
        ('B32:J32', 'Booking Flows',   'Golf → VNPay  ·  Swiss-Belresort → Hotel Link → Smile PMS  ·  Villa → Lead capture'),
        ('B33:J33', 'Engagement',      'Strategy, Design, Build, Migrate, Launch + 12-month Managed Services'),
        ('B34:J34', 'Delivery',        '20 weeks (5 months) from kickoff to launch · 4-week post-launch hypercare'),
    ]
    for rng, label, val in context_lines:
        start_row = int(''.join(filter(str.isdigit, rng.split(':')[0])))
        ws.merge_cells(rng)
        # Use 2-cell layout via composite text
        c = ws.cell(row=start_row, column=2,
                     value=f'  {label}')
        c.font = font(size=10, bold=True, color=C_GREY_DARK)
        c.alignment = align('left', 'center')
        c.border = Border(bottom=THIN)
        # Value
        ws.unmerge_cells(rng)
        ws.merge_cells(start_row=start_row, start_column=4,
                        end_row=start_row, end_column=10)
        c2 = ws.cell(row=start_row, column=4, value=val)
        c2.font = font(size=10, color=C_TEXT)
        c2.alignment = align('left', 'center')
        c2.border = Border(bottom=THIN)
        ws.row_dimensions[start_row].height = 22

    # Prepared by block
    ws.merge_cells('B37:J37')
    c = ws['B37']
    c.value = 'CONTACT & APPROVALS'
    c.font = font(size=11, bold=True, color=C_PRIMARY)
    c.alignment = align('left', 'center')
    ws.row_dimensions[37].height = 22

    contact_rows = [
        ('Prepared by',   'Ms. Uyen Tran — Account Director, Blue Coral',
         'uyen.tran@bluecoral.vn · +84 979 477 101'),
        ('Approved by',   'Mr. Nguyen — Managing Director, ADNS',
         '—'),
        ('Reviewed by',   'Ms. Vu Kieu Linh — Engagement Manager',
         '—'),
        ('Client sponsor','Mr. / Ms. ________________  (SAM Tuyen Lam)',
         'Date of signature: ____ / ____ / 2026'),
    ]
    r = 38
    for label, person, ctx in contact_rows:
        c = ws.cell(row=r, column=2, value=f'  {label}')
        c.font = font(size=10, bold=True, color=C_GREY_DARK)
        c.alignment = align('left', 'center')
        c.border = Border(bottom=THIN)
        ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=7)
        c = ws.cell(row=r, column=4, value=person)
        c.font = font(size=10, color=C_TEXT)
        c.alignment = align('left', 'center')
        c.border = Border(bottom=THIN)
        ws.merge_cells(start_row=r, start_column=8, end_row=r, end_column=10)
        c = ws.cell(row=r, column=8, value=ctx)
        c.font = font(size=9, color=C_GREY_MID, italic=True)
        c.alignment = align('left', 'center')
        c.border = Border(bottom=THIN)
        ws.row_dimensions[r].height = 24
        r += 1

    # Footer
    ws.merge_cells('B45:J45')
    c = ws['B45']
    c.value = ('This proposal is commercially confidential. Pricing and scope herein '
                'are valid for 30 days from the issue date.')
    c.font = font(size=8, color=C_GREY_MID, italic=True)
    c.alignment = align('center', 'center')

    ws.print_options.horizontalCentered = True
    ws.page_setup.orientation = ws.ORIENTATION_PORTRAIT
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 1
    ws.page_margins = PageMargins(left=0.4, right=0.4, top=0.4, bottom=0.4)


# ============================================================
# SHEET 2 — EXECUTIVE SUMMARY
# ============================================================
def build_executive_summary(wb):
    ws = wb.create_sheet('2. Executive Summary')
    ws.sheet_view.showGridLines = False
    ws.sheet_properties.tabColor = C_PRIMARY

    set_widths(ws, {'A': 2, 'B': 18, 'C': 22, 'D': 22, 'E': 22, 'F': 22,
                     'G': 22, 'H': 22, 'I': 22, 'J': 18, 'K': 2})

    repeat_brand_header(ws, ('B', 'J'), title='Executive Summary')

    # ── ENGAGEMENT OVERVIEW
    r = 5
    section_header(ws, r, (2, 10), '  01 · ENGAGEMENT OVERVIEW')
    r += 1
    ws.merge_cells(start_row=r, start_column=2, end_row=r+2, end_column=10)
    c = ws.cell(row=r, column=2)
    c.value = (
        "SAM Tuyen Lam currently operates four disconnected websites — one per property and one "
        "legacy 360° VR portal. Each runs on different infrastructure, lacks a unified brand voice, "
        "and presents fragmented booking journeys to a global audience.\n\n"
        "This programme consolidates the four sites into a single master experience at "
        "samtuyenlam.com.vn, modelled on Hoiana's multi-property architecture and Namia River "
        "Retreat's emotional, healing tone. The new platform will deliver an Alpine-retreat "
        "narrative across three properties, three languages (VI / EN / KO), and three independent "
        "booking flows — with the marketing team in full control of campaigns through a "
        "permission-managed CMS."
    )
    c.font = font(size=10, color=C_TEXT)
    c.alignment = align('left', 'top', wrap=True)
    set_row_heights(ws, {r: 60, r+1: 60, r+2: 60})
    r += 4

    # ── STRATEGIC OBJECTIVES (5 KPI tiles)
    section_header(ws, r, (2, 10), '  02 · STRATEGIC OBJECTIVES')
    r += 1
    objectives = [
        ('Brand consolidation',
         'Unify 4 fragmented sites under one master brand narrative — Alpine retreat, healing, enduring love.'),
        ('Conversion lift',
         'Persistent property-aware "Book" CTAs, friction-free booking journeys, direct-booking incentives.'),
        ('International reach',
         'Trilingual VI/EN/KO with Swiss-Belresort identity surfaced for inbound EN/KO traffic.'),
        ('Marketing autonomy',
         'Role-based CMS lets Marketing publish offers, blog, news, banners, pop-ups without engineering tickets.'),
        ('Performance & trust',
         'Core Web Vitals green, WCAG-AA accessibility, hardened security (post-incident posture), full backup & DR.'),
    ]
    for i, (title, desc) in enumerate(objectives):
        col_start = 2 + i * 2 if i < 4 else 2  # 5 items in 2 rows: 4 + 1, actually let's stack 5 horizontally
    # Use a clean 5-column grid (B, D, F, H — 4 items horizontally; row 2 for 5th)
    # Simpler: a 2x3 grid (3 across, 2 rows). Total 5 items -> last cell empty
    grid_rows = 2
    grid_cols = 3
    spans = [(2, 3), (5, 6), (8, 10)]  # column start/end for 3 cards
    r0 = r
    for idx, (title, desc) in enumerate(objectives):
        row_offset = (idx // 3) * 3
        col_idx = idx % 3
        cs, ce = spans[col_idx]
        # title row
        ws.merge_cells(start_row=r0 + row_offset, start_column=cs,
                       end_row=r0 + row_offset, end_column=ce)
        c = ws.cell(row=r0 + row_offset, column=cs, value=f'  {title.upper()}')
        c.fill = fill(C_ACCENT)
        c.font = font(size=10, bold=True, color=C_WHITE)
        c.alignment = align('left', 'center')
        # description row
        ws.merge_cells(start_row=r0 + row_offset + 1, start_column=cs,
                       end_row=r0 + row_offset + 1, end_column=ce)
        c = ws.cell(row=r0 + row_offset + 1, column=cs, value=desc)
        c.fill = fill(C_GREY_LITE)
        c.font = font(size=9, color=C_TEXT)
        c.alignment = align('left', 'top', wrap=True, indent=1)
        set_row_heights(ws, {r0 + row_offset: 22,
                             r0 + row_offset + 1: 56})
    r = r0 + 6 + 1  # advance below the grid + spacer

    # ── SCOPE AT A GLANCE
    section_header(ws, r, (2, 10), '  03 · SCOPE AT A GLANCE — PROPERTY MAP')
    r += 1
    headers = ['Property', 'Domain Path', 'Booking System', 'Primary Audience', 'Templates Delivered']
    spans_h = [(2, 2), (3, 3), (4, 5), (6, 7), (8, 10)]
    for h, (cs, ce) in zip(headers, spans_h):
        if cs != ce:
            ws.merge_cells(start_row=r, start_column=cs, end_row=r, end_column=ce)
        c = ws.cell(row=r, column=cs, value=h)
        c.fill = fill(C_PRIMARY)
        c.font = font(size=10, bold=True, color=C_WHITE)
        c.alignment = align('center', 'center')
        c.border = BORDER_BOX
    ws.row_dimensions[r].height = 22
    r += 1

    properties = [
        ('SAM Tuyen Lam\nGolf Course',
         '/samtuyenlamgolf',
         'VNPay (booking → PMS)',
         'Golfers · Couples',
         '1 Overview + 18-Hole + Coaching + Club House + Gallery + Booking'),
        ('Swiss-Belresort\nTuyen Lam',
         '/swiss-belresorttuyenlam',
         'Hotel Link → Smile PMS',
         '4★+ International · Wellness · MICE',
         '1 Property + 7 Room Types + Spa + MICE + Dining + Gallery + Booking'),
        ('SAM Tuyen Lam\nVilla',
         '/samtuyenlamvilla',
         'Lead capture (temporarily closed)',
         'Future launch · Newsletter audience',
         '1 Teaser + 5 Room Type design templates (no booking dev)'),
    ]
    for prop, dom, book, aud, tpl in properties:
        for (cs, ce), val in zip(spans_h, [prop, dom, book, aud, tpl]):
            if cs != ce:
                ws.merge_cells(start_row=r, start_column=cs, end_row=r, end_column=ce)
            c = ws.cell(row=r, column=cs, value=val)
            c.font = font(size=10, color=C_TEXT, bold=(cs==2))
            c.alignment = align('left', 'center', wrap=True, indent=1)
            c.border = BORDER_BOX
            c.fill = fill(C_WHITE)
        ws.row_dimensions[r].height = 38
        r += 1
    r += 1

    # ── PROGRAMME INVESTMENT
    section_header(ws, r, (2, 10), '  04 · PROGRAMME INVESTMENT')
    r += 1
    inv_headers = ['#', 'Phase', 'Description', 'Investment (VND)', 'Investment (USD)']
    inv_spans = [(2, 2), (3, 3), (4, 7), (8, 9), (10, 10)]
    for h, (cs, ce) in zip(inv_headers, inv_spans):
        if cs != ce:
            ws.merge_cells(start_row=r, start_column=cs, end_row=r, end_column=ce)
        c = ws.cell(row=r, column=cs, value=h)
        c.fill = fill(C_PRIMARY)
        c.font = font(size=10, bold=True, color=C_WHITE)
        c.alignment = align('center', 'center')
        c.border = BORDER_BOX
    ws.row_dimensions[r].height = 22
    r += 1

    inv_rows = [
        ('1', 'Design & Build',
         'Discovery · IA · Visual Design · 14 page templates · Booking integrations · CMS · '
         'Multi-language · SEO · QA · Launch · 4-week hypercare',
         "='4. Pricing — Build'!I_GRAND",
         "='4. Pricing — Build'!J_GRAND"),
        ('2', 'Hosting & Support',
         'Year 1 — Enterprise hosting · CDN · SSL · WAF · 20 hrs/month managed services',
         "='5. Pricing — Hosting'!D_GRAND",
         None),
    ]
    inv_data_rows = []
    for num, phase, desc, vnd, usd in inv_rows:
        ws.cell(row=r, column=2, value=num)
        ws.cell(row=r, column=2).alignment = align('center', 'center')
        ws.cell(row=r, column=2).font = font(size=10, bold=True, color=C_PRIMARY)
        ws.cell(row=r, column=2).border = BORDER_BOX
        ws.cell(row=r, column=3, value=phase)
        ws.cell(row=r, column=3).font = font(size=10, bold=True, color=C_TEXT)
        ws.cell(row=r, column=3).alignment = align('left', 'center', indent=1)
        ws.cell(row=r, column=3).border = BORDER_BOX
        ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=7)
        ws.cell(row=r, column=4, value=desc)
        ws.cell(row=r, column=4).font = font(size=9, color=C_GREY_DARK)
        ws.cell(row=r, column=4).alignment = align('left', 'center', wrap=True, indent=1)
        ws.cell(row=r, column=4).border = BORDER_BOX
        ws.merge_cells(start_row=r, start_column=8, end_row=r, end_column=9)
        ws.cell(row=r, column=8, value=vnd)
        ws.cell(row=r, column=8).font = font(size=10, bold=True, color=C_PRIMARY_DARK)
        ws.cell(row=r, column=8).alignment = align('right', 'center', indent=1)
        ws.cell(row=r, column=8).number_format = '#,##0 [$₫-vi-VN]'
        ws.cell(row=r, column=8).border = BORDER_BOX
        if usd:
            ws.cell(row=r, column=10, value=usd)
        else:
            ws.cell(row=r, column=10, value='—')
        ws.cell(row=r, column=10).font = font(size=10, color=C_GREY_DARK)
        ws.cell(row=r, column=10).alignment = align('right', 'center', indent=1)
        ws.cell(row=r, column=10).number_format = '"$"#,##0'
        ws.cell(row=r, column=10).border = BORDER_BOX
        ws.row_dimensions[r].height = 40
        inv_data_rows.append(r)
        r += 1

    # Grand total row
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=7)
    c = ws.cell(row=r, column=2, value='TOTAL PROGRAMME — Year 1 (VAT included)')
    c.fill = fill(C_PRIMARY_DARK)
    c.font = font(size=11, bold=True, color=C_WHITE)
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    ws.merge_cells(start_row=r, start_column=8, end_row=r, end_column=9)
    c = ws.cell(row=r, column=8, value='=SUM_GRAND_VND')
    c.fill = fill(C_ACCENT)
    c.font = font(size=12, bold=True, color=C_PRIMARY_DARK)
    c.alignment = align('right', 'center', indent=1)
    c.number_format = '#,##0 [$₫-vi-VN]'
    c.border = BORDER_BOX
    c = ws.cell(row=r, column=10, value='=SUM_GRAND_USD')
    c.fill = fill(C_ACCENT)
    c.font = font(size=12, bold=True, color=C_PRIMARY_DARK)
    c.alignment = align('right', 'center', indent=1)
    c.number_format = '"$"#,##0'
    c.border = BORDER_BOX
    ws.row_dimensions[r].height = 28
    r += 2

    # ── DELIVERY ROADMAP
    section_header(ws, r, (2, 10), '  05 · DELIVERY ROADMAP')
    r += 1
    roadmap = [
        ('M0', 'Discovery & Foundation',         'Weeks 1-2',  'Sitemap signoff · Content audit · Brand narrative outline'),
        ('M1', 'Design',                         'Weeks 3-8',  'Design system + 14 visual templates approved'),
        ('M2', 'Build',                          'Weeks 9-14', 'Front-end · Back-end · CMS · Multi-language operational'),
        ('M3', 'Integration',                    'Weeks 15-18','VNPay · Hotel Link/Smile · 360° · Live chat · Analytics live'),
        ('M4', 'QA, UAT & Launch',               'Weeks 19-20','301 redirects · Security · Go-live · 4-week hypercare'),
        ('M5+','Hosting & Managed Services',     '12 Months',  'SLA-backed support · backups · monitoring · monthly reports'),
    ]
    hh = ['Milestone', 'Phase', 'Duration', 'Key Deliverables']
    hh_spans = [(2, 2), (3, 5), (6, 6), (7, 10)]
    for h, (cs, ce) in zip(hh, hh_spans):
        if cs != ce:
            ws.merge_cells(start_row=r, start_column=cs, end_row=r, end_column=ce)
        c = ws.cell(row=r, column=cs, value=h)
        c.fill = fill(C_PRIMARY)
        c.font = font(size=10, bold=True, color=C_WHITE)
        c.alignment = align('center', 'center')
        c.border = BORDER_BOX
    ws.row_dimensions[r].height = 22
    r += 1
    for ms, phase, dur, deliv in roadmap:
        ws.cell(row=r, column=2, value=ms).font = font(size=11, bold=True, color=C_ACCENT)
        ws.cell(row=r, column=2).alignment = align('center', 'center')
        ws.cell(row=r, column=2).border = BORDER_BOX
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=5)
        c = ws.cell(row=r, column=3, value=phase)
        c.font = font(size=10, bold=True, color=C_TEXT)
        c.alignment = align('left', 'center', indent=1)
        c.border = BORDER_BOX
        c = ws.cell(row=r, column=6, value=dur)
        c.font = font(size=10, color=C_GREY_DARK)
        c.alignment = align('center', 'center')
        c.border = BORDER_BOX
        ws.merge_cells(start_row=r, start_column=7, end_row=r, end_column=10)
        c = ws.cell(row=r, column=7, value=deliv)
        c.font = font(size=9, color=C_TEXT)
        c.alignment = align('left', 'center', wrap=True, indent=1)
        c.border = BORDER_BOX
        ws.row_dimensions[r].height = 26
        r += 1


# ============================================================
# SHEET 3 — SCOPE OF WORK
# ============================================================
def build_scope(wb):
    ws = wb.create_sheet('3. Scope of Work')
    ws.sheet_view.showGridLines = False
    ws.sheet_properties.tabColor = C_PRIMARY

    set_widths(ws, {'A': 2, 'B': 6, 'C': 32, 'D': 60, 'E': 30, 'F': 2})
    repeat_brand_header(ws, ('B', 'E'), title='Scope of Work — Detailed Deliverables')

    # Sub-intro
    r = 5
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5)
    c = ws.cell(row=r, column=2,
                value=('  The scope below is organised by workstream. Each line is a discrete '
                       'deliverable with a defined acceptance output. All items are included in '
                       'the Phase 1 investment unless explicitly marked optional.'))
    c.font = font(size=10, italic=True, color=C_GREY_DARK)
    c.alignment = align('left', 'center', wrap=True)
    ws.row_dimensions[r].height = 36
    r += 2

    # Header
    headers = ['#', 'Deliverable', 'Description', 'Acceptance Output']
    for col_idx, val in enumerate(headers, start=2):
        c = ws.cell(row=r, column=col_idx, value=val)
        c.fill = fill(C_PRIMARY)
        c.font = font(size=10, bold=True, color=C_WHITE)
        c.alignment = align('center', 'center')
        c.border = BORDER_BOX
    ws.row_dimensions[r].height = 22
    r += 1

    sections = [
        ('A · DISCOVERY & BRAND FOUNDATION', [
            ('A.1', 'Stakeholder workshops & content audit',
             'On-site discovery with property GMs, marketing, IT, revenue. Inventory and quality-grade all assets across 4 legacy domains.',
             'Discovery report + asset inventory'),
            ('A.2', 'Information architecture & sitemap',
             'Master sitemap for 1 brand × 3 properties × 3 languages. URL strategy (clean, property-scoped, hreflang-ready).',
             'Approved sitemap + URL map'),
            ('A.3', 'Brand narrative & content strategy',
             'Brand storyline anchored on "Lost in nature, founding you" — nature, stillness, healing, enduring love. Tone guidelines, voice rules, lexicon.',
             'Brand narrative doc + tone guide'),
            ('A.4', 'Design system & component library',
             'Typography, colour, photographic mood, iconography, UI components (cards, hero, navigation, forms, modals).',
             'Figma design system file'),
        ]),
        ('B · PAGE TEMPLATES — BRAND HOME', [
            ('B.1', 'Brand Home (master)',
             'Sticky header · Full-screen hero video · Brand narrative block · 3 property gateways · 3 experience pillars · Featured offers grid · Audience-segment quick links · Gallery teaser · Blog & newsletter · Footer.',
             'Responsive template — VI/EN/KO'),
        ]),
        ('C · PAGE TEMPLATES — GOLF PROPERTY', [
            ('C.1', 'Golf overview & sub-pages',
             '6 blocks: Hero · Course intro · 18-hole / Coaching / Club House · Golf-lifestyle experiences · Gallery + 360° · Final CTA. Club House nested children (Restaurant · Rooms · Pro Shop).',
             'Responsive template + 3 sub-pages'),
        ]),
        ('D · PAGE TEMPLATES — SWISS-BELRESORT', [
            ('D.1', 'Resort overview',
             '7 blocks: Hero + Swiss-Bel identity · 151-room intro · Room grid · Spa & Wellness · Dining · MICE · Experiences · Gallery + 360° · Final CTA.',
             'Responsive template'),
            ('D.2', 'Room Type pages (×7)',
             'Deluxe Mountain View · Deluxe Golf View · Studio Mountain View · Family Deluxe Mountain View · King Suite Mountain View · Royal Suite Mountain View · Standard.',
             '7 detail templates with 360°'),
            ('D.3', 'Spa & Wellness',  'Curated wellness journeys, not service list.', 'Sub-page'),
            ('D.4', 'Dining',          'Restaurant & bar storytelling, menu module.', 'Sub-page'),
            ('D.5', 'MICE & Events',   'Venue specs, capacity tables, RFP form.', 'Sub-page + lead form'),
        ]),
        ('E · PAGE TEMPLATES — VILLA', [
            ('E.1', 'Villa teaser (Coming Soon)',
             'Brand storytelling, "Love Trekk-in / Forest Service Hub" narrative, lead-capture form. No live booking.',
             'Responsive template'),
            ('E.2', 'Villa Room Type design templates (×5)',
             'Standard · Deluxe Lake View · Deluxe Garden View · Suite Lake View · (1 reserve). Design only; build deferred until soft launch.',
             '5 Figma templates (design-only)'),
        ]),
        ('F · SHARED PAGES', [
            ('F.1', 'About Us — brand story',         'Master-brand origin, founding philosophy, leadership.', 'Template'),
            ('F.2', 'Experiences (unified)',          'Wellness · Golf lifestyle · Healing — three editorial pillars shared across properties.', 'Template + CMS taxonomy'),
            ('F.3', 'Offers & Packages',              'Filterable by property and audience; experience-led naming (no discount-only).', 'Template + filtering UI'),
            ('F.4', 'Blog / News — list',             'CMS-driven, 3-pillar taxonomy, infinite-scroll or pagination.', 'Template'),
            ('F.5', 'Blog / News — article',          'SEO-optimised, social-share, related cross-sells to properties & offers.', 'Template'),
            ('F.6', 'Careers',                        'Open positions list, structured-data JobPosting, application form.', 'Template'),
            ('F.7', 'Contact',                        'Property-routed forms, map, hotline, Zalo/Messenger, contact-by-purpose.', 'Template + 3 forms'),
            ('F.8', 'Search',                         'Site-wide search across properties, offers, blog. Suggestion + filter.', 'Search module + index'),
            ('F.9', 'Information pages',              'Privacy policy, Terms, Cookie policy, 404, FAQ.', '5 templates'),
        ]),
        ('G · BOOKING INTEGRATIONS', [
            ('G.1', 'Golf → VNPay',
             'Tee-time selection · greens-fee calc · VNPay payment · email confirmation · PMS push (data spec to be confirmed by VNPay).',
             'End-to-end booking flow live'),
            ('G.2', 'Swiss-Belresort → Hotel Link → Smile PMS',
             'Real-time availability & rate from Hotel Link channel manager; Smile PMS reservation push; booking confirmation; restorable PMS direct connection.',
             'End-to-end booking flow live'),
            ('G.3', 'Persistent booking widget',
             'Sticky top-right CTA contextual per property ("Book Tee Time" / "Book Room"). Survives scroll.',
             'Sticky widget across all pages'),
            ('G.4', 'Villa lead capture',
             'Newsletter form + interest form for villa launch waitlist; pushed to CRM/CSV export.',
             'Lead capture + 3rd-party feed'),
        ]),
        ('H · MULTI-LANGUAGE (VI / EN / KO)', [
            ('H.1', 'Translation framework',
             'Per-language URL structure (/vi /en /ko), language switcher, fallback rules, hreflang tags, locale-aware date/currency.',
             'Multi-language infrastructure'),
            ('H.2', 'Swiss-Bel identity priority for EN/KO',
             'Co-branded header on EN/KO surfaces "Swiss-Belresort Tuyen Lam" prominently for inbound brand recognition.',
             'Conditional branding rules'),
            ('H.3', 'Translation memory hand-off',
             'Translation export/import workflow (XLIFF or CSV) for SAM\'s translation vendor. Vendor work-out-of-scope.',
             'Translation tooling docs'),
        ]),
        ('I · CONTENT MANAGEMENT SYSTEM', [
            ('I.1', 'Headless / hybrid CMS setup',
             'Property pages set to static (admin-only); marketing-managed content (Offers, Blog, News, banners, pop-ups, gallery) freely editable.',
             'CMS instance + admin roles'),
            ('I.2', 'Role-based access control',
             'Roles: Super-admin, Property Editor, Marketing, Translator, Read-only. Audit log.',
             'RBAC + audit'),
            ('I.3', 'Featured Offers Cards engine',
             'Schedule offers, target by property/audience, A/B variant slots, expiry control.',
             'Offers module'),
            ('I.4', 'Pop-up Campaign engine',
             'Large center modal + small left slide-in; schedule, target by URL/segment, frequency capping, dismiss persistence.',
             'Pop-up module'),
            ('I.5', 'Newsletter integration',
             'Form capture → Mailchimp / SendGrid / Klaviyo (one provider). Double opt-in. (Email vendor account by client.)',
             'Newsletter integration live'),
        ]),
        ('J · SEO & ANALYTICS', [
            ('J.1', 'Technical SEO baseline',
             'Clean URLs · canonical · meta/OG · Open Graph images · sitemap.xml · robots.txt · hreflang · breadcrumb schema.',
             'SEO audit report (green)'),
            ('J.2', 'Schema markup (Hotel, Golf, Restaurant, Event)',
             'Structured data per property type for richer SERP snippets.',
             'Schema validation pass'),
            ('J.3', 'Google Analytics 4 + GTM',
             'GA4 property, GTM container, event taxonomy, booking-funnel events, source/medium taxonomy.',
             'GA4 + GTM live, events firing'),
            ('J.4', 'Heatmap & session replay',
             'Hotjar or Microsoft Clarity tag on key templates; sample size guidance.',
             'Tag live · sample dashboard'),
            ('J.5', '301 redirect map',
             'Full URL-by-URL map from 4 legacy domains to new URLs; bulk redirect rules; 404 catch & monitoring.',
             '301 map + 404 monitor (90 days)'),
        ]),
        ('K · PERFORMANCE, ACCESSIBILITY & TRUST', [
            ('K.1', 'Core Web Vitals optimisation',
             'LCP/INP/CLS green on mobile & desktop for top 10 templates. AVIF/WebP image pipeline. Lazy-load. Critical CSS.',
             'Lighthouse ≥ 90 mobile/desktop'),
            ('K.2', 'WCAG 2.1 AA accessibility',
             'Colour contrast, focus state, keyboard nav, ARIA roles for nav/modals/carousels, alt text framework.',
             'Accessibility audit pass'),
            ('K.3', 'Trust signal layer',
             'Award badges (Swiss-Bel certifications, golf awards), review aggregator widget, partner logos.',
             'Trust components in CMS'),
            ('K.4', 'Browser & device support matrix',
             'Modern evergreen browsers (Chrome, Edge, Safari, Firefox latest-2); iOS 15+, Android 10+. IE not supported.',
             'Documented support matrix'),
        ]),
        ('L · SECURITY & COMPLIANCE', [
            ('L.1', 'Security hardening (OWASP Top 10)',
             'Input validation, output encoding, CSRF, secure session, security headers, dependency scanning. Closes posture issues from prior incident.',
             'OWASP checklist signed off'),
            ('L.2', 'Web Application Firewall + DDoS',
             'Cloudflare WAF or equivalent, rate-limit rules, bot mitigation.',
             'WAF rules live'),
            ('L.3', 'Privacy & cookie compliance',
             'Cookie consent banner (Vietnam PDPL + GDPR-aware EU/KR), preference center, privacy policy templates VI/EN/KO.',
             'Cookie consent live + policy'),
            ('L.4', 'Backup & disaster recovery',
             'Daily automated backups, weekly off-site, documented RTO/RPO (4h / 24h), restore tested.',
             'Backup runbook + restore drill'),
            ('L.5', 'Legacy site archive',
             'Static archive of 4 legacy sites + media (read-only) for compliance/historical reference before redirect cutover.',
             'Cold-storage archive bundle'),
        ]),
        ('M · 360° VR INTEGRATION', [
            ('M.1', 'VR media re-integration',
             'Existing samtuyenlam.com.vn 360° media re-mounted as tab/modules inside Room Type pages, Property Galleries, and Experience pages. No standalone VR site.',
             'VR module embedded in 4+ pages'),
        ]),
        ('N · LIVE CHAT', [
            ('N.1', 'Zalo OA + Facebook Messenger',
             'Persistent floating widget across all pages; conversation routing per property.',
             'Live chat widget live'),
        ]),
        ('O · DOMAIN MIGRATION', [
            ('O.1', 'Domain cutover plan',
             'DNS swap, SSL provisioning, redirect deployment, search-console reverification across 4 legacy domains. 90-day monitoring of 404s & rankings.',
             'Cutover runbook executed'),
        ]),
        ('P · QA, UAT & LAUNCH', [
            ('P.1', 'Cross-browser & device QA',
             'Test matrix: 5 browsers × 3 device classes × 3 languages = 45 surfaces.',
             'QA report (zero P1/P2 open)'),
            ('P.2', 'Booking-flow end-to-end test',
             '3 booking systems × 3 user scenarios each = 9 happy-path + 6 edge-case scenarios.',
             'Booking QA sign-off'),
            ('P.3', 'UAT support',
             'Two structured UAT cycles with client team; bug triage; defect resolution.',
             'UAT sign-off'),
            ('P.4', 'Go-live & launch monitoring',
             'Coordinated go-live, real-time monitoring, rollback plan ready.',
             'Successful launch'),
        ]),
        ('Q · TRAINING & KNOWLEDGE TRANSFER', [
            ('Q.1', 'CMS training workshops',
             'Two half-day sessions for marketing team: content publishing, offers/pop-ups, blog, media library.',
             'Trained team + recordings'),
            ('Q.2', 'Admin & operations handbook',
             'Written guides: CMS, deployment, backup/restore, escalation paths.',
             'Operations handbook (PDF)'),
            ('Q.3', 'Source code & asset handover',
             'Git repository transfer, design files, infrastructure-as-code, credential vault hand-off.',
             'Repository + key handover'),
        ]),
        ('R · POST-LAUNCH HYPERCARE', [
            ('R.1', '4-week intensive hypercare',
             'Dedicated team on stand-by post-launch: bug triage <4h response, daily health checks, weekly status call.',
             'Stability sign-off after week 4'),
        ]),
    ]

    item_counter = 0
    for section_title, items in sections:
        # Section banner
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5)
        c = ws.cell(row=r, column=2, value=f'  {section_title}')
        c.fill = fill(C_GREY_DARK)
        c.font = font(size=10, bold=True, color=C_WHITE)
        c.alignment = align('left', 'center')
        c.border = BORDER_BOX
        ws.row_dimensions[r].height = 22
        r += 1

        for ref, deliv, desc, output in items:
            ws.cell(row=r, column=2, value=ref)
            ws.cell(row=r, column=2).font = font(size=10, bold=True, color=C_ACCENT)
            ws.cell(row=r, column=2).alignment = align('center', 'top')
            ws.cell(row=r, column=2).border = BORDER_BOX

            ws.cell(row=r, column=3, value=deliv)
            ws.cell(row=r, column=3).font = font(size=10, bold=True, color=C_TEXT)
            ws.cell(row=r, column=3).alignment = align('left', 'top', wrap=True, indent=1)
            ws.cell(row=r, column=3).border = BORDER_BOX

            ws.cell(row=r, column=4, value=desc)
            ws.cell(row=r, column=4).font = font(size=9, color=C_GREY_DARK)
            ws.cell(row=r, column=4).alignment = align('left', 'top', wrap=True, indent=1)
            ws.cell(row=r, column=4).border = BORDER_BOX

            ws.cell(row=r, column=5, value=output)
            ws.cell(row=r, column=5).font = font(size=9, italic=True, color=C_SUCCESS)
            ws.cell(row=r, column=5).alignment = align('left', 'top', wrap=True, indent=1)
            ws.cell(row=r, column=5).border = BORDER_BOX

            ws.row_dimensions[r].height = max(38, 14 + max(len(desc), len(output)) // 4)
            r += 1
            item_counter += 1


# ============================================================
# SHEET 4 — PRICING (BUILD)
# ============================================================
def build_pricing_build(wb):
    ws = wb.create_sheet('4. Pricing — Build')
    ws.sheet_view.showGridLines = False
    ws.sheet_properties.tabColor = C_ACCENT

    set_widths(ws, {'A': 2, 'B': 22, 'C': 38, 'D': 7, 'E': 8, 'F': 8, 'G': 7,
                     'H': 9, 'I': 18, 'J': 13, 'K': 9, 'L': 38, 'M': 2})

    repeat_brand_header(ws, ('B', 'L'),
                         title='Phase 1 — Design, Build & Launch — Detailed Pricing')

    # Pricing assumptions strip
    r = 5
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=12)
    c = ws.cell(row=r, column=2,
                value=(f'  Blended rate: {RATE_USD_HOUR} USD / hour  ·  '
                       f'FX reference: 1 USD = {FX_VND_USD:,} VND  ·  '
                       f'Hour cost: {int(RATE_USD_HOUR * FX_VND_USD):,} VND/h  ·  '
                       f'All figures incl. 10% VAT in Grand Total'))
    c.fill = fill(C_ACCENT_LITE)
    c.font = font(size=9, italic=True, color=C_GREY_DARK)
    c.alignment = align('left', 'center')
    ws.row_dimensions[r].height = 22
    r += 2

    # Table header (2-row merged)
    # Workstream | Deliverable | EFFORT (BA Design Dev PM Total) | Price VND | Price USD | Qty | Notes
    ws.merge_cells(start_row=r, start_column=2, end_row=r+1, end_column=2)
    ws.cell(row=r, column=2, value='WORKSTREAM')
    ws.merge_cells(start_row=r, start_column=3, end_row=r+1, end_column=3)
    ws.cell(row=r, column=3, value='DELIVERABLE')
    ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=8)
    ws.cell(row=r, column=4, value='EFFORT (HOURS)')
    ws.merge_cells(start_row=r, start_column=9, end_row=r+1, end_column=9)
    ws.cell(row=r, column=9, value='PRICE (VND)')
    ws.merge_cells(start_row=r, start_column=10, end_row=r+1, end_column=10)
    ws.cell(row=r, column=10, value='PRICE (USD)')
    ws.merge_cells(start_row=r, start_column=11, end_row=r+1, end_column=11)
    ws.cell(row=r, column=11, value='QTY')
    ws.merge_cells(start_row=r, start_column=12, end_row=r+1, end_column=12)
    ws.cell(row=r, column=12, value='NOTES')
    for col in [2, 3, 4, 9, 10, 11, 12]:
        c = ws.cell(row=r, column=col)
        c.fill = fill(C_PRIMARY)
        c.font = font(size=10, bold=True, color=C_WHITE)
        c.alignment = align('center', 'center')
        c.border = BORDER_BOX
    ws.row_dimensions[r].height = 22

    # Sub-header row
    for col, lbl in zip(range(4, 9), ['BA', 'DESIGN', 'DEV', 'PM', 'TOTAL']):
        c = ws.cell(row=r+1, column=col, value=lbl)
        c.fill = fill(C_GREY_DARK)
        c.font = font(size=9, bold=True, color=C_WHITE)
        c.alignment = align('center', 'center')
        c.border = BORDER_BOX
    ws.row_dimensions[r+1].height = 18
    r += 2

    # ============ DATA ROWS ============
    # (workstream, deliverable, BA, Design, Dev, PM, qty, note)
    # qty can be int OR "One-time" (no billing)
    data = [
        # === A. DISCOVERY & FOUNDATION ===
        ('A. Discovery & Foundation', 'Stakeholder workshops & content audit',
         16, None, None, 6, 1,
         'Multi-day on-site discovery + audit across 4 legacy domains.'),
        (None, 'Information architecture & sitemap',
         12, 8, None, 4, 1,
         'Sitemap, URL strategy, hreflang map.'),
        (None, 'Brand narrative & content strategy',
         12, 8, None, 4, 1,
         'Voice, tone, lexicon; "Lost in nature, founding you" big idea.'),
        (None, 'Design system & component library',
         None, 60, 16, 8, 1,
         'Figma system: typography, colour, components, dark/light tokens.'),

        # === B. BRAND HOME ===
        ('B. Brand Home', 'Brand Home — master template (10 blocks)',
         8, 56, 48, 6, 1,
         'Hero video, brand narrative, 3 gateways, 3 pillars, offers, audience links, gallery, blog, newsletter, footer.'),

        # === C. GOLF PROPERTY ===
        ('C. Golf Property', 'Golf property overview (6 blocks)',
         6, 32, 28, 4, 1,
         'Hero · Course intro · 18-Hole/Coaching/Club House · Lifestyle · Gallery + 360° · CTA.'),
        (None, 'Club House sub-pages (Restaurant · Rooms · Pro Shop)',
         2, 18, 16, 3, 3,
         '3 sub-templates.'),

        # === D. SWISS-BELRESORT ===
        ('D. Swiss-Belresort', 'Resort property overview (7 blocks)',
         8, 40, 32, 6, 1,
         'Hero w/ Swiss-Bel identity · 151-room intro · Room grid · Spa · Dining · MICE · Experiences · Gallery · CTA.'),
        (None, 'Room Type detail pages',
         3, 24, 18, 3, 7,
         '7 room types: Deluxe MV/GV, Studio MV, Family Deluxe, King Suite, Royal Suite, Standard.'),
        (None, 'Spa & Wellness sub-page',
         2, 16, 12, 2, 1,
         'Curated wellness journeys, not service list.'),
        (None, 'Dining sub-page',
         2, 12, 10, 2, 1,
         'Restaurant & bar storytelling, menu module.'),
        (None, 'MICE & Events sub-page',
         3, 16, 14, 3, 1,
         'Venue specs, capacity, RFP form.'),

        # === E. VILLA ===
        ('E. Villa (deferred launch)', 'Villa teaser (Coming Soon) + lead form',
         4, 16, 12, 2, 1,
         'No live booking. Brand storytelling + waitlist capture.'),
        (None, 'Villa Room Type design templates (design-only)',
         2, 16, None, 2, 5,
         'Standard, Deluxe Lake/Garden View, Suite Lake View, +1. Build deferred.'),

        # === F. SHARED PAGES ===
        ('F. Shared Pages', 'About Us — brand story',
         4, 16, 12, 2, 1, None),
        (None, 'Experiences (Wellness · Golf · Healing)',
         4, 20, 18, 2, 1, '3 editorial pillars shared across properties.'),
        (None, 'Offers & Packages — filterable',
         4, 20, 22, 2, 1, 'Filter by property × audience; CMS-driven cards.'),
        (None, 'Blog / News — listing',
         2, 14, 18, 2, 1, None),
        (None, 'Blog / News — article detail',
         2, 12, 12, 2, 1, None),
        (None, 'Careers (with JobPosting schema)',
         2, 12, 14, 2, 1, None),
        (None, 'Contact — property-routed forms (×3)',
         2, 14, 18, 2, 1, 'Map, hotline, Zalo/Messenger embed.'),
        (None, 'Search — site-wide',
         2, 10, 22, 2, 1, 'Cross-property search index.'),
        (None, 'Information pages (Privacy/Terms/Cookie/404/FAQ)',
         None, 8, 8, 1, 'One-time',
         '5 templates · mostly text.'),

        # === G. BOOKING INTEGRATIONS ===
        ('G. Booking Integrations', 'Golf → VNPay payment flow',
         6, None, 32, 4, 1,
         'Tee-time, fee calc, VNPay, confirmation, PMS push.'),
        (None, 'Swiss-Belresort → Hotel Link → Smile PMS',
         8, None, 40, 6, 1,
         'Real-time avail/rate, reservation push, confirmation.'),
        (None, 'Persistent booking widget (sticky)',
         2, 6, 12, 2, 1,
         'Top-right sticky CTA contextual per property.'),
        (None, 'Villa lead capture → CRM/CSV',
         2, None, 10, 2, 1,
         'Form + webhook to client CRM.'),

        # === H. MULTI-LANGUAGE ===
        ('H. Multi-language', 'Multi-language framework (VI/EN/KO)',
         4, 8, 36, 4, 1,
         'URL structure, switcher, hreflang, locale-aware formatting.'),
        (None, 'Swiss-Bel identity priority (EN/KO)',
         2, 6, 10, 2, 1,
         'Conditional branding for inbound EN/KO traffic.'),
        (None, 'Translation memory hand-off (XLIFF/CSV)',
         2, None, 8, 1, 1,
         'Vendor work-out-of-scope.'),

        # === I. CMS ===
        ('I. CMS', 'CMS setup (headless/hybrid) + DB structure',
         12, None, 28, 6, 1,
         'Multi-property data model, multi-language entries, media library.'),
        (None, 'Role-based access control + audit log',
         8, None, 12, 2, 1,
         'Super-admin, Property Editor, Marketing, Translator, Read-only.'),
        (None, 'Featured Offers Cards engine',
         4, 8, 18, 2, 1,
         'Schedule, target, A/B variants, expiry.'),
        (None, 'Pop-up Campaign engine',
         4, 8, 22, 2, 1,
         'Large center modal + small left slide-in; schedule, target, frequency cap.'),
        (None, 'Newsletter integration (one provider)',
         2, 4, 12, 2, 1,
         'Mailchimp/SendGrid/Klaviyo. Vendor account by client.'),
        (None, 'Content & media migration plan',
         8, None, 12, 2, 'One-time',
         'Mapping from 4 legacy sites; asset re-encoding.'),

        # === J. SEO & ANALYTICS ===
        ('J. SEO & Analytics', 'Technical SEO baseline',
         4, None, 20, 2, 1,
         'Canonical, meta/OG, sitemap.xml, robots.txt, breadcrumb schema, hreflang.'),
        (None, 'Schema markup (Hotel · Golf · Restaurant · Event)',
         2, None, 14, 2, 1,
         'Structured data for rich SERP snippets.'),
        (None, 'GA4 + GTM event taxonomy',
         3, None, 14, 2, 1,
         'Booking-funnel events, source/medium, custom dimensions.'),
        (None, 'Heatmap & session replay (Hotjar/Clarity)',
         1, None, 6, 1, 1, None),
        (None, '301 redirect map (URL-by-URL)',
         8, None, 16, 4, 1,
         'Map across 4 legacy domains + bulk rules.'),

        # === K. PERFORMANCE & ACCESSIBILITY ===
        ('K. Performance & A11y', 'Core Web Vitals optimisation',
         2, 4, 24, 3, 1,
         'LCP/INP/CLS green; AVIF/WebP pipeline; critical CSS.'),
        (None, 'WCAG 2.1 AA accessibility',
         4, 6, 18, 3, 1,
         'Contrast, focus, keyboard nav, ARIA, alt-text framework.'),
        (None, 'Trust signal layer (awards · Swiss-Bel · reviews)',
         2, 8, 12, 2, 1,
         'CMS-managed badges & review aggregator widget.'),

        # === L. SECURITY & COMPLIANCE ===
        ('L. Security & Compliance',
         'Security hardening (OWASP Top 10)',
         3, None, 18, 3, 1,
         'Closes posture issues from prior incident.'),
        (None, 'WAF + DDoS protection configuration',
         1, None, 8, 2, 1, None),
        (None, 'Cookie consent + privacy policy (VI/EN/KO)',
         3, 4, 14, 2, 1,
         'Vietnam PDPL + GDPR-aware preference center.'),
        (None, 'Backup & DR runbook + restore drill',
         2, None, 10, 2, 'One-time',
         'RTO 4h / RPO 24h; restore drill before go-live.'),
        (None, 'Legacy site archive (4 domains, read-only)',
         2, None, 12, 2, 'One-time',
         'Static snapshot + media bundle for compliance.'),

        # === M. 360° VR ===
        ('M. 360° VR', '360° VR re-integration into property pages',
         6, None, 36, 6, 1,
         'Embed existing media as tabs/modules in Room Type + Gallery + Experiences.'),

        # === N. LIVE CHAT ===
        ('N. Live Chat', 'Zalo OA + Facebook Messenger widget',
         2, 4, 10, 2, 1, None),

        # === O. MIGRATION ===
        ('O. Migration', 'Domain cutover plan + 90-day 404 monitor',
         4, None, 20, 6, 1,
         'DNS, SSL, redirect deploy, search-console reverification.'),

        # === P. QA, UAT & LAUNCH ===
        ('P. QA & Launch',
         'Cross-browser & device QA (45 surfaces)',
         8, None, 28, 4, 1,
         '5 browsers × 3 device classes × 3 languages.'),
        (None, 'Booking-flow end-to-end QA (15 scenarios)',
         6, None, 18, 3, 1, None),
        (None, 'UAT support (2 cycles)',
         8, None, 16, 6, 1, None),
        (None, 'Go-live & launch monitoring',
         2, None, 12, 4, 'One-time',
         'Coordinated go-live; rollback plan ready.'),

        # === Q. TRAINING ===
        ('Q. Training & Handover',
         'CMS training workshops (×2 half-day)',
         4, None, 6, 4, 1,
         'Recorded sessions for marketing team.'),
        (None, 'Admin & operations handbook',
         8, 4, 4, 2, 'One-time',
         'PDF + searchable web doc.'),
        (None, 'Source code + asset handover',
         2, None, 6, 2, 'One-time',
         'Git transfer, infra-as-code, credential vault.'),

        # === R. HYPERCARE ===
        ('R. Post-launch Hypercare',
         '4-week intensive hypercare',
         6, None, 32, 12, 1,
         '<4h response, daily health checks, weekly status call.'),
    ]

    data_start = r
    workstream_groups = {}  # for merging schedule column
    for row_data in data:
        workstream, deliv, ba, design, dev, pm, qty, note = row_data
        # Workstream tracking
        if workstream:
            workstream_groups[r] = {'name': workstream, 'count': 1}
            c = ws.cell(row=r, column=2, value=workstream)
            c.fill = fill(C_GREY_LITE)
            c.font = font(size=10, bold=True, color=C_PRIMARY)
            c.alignment = align('left', 'center', indent=1)
        else:
            last_key = max(workstream_groups.keys())
            workstream_groups[last_key]['count'] += 1

        # Deliverable
        c = ws.cell(row=r, column=3, value=deliv)
        c.font = font(size=10, color=C_TEXT)
        c.alignment = align('left', 'center', wrap=True, indent=1)

        # Hours
        for col_idx, val in zip([4, 5, 6, 7], [ba, design, dev, pm]):
            if val is not None:
                c = ws.cell(row=r, column=col_idx, value=val)
                c.font = font(size=10, color=C_TEXT)
                c.alignment = align('center', 'center')

        # Total
        c = ws.cell(row=r, column=8, value=f'=SUM(D{r}:G{r})')
        c.font = font(size=10, bold=True, color=C_GREY_DARK)
        c.alignment = align('center', 'center')

        # Price
        if isinstance(qty, int):
            c = ws.cell(row=r, column=9,
                         value=f'=H{r}*{RATE_USD_HOUR}*{FX_VND_USD}*K{r}')
            c.number_format = '#,##0 [$₫-vi-VN]'
            c.font = font(size=10, color=C_TEXT)
            c.alignment = align('right', 'center', indent=1)

            c = ws.cell(row=r, column=10, value=f'=I{r}/{FX_VND_USD}')
            c.number_format = '"$"#,##0'
            c.font = font(size=9, color=C_GREY_MID)
            c.alignment = align('right', 'center', indent=1)

            c = ws.cell(row=r, column=11, value=qty)
            c.font = font(size=10, color=C_TEXT)
            c.alignment = align('center', 'center')
        else:
            for col_idx in [9, 10]:
                c = ws.cell(row=r, column=col_idx, value='—')
                c.font = font(size=10, color=C_GREY_MID)
                c.alignment = align('center', 'center')
            c = ws.cell(row=r, column=11, value=qty)
            c.font = font(size=9, italic=True, color=C_GREY_MID)
            c.alignment = align('center', 'center')

        # Note
        if note:
            c = ws.cell(row=r, column=12, value=note)
            c.font = font(size=9, italic=True, color=C_GREY_MID)
            c.alignment = align('left', 'top', wrap=True, indent=1)

        # Borders
        for col_idx in range(2, 13):
            ws.cell(row=r, column=col_idx).border = BORDER_BOX

        ws.row_dimensions[r].height = 38
        r += 1

    data_end = r - 1

    # Merge workstream column
    for start, info in workstream_groups.items():
        if info['count'] > 1:
            ws.merge_cells(start_row=start, start_column=2,
                            end_row=start + info['count'] - 1, end_column=2)
            # Re-apply top alignment after merge
            c = ws.cell(row=start, column=2)
            c.alignment = align('left', 'top', wrap=True, indent=1)

    # ============ TOTALS ============
    r += 1
    subtotal_row = r
    offer_row    = r + 1
    vat_row      = r + 2
    grand_row    = r + 3

    # Subtotal
    ws.merge_cells(start_row=subtotal_row, start_column=2,
                    end_row=subtotal_row, end_column=8)
    c = ws.cell(row=subtotal_row, column=2, value='SUBTOTAL (before discount & VAT)')
    c.fill = fill(C_GREY_LITE)
    c.font = font(size=11, bold=True, color=C_GREY_DARK)
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    c = ws.cell(row=subtotal_row, column=9,
                 value=f'=SUM(I{data_start}:I{data_end})')
    c.fill = fill(C_GREY_LITE)
    c.font = font(size=11, bold=True, color=C_GREY_DARK)
    c.number_format = '#,##0 [$₫-vi-VN]'
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    c = ws.cell(row=subtotal_row, column=10, value=f'=I{subtotal_row}/{FX_VND_USD}')
    c.fill = fill(C_GREY_LITE)
    c.font = font(size=10, bold=True, color=C_GREY_DARK)
    c.number_format = '"$"#,##0'
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    ws.merge_cells(start_row=subtotal_row, start_column=11,
                    end_row=subtotal_row, end_column=12)
    ws.cell(row=subtotal_row, column=11).fill = fill(C_GREY_LITE)
    ws.cell(row=subtotal_row, column=11).border = BORDER_BOX
    ws.row_dimensions[subtotal_row].height = 26

    # Offer 15%
    ws.merge_cells(start_row=offer_row, start_column=2,
                    end_row=offer_row, end_column=8)
    c = ws.cell(row=offer_row, column=2, value='Volume discount (15%)')
    c.fill = fill(C_ACCENT_LITE)
    c.font = font(size=10, bold=True, color=C_GREY_DARK)
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    c = ws.cell(row=offer_row, column=9, value=f'=-I{subtotal_row}*0.15')
    c.fill = fill(C_ACCENT_LITE)
    c.font = font(size=10, color=C_DANGER)
    c.number_format = '#,##0 [$₫-vi-VN]'
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    c = ws.cell(row=offer_row, column=10, value=f'=I{offer_row}/{FX_VND_USD}')
    c.fill = fill(C_ACCENT_LITE)
    c.font = font(size=9, color=C_DANGER)
    c.number_format = '"$"#,##0'
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    ws.merge_cells(start_row=offer_row, start_column=11,
                    end_row=offer_row, end_column=12)
    ws.cell(row=offer_row, column=11).fill = fill(C_ACCENT_LITE)
    ws.cell(row=offer_row, column=11).border = BORDER_BOX
    ws.row_dimensions[offer_row].height = 22

    # VAT 10%
    ws.merge_cells(start_row=vat_row, start_column=2,
                    end_row=vat_row, end_column=8)
    c = ws.cell(row=vat_row, column=2, value='VAT (10%)')
    c.fill = fill(C_GREY_LITE)
    c.font = font(size=10, bold=True, color=C_GREY_DARK)
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    c = ws.cell(row=vat_row, column=9, value=f'=(I{subtotal_row}+I{offer_row})*0.1')
    c.fill = fill(C_GREY_LITE)
    c.font = font(size=10, color=C_GREY_DARK)
    c.number_format = '#,##0 [$₫-vi-VN]'
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    c = ws.cell(row=vat_row, column=10, value=f'=I{vat_row}/{FX_VND_USD}')
    c.fill = fill(C_GREY_LITE)
    c.font = font(size=9, color=C_GREY_DARK)
    c.number_format = '"$"#,##0'
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    ws.merge_cells(start_row=vat_row, start_column=11,
                    end_row=vat_row, end_column=12)
    ws.cell(row=vat_row, column=11).fill = fill(C_GREY_LITE)
    ws.cell(row=vat_row, column=11).border = BORDER_BOX
    ws.row_dimensions[vat_row].height = 22

    # GRAND TOTAL
    ws.merge_cells(start_row=grand_row, start_column=2,
                    end_row=grand_row, end_column=8)
    c = ws.cell(row=grand_row, column=2, value='GRAND TOTAL — Phase 1 (VAT included)')
    c.fill = fill(C_PRIMARY_DARK)
    c.font = font(size=12, bold=True, color=C_WHITE)
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    c = ws.cell(row=grand_row, column=9,
                 value=f'=I{subtotal_row}+I{offer_row}+I{vat_row}')
    c.fill = fill(C_ACCENT)
    c.font = font(size=12, bold=True, color=C_PRIMARY_DARK)
    c.number_format = '#,##0 [$₫-vi-VN]'
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    c = ws.cell(row=grand_row, column=10, value=f'=I{grand_row}/{FX_VND_USD}')
    c.fill = fill(C_ACCENT)
    c.font = font(size=11, bold=True, color=C_PRIMARY_DARK)
    c.number_format = '"$"#,##0'
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    ws.merge_cells(start_row=grand_row, start_column=11,
                    end_row=grand_row, end_column=12)
    ws.cell(row=grand_row, column=11).fill = fill(C_ACCENT)
    ws.cell(row=grand_row, column=11).border = BORDER_BOX
    ws.row_dimensions[grand_row].height = 32

    # Defined names for cross-sheet reference
    wb.defined_names['I_GRAND'] = openpyxl.workbook.defined_name.DefinedName(
        'I_GRAND', attr_text=f"'4. Pricing — Build'!$I${grand_row}")
    wb.defined_names['J_GRAND'] = openpyxl.workbook.defined_name.DefinedName(
        'J_GRAND', attr_text=f"'4. Pricing — Build'!$J${grand_row}")

    # Footnote
    r = grand_row + 2
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=12)
    c = ws.cell(row=r, column=2,
                 value=('  Effort estimates apply our blended team rate (Business Analysis, Visual '
                        'Design, Engineering, Project Management). One-time items are fixed-fee. '
                        'Volume discount of 15% reflects programme scale across three properties. '
                        'Grand Total is VAT-inclusive.'))
    c.font = font(size=9, italic=True, color=C_GREY_MID)
    c.alignment = align('left', 'top', wrap=True)
    ws.row_dimensions[r].height = 36


# ============================================================
# SHEET 5 — PRICING (HOSTING & SUPPORT)
# ============================================================
def build_pricing_hosting(wb):
    ws = wb.create_sheet('5. Pricing — Hosting')
    ws.sheet_view.showGridLines = False
    ws.sheet_properties.tabColor = C_ACCENT

    set_widths(ws, {'A': 2, 'B': 24, 'C': 44, 'D': 18, 'E': 14, 'F': 48, 'G': 2})

    repeat_brand_header(ws, ('B', 'F'),
                         title='Phase 2 — Hosting & Managed Services (Year 1)')

    r = 5
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)
    c = ws.cell(row=r, column=2,
                 value=('  Year-1 infrastructure and SLA-backed managed services. '
                        'Hosted on enterprise cloud with daily backups, hardened security posture '
                        '(post-incident baseline), and 20 hours of dedicated technical support per month.'))
    c.fill = fill(C_ACCENT_LITE)
    c.font = font(size=9, italic=True, color=C_GREY_DARK)
    c.alignment = align('left', 'center', wrap=True)
    ws.row_dimensions[r].height = 36
    r += 2

    # Header
    headers = ['WORKSTREAM', 'ITEM', 'PRICE (VND)', 'TERM', 'DESCRIPTION']
    for col_idx, val in enumerate(headers, start=2):
        c = ws.cell(row=r, column=col_idx, value=val)
        c.fill = fill(C_PRIMARY)
        c.font = font(size=10, bold=True, color=C_WHITE)
        c.alignment = align('center', 'center')
        c.border = BORDER_BOX
    ws.row_dimensions[r].height = 22
    r += 1

    data = [
        ('Cloud Infrastructure',
         'Enterprise hosting — multi-site, high-traffic profile',
         f'=2400000*12', '12 Months',
         'CPU 8 cores · RAM 16 GB · SSD 200 GB · daily backup · weekly snapshot'),
        (None,
         'CDN — Cloudflare Pro (global edge, image optimisation)',
         f'=600000*12', '12 Months',
         'Tunes Core Web Vitals; AVIF/WebP; global cache; bot management'),
        (None,
         'SSL Wildcard certificate (all subdomains)',
         0, '12 Months', 'Valued at 1,800,000 ₫ — included at no charge'),
        (None,
         'WAF + DDoS protection (application layer)',
         0, '12 Months',
         'Valued at 5,580,000 ₫ — included at no charge. Mandatory given prior incident posture.'),
        ('Managed Services',
         '20 hours of technical support per month\n'
         '· Managed hosting & SSL\n'
         '· Daily backups + weekly off-site\n'
         '· Security & threat scans (weekly)\n'
         '· Uptime monitoring 99.9% SLA\n'
         '· Performance & SEO on-page tweaks\n'
         '· Priority response < 4 hours\n'
         '· Module configuration & consulting\n'
         '· Source-code & version control\n'
         '· Monthly performance report',
         f'=2200000*12', '12 Months',
         '3 months free at start — valued 6,600,000 ₫'),
        ('Setup',
         'Initial migration & DNS cutover',
         'Free of charge', None,
         'DNS swap from legacy hosts; SSL provisioning; first-deploy.'),
    ]

    workstream_groups = {}
    for row_data in data:
        ws_, item, price, term, desc = row_data
        if ws_:
            workstream_groups[r] = {'name': ws_, 'count': 1}
            c = ws.cell(row=r, column=2, value=ws_)
            c.fill = fill(C_GREY_LITE)
            c.font = font(size=10, bold=True, color=C_PRIMARY)
            c.alignment = align('left', 'top', wrap=True, indent=1)
        else:
            last_key = max(workstream_groups.keys())
            workstream_groups[last_key]['count'] += 1

        c = ws.cell(row=r, column=3, value=item)
        c.font = font(size=10, color=C_TEXT)
        c.alignment = align('left', 'top', wrap=True, indent=1)

        if isinstance(price, str) and price.startswith('='):
            c = ws.cell(row=r, column=4, value=price)
            c.number_format = '#,##0 [$₫-vi-VN]'
            c.font = font(size=10, color=C_TEXT)
            c.alignment = align('right', 'center', indent=1)
        elif isinstance(price, str):
            c = ws.cell(row=r, column=4, value=price)
            c.font = font(size=10, italic=True, color=C_GREY_MID)
            c.alignment = align('center', 'center')
        else:
            c = ws.cell(row=r, column=4, value=price)
            c.number_format = '#,##0 [$₫-vi-VN]'
            c.font = font(size=10, color=C_TEXT)
            c.alignment = align('right', 'center', indent=1)

        if term:
            c = ws.cell(row=r, column=5, value=term)
            c.font = font(size=10, color=C_GREY_DARK)
            c.alignment = align('center', 'center')
        else:
            c = ws.cell(row=r, column=5, value='—')
            c.font = font(size=10, color=C_GREY_MID)
            c.alignment = align('center', 'center')

        if desc:
            c = ws.cell(row=r, column=6, value=desc)
            c.font = font(size=9, italic=True, color=C_GREY_MID)
            c.alignment = align('left', 'top', wrap=True, indent=1)

        for col_idx in range(2, 7):
            ws.cell(row=r, column=col_idx).border = BORDER_BOX

        # Dynamic row height
        if ws_ == 'Managed Services':
            ws.row_dimensions[r].height = 160
        else:
            ws.row_dimensions[r].height = 38
        r += 1

    data_end = r - 1
    # Merge workstream column
    for start, info in workstream_groups.items():
        if info['count'] > 1:
            ws.merge_cells(start_row=start, start_column=2,
                            end_row=start + info['count'] - 1, end_column=2)

    # Totals
    subtotal_row = r + 1
    offer_row    = subtotal_row + 1
    vat_row      = offer_row + 1
    grand_row    = vat_row + 1

    # Subtotal
    ws.merge_cells(start_row=subtotal_row, start_column=2,
                    end_row=subtotal_row, end_column=3)
    c = ws.cell(row=subtotal_row, column=2, value='SUBTOTAL (before discount & VAT)')
    c.fill = fill(C_GREY_LITE)
    c.font = font(size=11, bold=True, color=C_GREY_DARK)
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    c = ws.cell(row=subtotal_row, column=4,
                 value=f'=SUM(D10:D{data_end})')
    c.fill = fill(C_GREY_LITE)
    c.font = font(size=11, bold=True, color=C_GREY_DARK)
    c.number_format = '#,##0 [$₫-vi-VN]'
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    ws.merge_cells(start_row=subtotal_row, start_column=5,
                    end_row=subtotal_row, end_column=6)
    ws.cell(row=subtotal_row, column=5).fill = fill(C_GREY_LITE)
    ws.cell(row=subtotal_row, column=5).border = BORDER_BOX
    ws.row_dimensions[subtotal_row].height = 24

    # Offer 12.5%
    ws.merge_cells(start_row=offer_row, start_column=2,
                    end_row=offer_row, end_column=3)
    c = ws.cell(row=offer_row, column=2, value='Loyalty discount (12.5%)')
    c.fill = fill(C_ACCENT_LITE)
    c.font = font(size=10, bold=True, color=C_GREY_DARK)
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    c = ws.cell(row=offer_row, column=4, value=f'=-D{subtotal_row}*0.125')
    c.fill = fill(C_ACCENT_LITE)
    c.font = font(size=10, color=C_DANGER)
    c.number_format = '#,##0 [$₫-vi-VN]'
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    ws.merge_cells(start_row=offer_row, start_column=5,
                    end_row=offer_row, end_column=6)
    ws.cell(row=offer_row, column=5).fill = fill(C_ACCENT_LITE)
    ws.cell(row=offer_row, column=5).border = BORDER_BOX
    ws.row_dimensions[offer_row].height = 20

    # VAT
    ws.merge_cells(start_row=vat_row, start_column=2,
                    end_row=vat_row, end_column=3)
    c = ws.cell(row=vat_row, column=2, value='VAT (10%)')
    c.fill = fill(C_GREY_LITE)
    c.font = font(size=10, bold=True, color=C_GREY_DARK)
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    c = ws.cell(row=vat_row, column=4, value=f'=(D{subtotal_row}+D{offer_row})*0.1')
    c.fill = fill(C_GREY_LITE)
    c.font = font(size=10, color=C_GREY_DARK)
    c.number_format = '#,##0 [$₫-vi-VN]'
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    ws.merge_cells(start_row=vat_row, start_column=5,
                    end_row=vat_row, end_column=6)
    ws.cell(row=vat_row, column=5).fill = fill(C_GREY_LITE)
    ws.cell(row=vat_row, column=5).border = BORDER_BOX
    ws.row_dimensions[vat_row].height = 20

    # Grand Total
    ws.merge_cells(start_row=grand_row, start_column=2,
                    end_row=grand_row, end_column=3)
    c = ws.cell(row=grand_row, column=2, value='GRAND TOTAL — Phase 2 (VAT included)')
    c.fill = fill(C_PRIMARY_DARK)
    c.font = font(size=12, bold=True, color=C_WHITE)
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    c = ws.cell(row=grand_row, column=4,
                 value=f'=D{subtotal_row}+D{offer_row}+D{vat_row}')
    c.fill = fill(C_ACCENT)
    c.font = font(size=12, bold=True, color=C_PRIMARY_DARK)
    c.number_format = '#,##0 [$₫-vi-VN]'
    c.alignment = align('right', 'center', indent=1)
    c.border = BORDER_BOX
    ws.merge_cells(start_row=grand_row, start_column=5,
                    end_row=grand_row, end_column=6)
    ws.cell(row=grand_row, column=5).fill = fill(C_ACCENT)
    ws.cell(row=grand_row, column=5).border = BORDER_BOX
    ws.row_dimensions[grand_row].height = 30

    # Define name
    wb.defined_names['D_GRAND'] = openpyxl.workbook.defined_name.DefinedName(
        'D_GRAND', attr_text=f"'5. Pricing — Hosting'!$D${grand_row}")

    # Footnote
    r = grand_row + 2
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)
    c = ws.cell(row=r, column=2,
                 value=('  Billing options — quarterly (default) or annual prepayment '
                        '(additional 5% discount). Service term renewable annually. '
                        'Third-party license fees (Hotel Link, VNPay, Hotjar, Zalo OA) are billed '
                        'directly by the providers and are not included in this Phase 2 figure.'))
    c.font = font(size=9, italic=True, color=C_GREY_MID)
    c.alignment = align('left', 'top', wrap=True)
    ws.row_dimensions[r].height = 36


# ============================================================
# SHEET 6 — TIMELINE
# ============================================================
def build_timeline(wb):
    ws = wb.create_sheet('6. Timeline')
    ws.sheet_view.showGridLines = False
    ws.sheet_properties.tabColor = C_GREY_DARK

    cols = ['A'] + [chr(ord('B') + i) for i in range(22)] + ['X']
    # B=label, C..V = 20 weeks, W=deliverable, X=margin
    widths = {'A': 2, 'B': 22, 'W': 30, 'X': 2}
    for i in range(20):
        widths[chr(ord('C') + i)] = 4
    set_widths(ws, widths)

    repeat_brand_header(ws, ('B', 'W'), title='Project Timeline — 20-Week Build + 12-Month Operations')

    r = 5
    # Week-number header
    ws.cell(row=r, column=2, value='WORKSTREAM').fill = fill(C_PRIMARY)
    ws.cell(row=r, column=2).font = font(size=10, bold=True, color=C_WHITE)
    ws.cell(row=r, column=2).alignment = align('center', 'center')
    ws.cell(row=r, column=2).border = BORDER_BOX

    for i in range(20):
        col = 3 + i
        c = ws.cell(row=r, column=col, value=f'W{i+1}')
        c.fill = fill(C_PRIMARY)
        c.font = font(size=9, bold=True, color=C_WHITE)
        c.alignment = align('center', 'center')
        c.border = BORDER_BOX

    c = ws.cell(row=r, column=23, value='KEY DELIVERABLE')
    c.fill = fill(C_PRIMARY)
    c.font = font(size=10, bold=True, color=C_WHITE)
    c.alignment = align('center', 'center')
    c.border = BORDER_BOX
    ws.row_dimensions[r].height = 24

    # Phase shade row (M0..M4)
    r += 1
    phase_ranges = [
        ('M0 · Discovery', 1, 2,  C_GREY_DARK),
        ('M1 · Design',    3, 8,  C_PRIMARY),
        ('M2 · Build',     9, 14, C_PRIMARY),
        ('M3 · Integrate', 15, 18, C_ACCENT),
        ('M4 · Launch',    19, 20, C_SUCCESS),
    ]
    ws.cell(row=r, column=2, value='Phase').fill = fill(C_GREY_LITE)
    ws.cell(row=r, column=2).font = font(size=9, bold=True, color=C_GREY_DARK)
    ws.cell(row=r, column=2).alignment = align('right', 'center', indent=1)
    ws.cell(row=r, column=2).border = BORDER_BOX
    for label, start_w, end_w, color in phase_ranges:
        sc = 3 + start_w - 1
        ec = 3 + end_w - 1
        ws.merge_cells(start_row=r, start_column=sc, end_row=r, end_column=ec)
        c = ws.cell(row=r, column=sc, value=label)
        c.fill = fill(color)
        c.font = font(size=9, bold=True, color=C_WHITE)
        c.alignment = align('center', 'center')
        c.border = BORDER_BOX
    ws.cell(row=r, column=23).fill = fill(C_GREY_LITE)
    ws.cell(row=r, column=23).border = BORDER_BOX
    ws.row_dimensions[r].height = 22
    r += 1

    # Activities (workstream, start_week, end_week, deliverable, color)
    activities = [
        ('Discovery workshops',         1, 2,  'Discovery report + asset audit',           C_GREY_DARK),
        ('Information architecture',    1, 3,  'Sitemap & URL strategy approved',          C_GREY_DARK),
        ('Brand narrative',             2, 4,  'Brand voice + content strategy',           C_GREY_DARK),
        ('Design system',               3, 6,  'Design system in Figma',                   C_PRIMARY),
        ('Visual design — templates',   4, 8,  '14 templates approved',                    C_PRIMARY),
        ('Backend & CMS setup',         7, 12, 'CMS + RBAC operational',                   C_PRIMARY),
        ('Frontend build',              8, 14, 'Static build delivered',                   C_PRIMARY),
        ('Multi-language framework',    10,13, 'VI/EN/KO switching live',                  C_PRIMARY),
        ('Golf booking → VNPay',        13,16, 'Booking flow live',                        C_ACCENT),
        ('Resort booking → Hotel Link', 13,17, 'Booking flow live',                        C_ACCENT),
        ('360° VR integration',         14,17, '360° embedded in pages',                   C_ACCENT),
        ('Live chat · Analytics · SEO', 15,18, 'GA4 + chat + SEO baseline',                C_ACCENT),
        ('Content & media migration',   12,18, 'Content live in CMS',                      C_ACCENT),
        ('QA — cross-browser & device', 17,19, 'QA report (P1/P2 zero)',                   C_SUCCESS),
        ('UAT — 2 client cycles',       18,19, 'UAT sign-off',                             C_SUCCESS),
        ('301 redirects + cutover',     19,20, '4 legacy domains redirected',              C_SUCCESS),
        ('Security hardening',          18,20, 'OWASP checklist signed off',               C_SUCCESS),
        ('Go-live + monitoring',        20,20, 'Production launch',                        C_SUCCESS),
        ('Training & handover',         19,20, 'Trained team + handbook',                  C_SUCCESS),
    ]

    for activity, start_w, end_w, deliv, color in activities:
        c = ws.cell(row=r, column=2, value=activity)
        c.font = font(size=10, color=C_TEXT)
        c.alignment = align('left', 'center', indent=1)
        c.border = BORDER_BOX

        for w in range(1, 21):
            col = 3 + w - 1
            c = ws.cell(row=r, column=col, value='')
            c.border = BORDER_BOX
            if start_w <= w <= end_w:
                c.fill = fill(color)
            else:
                c.fill = fill(C_WHITE)

        c = ws.cell(row=r, column=23, value=deliv)
        c.font = font(size=9, italic=True, color=C_SUCCESS)
        c.alignment = align('left', 'center', wrap=True, indent=1)
        c.border = BORDER_BOX

        ws.row_dimensions[r].height = 22
        r += 1

    # Hypercare + Operations row
    r += 1
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=23)
    c = ws.cell(row=r, column=2,
                 value=('  POST-LAUNCH  —  4 weeks intensive hypercare (W21-W24)  ·  '
                        'then 12 months Managed Services with SLA & monthly performance reviews'))
    c.fill = fill(C_PRIMARY_DARK)
    c.font = font(size=10, bold=True, color=C_WHITE)
    c.alignment = align('left', 'center')
    ws.row_dimensions[r].height = 28

    # Legend
    r += 2
    ws.cell(row=r, column=2, value='Legend:').font = font(size=10, bold=True, color=C_GREY_DARK)
    legend = [
        (C_GREY_DARK, 'Discovery'),
        (C_PRIMARY,   'Design / Build'),
        (C_ACCENT,    'Integration'),
        (C_SUCCESS,   'Launch'),
    ]
    cc = 3
    for color, label in legend:
        c = ws.cell(row=r, column=cc, value='')
        c.fill = fill(color)
        c.border = BORDER_BOX
        c = ws.cell(row=r, column=cc + 1, value=label)
        c.font = font(size=9, color=C_GREY_DARK)
        c.alignment = align('left', 'center')
        cc += 3
    ws.row_dimensions[r].height = 22


# ============================================================
# SHEET 7 — COMMERCIAL TERMS
# ============================================================
def build_terms(wb):
    ws = wb.create_sheet('7. Commercial Terms')
    ws.sheet_view.showGridLines = False
    ws.sheet_properties.tabColor = C_GREY_DARK

    set_widths(ws, {'A': 2, 'B': 28, 'C': 70, 'D': 2})
    repeat_brand_header(ws, ('B', 'C'), title='Commercial Terms, Assumptions & Exclusions')

    r = 5

    # === PAYMENT SCHEDULE ===
    section_header(ws, r, (2, 3), '  01 · PAYMENT SCHEDULE — PHASE 1')
    r += 1
    payment = [
        ('Milestone 1 — Kickoff',
         '30%  ·  Payable within 7 business days of contract signature.'),
        ('Milestone 2 — Design Approval',
         '30%  ·  Payable upon written acceptance of UI/UX visual design (end of M1).'),
        ('Milestone 3 — UAT Sign-off',
         '30%  ·  Payable upon UAT acceptance, prior to production launch (end of M3).'),
        ('Milestone 4 — Launch & Handover',
         '10%  ·  Payable within 14 business days of go-live and complete handover (end of M4).'),
        ('Phase 2 — Hosting & Support',
         'Quarterly billing in advance, OR annual prepayment with 5% additional discount.'),
    ]
    for label, desc in payment:
        c = ws.cell(row=r, column=2, value=label)
        c.fill = fill(C_GREY_LITE)
        c.font = font(size=10, bold=True, color=C_PRIMARY)
        c.alignment = align('left', 'center', indent=1)
        c.border = BORDER_BOX
        c = ws.cell(row=r, column=3, value=desc)
        c.font = font(size=10, color=C_TEXT)
        c.alignment = align('left', 'center', wrap=True, indent=1)
        c.border = BORDER_BOX
        ws.row_dimensions[r].height = 30
        r += 1
    r += 1

    # === CHANGE REQUEST POLICY ===
    section_header(ws, r, (2, 3), '  02 · CHANGE REQUEST POLICY')
    r += 1
    cr_items = [
        ('Minor changes',
         'Changes inside agreed scope (e.g. copy tweaks, image swaps, layout micro-adjustments within a delivered template) are handled at no additional charge during the active sprint.'),
        ('Scope changes',
         'Net-new pages, integrations, templates, or workflows are estimated separately and signed off as a Change Order before work begins. Billed at the blended rate.'),
        ('Design revisions',
         'Three rounds of design revisions are included per template. Additional rounds quoted at the blended rate.'),
        ('Scope freeze',
         'Scope and visual design are frozen at end of M1. Subsequent changes follow the Change Order process.'),
    ]
    for label, desc in cr_items:
        c = ws.cell(row=r, column=2, value=label)
        c.fill = fill(C_GREY_LITE)
        c.font = font(size=10, bold=True, color=C_PRIMARY)
        c.alignment = align('left', 'top', indent=1)
        c.border = BORDER_BOX
        c = ws.cell(row=r, column=3, value=desc)
        c.font = font(size=10, color=C_TEXT)
        c.alignment = align('left', 'top', wrap=True, indent=1)
        c.border = BORDER_BOX
        ws.row_dimensions[r].height = 50
        r += 1
    r += 1

    # === WARRANTY ===
    section_header(ws, r, (2, 3), '  03 · WARRANTY & SUPPORT')
    r += 1
    warranty = [
        ('Post-launch warranty (90 days)',
         'Defects against agreed acceptance criteria fixed at no additional charge for 90 days from go-live.'),
        ('Hypercare (4 weeks)',
         'Dedicated team on standby immediately post-launch: <4-hour response on production incidents, daily health checks, weekly status call.'),
        ('Managed services (Phase 2)',
         '20 hours of monthly support, priority response <4 hours, with full SLA defined in the Hosting & Managed Services schedule.'),
    ]
    for label, desc in warranty:
        c = ws.cell(row=r, column=2, value=label)
        c.fill = fill(C_GREY_LITE)
        c.font = font(size=10, bold=True, color=C_PRIMARY)
        c.alignment = align('left', 'top', indent=1)
        c.border = BORDER_BOX
        c = ws.cell(row=r, column=3, value=desc)
        c.font = font(size=10, color=C_TEXT)
        c.alignment = align('left', 'top', wrap=True, indent=1)
        c.border = BORDER_BOX
        ws.row_dimensions[r].height = 44
        r += 1
    r += 1

    # === ASSUMPTIONS ===
    section_header(ws, r, (2, 3), '  04 · ENGAGEMENT ASSUMPTIONS')
    r += 1
    assumptions = [
        'Client provides a single empowered decision-maker per workstream (Marketing, IT, Property GMs).',
        'Client provides master content in Vietnamese on agreed schedule. Each week of content delay extends launch by the equivalent duration.',
        'Client provides API credentials and signs vendor NDAs/agreements with VNPay, Hotel Link, Smile PMS, Zalo OA, Facebook in time for M3 integration.',
        'Client provides existing photo & video assets (current 360° media, brand photography, room photography) by end of M0.',
        'EN and KO translations are produced by Client\'s translation vendor using our XLIFF/CSV export. Translation execution is out-of-scope.',
        'Client appoints UAT testers for two structured cycles in M4.',
        'Hosting Phase 2 begins on go-live; first invoice issued within 7 days of launch.',
        'All pricing is in Vietnamese Dong (VND). USD figures are reference only at the FX rate stated.',
    ]
    for item in assumptions:
        c = ws.cell(row=r, column=2, value='✓')
        c.font = font(size=12, bold=True, color=C_SUCCESS)
        c.alignment = align('center', 'top')
        c.border = BORDER_BOX
        c = ws.cell(row=r, column=3, value=item)
        c.font = font(size=10, color=C_TEXT)
        c.alignment = align('left', 'top', wrap=True, indent=1)
        c.border = BORDER_BOX
        ws.row_dimensions[r].height = 32
        r += 1
    r += 1

    # === EXCLUSIONS ===
    section_header(ws, r, (2, 3), '  05 · OUT OF SCOPE / EXCLUSIONS')
    r += 1
    exclusions = [
        'Third-party SaaS license fees (Hotel Link, VNPay merchant fees, Hotjar, Zalo OA premium, Mailchimp, font/stock asset licenses) — billed directly by providers.',
        'New filming, photography, drone capture, or 3D scans (for hero video and new room photography). Quoted separately if required.',
        'Content writing in Vietnamese (master content) and translation production into EN and KO.',
        'Ongoing SEO content marketing, paid media management, social media management — quoted as separate engagement.',
        'Property Management System (PMS) software licensing and configuration changes inside Smile PMS.',
        'Hardware procurement (servers, devices) and on-premise infrastructure changes.',
        'Custom mobile apps (iOS/Android). The website is fully responsive on mobile browsers.',
        'Loyalty programme platform, gift voucher engine, or third-party CRM integration beyond the Newsletter and Lead-capture handoff specified.',
        'Re-design or feature work after the 90-day warranty period — handled under Phase 2 Managed Services time pool or as a separate Change Order.',
    ]
    for item in exclusions:
        c = ws.cell(row=r, column=2, value='✗')
        c.font = font(size=12, bold=True, color=C_DANGER)
        c.alignment = align('center', 'top')
        c.border = BORDER_BOX
        c = ws.cell(row=r, column=3, value=item)
        c.font = font(size=10, color=C_TEXT)
        c.alignment = align('left', 'top', wrap=True, indent=1)
        c.border = BORDER_BOX
        ws.row_dimensions[r].height = 36
        r += 1
    r += 1

    # === IP & CONFIDENTIALITY ===
    section_header(ws, r, (2, 3), '  06 · INTELLECTUAL PROPERTY & CONFIDENTIALITY')
    r += 1
    ip_items = [
        ('Custom code & design',
         'Upon final payment, all custom code and original design assets created specifically for SAM Tuyen Lam become the exclusive property of the Client.'),
        ('Third-party components',
         'Open-source libraries and third-party plug-ins remain under their original licenses (MIT, Apache 2.0, etc.). License compliance documentation provided at handover.'),
        ('Confidentiality',
         'Both parties agree to keep this proposal, the engagement, and all shared business information confidential for a period of 3 years from disclosure.'),
        ('Portfolio rights',
         'Blue Coral may reference the project in our portfolio (name, screenshots, public-facing case study) unless Client opts out in writing.'),
    ]
    for label, desc in ip_items:
        c = ws.cell(row=r, column=2, value=label)
        c.fill = fill(C_GREY_LITE)
        c.font = font(size=10, bold=True, color=C_PRIMARY)
        c.alignment = align('left', 'top', indent=1)
        c.border = BORDER_BOX
        c = ws.cell(row=r, column=3, value=desc)
        c.font = font(size=10, color=C_TEXT)
        c.alignment = align('left', 'top', wrap=True, indent=1)
        c.border = BORDER_BOX
        ws.row_dimensions[r].height = 50
        r += 1
    r += 1

    # === SIGNATURE BLOCK ===
    section_header(ws, r, (2, 3), '  07 · ACCEPTANCE')
    r += 1
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
    c = ws.cell(row=r, column=2,
                 value=('  By signing below, both parties accept the scope, pricing, '
                        'timeline, and commercial terms set out in this proposal and its '
                        'referenced sheets.'))
    c.font = font(size=10, italic=True, color=C_GREY_DARK)
    c.alignment = align('left', 'center', wrap=True)
    ws.row_dimensions[r].height = 30
    r += 2

    sig_blocks = [
        ('FOR BLUE CORAL (ADNS)',  'Mr. Nguyen',         'Managing Director'),
        ('FOR SAM TUYEN LAM',      '______________',      'Authorised Representative'),
    ]
    for label, name, title in sig_blocks:
        c = ws.cell(row=r, column=2, value=label)
        c.fill = fill(C_PRIMARY)
        c.font = font(size=10, bold=True, color=C_WHITE)
        c.alignment = align('left', 'center', indent=1)
        c.border = BORDER_BOX
        ws.cell(row=r, column=3).fill = fill(C_PRIMARY)
        ws.cell(row=r, column=3).border = BORDER_BOX
        ws.row_dimensions[r].height = 22

        ws.cell(row=r+1, column=2, value='\n\nName:').font = font(size=10, color=C_TEXT)
        ws.cell(row=r+1, column=2).alignment = align('left', 'bottom', indent=1)
        ws.cell(row=r+1, column=2).border = Border(bottom=THIN)
        ws.cell(row=r+1, column=3, value=name).font = font(size=10, bold=True, color=C_TEXT)
        ws.cell(row=r+1, column=3).alignment = align('left', 'bottom', indent=1)
        ws.cell(row=r+1, column=3).border = Border(bottom=THIN)
        ws.row_dimensions[r+1].height = 36

        ws.cell(row=r+2, column=2, value='Title:').font = font(size=10, color=C_TEXT)
        ws.cell(row=r+2, column=2).alignment = align('left', 'bottom', indent=1)
        ws.cell(row=r+2, column=2).border = Border(bottom=THIN)
        ws.cell(row=r+2, column=3, value=title).font = font(size=10, color=C_GREY_DARK)
        ws.cell(row=r+2, column=3).alignment = align('left', 'bottom', indent=1)
        ws.cell(row=r+2, column=3).border = Border(bottom=THIN)
        ws.row_dimensions[r+2].height = 24

        ws.cell(row=r+3, column=2, value='Signature:').font = font(size=10, color=C_TEXT)
        ws.cell(row=r+3, column=2).alignment = align('left', 'bottom', indent=1)
        ws.cell(row=r+3, column=2).border = Border(bottom=THIN)
        ws.cell(row=r+3, column=3).border = Border(bottom=THIN)
        ws.row_dimensions[r+3].height = 36

        ws.cell(row=r+4, column=2, value='Date:').font = font(size=10, color=C_TEXT)
        ws.cell(row=r+4, column=2).alignment = align('left', 'bottom', indent=1)
        ws.cell(row=r+4, column=2).border = Border(bottom=THIN)
        ws.cell(row=r+4, column=3).border = Border(bottom=THIN)
        ws.row_dimensions[r+4].height = 24
        r += 6


# ============================================================
# CROSS-SHEET WIRING (resolve SUM_GRAND placeholders)
# ============================================================
def wire_cross_sheet_refs(wb):
    # 1. Resolve I_GRAND / J_GRAND / D_GRAND placeholders in cover/summary
    # These are already defined names — replace literal "I_GRAND" / etc. with
    # actual sheet refs in cover & exec summary placeholders.

    # I_GRAND, J_GRAND in '4. Pricing — Build', D_GRAND in '5. Pricing — Hosting'
    # First find actual cells from defined names
    i_grand = wb.defined_names['I_GRAND'].attr_text
    j_grand = wb.defined_names['J_GRAND'].attr_text
    d_grand = wb.defined_names['D_GRAND'].attr_text

    # Substitute textual placeholders in cover and exec summary
    for sn in ['1. Cover', '2. Executive Summary']:
        ws = wb[sn]
        for row in ws.iter_rows():
            for cell in row:
                v = cell.value
                if isinstance(v, str):
                    # The =SUM_GRAND_VND / USD placeholders
                    if v == '=SUM_GRAND_VND':
                        cell.value = f'={i_grand}+{d_grand}'
                    elif v == '=SUM_GRAND_USD':
                        cell.value = f'=({i_grand}+{d_grand})/{FX_VND_USD}'
                    # The I_GRAND / J_GRAND / D_GRAND-only placeholders
                    elif v == "='4. Pricing — Build'!I_GRAND":
                        cell.value = f'={i_grand}'
                    elif v == "='4. Pricing — Build'!J_GRAND":
                        cell.value = f'={j_grand}'
                    elif v == "='5. Pricing — Hosting'!D_GRAND":
                        cell.value = f'={d_grand}'


# ============================================================
# MAIN
# ============================================================
def main():
    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    build_cover(wb)
    build_executive_summary(wb)
    build_scope(wb)
    build_pricing_build(wb)
    build_pricing_hosting(wb)
    build_timeline(wb)
    build_terms(wb)

    wire_cross_sheet_refs(wb)

    output = ('/Users/rom/Projects/research/samtuyenlam/'
               'SAM Tuyen Lam - Proposal & Quotation.xlsx')
    wb.save(output)
    print(f'Saved: {output}')


if __name__ == '__main__':
    main()
