"""Marketing Delivery Timeline — BC × Ambrosia (v3.0).

Updates v3:
- Timeline: thêm phase divider rows để chia nhóm hạng mục
- Bỏ row 2 (italic description) ở mọi sheet
- Thêm sheet "Ước tính chi phí" — total $400/tháng cho tất cả ad channels
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import date, timedelta

PRE_WEEK = date(2026, 5, 11)
START_DATE = date(2026, 5, 18)
ADS_GOLIVE = date(2026, 5, 25)
NUM_WEEKS = 10
TOTAL_BUDGET_USD = 400  # per month
USD_TO_VND = 27000
OUT = "/Users/rom/Projects/research/_bmad-output/marketing-artifacts/marketing-delivery-timeline.xlsx"

# ----- Styles -----
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

H1 = Font(name="Calibri", size=16, bold=True, color="FFFFFF")
H2 = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
H3 = Font(name="Calibri", size=11, bold=True)
NORMAL = Font(name="Calibri", size=10)
SMALL = Font(name="Calibri", size=9, italic=True, color="595959")
APPROVAL_FONT = Font(name="Calibri", size=10, bold=True, color="9C0006")
PHASE_DIVIDER_FONT = Font(name="Calibri", size=12, bold=True, color="FFFFFF")

FILL_TITLE = PatternFill("solid", fgColor="1F4E78")
FILL_HEADER = PatternFill("solid", fgColor="2E75B6")
FILL_SECTION = PatternFill("solid", fgColor="DEEBF7")
FILL_BC = PatternFill("solid", fgColor="A9D08E")
FILL_AMBROSIA = PatternFill("solid", fgColor="F4B084")
FILL_BOTH = PatternFill("solid", fgColor="9DC3E6")
FILL_APPROVAL = PatternFill("solid", fgColor="FFE699")
FILL_RISK_HIGH = PatternFill("solid", fgColor="F8CBAD")
FILL_RISK_MED = PatternFill("solid", fgColor="FFE699")
FILL_RISK_LOW = PatternFill("solid", fgColor="C6E0B4")
FILL_PHASE_M1 = PatternFill("solid", fgColor="FFF2CC")
FILL_PHASE_M2 = PatternFill("solid", fgColor="DDEBF7")
FILL_PHASE_M3 = PatternFill("solid", fgColor="E2EFDA")
FILL_DIVIDER_PRE = PatternFill("solid", fgColor="A64D79")
FILL_DIVIDER_DISC = PatternFill("solid", fgColor="BF9000")
FILL_DIVIDER_ADS = PatternFill("solid", fgColor="C65911")
FILL_DIVIDER_WEB = PatternFill("solid", fgColor="2E75B6")
FILL_DIVIDER_MIG = PatternFill("solid", fgColor="674EA7")

CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
LEFT = Alignment(horizontal="left", vertical="center", wrap_text=True)


def week_label(n):
    s = START_DATE + timedelta(weeks=n - 1)
    e = s + timedelta(days=6)
    return f"W{n}\n{s.strftime('%d/%m')} - {e.strftime('%d/%m')}"


def style_cell(c, font=NORMAL, fill=None, align=LEFT, border=BORDER):
    c.font = font
    if fill:
        c.fill = fill
    c.alignment = align
    c.border = border


def fmt_usd(v):
    return f"${v:,.0f}"


def fmt_vnd(v):
    return f"{v:,.0f} VND"


wb = Workbook()

# ============================================================
# SHEET 0: TỔNG QUAN
# ============================================================
ws0 = wb.active
ws0.title = "Tổng quan"

ws0.merge_cells("A1:F1")
c = ws0.cell(1, 1, "TIMELINE TRIỂN KHAI MARKETING — BC × AMBROSIA")
style_cell(c, font=H1, fill=FILL_TITLE, align=CENTER)
ws0.row_dimensions[1].height = 30

overview = [
    ("Khách hàng (Ambrosia)", "Nhà hàng cafe high-class, đối tượng B2B (corporate event, partnership) + B2C cao cấp (booking, walk-in)"),
    ("Đơn vị triển khai (BC)", "Team Blue Coral — Project lead + UI/UX + FE/BE Dev + Performance Marketer + Content/Creative"),
    ("Mục tiêu marketing", "Tháng 1 = FOUNDATION (setup, learning, không kỳ vọng KPI số). Tháng 2 = AWARENESS (KPI số chính thức: reach, audience). Tháng 3+ = retargeting + convert dần (ngoài scope dự án)."),
    ("Kênh ads (go-live 25/05)", "Facebook Ads + Instagram Ads (Meta) + TikTok Ads + Google Ads"),
    ("Ngân sách ads", f"{fmt_usd(TOTAL_BUDGET_USD)}/tháng (~{fmt_vnd(TOTAL_BUDGET_USD * USD_TO_VND)}) cho tất cả 4 kênh — chi tiết tại sheet 'Ước tính chi phí'"),
    ("Website rebuild", "2 tháng (W1 → W8) — đủ UI / Frontend / Backend / UAT / Go-live, có review nội bộ + Ambrosia ở từng giai đoạn"),
    ("Vận hành song song", "Ads chạy trên website hiện tại của Ambrosia từ W2 (25/05); migrate sang website mới ở W9 (sau khi go-live)"),
    ("Pre-week 11-15/05", "Ambrosia gửi mục tiêu kinh doanh + yêu cầu (target customer, brand reference, budget range, deadline cứng nếu có) → BC chuẩn bị Discovery Brief chi tiết cho W1"),
    ("Cadence phối hợp", "Bi-weekly sync 30 phút (W3, W7) + Monthly catchup 60 phút (W5, W10) + 2 buổi bắt buộc: Kickoff W1, Website UAT W8 → Tổng 6 meeting / 10 tuần"),
    ("Approval flow", "Linh động — gần như mọi approval async qua email/Slack. Chỉ Kickoff + UAT là mandatory in-person/video"),
]
for i, (k, v) in enumerate(overview):
    r = 3 + i
    a = ws0.cell(r, 1, k)
    style_cell(a, font=H3, fill=FILL_SECTION, align=LEFT)
    ws0.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)
    b = ws0.cell(r, 2, v)
    style_cell(b, font=NORMAL, align=LEFT)
    ws0.row_dimensions[r].height = 32

phase_start = 3 + len(overview) + 2
ws0.merge_cells(start_row=phase_start, start_column=1, end_row=phase_start, end_column=6)
c = ws0.cell(phase_start, 1, "TÓM TẮT 4 PHASE")
style_cell(c, font=H2, fill=FILL_HEADER, align=CENTER)

ph_h = ["Phase", "Tên", "Tuần", "Mục tiêu chính", "Owner chính", "Output"]
for col, h in enumerate(ph_h, 1):
    c = ws0.cell(phase_start + 1, col, h)
    style_cell(c, font=H3, fill=FILL_SECTION, align=CENTER)

phases = [
    ("0", "Pre-launch (Async)", "11-15/5", "Ambrosia gửi mục tiêu + yêu cầu; BC chuẩn bị Discovery Brief", "Ambrosia", "Goals brief gửi BC"),
    ("1", "Discovery & Ads Setup", "W1 (18-24/5)", "Onboard, audit, setup ads infra, sản xuất creative bộ 1", "BC + Ambrosia", "Ads accounts ready, creative approved"),
    ("2", "Ads Live & Social Mgmt", "W2 → W10 (25/5-26/7)", "Ads chạy 4 kênh + organic social. M1 = foundation (chưa KPI), M2 = bắt đầu KPI awareness", "BC", "Ads live, weekly report"),
    ("3", "Website Rebuild (UI/FE/BE/UAT)", "W1 → W8 (18/5-13/7)", "Rebuild website 2 tháng song song với ads", "BC + Ambrosia (review)", "Website mới live cuối W8"),
    ("4", "Migration & Stabilize", "W9 → W10 (13-26/7)", "Migrate tracking + ads sang web mới, re-baseline KPI", "BC", "Website mới đã connect ads, month-1 report"),
]
for i, p in enumerate(phases):
    r = phase_start + 2 + i
    for col, val in enumerate(p, 1):
        c = ws0.cell(r, col, val)
        style_cell(c, font=NORMAL, align=LEFT if col in (2, 4, 6) else CENTER)
    ws0.row_dimensions[r].height = 36

legend_start = phase_start + 2 + len(phases) + 2
ws0.merge_cells(start_row=legend_start, start_column=1, end_row=legend_start, end_column=6)
c = ws0.cell(legend_start, 1, "QUY ƯỚC MÀU TRONG SHEET TIMELINE")
style_cell(c, font=H2, fill=FILL_HEADER, align=CENTER)

legend = [
    ("Xanh lá — BC làm", FILL_BC),
    ("Cam — Ambrosia làm", FILL_AMBROSIA),
    ("Xanh dương — Cả hai (meeting / sync)", FILL_BOTH),
    ("Vàng — Cần Ambrosia phê duyệt (async hoặc tại meeting)", FILL_APPROVAL),
]
for i, (label, fill) in enumerate(legend):
    r = legend_start + 1 + i
    sw = ws0.cell(r, 1, "")
    sw.fill = fill
    sw.border = BORDER
    ws0.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)
    c = ws0.cell(r, 2, label)
    style_cell(c, font=NORMAL, align=LEFT)

ws0.column_dimensions["A"].width = 26
for col in "BCDEF":
    ws0.column_dimensions[col].width = 22

# ============================================================
# SHEET 1: TIMELINE (with phase divider rows)
# ============================================================
ws = wb.create_sheet("Timeline")

ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=5 + NUM_WEEKS)
c = ws.cell(1, 1, "GANTT — 10 TUẦN TRIỂN KHAI (Pre-week 11-15/5 → 26/7/2026)")
style_cell(c, font=H1, fill=FILL_TITLE, align=CENTER)
ws.row_dimensions[1].height = 28

headers = ["STT", "Hoạt động", "Phase", "Owner", "Output / Deliverable"]
for i in range(NUM_WEEKS):
    headers.append(week_label(i + 1))
for col, h in enumerate(headers, 1):
    c = ws.cell(3, col, h)
    style_cell(c, font=H2, fill=FILL_HEADER, align=CENTER)
ws.row_dimensions[3].height = 40

# Tasks structured by phase blocks. Each phase has divider + list of tasks.
phase_blocks = [
    {
        "name": "PHASE 0 — PRE-WEEK (11-15/5): Ambrosia gửi mục tiêu + BC chuẩn bị Discovery",
        "fill": FILL_DIVIDER_PRE,
        "phase_label": "0. Pre",
        "phase_color": "EAD1DC",
        "tasks": [
            ("0.1", "Ambrosia gửi mục tiêu kinh doanh + yêu cầu (target customer, brand reference, budget range, deadline)", "Ambrosia", "Goals & requirements brief", []),
            ("0.2", "BC chuẩn bị Discovery Questionnaire chi tiết + lịch Kickoff", "BC", "Questionnaire + Kickoff invite", []),
        ],
    },
    {
        "name": "PHASE 1 — DISCOVERY & ADS SETUP (W1, 18-24/5): Onboard + setup ads + creative bộ 1",
        "fill": FILL_DIVIDER_DISC,
        "phase_label": "1. Discovery",
        "phase_color": "FFF2CC",
        "tasks": [
            ("1.1", "Kickoff Call (60 phút) — đồng thuận scope, mục tiêu, KPI baseline", "Cả hai", "Meeting notes + scope confirmed", [(1, "meeting")]),
            ("1.2", "Ambrosia cấp truy cập tài khoản (xem sheet 'Tài khoản & Hệ thống')", "Ambrosia", "Access list xác nhận", [(1, "work")]),
            ("1.3", "Ambrosia cung cấp brand assets (logo, font, màu, ảnh, video sản phẩm có sẵn)", "Ambrosia", "Asset folder", [(1, "work")]),
            ("1.4", "Audit website hiện tại + social hiện tại + 3-5 đối thủ cạnh tranh", "BC", "Audit report", [(1, "work")]),
            ("1.5", "Brand voice + messaging quick brief (cho ads + social)", "BC", "Messaging brief", [(1, "work")]),
            ("1.6", "Setup tracking trên website hiện tại (Meta Pixel + GA4 + GTM + Conversion API)", "BC", "Tracking firing OK", [(1, "work")]),
            ("1.7", "Setup / connect 4 ads accounts (Meta, Google, TikTok) + verify domain", "BC", "Accounts ready", [(1, "work")]),
            ("1.8", "Sản xuất creative bộ 1: 5 ad Meta + 3 ad Google Search/GDN + 3 video TikTok-native", "BC", "Creative folder", [(1, "work")]),
            ("1.9", "Build campaign structure trên 4 platform (chưa publish)", "BC", "Campaign drafts", [(1, "work")]),
            ("1.10", "Phê duyệt creative + audience + budget bộ 1 (async qua email/Slack)", "Ambrosia", "Approval", [(1, "approval")]),
        ],
    },
    {
        "name": "PHASE 2 — ADS LIVE & SOCIAL MANAGEMENT (W2 → W10, 25/5 → 26/7): Always-on 4 kênh",
        "fill": FILL_DIVIDER_ADS,
        "phase_label": "2. Ads",
        "phase_color": "F8CBAD",
        "tasks": [
            ("2.1", "Publish Facebook Ads + Instagram Ads (Meta) — soft launch awareness", "BC", "Ads LIVE 25/05", [(2, "meeting")]),
            ("2.2", "Publish Google Ads (Search Brand + Search Non-brand + GDN remarketing)", "BC", "Ads LIVE 25/05", [(2, "meeting")]),
            ("2.3", "Publish TikTok Ads (Spark Ads — awareness + video views)", "BC", "Ads LIVE 25/05", [(2, "meeting")]),
            ("2.4", "Daily monitoring 4 platform (delivery, reach, CTR, video view, engagement)", "BC", "Daily log", [(2, "work"), (3, "work"), (4, "work"), (5, "work"), (6, "work"), (7, "work"), (8, "work"), (9, "work"), (10, "work")]),
            ("2.5", "Weekly optimization: pause low-performer, scale winner, refine audience + keyword", "BC", "Optimize log", [(3, "work"), (4, "work"), (5, "work"), (6, "work"), (7, "work"), (8, "work"), (9, "work"), (10, "work")]),
            ("2.6", "Creative refresh batch (1 batch / 2 tuần) — chống ad fatigue", "BC", "Creative folder mới", [(3, "work"), (5, "work"), (7, "work"), (9, "work")]),
            ("2.7", "Build retargeting audience (website visitor, video viewer ≥50%, page engager)", "BC", "Audience size growing", [(3, "work"), (4, "work"), (5, "work"), (6, "work"), (7, "work"), (8, "work")]),
            ("2.8", "Activate retargeting campaigns (consideration phase) — khi audience đủ size", "BC", "Retarget LIVE", [(5, "meeting"), (6, "work"), (7, "work"), (8, "work"), (9, "work"), (10, "work")]),
            ("2.9", "Báo cáo tuần (Looker Studio dashboard auto + email Mon 9AM)", "BC", "Dashboard URL + email", [(2, "work"), (3, "work"), (4, "work"), (5, "work"), (6, "work"), (7, "work"), (8, "work"), (9, "work"), (10, "work")]),
            ("2.10", "Organic social management: post FB+IG (3/tuần), TikTok (2-3/tuần)", "BC", "Live posts + content calendar", [(2, "work"), (3, "work"), (4, "work"), (5, "work"), (6, "work"), (7, "work"), (8, "work"), (9, "work"), (10, "work")]),
            ("2.11", "Trả comment / inbox social + B2B inquiry (Ambrosia hoặc BC tùy SOW)", "Ambrosia", "Engagement", [(2, "work"), (3, "work"), (4, "work"), (5, "work"), (6, "work"), (7, "work"), (8, "work"), (9, "work"), (10, "work")]),
        ],
    },
    {
        "name": "PHASE 3 — WEBSITE REBUILD (W1 → W8, 18/5 → 13/7): UI / FE / BE / UAT / Go-live",
        "fill": FILL_DIVIDER_WEB,
        "phase_label": "3. Website",
        "phase_color": "DDEBF7",
        "tasks": [
            ("3.1", "UX research + sitemap (Home / Services / Events / Gallery / Others)", "BC", "Sitemap doc + user flow", [(1, "work"), (2, "work")]),
            ("3.2", "Wireframe low-fi (Figma) — toàn bộ page chính", "BC", "Figma wireframe link", [(2, "work"), (3, "work")]),
            ("3.3", "Wireframe review + Ambrosia phê duyệt (tại bi-weekly sync W3)", "Cả hai", "Approval", [(3, "approval")]),
            ("3.4", "UI Design hi-fi (Figma) — Home + key pages, sau đó full pages", "BC", "Figma design link", [(3, "work"), (4, "work")]),
            ("3.5", "UI review + Ambrosia phê duyệt (async)", "Ambrosia", "Approval", [(4, "approval")]),
            ("3.6", "Frontend dev — build 5 page (Home, Services, Events, Gallery, Others)", "BC", "Pages on staging", [(4, "work"), (5, "work"), (6, "work")]),
            ("3.7", "Backend dev — booking form, contact form, B2B inquiry form, CMS basic", "BC", "Backend live on staging", [(5, "work"), (6, "work"), (7, "work")]),
            ("3.8", "Ambrosia cung cấp content + ảnh / video cho 5 page (đợt chính)", "Ambrosia", "Content folder", [(4, "work"), (5, "work")]),
            ("3.9", "Content integration + copy editing trên website", "BC", "Content live on staging", [(6, "work"), (7, "work")]),
            ("3.10", "SEO foundation: meta tags, schema (LocalBusiness + Restaurant), sitemap.xml, robots.txt", "BC", "SEO checklist passed", [(7, "work")]),
            ("3.11", "Internal QA: speed (mobile >80), responsive, form, tracking, accessibility", "BC", "QA report", [(7, "work"), (8, "work")]),
            ("3.12", "Website UAT (60 phút) — Ambrosia test trên staging", "Cả hai", "UAT signoff", [(8, "meeting")]),
            ("3.13", "Bugfix sau UAT + Ambrosia phê duyệt go-live", "BC", "Bugfix log + approval", [(8, "approval")]),
            ("3.14", "DNS switch + SSL + go-live website mới", "BC", "Website LIVE 13/07", [(8, "meeting")]),
        ],
    },
    {
        "name": "PHASE 4 — MIGRATION & STABILIZE (W9 → W10, 13/7 → 26/7): Migrate ads + KPI re-baseline",
        "fill": FILL_DIVIDER_MIG,
        "phase_label": "4. Migration",
        "phase_color": "D9D2E9",
        "tasks": [
            ("4.1", "Migrate Pixel + GA4 + GTM container sang website mới", "BC", "Tracking firing trên web mới", [(9, "work")]),
            ("4.2", "Verify tracking (Tag Assistant + GA4 DebugView + test conversion thật)", "BC", "Verification report", [(9, "work")]),
            ("4.3", "Update destination URL của tất cả ads sang website mới", "BC", "Updated campaign URLs", [(9, "work")]),
            ("4.4", "Monitor performance shift sau migration (learning phase 7-14 ngày)", "BC", "Daily log", [(9, "work"), (10, "work")]),
            ("4.5", "Re-baseline KPI cho website mới + tăng cường retargeting", "BC", "KPI re-baseline doc", [(10, "work")]),
            ("4.6", "Monthly catchup (60 phút) — kết quả 2 tháng + roadmap tháng tiếp", "Cả hai", "Month-2 report + plan", [(10, "meeting")]),
            ("4.7", "Ambrosia phê duyệt month-2 performance + budget tháng 3 (async)", "Ambrosia", "Approval", [(10, "approval")]),
        ],
    },
]

owner_fill = {"BC": FILL_BC, "Ambrosia": FILL_AMBROSIA, "Cả hai": FILL_BOTH}

row = 4
for block in phase_blocks:
    # Phase divider row (merged across all columns)
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=5 + NUM_WEEKS)
    c = ws.cell(row, 1, block["name"])
    style_cell(c, font=PHASE_DIVIDER_FONT, fill=block["fill"], align=LEFT)
    ws.row_dimensions[row].height = 24
    row += 1

    # Phase tasks
    phase_fill = PatternFill("solid", fgColor=block["phase_color"])
    for tid, name, owner, deliverable, weeks in block["tasks"]:
        cells = [
            (1, tid, NORMAL, None, CENTER),
            (2, name, NORMAL, None, LEFT),
            (3, block["phase_label"], NORMAL, phase_fill, CENTER),
            (4, owner, NORMAL, owner_fill.get(owner), CENTER),
            (5, deliverable, NORMAL, None, LEFT),
        ]
        for col, val, font, fill, align in cells:
            c = ws.cell(row, col, val)
            style_cell(c, font=font, fill=fill, align=align)

        week_marks = {w: kind for w, kind in weeks}
        for w in range(1, NUM_WEEKS + 1):
            col = 5 + w
            c = ws.cell(row, col, "")
            kind = week_marks.get(w)
            if kind == "work":
                c.fill = owner_fill.get(owner, FILL_BC)
            elif kind == "meeting":
                c.fill = FILL_BOTH
                c.value = "M"
                c.font = H3
            elif kind == "approval":
                c.fill = FILL_APPROVAL
                c.value = "A"
                c.font = APPROVAL_FONT
            c.alignment = CENTER
            c.border = BORDER
            if c.font is None:
                c.font = NORMAL
        row += 1

ws.column_dimensions["A"].width = 6
ws.column_dimensions["B"].width = 60
ws.column_dimensions["C"].width = 14
ws.column_dimensions["D"].width = 11
ws.column_dimensions["E"].width = 32
for w in range(1, NUM_WEEKS + 1):
    ws.column_dimensions[get_column_letter(5 + w)].width = 11

# Legend
legend_row = row + 2
c = ws.cell(legend_row, 2, "QUY ƯỚC MARKER TRONG Ô TUẦN")
style_cell(c, font=H3, align=LEFT, border=None)
items = [
    ("Ô màu (xanh lá / cam) không text", "Đang làm việc trong tuần đó", FILL_BC),
    ("Ô vàng + chữ A", "Cần Ambrosia phê duyệt (async qua email/Slack)", FILL_APPROVAL),
    ("Ô xanh dương + chữ M", "Meeting / sync trong tuần đó", FILL_BOTH),
]
for i, (mark, desc, fill) in enumerate(items):
    r = legend_row + 1 + i
    a = ws.cell(r, 2, mark)
    style_cell(a, font=NORMAL, fill=fill, align=LEFT)
    b = ws.cell(r, 3, desc)
    style_cell(b, font=NORMAL, align=LEFT, border=None)

ws.freeze_panes = "F4"

# ============================================================
# SHEET 2: TOUCHPOINTS
# ============================================================
ws2 = wb.create_sheet("Touchpoints")
ws2.merge_cells("A1:G1")
c = ws2.cell(1, 1, "LỊCH MEETING BC × AMBROSIA — LEAN (6 buổi)")
style_cell(c, font=H1, fill=FILL_TITLE, align=CENTER)
ws2.row_dimensions[1].height = 26

th = ["#", "Tuần", "Ngày dự kiến", "Tên Meeting", "Thời lượng", "Hình thức", "Mục tiêu"]
for col, h in enumerate(th, 1):
    c = ws2.cell(3, col, h)
    style_cell(c, font=H2, fill=FILL_HEADER, align=CENTER)
ws2.row_dimensions[3].height = 32

touchpoints = [
    ("W1", START_DATE + timedelta(days=1), "Kickoff Call (mandatory)", "60 phút", "Video call", "Đồng thuận scope, mục tiêu, KPI baseline, agenda 10 tuần. Walk-through Discovery Brief"),
    ("W3", START_DATE + timedelta(weeks=2, days=2), "Bi-weekly Sync #1", "30 phút", "Video call", "Báo cáo ads 2 tuần đầu, present wireframe website, lấy feedback nhanh"),
    ("W5", START_DATE + timedelta(weeks=4, days=2), "Monthly Catchup #1 (cuối tháng 1)", "60 phút", "Video call", "Foundation review: setup completion, early signals (chưa đo KPI chính thức), website progress, đồng thuận tháng 2 awareness scaling"),
    ("W7", START_DATE + timedelta(weeks=6, days=2), "Bi-weekly Sync #2", "30 phút", "Video call", "Update ads tháng 2, demo website 80%, chuẩn bị UAT"),
    ("W8", START_DATE + timedelta(weeks=7, days=3), "Website UAT (mandatory)", "60 phút", "Video call (share staging)", "Test website mới, feedback bugfix, phê duyệt go-live"),
    ("W10", START_DATE + timedelta(weeks=9, days=4), "Monthly Catchup #2 (cuối tháng 2)", "60 phút", "Video call", "Tổng kết: foundation tháng 1 (qualitative) + KPI tháng 2 awareness vs target, learning, plan M3 retargeting + budget"),
]
for i, t in enumerate(touchpoints):
    r = 4 + i
    week, dt, name, dur, fmt, goal = t
    ws2.cell(r, 1, i + 1)
    ws2.cell(r, 2, week)
    ws2.cell(r, 3, dt.strftime("%a %d/%m/%Y"))
    ws2.cell(r, 4, name)
    ws2.cell(r, 5, dur)
    ws2.cell(r, 6, fmt)
    ws2.cell(r, 7, goal)
    for col in range(1, 8):
        c = ws2.cell(r, col)
        c.font = NORMAL
        c.alignment = LEFT if col in (4, 7) else CENTER
        c.border = BORDER
    ws2.row_dimensions[r].height = 38

ws2.column_dimensions["A"].width = 5
ws2.column_dimensions["B"].width = 8
ws2.column_dimensions["C"].width = 18
ws2.column_dimensions["D"].width = 32
ws2.column_dimensions["E"].width = 12
ws2.column_dimensions["F"].width = 24
ws2.column_dimensions["G"].width = 50
ws2.freeze_panes = "A4"

note_row = 4 + len(touchpoints) + 2
ws2.merge_cells(start_row=note_row, start_column=1, end_row=note_row, end_column=7)
c = ws2.cell(note_row, 1, "Lưu ý: Lịch trên là dự kiến — linh động dời ±1-2 ngày tùy 2 bên. Ambrosia không cần dành nhiều thời gian giữa các meeting; mọi tài liệu approve gửi qua email/Slack, BC chủ động xử lý.")
style_cell(c, font=SMALL, align=CENTER)

# ============================================================
# SHEET 3: TÀI KHOẢN & HỆ THỐNG
# ============================================================
ws_a = wb.create_sheet("Tài khoản & Hệ thống")
ws_a.merge_cells("A1:E1")
c = ws_a.cell(1, 1, "TÀI KHOẢN AMBROSIA CẤP + HỆ THỐNG BC ĐỀ XUẤT")
style_cell(c, font=H1, fill=FILL_TITLE, align=CENTER)
ws_a.row_dimensions[1].height = 26

ws_a.merge_cells("A3:E3")
c = ws_a.cell(3, 1, "SECTION A — TÀI KHOẢN AMBROSIA CẤP CHO BC (mandatory, hạn cuối W1 ngày 2)")
style_cell(c, font=H2, fill=FILL_HEADER, align=CENTER)

th = ["#", "Tài khoản / Hệ thống", "Mục đích sử dụng", "Loại quyền cấp cho BC", "Status"]
for col, h in enumerate(th, 1):
    c = ws_a.cell(4, col, h)
    style_cell(c, font=H3, fill=FILL_SECTION, align=CENTER)

accounts_ambrosia = [
    ("Domain registrar (vd: Mắt Bão / GoDaddy / Namecheap)", "Quản lý DNS, SSL, chuyển hosting cho website mới", "Admin / DNS access"),
    ("Hosting hiện tại (nếu có)", "Backup website cũ, kiểm tra performance, chuẩn bị migration", "Admin / FTP / cPanel"),
    ("Google Workspace (email công ty Ambrosia)", "Tạo email project, share Drive, calendar invite", "Member account hoặc share email"),
    ("Google Analytics 4 (GA4)", "Tracking traffic + conversion website", "Editor / Admin"),
    ("Google Search Console (GSC)", "SEO performance, sitemap, indexing", "Owner / Full"),
    ("Google Tag Manager (GTM)", "Quản lý tag tracking (Pixel, GA4 events)", "Publish / Edit"),
    ("Google Business Profile (GBP)", "Local SEO, hiển thị trên Google Maps + Search", "Manager / Owner"),
    ("Google Ads", "Chạy Google Ads (Search + GDN + YouTube)", "Standard access (link MCC nếu có)"),
    ("Meta Business Manager", "Quản lý Facebook Page + Instagram + Pixel + Ads", "Admin / Full control"),
    ("Facebook Page Ambrosia", "Quản lý nội dung organic + run ads", "Admin"),
    ("Instagram Business account (link với FB Page)", "Quản lý content IG + IG Ads", "Admin"),
    ("Meta Pixel + Conversion API", "Tracking website conversion + retargeting", "Admin (qua Business Manager)"),
    ("TikTok Business Center", "Quản lý TikTok account + Ads", "Admin"),
    ("TikTok Business / Creator account", "Post organic + run TikTok Ads", "Admin"),
    ("TikTok Pixel", "Tracking website + retargeting TikTok", "Admin"),
    ("Email tool hiện tại (Mailchimp / Sendinblue / nếu có)", "Lifecycle email, newsletter, B2B nurture", "Admin"),
    ("CRM hiện tại (nếu có — HubSpot / Notion / Excel)", "Quản lý B2B leads, partnership inquiry", "Editor"),
    ("Booking / reservation tool (nếu đang dùng)", "Sync booking từ ads → backend Ambrosia", "Admin / API access"),
    ("Stock ảnh / video Ambrosia (Drive / Dropbox)", "Lấy asset cho creative + website", "Editor"),
    ("Brand guidelines doc (nếu có)", "Đảm bảo creative đúng brand voice + visual", "Viewer"),
]
for i, (acc, purpose, perm) in enumerate(accounts_ambrosia):
    r = 5 + i
    ws_a.cell(r, 1, i + 1)
    ws_a.cell(r, 2, acc)
    ws_a.cell(r, 3, purpose)
    ws_a.cell(r, 4, perm)
    ws_a.cell(r, 5, "Pending")
    for col in range(1, 6):
        c = ws_a.cell(r, col)
        c.font = NORMAL
        c.alignment = LEFT if col in (2, 3, 4) else CENTER
        c.border = BORDER
        if col == 5:
            c.fill = FILL_AMBROSIA

sec_b_start = 5 + len(accounts_ambrosia) + 2
ws_a.merge_cells(start_row=sec_b_start, start_column=1, end_row=sec_b_start, end_column=5)
c = ws_a.cell(sec_b_start, 1, "SECTION B — BC ĐỀ XUẤT BỔ SUNG (chốt với Ambrosia tại Kickoff W1)")
style_cell(c, font=H2, fill=FILL_HEADER, align=CENTER)

th = ["#", "Hạng mục", "BC đề xuất (option A — chính)", "Option B (alternative)", "Chi phí ước tính / tháng"]
for col, h in enumerate(th, 1):
    c = ws_a.cell(sec_b_start + 1, col, h)
    style_cell(c, font=H3, fill=FILL_SECTION, align=CENTER)

bc_proposals = [
    ("Hosting website mới", "Webflow Business plan ($39/tháng) — fast, no-code, dễ Ambrosia tự update menu/event", "WordPress + SiteGround GrowBig (~$15/tháng) — flexible, plugin-rich", "$15-39"),
    ("CDN + Performance", "Cloudflare Free / Pro ($20/tháng nếu cần advanced)", "Bao gồm trong Webflow / WP-Rocket cho WordPress", "$0-20"),
    ("CMS cho menu / event", "Webflow CMS native (bao gồm trong plan)", "WordPress + ACF (free) hoặc Sanity ($0 starter)", "$0"),
    ("Email marketing tool", "Brevo (Sendinblue) — Free tier 300 email/ngày, plan trả từ $9", "Mailchimp ($13+/tháng) hoặc Klaviyo ($20+ cho B2B nurture)", "$9-20"),
    ("CRM nhẹ cho B2B leads", "HubSpot Free CRM (đủ dùng giai đoạn đầu)", "Notion CRM template (free) hoặc Airtable Free", "$0"),
    ("Booking / reservation widget", "Bookatable / TheFork (free cho restaurant)", "Custom form + WhatsApp Business / Zalo OA cho B2B", "$0-30"),
    ("Reporting dashboard", "Looker Studio (Google) — free, kết nối GA4 + Google Ads + Sheets", "Whatagraph ($199+) nếu cần PDF báo cáo đẹp", "$0"),
    ("Project mgmt / workspace chung", "Notion (free workspace) — share docs, status, asset link", "Trello / ClickUp Free", "$0"),
    ("Communication channel", "Slack Free (lưu trữ 90 ngày) — daily comm BC × Ambrosia", "Zalo group / WhatsApp group nếu Ambrosia quen", "$0"),
    ("Asset storage", "Google Drive (chung trong Workspace)", "Dropbox 2GB free", "$0"),
    ("Social scheduling", "Meta Business Suite (free, native cho FB+IG)", "Buffer Free / Hootsuite Free", "$0"),
    ("Stock ảnh / video bổ sung", "Pexels / Unsplash (free)", "Envato Elements ($16/tháng) nếu cần motion / template", "$0-16"),
    ("AI tool cho content / copy", "ChatGPT Free / Claude Free", "Jasper / Copy.ai trả phí nếu volume lớn", "$0"),
]
for i, (item, opt_a, opt_b, cost) in enumerate(bc_proposals):
    r = sec_b_start + 2 + i
    ws_a.cell(r, 1, i + 1)
    ws_a.cell(r, 2, item)
    ws_a.cell(r, 3, opt_a)
    ws_a.cell(r, 4, opt_b)
    ws_a.cell(r, 5, cost)
    for col in range(1, 6):
        c = ws_a.cell(r, col)
        c.font = NORMAL
        c.alignment = LEFT if col in (2, 3, 4) else CENTER
        c.border = BORDER

note_row = sec_b_start + 2 + len(bc_proposals) + 1
ws_a.merge_cells(start_row=note_row, start_column=1, end_row=note_row + 4, end_column=5)
note = (
    "GỢI Ý HOSTING CHI TIẾT CHO AMBROSIA (cafe + B2B):\n"
    "• Recommend chính: Webflow Business plan ($39/tháng) — performance tốt, dễ Ambrosia tự update menu/event/gallery, có CMS + form + booking widget tích hợp. Phù hợp brand high-class vì design control rất tốt.\n"
    "• Alternative: WordPress + SiteGround GrowBig ($14.99/tháng năm đầu) — cộng đồng plugin lớn, nếu Ambrosia muốn nhiều tính năng booking phức tạp hoặc có ý định bán online sau này.\n"
    "• KHÔNG khuyến nghị: shared hosting Việt Nam giá rẻ (PA Vietnam, Mắt Bão hosting) — page speed kém, ảnh hưởng SEO + ads Quality Score.\n"
    "• Domain: giữ tại registrar Ambrosia đang dùng, BC chỉ cần DNS access để trỏ về hosting mới."
)
c = ws_a.cell(note_row, 1, note)
style_cell(c, font=SMALL, fill=PatternFill("solid", fgColor="FFF2CC"), align=LEFT)

ws_a.column_dimensions["A"].width = 5
ws_a.column_dimensions["B"].width = 38
ws_a.column_dimensions["C"].width = 38
ws_a.column_dimensions["D"].width = 38
ws_a.column_dimensions["E"].width = 22
ws_a.freeze_panes = "A5"

# ============================================================
# SHEET 4: TRÁCH NHIỆM AMBROSIA
# ============================================================
ws3 = wb.create_sheet("Trách nhiệm Ambrosia")
ws3.merge_cells("A1:F1")
c = ws3.cell(1, 1, "CHECKLIST TRÁCH NHIỆM AMBROSIA")
style_cell(c, font=H1, fill=FILL_TITLE, align=CENTER)
ws3.row_dimensions[1].height = 26

th = ["STT", "Tuần", "Hạng mục", "Hạn chót", "Người phụ trách (Ambrosia)", "Status"]
for col, h in enumerate(th, 1):
    c = ws3.cell(3, col, h)
    style_cell(c, font=H2, fill=FILL_HEADER, align=CENTER)
ws3.row_dimensions[3].height = 30

ambrosia_tasks = [
    ("Pre-week", "Gửi mục tiêu kinh doanh + yêu cầu (target customer, brand reference, budget range, deadline cứng nếu có)", PRE_WEEK + timedelta(days=4)),
    ("W1", "Tham gia Kickoff Call (decision maker có mặt)", START_DATE + timedelta(days=1)),
    ("W1", "Cấp đầy đủ tài khoản theo sheet 'Tài khoản & Hệ thống' Section A (20 tài khoản)", START_DATE + timedelta(days=2)),
    ("W1", "Cung cấp brand assets: logo (vector), font, mã màu, ảnh + video sản phẩm có sẵn", START_DATE + timedelta(days=3)),
    ("W1", "Cung cấp danh sách 3-5 đối thủ + 5-10 khách hàng B2C tiêu biểu + 3-5 corporate client (nếu có)", START_DATE + timedelta(days=4)),
    ("W1", "Chốt với BC: hosting + tools đề xuất ở Section B (xem sheet 'Tài khoản & Hệ thống')", START_DATE + timedelta(days=4)),
    ("W1", "Phê duyệt creative + audience + budget bộ 1 (async qua email/Slack)", START_DATE + timedelta(days=4)),
    ("W2-3", "Cung cấp content + ảnh/video cho website (đợt 1: Home, Services)", START_DATE + timedelta(weeks=1, days=4)),
    ("W3", "Tham gia Bi-weekly Sync #1 (30 phút) + phê duyệt wireframe website", START_DATE + timedelta(weeks=2, days=2)),
    ("W4", "Phê duyệt UI design (async)", START_DATE + timedelta(weeks=3, days=4)),
    ("W4-5", "Cung cấp content đợt 2: Events + Gallery + Others (ảnh/video chính)", START_DATE + timedelta(weeks=4, days=2)),
    ("W5", "Tham gia Monthly Catchup #1 (60 phút) — review foundation tháng 1, đồng thuận tháng 2 awareness scaling", START_DATE + timedelta(weeks=4, days=2)),
    ("W2-W10", "Trả comment / inbox FB + IG + TikTok + B2B inquiry (community management)", "Hàng ngày"),
    ("W2-W10", "Cung cấp ảnh / video gốc khi BC yêu cầu refresh creative (1 batch / 2 tuần)", "Khi BC yêu cầu"),
    ("W7", "Tham gia Bi-weekly Sync #2 (30 phút) — demo website 80%", START_DATE + timedelta(weeks=6, days=2)),
    ("W8", "Tham gia Website UAT (60 phút) — test website trên staging, gửi bugfix list", START_DATE + timedelta(weeks=7, days=3)),
    ("W8", "Phê duyệt go-live website mới", START_DATE + timedelta(weeks=7, days=4)),
    ("W10", "Tham gia Monthly Catchup #2 (60 phút) — tổng kết 2 tháng", START_DATE + timedelta(weeks=9, days=4)),
    ("W10", "Quyết định: budget tháng 3 + roadmap tiếp theo (async)", START_DATE + timedelta(weeks=9, days=4)),
]
for i, item in enumerate(ambrosia_tasks):
    r = 4 + i
    week, task, deadline = item
    deadline_str = deadline.strftime("%a %d/%m/%Y") if isinstance(deadline, date) else deadline
    ws3.cell(r, 1, i + 1)
    ws3.cell(r, 2, week)
    ws3.cell(r, 3, task)
    ws3.cell(r, 4, deadline_str)
    ws3.cell(r, 5, "")
    ws3.cell(r, 6, "Pending")
    for col in range(1, 7):
        c = ws3.cell(r, col)
        c.font = NORMAL
        c.alignment = LEFT if col == 3 else CENTER
        c.border = BORDER
        if col == 6:
            c.fill = FILL_AMBROSIA

ws3.column_dimensions["A"].width = 5
ws3.column_dimensions["B"].width = 11
ws3.column_dimensions["C"].width = 65
ws3.column_dimensions["D"].width = 18
ws3.column_dimensions["E"].width = 24
ws3.column_dimensions["F"].width = 18
ws3.freeze_panes = "A4"

# ============================================================
# SHEET 5: KPIs
# ============================================================
ws5 = wb.create_sheet("KPIs")
ws5.merge_cells("A1:F1")
c = ws5.cell(1, 1, "KPI FRAMEWORK — AWARENESS-FIRST CHO AMBROSIA")
style_cell(c, font=H1, fill=FILL_TITLE, align=CENTER)
ws5.row_dimensions[1].height = 26

ws5.merge_cells("A3:G3")
c = ws5.cell(3, 1, "CHIẾN LƯỢC THEO PHASE")
style_cell(c, font=H2, fill=FILL_HEADER, align=CENTER)

ph_h = ["Phase", "Tháng", "Mục tiêu chính", "% Budget allocation", "Loại campaign chính", "Cách đo", "KPI số liệu"]
for col, h in enumerate(ph_h, 1):
    c = ws5.cell(4, col, h)
    style_cell(c, font=H3, fill=FILL_SECTION, align=CENTER)

phases_kpi = [
    ("Phase 1 — FOUNDATION", "Tháng 1 (W1-W5)", "Setup hoàn chỉnh tracking + ads infra, launch creative, bắt đầu học. KHÔNG kỳ vọng kết quả KPI.", "70% awareness / 20% video / 10% test (để học, không phải đạt target)", "Reach, Brand Awareness, Video View, Engagement (soft launch)", "Setup completion checklist (binary: done/pending)", "KHÔNG có target số liệu (xem block 'Foundation Checklist')"),
    ("Phase 2 — AWARENESS + AUDIENCE", "Tháng 2 (W6-W10)", "Mở reach rộng, xây pixel audience đủ size, bắt đầu retargeting layer nhẹ. KPI số liệu chính thức bắt đầu từ đây.", "50% awareness / 25% retargeting layer / 15% search / 10% test", "Reach + Retargeting (website visitor, video viewer 50%+)", "Số liệu định lượng theo bảng KPI bên dưới", "Reach, impressions, audience size, engagement, follower growth"),
    ("Phase 3 — CONSIDERATION + CONVERSION", "Tháng 3+ (ngoài scope dự án)", "Retargeting mạnh, lead gen, optimize CPA, scale kênh có ROAS dương", "30% awareness / 35% retargeting / 35% conversion", "Conversion campaign + Lead Gen Form + Lookalike", "CPA + ROAS + qualified lead", "B2B qualified lead, booking confirmed, CPA, ROAS"),
]
phase_fills_list = [FILL_PHASE_M1, FILL_PHASE_M2, FILL_PHASE_M3]
for i, p in enumerate(phases_kpi):
    r = 5 + i
    for col, val in enumerate(p, 1):
        c = ws5.cell(r, col, val)
        style_cell(c, font=NORMAL, fill=phase_fills_list[i] if col == 1 else None, align=LEFT if col in (3, 5, 6, 7) else CENTER)
    ws5.row_dimensions[r].height = 64

# Foundation Setup Checklist block (M1 only)
fc_start = 5 + len(phases_kpi) + 2
ws5.merge_cells(start_row=fc_start, start_column=1, end_row=fc_start, end_column=7)
c = ws5.cell(fc_start, 1, "FOUNDATION SETUP CHECKLIST — THÁNG 1 (W1-W5): hạng mục PHẢI hoàn thành, không phải target số liệu")
style_cell(c, font=H2, fill=FILL_HEADER, align=CENTER)

fc_th = ["Hạng mục foundation", "Tuần hoàn thành", "Status check", "Ghi chú"]
for col, h in enumerate(fc_th, 1):
    c = ws5.cell(fc_start + 1, col, h)
    style_cell(c, font=H3, fill=FILL_SECTION, align=CENTER)
ws5.merge_cells(start_row=fc_start + 1, start_column=4, end_row=fc_start + 1, end_column=7)

foundation = [
    ("Meta Pixel + Conversion API firing trên website hiện tại", "W1", "Verify với Tag Assistant + Meta Events Manager"),
    ("GA4 + GTM container active, các event conversion firing đúng", "W1", "Verify với GA4 DebugView"),
    ("4 ads accounts (Meta, Google, TikTok) connected + domain verified", "W1", "Cập nhật trong sheet 'Tài khoản & Hệ thống'"),
    ("Creative bộ 1 produced (5 Meta + 3 Google + 3 TikTok) + Ambrosia approved", "W1", "Approval qua email/Slack"),
    ("Campaign structure built trên 4 platform (chưa publish)", "W1", "Draft sẵn để publish 25/5"),
    ("Ads LIVE trên Meta + Google + TikTok ngày 25/5 (W2)", "W2", "Mandatory milestone — không trễ"),
    ("Looker Studio dashboard live + share link cho Ambrosia", "W2", "Dashboard auto-refresh từ GA4, Meta, Google, TikTok"),
    ("Báo cáo tuần đầu tiên gửi Ambrosia (Mon 9AM)", "W3", "Email + Slack note tóm tắt setup"),
    ("Daily monitoring routine bắt đầu (BC theo dõi delivery, không panic optimize)", "W2-W5", "Học hành vi audience, chưa optimize aggressive"),
    ("Audience seeding: pixel bắt đầu collect data (chưa cần đủ size)", "W2-W5", "End-of-M1: tham khảo, không phải target"),
    ("Content calendar organic post FB+IG+TikTok publish theo lịch", "W2-W5", "3 post FB+IG/tuần, 2-3 video TikTok/tuần"),
    ("Creative refresh #1 (1 batch mới) cuối M1", "W5", "Học content gì hook tốt → chuẩn bị M2"),
    ("Foundation review meeting với Ambrosia (Monthly Catchup #1)", "W5", "Qualitative review, KHÔNG đánh giá KPI số"),
]
for i, (item, week, note) in enumerate(foundation):
    r = fc_start + 2 + i
    ws5.cell(r, 1, item)
    ws5.cell(r, 2, week)
    ws5.cell(r, 3, "Pending")
    ws5.merge_cells(start_row=r, start_column=4, end_row=r, end_column=7)
    ws5.cell(r, 4, note)
    for col in range(1, 5):
        c = ws5.cell(r, col)
        c.font = NORMAL
        c.alignment = LEFT if col in (1, 4) else CENTER
        c.border = BORDER
        if col == 3:
            c.fill = FILL_PHASE_M1

# KPI detail table (M2 + M3+ only — M1 = foundation handled above)
kpi_start = fc_start + 2 + len(foundation) + 2
ws5.merge_cells(start_row=kpi_start, start_column=1, end_row=kpi_start, end_column=7)
c = ws5.cell(kpi_start, 1, "KPI CHI TIẾT THEO KÊNH (bắt đầu từ THÁNG 2)")
style_cell(c, font=H2, fill=FILL_HEADER, align=CENTER)

th = ["Nhóm", "Kênh", "Metric", "Ý nghĩa", "Tháng 1 (Foundation)", "Tháng 2 (Awareness)", "Tháng 3+ (Consideration)"]
for col, h in enumerate(th, 1):
    c = ws5.cell(kpi_start + 1, col, h)
    style_cell(c, font=H3, fill=FILL_SECTION, align=CENTER)

# Format: (nhóm, kênh, metric, ý nghĩa, target_M1_foundation, target_M2_awareness, target_M3_consideration)
kpis = [
    ("Awareness", "Facebook + Instagram Ads", "Reach", "Số người unique nhìn thấy ads", "Reference only (chưa target)", "≥ 50,000 unique reach / tháng", "Maintain + 20% growth"),
    ("Awareness", "Facebook + Instagram Ads", "Impressions", "Tổng số lần ads hiển thị", "Reference only", "≥ 200,000 / tháng", "Maintain"),
    ("Awareness", "Facebook + Instagram Ads", "Frequency", "Số lần 1 người thấy ads (tránh ad fatigue)", "Track (chưa target)", "1.5 - 3.5", "1.5 - 3.5"),
    ("Awareness", "Facebook + Instagram Ads", "CPM", "Cost per 1000 impressions", "Baseline (đo)", "Track + tối ưu", "Giảm 10-20%"),
    ("Awareness", "TikTok Ads", "Video views (≥6s)", "Số người xem video ads >6 giây", "Reference only", "≥ 30,000 / tháng", "Maintain + 30%"),
    ("Awareness", "TikTok Ads", "VTR (View-Through Rate)", "% người xem hết video", "Reference only", ">10% (≥6s)", ">15%"),
    ("Awareness", "TikTok Ads", "Reach", "Người unique tiếp cận", "Reference only", "≥ 30,000", "Maintain + 30%"),
    ("Awareness", "Google Ads", "Search Impression Share (Brand)", "% Ambrosia hiển thị khi search brand", "Live + đo (chưa target)", ">80%", ">90%"),
    ("Awareness", "Google Ads", "GDN Impressions", "Banner display network reach", "Reference only", "≥ 100,000 / tháng", "Maintain"),
    ("Engagement", "Facebook + Instagram organic", "Engagement rate", "(Like + Comment + Share + Save) / Reach", "Track (chưa target)", ">3%", ">4%"),
    ("Engagement", "Facebook + Instagram organic", "Saves + Shares", "Tín hiệu intent cao", "Track", "≥ 50 / tháng", "≥ 100 / tháng"),
    ("Engagement", "TikTok organic", "Average watch time", "Thời gian xem trung bình", "Track", ">15 giây", ">20 giây"),
    ("Engagement", "Facebook Page + IG", "Follower growth", "Số follower mới", "Track (chưa target)", "+10% / tháng", "+10% / tháng"),
    ("Audience", "Meta Pixel", "Website visitor (30 ngày)", "Custom audience website đã ghé", "Bắt đầu seed (chưa target)", "≥ 5,000 size", "≥ 10,000 size"),
    ("Audience", "Meta Pixel", "Video viewer 50%+", "Custom audience xem video ads ≥50%", "Bắt đầu seed", "≥ 10,000 size", "≥ 20,000 size"),
    ("Audience", "Meta Pixel", "Page engager (90 ngày)", "Custom audience đã engage FB/IG", "Bắt đầu seed", "≥ 3,000 size", "≥ 7,000 size"),
    ("Audience", "TikTok Pixel", "Video viewer + website visitor", "Custom audience TikTok cho retargeting", "Bắt đầu seed", "≥ 5,000 size", "≥ 10,000 size"),
    ("Audience", "Google Ads", "Remarketing list size", "Audience cho GDN remarketing", "Bắt đầu seed", "≥ 2,000 (đủ ngưỡng GDN)", "≥ 5,000"),
    ("Intent", "Website (cũ → mới W9)", "Sessions từ ads", "Traffic ads về website", "Reference only", "≥ 1,500 / tháng", "≥ 3,000 / tháng"),
    ("Intent", "Website", "Avg session duration", "Chất lượng traffic", "Track baseline", ">45 giây", ">60 giây"),
    ("Intent", "Website", "B2B inquiry form submit", "Lead B2B gửi form (event, partnership)", "Reference only", "≥ 5 / tháng", "≥ 15 / tháng"),
    ("Intent", "Website", "Booking / Reservation click", "Click vào nút booking", "Reference only", "≥ 30 / tháng", "≥ 80 / tháng"),
    ("Intent", "Website", "Phone call click (mobile)", "Click số điện thoại trên mobile", "Reference only", "≥ 20 / tháng", "≥ 50 / tháng"),
    ("Intent", "Google Business Profile", "Direction + Call request", "Người tìm đường đến nhà hàng", "Baseline (đo)", "Tăng 20% MoM", "Tăng 30% MoM"),
    ("Brand", "Google Search", "Branded search volume", "Người chủ động search 'Ambrosia'", "Baseline (đo)", "+30% so với baseline", "+50%"),
    ("Brand", "Direct traffic website", "Direct sessions", "Người truy cập trực tiếp domain", "Baseline (đo)", "+20% so với baseline", "+30%"),
    ("B2B", "LinkedIn / Email outbound (nếu add scope)", "Corporate inquiry", "Inquiry từ doanh nghiệp", "Reference only", "≥ 3 / tháng", "≥ 8 / tháng"),
    ("B2B", "Email nurture list", "B2B subscriber", "B2B đăng ký nhận newsletter", "Bắt đầu collect", "≥ 50 subscriber", "≥ 150 subscriber"),
    ("Reporting", "Looker Studio", "Dashboard auto-refresh", "Live link real-time", "Live W2 (mandatory)", "Maintain", "Maintain"),
    ("Reporting", "Email + Slack", "Báo cáo tuần (Mon 9AM)", "Auto email KPI + insight", "Bắt đầu W3", "Liên tục", "Liên tục"),
    ("Reporting", "PDF + meeting", "Monthly catchup report", "PDF chi tiết + present 60 phút", "W5 (Foundation review)", "W10 (Awareness review)", "—"),
]
group_fills = {
    "Awareness": FILL_PHASE_M1,
    "Engagement": PatternFill("solid", fgColor="FCE4D6"),
    "Audience": FILL_PHASE_M2,
    "Intent": PatternFill("solid", fgColor="C6E0B4"),
    "Brand": PatternFill("solid", fgColor="DDEBF7"),
    "B2B": PatternFill("solid", fgColor="EAD1DC"),
    "Reporting": PatternFill("solid", fgColor="E2EFDA"),
}
for i, k in enumerate(kpis):
    r = kpi_start + 2 + i
    for col, val in enumerate(k, 1):
        c = ws5.cell(r, col, val)
        style_cell(c, font=NORMAL, fill=group_fills.get(k[0]) if col == 1 else None, align=LEFT if col in (3, 4, 5, 6, 7) else CENTER)
    ws5.row_dimensions[r].height = 26

note_row = kpi_start + 2 + len(kpis) + 1
ws5.merge_cells(start_row=note_row, start_column=1, end_row=note_row + 4, end_column=7)
note = (
    "LƯU Ý KPI — QUAN TRỌNG:\n"
    "• THÁNG 1 (W1-W5) = FOUNDATION: KHÔNG có target số liệu. Đo bằng SETUP COMPLETION CHECKLIST. Số liệu thu được trong M1 là tham khảo để học, KHÔNG dùng đánh giá hiệu suất.\n"
    "• THÁNG 2 (W6-W10) = AWARENESS: tháng đầu có KPI số liệu chính thức (Reach, Audience size, Video views, Engagement). Retargeting layer nhẹ bắt đầu hỗ trợ.\n"
    "• THÁNG 3+ (ngoài scope dự án) = CONSIDERATION + CONVERSION: lúc này CPA, ROAS, qualified lead mới được tracking chính thức làm KPI đánh giá.\n"
    "• High-class brand → KHÔNG dùng creative giảm giá / promo gấp. Tone tinh tế, focus vào trải nghiệm + storytelling."
)
c = ws5.cell(note_row, 1, note)
style_cell(c, font=SMALL, fill=PatternFill("solid", fgColor="FFF2CC"), align=LEFT)

ws5.column_dimensions["A"].width = 14
ws5.column_dimensions["B"].width = 22
ws5.column_dimensions["C"].width = 30
ws5.column_dimensions["D"].width = 34
ws5.column_dimensions["E"].width = 24
ws5.column_dimensions["F"].width = 26
ws5.column_dimensions["G"].width = 24
ws5.freeze_panes = "A" + str(kpi_start + 2)

# ============================================================
# SHEET 6: ƯỚC TÍNH CHI PHÍ (NEW)
# ============================================================
wsB = wb.create_sheet("Ước tính chi phí")
wsB.merge_cells("A1:G1")
c = wsB.cell(1, 1, f"ƯỚC TÍNH CHI PHÍ ADS — {fmt_usd(TOTAL_BUDGET_USD)}/THÁNG (~{fmt_vnd(TOTAL_BUDGET_USD * USD_TO_VND)})")
style_cell(c, font=H1, fill=FILL_TITLE, align=CENTER)
wsB.row_dimensions[1].height = 28

# === Block 1: Recommended scenario (Scenario A) ===
wsB.merge_cells("A3:G3")
c = wsB.cell(3, 1, "SCENARIO A — RECOMMENDED: Foundation phase, chia 4 kênh (tháng 1 — đặt nền, chưa kỳ vọng KPI số)")
style_cell(c, font=H2, fill=FILL_HEADER, align=CENTER)

th = ["Kênh", "% Budget", "USD / tháng", "VND / tháng", "USD / ngày", "Loại campaign chính", "Reach / Impressions ước tính"]
for col, h in enumerate(th, 1):
    c = wsB.cell(4, col, h)
    style_cell(c, font=H3, fill=FILL_SECTION, align=CENTER)

scenario_a = [
    ("Facebook + Instagram (Meta)", 0.50, "Awareness + Engagement campaign (Reach, Brand Awareness)", "30,000-60,000 reach"),
    ("Google Ads — Search Brand", 0.15, "Brand keyword 'Ambrosia + variations'", "150-400 click (~5,000 impr)"),
    ("Google Ads — GDN Remarketing", 0.10, "Banner remarketing website visitor", "8,000-15,000 impr"),
    ("TikTok Ads", 0.20, "Spark Ads từ organic top-performer (video views)", "15,000-30,000 video views"),
    ("Buffer / contingency", 0.05, "Test creative mới, scale winner đột xuất", "—"),
]
total_pct = 0
total_usd = 0
for i, (channel, pct, campaign, reach) in enumerate(scenario_a):
    r = 5 + i
    usd_month = TOTAL_BUDGET_USD * pct
    vnd_month = usd_month * USD_TO_VND
    usd_day = usd_month / 30
    total_pct += pct
    total_usd += usd_month
    wsB.cell(r, 1, channel)
    wsB.cell(r, 2, f"{int(pct*100)}%")
    wsB.cell(r, 3, fmt_usd(usd_month))
    wsB.cell(r, 4, fmt_vnd(vnd_month))
    wsB.cell(r, 5, fmt_usd(usd_day))
    wsB.cell(r, 6, campaign)
    wsB.cell(r, 7, reach)
    for col in range(1, 8):
        c = wsB.cell(r, col)
        c.font = NORMAL
        c.alignment = LEFT if col in (1, 6, 7) else CENTER
        c.border = BORDER

# Total row
total_row = 5 + len(scenario_a)
wsB.cell(total_row, 1, "TOTAL")
wsB.cell(total_row, 2, f"{int(total_pct*100)}%")
wsB.cell(total_row, 3, fmt_usd(total_usd))
wsB.cell(total_row, 4, fmt_vnd(total_usd * USD_TO_VND))
wsB.cell(total_row, 5, fmt_usd(total_usd / 30))
wsB.cell(total_row, 6, "")
wsB.cell(total_row, 7, "")
for col in range(1, 8):
    c = wsB.cell(total_row, col)
    c.font = H3
    c.fill = FILL_SECTION
    c.alignment = LEFT if col == 6 else CENTER
    c.border = BORDER

# === Block 2: Tháng 2 shift (retargeting) ===
b2_start = total_row + 3
wsB.merge_cells(start_row=b2_start, start_column=1, end_row=b2_start, end_column=7)
c = wsB.cell(b2_start, 1, "SCENARIO A — THÁNG 2: Awareness KPI chính thức + bắt đầu retargeting layer khi audience đủ size")
style_cell(c, font=H2, fill=FILL_HEADER, align=CENTER)

for col, h in enumerate(th, 1):
    c = wsB.cell(b2_start + 1, col, h)
    style_cell(c, font=H3, fill=FILL_SECTION, align=CENTER)

scenario_a_m2 = [
    ("Facebook + Instagram — Awareness", 0.30, "Vẫn duy trì reach mới", "20,000-40,000 reach"),
    ("Facebook + Instagram — Retargeting", 0.25, "Retarget website visitor + video viewer 50%+", "Higher CTR + lower CPA"),
    ("Google Ads — Search Brand + Non-brand", 0.15, "Mở rộng keyword non-brand (cafe high-class HCM, etc.)", "200-500 click"),
    ("Google Ads — GDN Remarketing", 0.10, "Tăng frequency cho audience đã visit", "10,000-20,000 impr"),
    ("TikTok Ads — Awareness + Spark", 0.15, "Maintain awareness, scale Spark winner", "15,000-25,000 video views"),
    ("Buffer / lead gen test", 0.05, "Test Lead Gen Form Meta cho B2B inquiry", "5-15 lead test"),
]
for i, (channel, pct, campaign, reach) in enumerate(scenario_a_m2):
    r = b2_start + 2 + i
    usd_month = TOTAL_BUDGET_USD * pct
    vnd_month = usd_month * USD_TO_VND
    usd_day = usd_month / 30
    wsB.cell(r, 1, channel)
    wsB.cell(r, 2, f"{int(pct*100)}%")
    wsB.cell(r, 3, fmt_usd(usd_month))
    wsB.cell(r, 4, fmt_vnd(vnd_month))
    wsB.cell(r, 5, fmt_usd(usd_day))
    wsB.cell(r, 6, campaign)
    wsB.cell(r, 7, reach)
    for col in range(1, 8):
        c = wsB.cell(r, col)
        c.font = NORMAL
        c.alignment = LEFT if col in (1, 6, 7) else CENTER
        c.border = BORDER

# Total
total_row2 = b2_start + 2 + len(scenario_a_m2)
total_usd2 = sum(TOTAL_BUDGET_USD * p for _, p, _, _ in scenario_a_m2)
wsB.cell(total_row2, 1, "TOTAL")
wsB.cell(total_row2, 2, "100%")
wsB.cell(total_row2, 3, fmt_usd(total_usd2))
wsB.cell(total_row2, 4, fmt_vnd(total_usd2 * USD_TO_VND))
wsB.cell(total_row2, 5, fmt_usd(total_usd2 / 30))
wsB.cell(total_row2, 6, "")
wsB.cell(total_row2, 7, "")
for col in range(1, 8):
    c = wsB.cell(total_row2, col)
    c.font = H3
    c.fill = FILL_SECTION
    c.alignment = LEFT if col == 6 else CENTER
    c.border = BORDER

# === Block 3: Alternative scenarios ===
b3_start = total_row2 + 3
wsB.merge_cells(start_row=b3_start, start_column=1, end_row=b3_start, end_column=7)
c = wsB.cell(b3_start, 1, "SCENARIO B & C — ALTERNATIVE (chọn nếu Scenario A quá mỏng)")
style_cell(c, font=H2, fill=FILL_HEADER, align=CENTER)

th2 = ["Scenario", "Cách phân bổ", "Ưu", "Nhược", "Khi nào nên dùng"]
for col, h in enumerate(th2, 1):
    c = wsB.cell(b3_start + 1, col, h)
    style_cell(c, font=H3, fill=FILL_SECTION, align=CENTER)

alt_scenarios = [
    ("Scenario B — Concentrated 3 kênh", "Meta 60% ($240) + Google 30% ($120) + TikTok organic only (drop ads), TikTok 0% / 10% buffer", "Đủ ngân sách cho Meta + Google ra data sạch. TikTok organic vẫn build awareness", "Mất kênh ads paid của TikTok → reach trẻ giảm", "Nếu Scenario A cho thấy TikTok ads quá ít data sau 2-3 tuần đầu"),
    ("Scenario C — Burst mode 2 kênh", "Tuần 1-2: Meta $200 + Google $200 (full budget). Tuần 3-4: TikTok $200 + Meta $200. Quay vòng", "Mỗi 2 tuần có 1 platform được fund đủ để học nhanh", "Khó duy trì always-on; gián đoạn signal cho từng platform", "Nếu muốn test sâu từng platform trước khi commit budget dài hạn"),
    ("Scenario D — Scale up", "Tăng budget lên $800-1,500/tháng từ tháng 3 nếu KPI tháng 1-2 đạt target", "Đủ ngân sách cho conversion campaign + lookalike scale", "Cần Ambrosia confirm trước cuối tháng 2", "Khi CPA tháng 2 đã có baseline + retargeting performance dương"),
]
for i, (sc, alloc, pro, con, when) in enumerate(alt_scenarios):
    r = b3_start + 2 + i
    wsB.cell(r, 1, sc)
    wsB.cell(r, 2, alloc)
    wsB.cell(r, 3, pro)
    wsB.cell(r, 4, con)
    wsB.cell(r, 5, when)
    for col in range(1, 6):
        c = wsB.cell(r, col)
        c.font = NORMAL
        c.alignment = LEFT
        c.border = BORDER
    wsB.row_dimensions[r].height = 50

# === Block 4: Total cost of ownership (Ads + Tools + BC fee placeholder) ===
b4_start = b3_start + 2 + len(alt_scenarios) + 2
wsB.merge_cells(start_row=b4_start, start_column=1, end_row=b4_start, end_column=7)
c = wsB.cell(b4_start, 1, "TỔNG CHI PHÍ VẬN HÀNH HÀNG THÁNG (Ads + Tools)")
style_cell(c, font=H2, fill=FILL_HEADER, align=CENTER)

th3 = ["Hạng mục", "USD / tháng (low)", "USD / tháng (high)", "VND / tháng (low)", "VND / tháng (high)", "Ghi chú"]
for col, h in enumerate(th3, 1):
    c = wsB.cell(b4_start + 1, col, h)
    style_cell(c, font=H3, fill=FILL_SECTION, align=CENTER)

cost_breakdown = [
    ("Ads spend (Meta + Google + TikTok)", 400, 400, "Cố định theo agreement"),
    ("Hosting Webflow Business", 39, 39, "Recommend chính (Section B sheet 'Tài khoản & Hệ thống')"),
    ("Email marketing (Brevo / Mailchimp)", 0, 20, "Free tier OK giai đoạn đầu, scale lên khi list >300"),
    ("CDN / Performance (Cloudflare)", 0, 20, "Free tier đủ cho cafe website"),
    ("CRM (HubSpot Free)", 0, 0, "Free tier đủ cho B2B leads giai đoạn đầu"),
    ("Stock asset (Pexels / Envato)", 0, 16, "Free option đủ cho hầu hết creative"),
    ("Reporting (Looker Studio)", 0, 0, "Free, native Google"),
    ("Buffer cho phát sinh (creative production, chụp ảnh)", 0, 50, "Tùy nhu cầu — refresh creative, chụp menu mới"),
]
total_low = 0
total_high = 0
for i, (item, low, high, note) in enumerate(cost_breakdown):
    r = b4_start + 2 + i
    total_low += low
    total_high += high
    wsB.cell(r, 1, item)
    wsB.cell(r, 2, fmt_usd(low))
    wsB.cell(r, 3, fmt_usd(high))
    wsB.cell(r, 4, fmt_vnd(low * USD_TO_VND))
    wsB.cell(r, 5, fmt_vnd(high * USD_TO_VND))
    wsB.cell(r, 6, note)
    for col in range(1, 7):
        c = wsB.cell(r, col)
        c.font = NORMAL
        c.alignment = LEFT if col in (1, 6) else CENTER
        c.border = BORDER

# Total
tr = b4_start + 2 + len(cost_breakdown)
wsB.cell(tr, 1, "TỔNG CỘNG (Ads + Tools)")
wsB.cell(tr, 2, fmt_usd(total_low))
wsB.cell(tr, 3, fmt_usd(total_high))
wsB.cell(tr, 4, fmt_vnd(total_low * USD_TO_VND))
wsB.cell(tr, 5, fmt_vnd(total_high * USD_TO_VND))
wsB.cell(tr, 6, "Chưa bao gồm phí dịch vụ BC (báo giá riêng)")
for col in range(1, 7):
    c = wsB.cell(tr, col)
    c.font = H3
    c.fill = FILL_SECTION
    c.alignment = LEFT if col in (1, 6) else CENTER
    c.border = BORDER

# === Block 5: Cảnh báo + lưu ý quan trọng ===
b5_start = tr + 3
wsB.merge_cells(start_row=b5_start, start_column=1, end_row=b5_start, end_column=7)
c = wsB.cell(b5_start, 1, "LƯU Ý NGÂN SÁCH — ĐỌC KỸ TRƯỚC KHI APPROVE")
style_cell(c, font=H2, fill=FILL_HEADER, align=CENTER)

notes = [
    ("⚠ Ngưỡng tối thiểu của ad platform", "Meta: $5/ad set/ngày để thoát Learning Phase. Google Ads: $5-10/ngày/campaign để cạnh tranh auction. TikTok: $20/ngày khuyến nghị. Với $400/tháng chia 4 kênh → mỗi kênh chạm ngưỡng tối thiểu, không có biên optimize aggressive."),
    ("⚠ Trade-off của ngân sách $400/tháng", "Đây là 'starter budget' để học và xây audience, KHÔNG để scale doanh thu. Tháng 1 = FOUNDATION (chưa kỳ vọng KPI số); tháng 2 = bắt đầu KPI awareness; muốn convert mạnh cần scale lên $800-1,500/tháng từ tháng 3."),
    ("⚠ Tỉ giá USD/VND", f"Ước tính theo tỷ giá {USD_TO_VND:,} VND/USD (cập nhật 05/2026). Nếu Ambrosia thanh toán ads bằng VND, chi phí thực tế có thể dao động ±5%."),
    ("⚠ Phí dịch vụ BC", "Ngân sách $400 trên CHỈ là chi phí ads + tools. Phí dịch vụ BC (project lead, dev, creative, ads management) báo giá riêng theo SOW."),
    ("✓ Khuyến nghị Scenario A", "BC đề xuất Scenario A cho tháng 1 (chia 4 kênh, awareness-first). Cuối tháng 1, review data + chuyển sang Scenario A-tháng-2 (tăng retargeting). Reassess Scenario B/C nếu 1 platform không sinh data."),
    ("✓ Cần Ambrosia confirm", "(1) Ngân sách $400/tháng cố định trong 2 tháng dự án. (2) Có sẵn quyết định scale lên $800+ từ tháng 3 nếu KPI tháng 2 đạt target."),
]
for i, (title, content) in enumerate(notes):
    r = b5_start + 1 + i
    a = wsB.cell(r, 1, title)
    style_cell(a, font=H3, fill=FILL_SECTION, align=LEFT)
    wsB.merge_cells(start_row=r, start_column=2, end_row=r, end_column=7)
    b = wsB.cell(r, 2, content)
    style_cell(b, font=NORMAL, align=LEFT)
    wsB.row_dimensions[r].height = 48

# Column widths
wsB.column_dimensions["A"].width = 32
wsB.column_dimensions["B"].width = 16
wsB.column_dimensions["C"].width = 16
wsB.column_dimensions["D"].width = 18
wsB.column_dimensions["E"].width = 16
wsB.column_dimensions["F"].width = 38
wsB.column_dimensions["G"].width = 32

# ============================================================
# SHEET 7: RỦI RO & PHƯƠNG ÁN
# ============================================================
ws4 = wb.create_sheet("Rủi ro & Phương án")
ws4.merge_cells("A1:E1")
c = ws4.cell(1, 1, "RỦI RO & PHƯƠNG ÁN GIẢM THIỂU")
style_cell(c, font=H1, fill=FILL_TITLE, align=CENTER)
ws4.row_dimensions[1].height = 26

th = ["STT", "Rủi ro", "Khả năng", "Tác động", "Phương án giảm thiểu"]
for col, h in enumerate(th, 1):
    c = ws4.cell(3, col, h)
    style_cell(c, font=H2, fill=FILL_HEADER, align=CENTER)
ws4.row_dimensions[3].height = 30

risks = [
    ("Ambrosia trễ gửi mục tiêu / yêu cầu trong pre-week (11-15/5)", "Cao", "Kickoff W1 không có cơ sở, BC phải hỏi lại nhiều", "BC gửi template Goals & Requirements 11/5 với guideline rõ; reminder ngày 13/5"),
    ("Ambrosia trễ phê duyệt creative / approve gate", "Cao", "Trượt deadline ads 25/05 và website 13/07", "SOW: trễ N ngày = ads/website delay N ngày; reminder 24h trước hạn"),
    ("Brand asset Ambrosia không đủ / không chất lượng", "Trung bình", "Creative ads yếu cho thương hiệu high-class", "BC quote thêm phí chụp ảnh/video chuyên nghiệp (5-15 triệu VND) — high-class brand cần asset tương xứng"),
    ("Domain / DNS / SSL trục trặc khi go-live website", "Trung bình", "Website delay 1-3 ngày", "BC chuẩn bị DNS từ W7, có rollback plan, test trước go-live"),
    ("Meta / Google / TikTok ads bị reject ở W1-W2", "Trung bình", "Ads delay 1-2 ngày so với 25/05", "BC submit ads chiều thứ 6 W1 để có buffer xử lý reject"),
    ("Ambrosia thay đổi scope giữa chừng (thêm SEO, email blast, event...)", "Cao", "Trượt timeline gốc", "SOW: change request → quote riêng, không nhét timeline gốc"),
    ("Conversion rate thấp khiến Ambrosia mất kiên nhẫn ở tháng 1", "Cao", "Áp lực dừng ads sớm trước khi audience đủ data", "Education ngay Kickoff: tháng 1 = FOUNDATION (setup + học), KHÔNG có KPI số. Tháng 2 mới có target REACH + AUDIENCE SIZE. Conversion là M3+ (ngoài scope)."),
    ("Ngân sách $400/tháng quá mỏng cho 4 kênh", "Cao", "Mỗi kênh không đủ data để optimize aggressive", "Đề xuất Scenario B (3 kênh) hoặc Scenario C (burst mode) — xem sheet 'Ước tính chi phí'"),
    ("Website mới có page speed kém (mobile <80)", "Trung bình", "Ads CPA cao + Quality Score thấp sau migration", "W7-8 dành buổi cuối QA speed; không go-live nếu mobile <80"),
    ("Tracking sai sau migration W9 (Pixel/GA4 không fire)", "Trung bình", "Mất conversion data, optimize sai hướng", "BC verify với Tag Assistant + GA4 DebugView ở W1 và W9; test conversion thật"),
    ("Performance ads giảm 1-2 tuần sau migration website W9", "Cao", "CTR/CPA xấu tạm thời", "Dự trù 'learning phase' 7-14 ngày sau migration; báo trước Ambrosia ở W7-8"),
    ("Ambrosia không có người trả comment / B2B inquiry", "Cao", "Mất leads, đặc biệt B2B (cần phản hồi nhanh)", "Chốt SOW: Ambrosia tự xử lý hoặc BC quote thêm community management"),
    ("Tone creative chưa đúng brand high-class (dùng template / cliché)", "Trung bình", "Tổn hại brand perception", "BC submit creative concept cho Ambrosia review trước khi sản xuất; 1-2 vòng feedback"),
    ("Ảnh / nội dung Ambrosia gửi không đúng format (file lớn, sai tỉ lệ)", "Trung bình", "BC mất thời gian xử lý lại", "BC gửi 'asset spec sheet' ngay W1 (kích thước, format, naming)"),
    ("Decision maker Ambrosia thay đổi giữa dự án", "Thấp", "Phải re-align toàn bộ scope", "SOW ghi rõ decision maker đầu dự án; đổi → kickoff lại 60 phút"),
]
risk_fill = {"Cao": FILL_RISK_HIGH, "Trung bình": FILL_RISK_MED, "Thấp": FILL_RISK_LOW}
for i, (risk, prob, impact, mit) in enumerate(risks):
    r = 4 + i
    ws4.cell(r, 1, i + 1)
    ws4.cell(r, 2, risk)
    ws4.cell(r, 3, prob)
    ws4.cell(r, 4, impact)
    ws4.cell(r, 5, mit)
    for col in range(1, 6):
        c = ws4.cell(r, col)
        c.font = NORMAL
        c.alignment = LEFT if col in (2, 4, 5) else CENTER
        c.border = BORDER
    ws4.cell(r, 3).fill = risk_fill[prob]
    ws4.row_dimensions[r].height = 38

ws4.column_dimensions["A"].width = 5
ws4.column_dimensions["B"].width = 45
ws4.column_dimensions["C"].width = 13
ws4.column_dimensions["D"].width = 38
ws4.column_dimensions["E"].width = 60
ws4.freeze_panes = "A4"

wb.save(OUT)
print(f"Saved: {OUT}")
