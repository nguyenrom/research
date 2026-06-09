"""Generate 4 Word documents for Databricks implementation project PM kit."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from pathlib import Path

OUT = Path(__file__).parent

# ---------- party names ----------
VENDOR = "Blue Coral"
VENDOR_SHORT = "BC"
CUSTOMER = "VinaCapital"
CUSTOMER_SHORT = "VC"

# ---------- project metadata ----------
PROJECT_CODE = "Databricks-P1"
PROJECT_FULL = "VinaCapital Core Data Platform — Phase 1 (Assessment + Foundation + PoC)"
CLOUD = "Azure"
TENANT = "Tenant VinaCapital"
WORK_MODE = "Hybrid (onsite VinaCapital office + remote)"

# ---------- people ----------
PREPARER = "Nguyen Le"
BC_CEO_PO = "Nguyen Le"      # Blue Coral CEO / Project Owner
BC_PM = "Tin Huynh"
BC_TECH_LEAD = "Dung Phan"   # also Architect
BC_ARCHITECT = "Dung Phan"
BC_FINANCE_BA = "Tess Pham"  # Finance domain Business Analyst
VC_PO = "Khiem Pham"
VC_TECH_LEAD = "Hien Vo"

# ---------- key dates ----------
PROJECT_START = "18/05/2026"   # work begins (T2)
KICKOFF = "19/05/2026"          # formal kickoff meeting (T3)
TARGET_CLOSE = "09/07/2026"
PROJECT_END = "10/07/2026"
DOC_DATE = "12/05/2026"

# ---------- shared helpers ----------
NAVY = RGBColor(0x1F, 0x3A, 0x5F)
GRAY = RGBColor(0x55, 0x55, 0x55)
LIGHT = RGBColor(0xEE, 0xEE, 0xEE)


def set_cell_bg(cell, hex_color):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tc_pr.append(shd)


def style_doc(doc):
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)
    for s in ["Heading 1", "Heading 2", "Heading 3"]:
        if s in [x.name for x in doc.styles]:
            doc.styles[s].font.color.rgb = NAVY
            doc.styles[s].font.name = "Calibri"


def add_title(doc, text, subtitle=None):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(22)
    run.font.color.rgb = NAVY
    if subtitle:
        p2 = doc.add_paragraph()
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r2 = p2.add_run(subtitle)
        r2.italic = True
        r2.font.size = Pt(11)
        r2.font.color.rgb = GRAY
    doc.add_paragraph()


def add_h1(doc, text):
    h = doc.add_heading(text, level=1)
    for r in h.runs:
        r.font.color.rgb = NAVY


def add_h2(doc, text):
    h = doc.add_heading(text, level=2)
    for r in h.runs:
        r.font.color.rgb = NAVY


def add_para(doc, text, italic=False, bold=False):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.italic = italic
    r.bold = bold
    return p


def add_bullets(doc, items):
    for it in items:
        doc.add_paragraph(it, style="List Bullet")


def add_table(doc, headers, rows, col_widths=None):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.style = "Light Grid Accent 1"
    hdr = t.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = ""
        p = hdr[i].paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_bg(hdr[i], "1F3A5F")
        hdr[i].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    for ri, row in enumerate(rows):
        cells = t.rows[ri + 1].cells
        for ci, val in enumerate(row):
            cells[ci].text = str(val)
            cells[ci].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    if col_widths:
        for row in t.rows:
            for i, w in enumerate(col_widths):
                row.cells[i].width = w
    return t


def add_signoff(doc, parties):
    add_h1(doc, "Sign-off")
    add_para(doc, "Các bên xác nhận đã đọc, hiểu và đồng ý với nội dung tài liệu này.")
    t = doc.add_table(rows=4, cols=len(parties))
    t.style = "Table Grid"
    for ci, p in enumerate(parties):
        t.rows[0].cells[ci].text = p
        for r in t.rows[0].cells[ci].paragraphs[0].runs:
            r.bold = True
        t.rows[1].cells[ci].text = "Họ tên: ________________________"
        t.rows[2].cells[ci].text = "Chức vụ: ________________________"
        t.rows[3].cells[ci].text = "Ngày ký: ________________________"


def add_footer_note(doc, version="1.0", owner=None):
    if owner is None:
        owner = f"{BC_CEO_PO} (PO)"
    section = doc.sections[0]
    footer = section.footer
    p = footer.paragraphs[0]
    p.text = f"Version {version}  |  Owner: {owner}  |  Confidential — {VENDOR} x {CUSTOMER}"
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.size = Pt(9)
        r.font.color.rgb = GRAY


# ============================================================
# DOC 1 — PROJECT CHARTER
# ============================================================
def doc_charter():
    doc = Document()
    style_doc(doc)
    add_title(
        doc,
        "PROJECT CHARTER",
        f"{PROJECT_CODE} — {PROJECT_FULL}",
    )

    # Document control
    add_h1(doc, "1. Document Control")
    add_table(
        doc,
        ["Field", "Value"],
        [
            ["Project Code", PROJECT_CODE],
            ["Project Title", PROJECT_FULL],
            ["Document Title", "Project Charter"],
            ["Version", "1.0 (Draft)"],
            ["Prepared by", f"{PREPARER} ({VENDOR_SHORT})"],
            ["Approved by", f"{VC_PO} ({CUSTOMER_SHORT}) / {BC_CEO_PO} ({VENDOR_SHORT})"],
            ["Date issued", DOC_DATE],
            ["Project Start", f"{PROJECT_START} (work begins, parallel workstream 1/2/3)"],
            ["Kickoff Meeting", f"{KICKOFF}"],
            ["Target Sign-off", f"{TARGET_CLOSE}"],
            ["Next review", f"Sau Kickoff Meeting ({KICKOFF})"],
        ],
    )

    add_h1(doc, "2. Project Overview")
    add_h2(doc, "2.1 Background")
    add_para(
        doc,
        f"{CUSTOMER} là tập đoàn quản lý quỹ và đầu tư hàng đầu tại Việt Nam, vận hành nhiều "
        "hệ thống nghiệp vụ và nguồn dữ liệu phân tán: PMS (Portfolio Management System), MIO, "
        "Salesforce, Distributor, Custodian, Excel-based reports, VSDC (Depository), ESM, "
        f"Datahub và các MarketS. Hiện tại dữ liệu rời rạc, khó tổng hợp phục vụ báo cáo và phân tích. "
        f"{CUSTOMER} chọn {VENDOR} đồng hành xây dựng nền tảng Core Data Platform trên Databricks "
        f"({CLOUD}), bắt đầu bằng giai đoạn Phase 1 này: khảo sát toàn cảnh hệ thống nguồn, "
        "thiết kế kiến trúc nền tảng, setup hạ tầng và triển khai PoC.",
    )
    add_h2(doc, "2.2 Business Case")
    add_para(
        doc,
        "Phase 1 đặt nền móng cho lộ trình Lakehouse dài hạn: (a) có được bản đồ toàn cảnh "
        "hệ thống nguồn và roadmap tích hợp, (b) có nền tảng kỹ thuật vận hành được (workspace, "
        "Unity Catalog, security, CI/CD baseline) để các phase sau ingest pipeline thực tế, "
        "(c) PoC chứng minh framework phù hợp với nghiệp vụ Fund Management trước khi đầu tư lớn.",
    )
    add_h2(doc, "2.3 Strategic Alignment")
    add_para(
        doc,
        f"Dự án này là Phase 1 trong lộ trình Data Modernization của {CUSTOMER}. "
        "Kết quả Phase 1 là input bắt buộc cho các phase tiếp theo (ingest production data, "
        "BI consolidation, ML use case). Đây không phải dự án độc lập mà là bước khởi động "
        "của chương trình đa năm.",
    )

    add_h1(doc, "3. Objectives (SMART)")
    add_table(
        doc,
        ["#", "Objective", "Metric / Target", "Deadline"],
        [
            ["O1", "Hoàn thành Landscape Assessment hệ thống PMS & MarketS", "Báo cáo hiện trạng + roadmap được nghiệm thu", "12/06/2026"],
            ["O2", "Hoàn thành Landscape Assessment 8 hệ thống nguồn còn lại + Consolidate", "Báo cáo hợp nhất + roadmap được nghiệm thu", "03/07/2026"],
            ["O3", "Thiết kế & setup Core Data Platform trên Azure Databricks", "Workspace, Unity Catalog, security, CI/CD baseline live", "15/06/2026"],
            ["O4", "Triển khai PoC + Demo framework cho VinaCapital", "PoC chạy được, demo được nghiệm thu", "03/07/2026"],
            ["O5", "Closure & sign-off bàn giao", "Biên bản nghiệm thu ký", "09/07/2026"],
        ],
    )

    add_h1(doc, "4. Scope")
    add_h2(doc, "4.1 In-Scope")
    add_para(doc, "Workstream 1 — Landscape Assessment: PMS System & MarketS", bold=True)
    add_bullets(
        doc,
        [
            "Khảo sát hiện trạng PMS và các MarketS",
            "Phỏng vấn người dùng, thu thập tài liệu, phân tích luồng dữ liệu",
            "Xây dựng roadmap tích hợp",
        ],
    )
    add_para(doc, "Workstream 2 — Landscape Assessment: Source Systems & Consolidate", bold=True)
    add_bullets(
        doc,
        [
            "Khảo sát đánh giá 8 hệ thống nguồn: MIO, Salesforce, Distributor, Custodian, "
            "Excel, Depository (VSDC), ESM, Datahub",
            "Tổng hợp kết quả khảo sát từ WS1 và WS2",
            "Hoàn thiện roadmap tích hợp hợp nhất",
        ],
    )
    add_para(doc, "Workstream 3 — Design & Setup Core Data Platform", bold=True)
    add_bullets(
        doc,
        [
            "Thiết kế kiến trúc nền tảng dữ liệu lõi (Lakehouse medallion architecture)",
            f"Cài đặt và cấu hình hạ tầng Databricks trên {CLOUD}: Workspace, Unity Catalog, "
            "networking, IAM, secret management, cluster policy, CI/CD baseline",
            "Triển khai PoC trên framework đã thiết kế",
            f"Trình bày framework và demo PoC cho {CUSTOMER}",
        ],
    )
    add_para(doc, "Workstream 4 — Closure", bold=True)
    add_bullets(
        doc,
        [
            "Họp tổng kết dự án",
            "Nghiệm thu các sản phẩm bàn giao",
            "Ký biên bản kết thúc Phase 1",
        ],
    )

    add_h2(doc, "4.2 Out-of-Scope (Phase 1)")
    add_bullets(
        doc,
        [
            "Ingest dữ liệu production từ source systems (chuyển sang Phase 2)",
            "Pipeline ETL/ELT cho từng hệ thống nguồn cụ thể (Phase 2)",
            "Migration BI dashboard hiện hữu (Phase sau)",
            "Triển khai ML model production (Phase sau)",
            "Mua sắm Databricks license / Azure subscription — do VinaCapital chịu",
            "Hỗ trợ 24/7 dài hạn sau closure (cần hợp đồng MSA riêng nếu có nhu cầu)",
            "Đào tạo end-user sâu (chỉ có KT cho team kỹ thuật)",
        ],
    )

    add_h1(doc, "5. Key Deliverables")
    add_table(
        doc,
        ["Phase / WS", "Deliverable", "Format", "Acceptance Owner"],
        [
            ["Inception", "Project Charter, Working Agreement", "Word/PDF, signed", f"{VC_PO} ({CUSTOMER_SHORT})"],
            ["WS1 — Assessment PMS", "Báo cáo hiện trạng PMS & MarketS + roadmap WS1", "Word/PDF + slide", f"{VC_PO} ({CUSTOMER_SHORT})"],
            ["WS2 — Assessment Sources", "Báo cáo 8 hệ thống nguồn + roadmap hợp nhất", "Word/PDF + slide", f"{VC_PO} ({CUSTOMER_SHORT})"],
            ["WS3 — Design", "Solution Architecture + Security Design", "Word + Diagram", f"{VC_TECH_LEAD} ({CUSTOMER_SHORT})"],
            ["WS3 — Setup", "Workspace provisioned, IaC code, Setup guide", "Git + Word", f"{VC_TECH_LEAD} ({CUSTOMER_SHORT})"],
            ["WS3 — PoC + Demo", "PoC running + Demo deck + Framework doc", "Notebook + slide", f"{VC_PO} ({CUSTOMER_SHORT})"],
            ["WS4 — Closure", "Biên bản nghiệm thu + Handover Pack", "Word/PDF signed", f"{VC_PO} ({CUSTOMER_SHORT})"],
        ],
    )

    add_h1(doc, "6. Timeline & Milestones")
    add_para(
        doc,
        "Đặc thù dự án: 3 workstream (WS1, WS2, WS3) chạy SONG SONG từ ngày Project Start "
        f"({PROJECT_START}). WS4 (Closure) chạy nối tiếp ở cuối. Daily sync cần coordinate "
        "cả 3 workstream để tránh dependency lock.",
        bold=True,
    )
    add_table(
        doc,
        ["Milestone", "Date", "Workstream", "Exit Criteria"],
        [
            ["M0 — Project Start", PROJECT_START, "Tất cả", "Charter signed, access provisioned"],
            ["M0.1 — Kickoff Meeting", KICKOFF, "Tất cả", "Kickoff held, team aligned on scope"],
            ["M1 — WS1 Complete", "12/06/2026", "WS1", "Báo cáo PMS & MarketS nghiệm thu"],
            ["M2 — WS3 Design Done", "08/06/2026", "WS3", "Architecture & Security Design signed"],
            ["M3 — WS3 Setup Done", "15/06/2026", "WS3", "Workspace, UC, CI/CD baseline ready"],
            ["M4 — WS3 PoC Implement Done", "29/06/2026", "WS3", "PoC chạy được trên framework"],
            ["M5 — WS2 Assessment Done", "26/06/2026", "WS2", "Báo cáo 8 hệ thống nguồn nghiệm thu"],
            ["M6 — Consolidate & PoC Demo", "03/07/2026", "WS2 + WS3", "Roadmap hợp nhất + Demo PoC done"],
            ["M7 — Closure Sign-off", f"{TARGET_CLOSE} ({PROJECT_END} buffer)", "WS4", "Biên bản nghiệm thu ký, project closed"],
        ],
    )

    add_h1(doc, "7. Budget & Resources")
    add_table(
        doc,
        ["Item", "Description", "Owner", "Estimate"],
        [
            [f"{VENDOR} effort", "Implementation services Phase 1", VENDOR_SHORT, "[Theo SOW]"],
            ["Databricks license", "DBU consumption (PoC scale)", CUSTOMER_SHORT, "[Theo Azure billing]"],
            ["Azure infra", "Compute + storage (PoC scale)", CUSTOMER_SHORT, "[Theo Azure billing]"],
            [f"{CUSTOMER} effort", "PO, Tech Lead, SME participation", CUSTOMER_SHORT, "[Internal allocation]"],
            ["Contingency", "10–15% reserve cho schedule slip", "Shared", "—"],
        ],
    )

    add_h1(doc, "8. Stakeholders")
    add_table(
        doc,
        ["Role", "Name", "Organization", "Responsibility"],
        [
            ["Project Owner", VC_PO, CUSTOMER_SHORT, "Sponsor, approval, escalation cuối phía VC"],
            ["Tech Lead", VC_TECH_LEAD, CUSTOMER_SHORT, "Technical decision, design review phía VC"],
            ["CEO / Project Owner", BC_CEO_PO, VENDOR_SHORT, "BC accountability, escalation phía BC"],
            ["Project Manager", BC_PM, VENDOR_SHORT, "Delivery management, day-to-day coordination"],
            ["Tech Lead / Architect", BC_TECH_LEAD, VENDOR_SHORT, "Solution design, technical leadership"],
            ["Finance BA", BC_FINANCE_BA, VENDOR_SHORT, "Business analysis Finance domain (PMS, ESM, Custodian, VSDC); workshop lead với VC Finance SME"],
            ["Document Preparer", PREPARER, VENDOR_SHORT, "Documentation, governance artifact"],
        ],
    )
    add_para(
        doc,
        "Stakeholder mở rộng (Security, Infra Ops, SME từng hệ thống nguồn) sẽ được nominate "
        "trong Kickoff Meeting và bổ sung vào Stakeholder Register (SharePoint /01_Governance).",
        italic=True,
    )

    add_h1(doc, "9. Success Criteria")
    add_bullets(
        doc,
        [
            "Tất cả Objectives (Section 3) đạt target",
            f"PoC demo nghiệm thu thành công bởi {VC_PO} trước {TARGET_CLOSE}",
            "Báo cáo Landscape Assessment 9 hệ thống được ký nghiệm thu",
            "Core Data Platform foundation hoạt động ổn định, có CI/CD",
            "Schedule variance ≤ ±5 business days so với baseline",
            "Roadmap tích hợp hợp nhất được chấp nhận làm input cho Phase 2",
        ],
    )

    add_h1(doc, "10. Risks & Assumptions")
    add_h2(doc, "10.1 Top Risks (initial register)")
    add_table(
        doc,
        ["#", "Risk", "Impact", "Likelihood", "Mitigation"],
        [
            ["R1", f"Chậm cấp Azure access / Databricks workspace cho {VENDOR} team", "High", "Medium", "Pre-flight checklist tuần 0, escalate VC IT Infra ngay nếu chậm"],
            ["R2", "9 system owner phía VC không sắp xếp được lịch phỏng vấn assessment", "High", "High", f"{VC_PO} pre-block calendar, escalate Steerco nếu trễ"],
            ["R3", "Tài liệu hệ thống nguồn (PMS, MIO, VSDC...) thiếu hoặc lỗi thời", "Medium", "High", "Phỏng vấn bổ sung, chấp nhận best-effort cho phase 1"],
            ["R4", "3 workstream song song gây quá tải coordination", "Medium", "Medium", "Daily sync chia theo WS lead, dùng WS owner model"],
            ["R5", "PoC scope creep từ VC business team", "Medium", "Medium", "Lock PoC scope trong Design phase, CR process bắt buộc"],
            ["R6", "Compliance review (SSC/SBV) phát sinh yêu cầu mới", "Medium", "Low", "Engage VC Security/Compliance sớm trong WS3 Design"],
            ["R7", "Timeline 7.5 tuần không buffer cho rework", "High", "Medium", "Weekly status RAG; sớm flag để negotiate scope hoặc deadline"],
        ],
    )
    add_h2(doc, "10.2 Assumptions")
    add_bullets(
        doc,
        [
            f"{CUSTOMER} đã có Azure tenant ({TENANT}) và Databricks subscription/license",
            f"{CUSTOMER} cung cấp guest access (Entra B2B) cho {VENDOR} team trước {KICKOFF}",
            "9 system owner phía VC available tối thiểu 4 giờ/người trong giai đoạn assessment",
            f"{VC_TECH_LEAD} dành ≥ 50% thời gian cho dự án trong giai đoạn WS3 Design + Setup",
            "PoC sử dụng synthetic data hoặc anonymized sample, không cần production data",
            f"Mọi tài liệu chính lưu tại SharePoint của {CUSTOMER}, {VENDOR} truy cập qua guest account",
        ],
    )

    add_h1(doc, "11. Governance")
    add_para(doc, "Cấu trúc ra quyết định và escalation:")
    add_table(
        doc,
        ["Tier", "Forum", "Cadence", "Decisions"],
        [
            ["T1", f"Daily sync 3 WS ({BC_PM} ↔ WS leads)", "Daily", "Ad-hoc, blocker, dependency"],
            ["T2", f"Weekly Status ({BC_PM} ↔ {VC_PO})", "Weekly (T6)", "Schedule, RAID review, decision queue"],
            ["T3", "Workstream Review / Milestone", "Per milestone", "Accept deliverable cho từng WS"],
            ["T4", f"Steering Committee ({BC_CEO_PO} + {VC_PO})", "Bi-weekly (project ngắn 7.5w)", "Scope, escalated risk, sign-off"],
        ],
    )
    add_para(
        doc,
        f"Escalation path: WS Lead → {BC_PM} (BC PM) → {BC_CEO_PO} / {VC_PO} (Steerco). "
        "SLA escalation: 2 business days nếu PM-level không giải quyết được. "
        "Sev1 (production access/security): escalate ngay lập tức.",
    )

    add_h1(doc, "12. Change Management")
    add_para(
        doc,
        f"Vì timeline ngắn (7.5 tuần) và 3 workstream song song, MỌI thay đổi scope/timeline "
        f"phải đi qua Change Request — kể cả change nhỏ. {BC_PM} review impact analysis trong "
        "3 business days. CR > 5% effort hoặc ảnh hưởng milestone phải có sign-off từ "
        f"{BC_CEO_PO} và {VC_PO}. CR template lưu tại SharePoint /01_Governance/Change_Requests/.",
    )

    add_signoff(
        doc,
        [f"{VC_PO}\n({CUSTOMER_SHORT} — Project Owner)",
         f"{BC_CEO_PO}\n({VENDOR_SHORT} — CEO / PO)",
         f"{BC_PM}\n({VENDOR_SHORT} — PM)"],
    )

    add_footer_note(doc, owner=f"{BC_CEO_PO} (PO)")
    out = OUT / "01_Project_Charter_Template.docx"
    doc.save(out)
    return out


# ============================================================
# DOC 2 — WORKING AGREEMENT
# ============================================================
def doc_working_agreement():
    doc = Document()
    style_doc(doc)
    add_title(
        doc,
        "WORKING AGREEMENT",
        f"{PROJECT_CODE} — {VENDOR} ({VENDOR_SHORT}) ↔ {CUSTOMER} ({CUSTOMER_SHORT})",
    )

    add_h1(doc, "0. Project Snapshot")
    add_table(
        doc,
        ["Field", "Value"],
        [
            ["Project Code", PROJECT_CODE],
            ["Project Scope", "Assessment 9 source systems + Core Data Platform Foundation + PoC"],
            ["Cloud", CLOUD],
            ["Project Start", f"{PROJECT_START} (work begins, 3 workstream song song)"],
            ["Kickoff Meeting", KICKOFF],
            ["Target Sign-off", TARGET_CLOSE],
            ["Working mode", WORK_MODE],
            [f"{CUSTOMER_SHORT} Project Owner", VC_PO],
            [f"{CUSTOMER_SHORT} Tech Lead", VC_TECH_LEAD],
            [f"{VENDOR_SHORT} CEO / Project Owner", BC_CEO_PO],
            [f"{VENDOR_SHORT} PM", BC_PM],
            [f"{VENDOR_SHORT} Tech Lead / Architect", BC_TECH_LEAD],
            [f"{VENDOR_SHORT} Finance BA", BC_FINANCE_BA],
        ],
    )

    add_h1(doc, "1. Mục đích")
    add_para(
        doc,
        f"Tài liệu này quy định cách 2 bên ({VENDOR}/{VENDOR_SHORT} với vai trò Vendor và "
        f"{CUSTOMER}/{CUSTOMER_SHORT} với vai trò Customer) phối hợp trong dự án {PROJECT_CODE}. "
        f"Mục tiêu: giảm hiểu lầm, tăng tốc ra quyết định, đảm bảo audit trail rõ ràng. Mọi thành "
        f"viên dự án đọc tài liệu này trong tuần đầu onboarding. Vì dự án có 3 workstream song "
        f"song và timeline 7.5 tuần, quy tắc phối hợp đặc biệt quan trọng.",
    )

    add_h1(doc, "2. Channel Matrix — Cái gì đi qua đâu")
    add_table(
        doc,
        ["Loại thông tin", "Kênh chính", "Kênh phụ", "Of-Record?"],
        [
            ["Hỏi nhanh, ad-hoc", "Teams Chat (#daily-sync)", "—", "Không"],
            ["Daily standup", "Teams Meeting (15')", "Note → Teams post", "Không"],
            ["Technical discussion", "Teams (#tech-databricks)", "DevOps comment", "Không"],
            ["Quyết định scope/design", "Email + Teams pin", "DevOps decision log", "Có"],
            ["Issue / Bug / Task", "Azure DevOps Board", "Teams notification", "Có"],
            ["Change Request", "Email + CR form (SharePoint)", "Steerco minutes", "Có"],
            ["Weekly Status Report", "Email + SharePoint /01_Governance", "Teams post", "Có"],
            ["Meeting minutes (formal)", "SharePoint /01_Governance", "Email summary", "Có"],
            ["Code / Notebook", "Git (Azure DevOps Repos)", "Databricks Repos", "Có"],
            ["Secret / Connection string", "Azure Key Vault", "Databricks Secret Scope", "Có"],
            ["Document (BRD, design, runbook)", f"SharePoint ({CUSTOMER} tenant)", "—", "Có"],
            ["Sample data", f"ADLS / Storage {CUSTOMER}", "—", "Có (no copy out)"],
        ],
    )
    add_para(doc, "Quy tắc vàng: thông tin còn cần tra cứu sau 3 tháng → KHÔNG để trong Teams chat.", bold=True)

    add_h1(doc, "3. Response Time SLA")
    add_table(
        doc,
        ["Loại tin nhắn", "Trong giờ làm việc", "Ngoài giờ"],
        [
            ["Teams chat (non-urgent)", "Trong 4h", "Sáng hôm sau"],
            ["Teams @mention", "Trong 2h", "Sáng hôm sau"],
            ["Email thông thường", "Trong 1 business day", "—"],
            ["Email có 'URGENT' ở tiêu đề", "Trong 2h", "Trong 4h"],
            ["DevOps ticket assigned", "Trong 1 business day", "—"],
            ["Production incident (Sev1)", "Trong 30 phút", "Trong 1h (hotline)"],
        ],
    )
    add_para(doc, "Giờ làm việc mặc định: 09:00–18:00 (GMT+7), Thứ 2 đến Thứ 6.")
    add_para(doc, "Out-of-office: thông báo qua Teams status + email auto-reply ≥ 1 ngày trước.")

    add_h1(doc, "4. Meeting Cadence")
    add_para(
        doc,
        "Vì có 3 workstream song song (WS1 Assessment PMS, WS2 Assessment Sources, "
        "WS3 Core Platform Design+Setup+PoC) và timeline ngắn, cadence chặt hơn dự án thường:",
        bold=True,
    )
    add_table(
        doc,
        ["Meeting", "Tần suất", "Thời lượng", "Bắt buộc", "Output"],
        [
            ["Daily Sync 3 WS", "Daily (T2–T6)", "15–20'", f"{BC_PM} + 3 WS Lead + {VC_TECH_LEAD} (optional)", "Teams post (blocker per WS)"],
            ["WS1/WS2 Workshop", "Per system", "60–90'", f"WS Lead + {CUSTOMER_SHORT} SME hệ thống đó", "Workshop notes + roadmap input"],
            ["Architecture Review (WS3)", "Per design milestone", "60–90'", f"{BC_TECH_LEAD} + {VC_TECH_LEAD}", "ADR + Decision log update"],
            ["Weekly Status", "Weekly (T6, 16:00)", "45'", f"{BC_PM} + {VC_PO} (+ {VC_TECH_LEAD})", "Status report → SharePoint /07_Reports"],
            ["WS Milestone Review", "Per milestone (M1–M7)", "60'", f"WS Lead + {VC_PO} + {BC_PM}", "Acceptance log per deliverable"],
            ["Steering Committee", "Bi-weekly", "45'", f"{BC_CEO_PO} + {VC_PO} + {BC_PM}", "Steerco minutes + decisions"],
            ["PoC Demo", "29/06 – 03/07/2026", "90'", f"Full team + {VC_PO} + {CUSTOMER_SHORT} stakeholders", "Demo recording + feedback log"],
            ["Closure Meeting", "06/07 – 10/07/2026", "120'", "Full team + Sponsors", "Biên bản nghiệm thu signed"],
        ],
    )
    add_para(
        doc,
        "Quy tắc meeting: gửi agenda ≥ 24h trước; meeting > 30' phải có agenda; "
        "không có agenda → cancel. Ghi minutes trong vòng 24h. Recording bắt buộc cho "
        "Milestone Review, Steerco, PoC Demo, Closure.",
    )

    add_h1(doc, "5. Decision-Making Process")
    add_h2(doc, "5.1 Phân tầng quyết định")
    add_table(
        doc,
        ["Loại quyết định", "Ai duyệt", "Format ghi nhận"],
        [
            ["Technical implementation (trong scope WS)", f"{BC_TECH_LEAD} ({VENDOR_SHORT}) + {VC_TECH_LEAD} ({CUSTOMER_SHORT})", "DevOps decision log"],
            ["WS-level scope (trong milestone)", f"{BC_PM} + {VC_PO}", "WS Review minutes"],
            ["Architecture / Design (WS3)", f"{BC_ARCHITECT} ({VENDOR_SHORT}) + {VC_TECH_LEAD} ({CUSTOMER_SHORT})", "Architecture Decision Record (ADR)"],
            ["Assessment scope (WS1/WS2)", f"{BC_PM} + {VC_PO}", "Workshop minutes"],
            ["Scope change ảnh hưởng < 1 ngày", f"{BC_PM} + {VC_PO}", "CR Light (email)"],
            ["Scope change ảnh hưởng milestone hoặc > 5% effort", f"{BC_CEO_PO} ({VENDOR_SHORT}) + {VC_PO} ({CUSTOMER_SHORT})", "CR đầy đủ → Steerco"],
            ["Security / Compliance", f"{CUSTOMER_SHORT} Security + {VC_PO}", "Email + sign-off"],
        ],
    )
    add_h2(doc, "5.2 Nguyên tắc")
    add_bullets(
        doc,
        [
            "Mặc định: Disagree & Commit — không đồng ý vẫn thực thi nếu quyết định đã chốt, escalate sau",
            "Quyết định mặc định public: ghi nhận tại nơi cả 2 bên truy cập được",
            "Reversible decision: làm thử nhanh, đo, sửa nếu sai. Irreversible: phải có ADR",
            "Im lặng = đồng ý sau 2 business days kể từ khi gửi proposal có deadline rõ ràng",
        ],
    )

    add_h1(doc, "6. Change Request Process")
    add_para(doc, "Mọi thay đổi về scope, timeline, hoặc budget tuân theo quy trình:")
    add_table(
        doc,
        ["Bước", "Hành động", "Owner", "SLA"],
        [
            ["1", "Submit CR form (SharePoint template)", "Người đề xuất", "—"],
            ["2", "Impact analysis (effort, schedule, cost, risk)", f"{BC_PM} + {BC_TECH_LEAD}", "2 business days"],
            ["3", "Review", f"{BC_PM} ↔ {VC_PO}", "1 business day"],
            ["4", "Approve / Reject / Defer", "Theo phân tầng Section 5.1", "3 business days"],
            ["5", "Update Charter, plan, backlog", BC_PM, "1 business day sau approve"],
        ],
    )
    add_para(
        doc,
        "Lưu ý: timeline ngắn (7.5 tuần) → SLA CR rút lại còn ~7 business days end-to-end "
        "thay vì 10–12 ngày như dự án thường.",
        italic=True,
    )

    add_h1(doc, "7. Document Standards")
    add_bullets(
        doc,
        [
            "Naming: YYYY-MM-DD_[Doc-Type]_[Topic]_v[X.Y]. Ví dụ: 2026-05-12_Design_DataModel_v1.0.docx",
            "Storage: SharePoint (xem Folder Structure document). KHÔNG lưu working file trên máy cá nhân quá 1 tuần",
            "Versioning: Major.Minor — Major khi nội dung đổi đáng kể, Minor khi sửa nhỏ",
            "Draft prefix: '[DRAFT]' trong tên file cho đến khi được review",
            "Sign-off: dùng SharePoint metadata 'Status' hoặc trang Sign-off cuối tài liệu",
            "Retention: tài liệu dự án giữ tối thiểu 5 năm sau project close (per Customer policy)",
        ],
    )

    add_h1(doc, "8. Tool Stack & Access")
    add_table(
        doc,
        ["Công cụ", "Mục đích", "Tenant", "Access cho Vendor"],
        [
            ["Microsoft Teams", "Communication, meeting", CUSTOMER, "Guest (Entra B2B)"],
            ["SharePoint Online", "Document repository", CUSTOMER, "Guest — Contributor"],
            ["Azure DevOps", "Backlog, Repo, Pipeline, Wiki", CUSTOMER, "Stakeholder + Basic"],
            ["Azure Key Vault", "Secrets", CUSTOMER, "Read via managed identity"],
            ["Databricks Workspace", "Build & run", CUSTOMER, "Workspace user, Unity Catalog scoped"],
            ["Email (Outlook/Exchange)", "Of-record comms", "Mỗi bên dùng tenant riêng", "—"],
        ],
    )
    add_para(
        doc,
        f"{VENDOR} team KHÔNG cài file dự án vào OneDrive cá nhân (tenant {VENDOR}) nếu file đó là of-record. "
        f"Internal working draft có thể giữ tạm trên OneDrive {VENDOR} nhưng phải sync sang SharePoint "
        f"{CUSTOMER} trước khi share.",
    )

    add_h1(doc, "9. Security & Data Handling")
    add_bullets(
        doc,
        [
            f"Sample / production data KHÔNG được tải về máy cá nhân của {VENDOR}",
            f"Mọi xử lý data thực hiện trong Databricks Workspace của {CUSTOMER}",
            "Không screenshot dữ liệu thật khi demo — luôn dùng masked / synthetic",
            "Secret / token KHÔNG bao giờ commit vào Git hoặc paste vào Teams/email",
            f"Laptop {VENDOR} phải bật full-disk encryption + screen lock ≤ 5 phút",
            f"Báo cáo incident bảo mật ngay lập tức qua hotline {CUSTOMER} (Sponsor + Security)",
            f"Tuân thủ chính sách bảo mật & compliance của {CUSTOMER} (financial services regulation)",
        ],
    )

    add_h1(doc, "10. Holiday, OOO & Coverage")
    add_bullets(
        doc,
        [
            "Mỗi bên chia sẻ lịch nghỉ lễ chính thức tại tuần Kickoff (đính kèm Appendix A)",
            "Cá nhân OOO ≥ 1 ngày: thông báo Teams status + email backup contact trước 24h",
            f"{VENDOR} OOO ≥ 3 ngày: phải có backup được nominate, handover trong Teams channel",
            f"Không deploy production trong tuần có ngày nghỉ lễ của {CUSTOMER} (trừ khi Sponsor approve)",
        ],
    )

    add_h1(doc, "11. Review & Update")
    add_para(
        doc,
        "Working Agreement được review tại Retro đầu tiên (sau Sprint 1) và mỗi quý. "
        "Bất kỳ thay đổi nào cần được PM 2 bên ký nhận. Version mới ghi đè bản cũ tại "
        "SharePoint /01_Governance/Working_Agreement/.",
    )

    add_signoff(
        doc,
        [f"{VC_PO}\n({CUSTOMER_SHORT} — Project Owner)",
         f"{BC_PM}\n({VENDOR_SHORT} — PM)"],
    )

    add_footer_note(doc, owner=f"{BC_CEO_PO} (PO)")
    out = OUT / "02_Working_Agreement.docx"
    doc.save(out)
    return out


# ============================================================
# DOC 3 — SHAREPOINT FOLDER STRUCTURE
# ============================================================
def doc_folder_structure():
    doc = Document()
    style_doc(doc)
    add_title(
        doc,
        "SHAREPOINT FOLDER STRUCTURE",
        "Databricks Implementation — Document Repository Design",
    )

    add_h1(doc, "1. Nguyên tắc thiết kế")
    add_bullets(
        doc,
        [
            f"Lưu trữ tại tenant của {CUSTOMER} → khi project close không cần migrate",
            "Cấu trúc theo phase + governance, không theo team / cá nhân",
            "Tối đa 3 cấp folder — sâu hơn dùng filter/metadata thay vì đào folder",
            "Mỗi top-level folder có _README.md mô tả mục đích",
            "File working draft prefix [DRAFT]; final bỏ prefix",
            "Lock folder khi phase kết thúc (read-only) để tránh sửa hồi cố",
        ],
    )

    add_h1(doc, "2. Top-Level Structure")
    add_para(
        doc,
        f"SharePoint Site name: '{PROJECT_CODE} — {CUSTOMER_SHORT} x {VENDOR_SHORT}' "
        f"(gắn với Teams cùng tên, host trên {TENANT}). Document Library mặc định: 'Documents'. "
        f"Cấu trúc bám theo 4 workstream của dự án (WS1 Assessment PMS, WS2 Assessment Sources, "
        f"WS3 Core Platform, WS4 Closure).",
    )
    add_table(
        doc,
        ["Folder", "Mục đích", "Owner", "Workstream / Phase"],
        [
            ["00_Read_First", "Onboarding pack: start-here guide, quick links, glossary, where-to-find-what", BC_PM, "Toàn dự án"],
            ["01_Governance", "Charter, Working Agreement, Comm Plan, Steerco minutes, RAID log, CR", BC_PM, "Toàn dự án"],
            ["02_WS1_Assessment_PMS_MarketS", "Khảo sát PMS, MarketS: interview note, doc, roadmap WS1", "WS1 Lead", "WS1 (18/05–12/06)"],
            ["03_WS2_Assessment_Sources", "Khảo sát 8 hệ thống nguồn + Consolidate roadmap", "WS2 Lead", "WS2 (18/05–03/07)"],
            ["04_WS3_Design_Setup_PoC", "Architecture, security design, setup guide, PoC artifact, demo deck", BC_TECH_LEAD, "WS3 (18/05–03/07)"],
            ["05_WS4_Closure", "Closure deck, biên bản nghiệm thu, handover pack, lessons learned", BC_PM, "WS4 (06/07–10/07)"],
            ["06_Shared_References", "Tài liệu tham khảo: Databricks docs, VC policy, BC standards, glossary", BC_PM, "Toàn dự án"],
            ["07_Reports", "Weekly status, steerco deck, milestone report", BC_PM, "Toàn dự án"],
            ["99_Archive", "Tài liệu deprecated, version cũ", BC_PM, "Toàn dự án"],
        ],
    )
    add_para(
        doc,
        "Lưu ý cấu trúc số thứ tự: 00 = Read First (đọc đầu tiên khi onboarding), 01 = Governance "
        "(quy trình & artifact chính), 02–05 = 4 Workstream theo timeline, 06 = tài liệu tham khảo, "
        "07 = báo cáo, 99 = archive (đặt cuối để luôn nằm cuối khi sort).",
        italic=True,
    )

    add_h1(doc, "3. Chi tiết từng folder")

    # 00 Read First
    add_h2(doc, "3.1 /00_Read_First")
    add_para(
        doc,
        "Onboarding pack — mọi thành viên mới phải đọc folder này TRƯỚC khi vào các folder khác. "
        "Mục tiêu: 30 phút để hiểu dự án, biết tìm gì ở đâu, biết ai phụ trách gì.",
    )
    add_table(
        doc,
        ["Subfolder / File", "Nội dung"],
        [
            ["00_Start_Here.md", "Welcome + must-read trong 30': dự án là gì, scope, ai phụ trách, deadline"],
            ["01_Project_One_Pager.pdf", "1 trang tóm tắt: 4 workstream, timeline, key milestone"],
            ["02_Team_Directory.xlsx", "Danh bạ team 2 bên: tên, vai trò, contact, hình ảnh"],
            ["03_Where_To_Find_What.md", "Cheatsheet: tìm Charter ở đâu, log issue ở đâu, hỏi ai về cái gì"],
            ["04_Glossary.md", "Thuật ngữ: PMS, VSDC, MIO, ESM, Custodian, Lakehouse, UC, ADR..."],
            ["05_Tools_Access_Guide.md", "Hướng dẫn access Teams, SharePoint, Azure DevOps, Databricks"],
            ["06_FAQ.md", "Câu hỏi thường gặp khi onboard"],
            ["_README.md", "Mô tả folder + lịch sử update"],
        ],
    )

    # 01 Governance
    add_h2(doc, "3.2 /01_Governance")
    add_table(
        doc,
        ["Subfolder / File", "Nội dung"],
        [
            ["_Templates/", "Template chuẩn: Charter, Status Report, ADR, CR, Workshop Note"],
            ["Charter/", "Project Charter (latest + history)"],
            ["Working_Agreement/", "Working Agreement (latest + history)"],
            ["Communication_Plan/", "Communication Plan (latest + history)"],
            ["Steerco/", "1 subfolder per meeting: YYYY-MM-DD_Steerco/ (deck + minutes)"],
            ["Change_Requests/", "CR-001_[short-name].docx + CR_Tracker.xlsx"],
            ["RAID_Log.xlsx", "Risks, Assumptions, Issues, Decisions — single source"],
            ["Stakeholder_Register.xlsx", "Danh sách stakeholder, contact, role (VC + BC)"],
            ["Kickoff_Meeting/", f"Material kickoff {KICKOFF} (deck, attendance, minutes)"],
            ["_README.md", "Mô tả folder và quy tắc"],
        ],
    )

    # 02 WS1
    add_h2(doc, "3.3 /02_WS1_Assessment_PMS_MarketS")
    add_para(doc, f"Workstream 1: Landscape Assessment hệ thống PMS & MarketS (18/05 – 12/06/2026).")
    add_table(
        doc,
        ["Subfolder / File", "Nội dung"],
        [
            ["00_Plan/", "WS1 plan, interview schedule, stakeholder list per system"],
            ["01_PMS/", "Interview note, document, data flow analysis cho PMS"],
            ["02_MarketS/", "Interview note, document, data flow analysis cho MarketS"],
            ["03_Findings/", "Findings tổng hợp, gap analysis"],
            ["04_Roadmap_WS1/", "Roadmap tích hợp WS1 (draft → final)"],
            ["05_Acceptance/", "Acceptance form WS1, sign-off evidence"],
        ],
    )

    # 03 WS2
    add_h2(doc, "3.4 /03_WS2_Assessment_Sources")
    add_para(
        doc,
        "Workstream 2: Landscape Assessment 8 hệ thống nguồn (18/05 – 26/06) "
        "+ Consolidate roadmap (29/06 – 03/07).",
    )
    add_table(
        doc,
        ["Subfolder / File", "Nội dung"],
        [
            ["00_Plan/", "WS2 plan, interview schedule, stakeholder list"],
            ["01_MIO/", "Assessment MIO"],
            ["02_Salesforce/", "Assessment Salesforce"],
            ["03_Distributor/", "Assessment Distributor system"],
            ["04_Custodian/", "Assessment Custodian system"],
            ["05_Excel/", "Assessment Excel-based reports / spreadsheets"],
            ["06_VSDC/", "Assessment Vietnam Securities Depository (VSDC)"],
            ["07_ESM/", "Assessment ESM"],
            ["08_Datahub/", "Assessment Datahub"],
            ["09_Consolidated_Findings/", "Findings hợp nhất WS1 + WS2"],
            ["10_Roadmap_Final/", "Roadmap tích hợp final cho toàn bộ source landscape"],
            ["11_Acceptance/", "Acceptance form WS2, sign-off evidence"],
        ],
    )

    # 04 WS3
    add_h2(doc, "3.5 /04_WS3_Design_Setup_PoC")
    add_para(
        doc,
        "Workstream 3: Design & Setup Core Data Platform + PoC (Design 18/05–08/06, "
        "Setup 01/06–15/06, PoC 08/06–29/06, Demo 29/06–03/07).",
    )
    add_table(
        doc,
        ["Subfolder / File", "Nội dung"],
        [
            ["01_Architecture/", "High-level + low-level architecture, diagram source (Lucid/Drawio)"],
            ["02_Security_Design/", f"IAM, network (VNet/Private Link), encryption, Unity Catalog policy on {CLOUD}"],
            ["03_Data_Model/", "Medallion design (Bronze/Silver/Gold sample), naming convention"],
            ["04_ADR/", "Architecture Decision Records — ADR-001, ADR-002..."],
            ["05_Setup_Guide/", "Workspace provisioning, IaC reference, runbook setup"],
            ["06_Standards/", "Coding standard, branching strategy, CI/CD baseline"],
            ["07_PoC/", "PoC scope, notebook reference (code trong Git), result"],
            ["08_Demo/", "Demo deck, demo recording, feedback log"],
            ["09_Acceptance/", "Design sign-off, Setup acceptance, PoC acceptance"],
        ],
    )
    add_para(
        doc,
        f"Lưu ý: code, notebook và IaC nằm trong Azure DevOps Repos của {CUSTOMER}. "
        "SharePoint chỉ chứa documentation, KHÔNG copy code sang đây.",
        italic=True,
    )

    # 05 WS4
    add_h2(doc, "3.6 /05_WS4_Closure")
    add_para(doc, "Workstream 4: Closure Meeting (06/07 – 10/07/2026, target 09/07).")
    add_table(
        doc,
        ["Subfolder / File", "Nội dung"],
        [
            ["01_Closure_Deck/", "Slide tổng kết dự án"],
            ["02_Acceptance_Master/", "Biên bản nghiệm thu master + sub-acceptance từ WS1/WS2/WS3"],
            ["03_Handover_Pack/", "Tài liệu bàn giao cuối: architecture, runbook, KT note, access list"],
            ["04_Lessons_Learned/", "Lessons learned từ retrospective"],
            ["05_Final_Reports/", "Final project report, financial summary"],
        ],
    )

    # 06 Shared
    add_h2(doc, "3.7 /06_Shared_References")
    add_table(
        doc,
        ["Subfolder / File", "Nội dung"],
        [
            ["Databricks_Docs/", "Link / PDF official Databricks docs liên quan"],
            ["VC_Policies/", f"Tài liệu policy {CUSTOMER} chia sẻ (security, naming, compliance)"],
            ["BC_Standards/", f"{VENDOR} internal standards áp dụng cho dự án"],
            ["Glossary.docx", "Thuật ngữ chung cả 2 bên (Fund Management + Data terms)"],
        ],
    )

    # 07 Reports
    add_h2(doc, "3.8 /07_Reports")
    add_table(
        doc,
        ["Subfolder / File", "Nội dung"],
        [
            ["Weekly_Status/", "YYYY-WW_Status.pdf (1 file/tuần)"],
            ["Steerco_Deck/", "YYYY-MM-DD_Steerco.pptx (bi-weekly)"],
            ["Milestone_Reports/", "Báo cáo per milestone M1–M7"],
            ["Effort_Tracking.xlsx", "Burn-down effort theo WS"],
        ],
    )

    # 99 Archive
    add_h2(doc, "3.9 /99_Archive")
    add_para(
        doc,
        "Chứa version cũ đã bị thay thế, draft bị bỏ, tài liệu phase đã đóng. "
        "Read-only. Không xoá để giữ audit trail.",
    )

    add_h1(doc, "4. Permission Matrix")
    add_table(
        doc,
        ["Role", "00_RF", "01_Gov", "02_WS1", "03_WS2", "04_WS3", "05_WS4", "06_Ref", "07_Rep", "99_Arc"],
        [
            [f"{VC_PO} ({CUSTOMER_SHORT} PO)", "R", "R/W", "R/W", "R/W", "R/W", "R/W", "R", "R/W", "R"],
            [f"{VC_TECH_LEAD} ({CUSTOMER_SHORT} TL)", "R", "R", "R/W", "R/W", "R/W", "R/W", "R/W", "R", "R"],
            [f"{CUSTOMER_SHORT} SME (per system)", "R", "R", "R/W (assigned)", "R/W (assigned)", "R", "R", "R", "R", "R"],
            [f"{CUSTOMER_SHORT} Security", "R", "R", "R", "R", "R/W (Sec)", "R", "R", "R", "R"],
            [f"{BC_CEO_PO} ({VENDOR_SHORT} PO)", "R/W", "R/W", "R/W", "R/W", "R/W", "R/W", "R/W", "R/W", "R/W"],
            [f"{BC_PM} ({VENDOR_SHORT} PM)", "R/W", "R/W", "R/W", "R/W", "R/W", "R/W", "R/W", "R/W", "R/W"],
            [f"{BC_TECH_LEAD} ({VENDOR_SHORT} TL/Arch)", "R", "R", "R/W", "R/W", "R/W", "R/W", "R/W", "R", "R"],
            [f"{BC_FINANCE_BA} ({VENDOR_SHORT} Finance BA)", "R", "R", "R/W", "R/W", "R", "R", "R/W", "R", "R"],
            [f"{VENDOR_SHORT} Dev / Eng", "R", "R", "R/W", "R/W", "R/W", "R", "R", "R", "R"],
        ],
        col_widths=[Cm(3.8)] + [Cm(1.4)] * 9,
    )
    add_para(
        doc,
        "00_RF (Read First) chỉ Read cho tất cả role bên VC và Dev — chỉ BC PM/PO/Lead có quyền "
        "edit. Mục tiêu: nội dung onboarding ổn định, không bị sửa lung tung. Update onboarding "
        "đi qua PR review của PM.",
        italic=True,
    )
    add_para(doc, "R = Read, R/W = Read/Write. Quản lý qua SharePoint Groups (không gán trực tiếp cá nhân).")

    add_h1(doc, "5. Metadata & Naming Convention")
    add_para(doc, "Bật các cột metadata sau cho Document Library:")
    add_bullets(
        doc,
        [
            "Document Type: Charter | Plan | Assessment | Design | ADR | Report | Acceptance | Other",
            "Status: Draft | In Review | Approved | Deprecated",
            "Workstream: WS1 | WS2 | WS3 | WS4 | Governance",
            "Source System: PMS | MarketS | MIO | Salesforce | Distributor | Custodian | Excel | VSDC | ESM | Datahub | N/A",
            "Owner: (person column)",
            "Reviewer(s): (person column, multi)",
            "Acceptance By: (person column — VC side)",
        ],
    )
    add_para(doc, "File naming:", bold=True)
    add_bullets(
        doc,
        [
            "Format: YYYY-MM-DD_[DocType]_[Topic]_v[X.Y].[ext]",
            "Ví dụ: 2026-05-12_Design_DataModel_v1.2.docx",
            "Không space — dùng dấu gạch dưới _ hoặc gạch nối -",
            "Không tiếng Việt có dấu (để tránh lỗi URL khi share)",
        ],
    )

    add_h1(doc, "6. Retention & Lifecycle")
    add_table(
        doc,
        ["Loại tài liệu", "Retention", "Khi nào archive"],
        [
            ["Charter, signed agreement", "≥ 5 năm sau close", "Sau close → Archive (read-only)"],
            ["Design, ADR", "≥ 5 năm sau close", "Sau close → Archive"],
            ["Working draft (DRAFT prefix)", "60 ngày không update", "Auto-flag, PM review"],
            ["Weekly status", "≥ 2 năm sau close", "Sau close → Archive"],
            ["Defect report, hypercare log", "≥ 3 năm sau close", "Sau hypercare → Archive"],
            ["Sample data, evidence", f"Theo policy của {CUSTOMER} (financial services)", "—"],
        ],
    )

    add_h1(doc, "7. Setup Checklist (trước Project Start 18/05/2026)")
    add_bullets(
        doc,
        [
            f"[ ] {CUSTOMER_SHORT} tạo SharePoint Site '{PROJECT_CODE} — {CUSTOMER_SHORT} x {VENDOR_SHORT}' liên kết với Teams",
            "[ ] Tạo 9 top-level folder theo Section 2 (00_Read_First → 99_Archive)",
            "[ ] Tạo nội dung onboarding cho /00_Read_First/: Start Here, One-Pager, Team Directory, Where-To-Find-What, Glossary, Tools Access Guide, FAQ",
            "[ ] Tạo subfolder per workstream (WS1: PMS, MarketS / WS2: 8 source systems / WS3: design+setup+poc / WS4: closure)",
            "[ ] Upload _README.md vào mỗi top-level folder",
            "[ ] Bật metadata cột theo Section 5 (gồm Workstream + Source System)",
            "[ ] Tạo SharePoint Groups theo Permission Matrix (Section 4)",
            f"[ ] Cấp guest access cho {VENDOR_SHORT} team trên {TENANT} (Entra B2B)",
            "[ ] Tạo template document (Charter, Status Report, ADR, CR, Workshop Note) trong /01_Governance/_Templates/",
            f"[ ] Upload Kickoff Meeting material vào /01_Governance/Kickoff_Meeting/ trước {KICKOFF}",
            f"[ ] Test upload + edit từ tài khoản {VENDOR_SHORT} (Tin Huynh, Dung Phan, Nguyen Le)",
            "[ ] Publish hướng dẫn truy cập + link /00_Read_First/ trong Teams channel #general (pinned)",
        ],
    )
    add_footer_note(doc, owner=f"{BC_CEO_PO} (PO)")
    out = OUT / "03_SharePoint_Folder_Structure.docx"
    doc.save(out)
    return out


# ============================================================
# DOC 4 — COMMUNICATION PLAN
# ============================================================
def doc_comm_plan():
    doc = Document()
    style_doc(doc)
    add_title(
        doc,
        "COMMUNICATION PLAN",
        f"{PROJECT_CODE} — {VENDOR} ({VENDOR_SHORT}) ↔ {CUSTOMER} ({CUSTOMER_SHORT})",
    )

    add_h1(doc, "1. Mục đích")
    add_para(
        doc,
        f"Communication Plan cho dự án {PROJECT_CODE} quy định AI cần biết CÁI GÌ, KHI NÀO, qua "
        f"KÊNH NÀO, và AI chịu trách nhiệm. Vì dự án có 3 workstream chạy song song từ {PROJECT_START} "
        f"đến {TARGET_CLOSE} (~7.5 tuần), comm phải đủ chặt để tránh dependency lock nhưng đủ "
        "thoáng để không tiêu thời gian thực thi.",
    )

    add_h1(doc, "2. Stakeholder Matrix")
    add_table(
        doc,
        ["Stakeholder", "Name", "Interest", "Influence", "Strategy"],
        [
            [f"{CUSTOMER_SHORT} Project Owner", VC_PO, "High", "High", "Manage Closely — daily contact, weekly status, bi-weekly Steerco"],
            [f"{CUSTOMER_SHORT} Tech Lead", VC_TECH_LEAD, "High", "High", "Manage Closely — WS3 daily, architecture review"],
            [f"{CUSTOMER_SHORT} SME (per system)", "Per system (9 system)", "High", "Medium", "Keep Engaged — assessment workshop WS1/WS2"],
            [f"{CUSTOMER_SHORT} Security / Compliance", "TBD (nominate at Kickoff)", "Medium", "High", "Manage Closely — checkpoint WS3 Design"],
            [f"{CUSTOMER_SHORT} IT Infra", "TBD (nominate at Kickoff)", "Medium", "Medium", "Keep Informed — provisioning, access"],
            [f"{VENDOR_SHORT} CEO / PO", BC_CEO_PO, "High", "High", "Manage Closely — Steerco, escalation"],
            [f"{VENDOR_SHORT} PM", BC_PM, "High", "High", "Owner of plan — drive all comm"],
            [f"{VENDOR_SHORT} Tech Lead / Architect", BC_TECH_LEAD, "High", "High", "Daily WS3 + architecture decisions"],
            [f"{VENDOR_SHORT} Finance BA", BC_FINANCE_BA, "High", "Medium", "Workshop WS1/WS2 cho Finance system (PMS, ESM, Custodian, VSDC); requirement analysis"],
            [f"{VENDOR_SHORT} WS1 Lead", "TBD", "High", "Medium", "Daily WS1, weekly status"],
            [f"{VENDOR_SHORT} WS2 Lead", "TBD", "High", "Medium", "Daily WS2, weekly status"],
        ],
    )
    add_para(
        doc,
        f"Note: tên cụ thể của WS1/WS2 Lead, Security, Infra contact sẽ được fill in tại "
        f"Kickoff Meeting ({KICKOFF}) và cập nhật vào Stakeholder Register tại "
        "/01_Governance/Stakeholder_Register.xlsx.",
        italic=True,
    )

    add_h1(doc, "3. Communication Matrix")
    add_table(
        doc,
        ["Loại comm", "Audience", "Kênh", "Tần suất", "Owner"],
        [
            ["Daily Sync 3 WS", f"{BC_PM} + 3 WS Lead + {VC_TECH_LEAD} (opt)", "Teams Meeting", "Daily 09:00 (15–20')", BC_PM],
            ["Daily summary", "Core team", "Teams post #daily-sync", "Daily EOD", "WS Lead per WS"],
            ["WS1 Assessment Workshop", f"WS1 Lead + {CUSTOMER_SHORT} SME PMS/MarketS", "Teams + onsite", "On-demand per system", "WS1 Lead"],
            ["WS2 Assessment Workshop", f"WS2 Lead + {CUSTOMER_SHORT} SME source system", "Teams + onsite", "On-demand per system", "WS2 Lead"],
            ["Architecture Review (WS3)", f"{BC_TECH_LEAD} + {VC_TECH_LEAD}", "Teams + Lucid/Drawio", "Per design milestone", BC_TECH_LEAD],
            ["Weekly Status Meeting", f"{BC_PM} + {VC_PO} (+ {VC_TECH_LEAD})", "Teams Meeting (recorded)", "Weekly T6 16:00 (45')", BC_PM],
            ["Weekly Status Report", "DL-Project-Extended", "Email + SharePoint /07_Reports", "Weekly T6 EOD", BC_PM],
            ["Steering Committee", f"{BC_CEO_PO} + {VC_PO} + {BC_PM}", "Teams Meeting (recorded)", "Bi-weekly (45')", BC_PM],
            ["WS Milestone Review", f"WS Lead + {VC_PO} + {BC_PM}", "Teams Meeting (recorded)", "Per milestone", "WS Lead"],
            ["Change Request", f"{BC_PM} ↔ {VC_PO} (+ {BC_CEO_PO} nếu >5%)", "Email + SharePoint CR form", "On-demand", "CR initiator"],
            ["Incident / Escalation", f"{BC_PM} + {VC_PO} (+ Sponsor)", "Phone/Teams call + email", "Real-time", "Person phát hiện"],
            ["PoC Demo", f"Full team + {VC_PO} + VC stakeholders", "Teams Meeting (recorded)", "29/06 – 03/07/2026", BC_TECH_LEAD],
            ["Closure Meeting", "Full team + Sponsors", "Teams Meeting + onsite", "06/07 – 10/07/2026", BC_PM],
            ["Retrospective", f"{VENDOR_SHORT} team (VC optional)", "Teams Meeting", "Per milestone + final", BC_PM],
        ],
    )

    add_h1(doc, "4. Cadence Calendar (week typical)")
    add_table(
        doc,
        ["Day", "Time (GMT+7)", "Event", "Channel"],
        [
            ["Mon", "09:00", "Daily Sync 3 WS", "Teams call"],
            ["Mon–Fri", "09:00", "Daily Sync 3 WS", "Teams call"],
            ["Mon–Fri", "EOD", "Daily Summary post per WS", "Teams #daily-sync"],
            ["Tue/Thu", "On-demand", "WS1/WS2 Assessment Workshop với SME", "Teams + onsite"],
            ["Wed", "On-demand", "Architecture Review (WS3)", "Teams + Lucid"],
            ["Fri", "16:00", "Weekly Status Meeting", "Teams call (recorded)"],
            ["Fri", "EOD", "Weekly Status Report sent", "Email + SharePoint /07_Reports"],
            ["Bi-weekly (T4)", "14:00", "Steering Committee", "Teams call (recorded)"],
            ["Per milestone", "—", "WS Milestone Review", "Teams call (recorded)"],
        ],
    )
    add_para(
        doc,
        f"Working hours: 09:00–18:00 GMT+7 (T2–T6). Working mode: {WORK_MODE}. "
        f"Onsite days tại {CUSTOMER_SHORT} office sẽ được thống nhất tại Kickoff Meeting.",
        italic=True,
    )

    add_h1(doc, "5. Status Report Template")
    add_para(doc, "Mỗi Weekly Status Report (max 2 trang) bao gồm:")
    add_bullets(
        doc,
        [
            "Overall RAG (Schedule / Scope / Risk) per workstream — màu Red / Amber / Green",
            "Workstream progress: WS1 / WS2 / WS3 / WS4 — % complete + milestone status",
            "Highlights tuần (top 3–5 thành tựu)",
            "Lowlights / Issues (top 3 vấn đề + owner + action)",
            "Schedule view: milestone tới (M1–M7) + ngày dự kiến",
            "Burn-down effort per WS",
            "Top 5 risks + mitigation status",
            f"Decisions needed (từ {CUSTOMER_SHORT} side)",
            "Look-ahead: ưu tiên tuần tới per WS",
        ],
    )

    add_h1(doc, "6. Escalation Path & SLA")
    add_table(
        doc,
        ["Severity", "Định nghĩa", "Escalate đến", "SLA phản hồi"],
        [
            ["Sev1 — Critical", "Access blocker, security incident, milestone tại risk", f"{BC_PM} + {VC_PO} + {BC_CEO_PO}", "30' (giờ làm việc) / 1h (ngoài giờ)"],
            ["Sev2 — High", "Workstream blocker, no workaround", f"{BC_PM} + {VC_TECH_LEAD}", "2h"],
            ["Sev3 — Medium", "Task blocker, có workaround", f"{BC_PM} + {VC_PO}", "1 business day"],
            ["Sev4 — Low", "Cosmetic, request enhancement", f"DevOps ticket → {BC_PM} review", "3 business days"],
        ],
    )
    add_h2(doc, "6.1 Escalation Levels")
    add_bullets(
        doc,
        [
            f"L1: Team member → WS Lead / {BC_TECH_LEAD}",
            f"L2: WS Lead / {BC_TECH_LEAD} → {BC_PM}",
            f"L3: {BC_PM} → {VC_PO} (BC side) hoặc {BC_CEO_PO} (escalation BC)",
            f"L4: {BC_CEO_PO} + {VC_PO} → Steerco / Executive (Sev1 escalate ngay)",
        ],
    )

    add_h1(doc, "7. Tools & Templates")
    add_table(
        doc,
        ["Mục đích", "Tool / Template", "Vị trí"],
        [
            ["Weekly status template", ".docx", "SharePoint /01_Governance/_Templates/"],
            ["Steerco deck template", ".pptx", "SharePoint /01_Governance/_Templates/"],
            ["Workshop note template (WS1/WS2)", ".docx", "SharePoint /01_Governance/_Templates/"],
            ["Meeting minutes template", ".docx", "SharePoint /01_Governance/_Templates/"],
            ["CR form", ".docx", "SharePoint /01_Governance/_Templates/"],
            ["ADR template", ".md / .docx", "SharePoint /01_Governance/_Templates/"],
            ["Decision log", ".xlsx", "SharePoint /01_Governance/RAID_Log.xlsx"],
            ["RAID log", ".xlsx", "SharePoint /01_Governance/RAID_Log.xlsx"],
            ["Project Teams channel", "Teams group", f"{TENANT}"],
        ],
    )

    add_h1(doc, "8. Distribution Lists / Teams Channels")
    add_table(
        doc,
        ["Group / Channel", "Members", "Khi nào dùng"],
        [
            ["Teams #general", "Toàn bộ project team", "Announcement, pinned doc"],
            ["Teams #daily-sync", "Core team", "Daily standup + EOD summary"],
            ["Teams #ws1-assessment-pms", f"WS1 Lead + relevant SME", "WS1 discussion"],
            ["Teams #ws2-assessment-sources", f"WS2 Lead + relevant SME", "WS2 discussion"],
            ["Teams #ws3-core-platform", f"{BC_TECH_LEAD} + {VC_TECH_LEAD} + devs", "WS3 technical discussion"],
            ["Teams #governance", f"{BC_PM} + {VC_PO} + sponsors", "Steerco material, formal announcement"],
            ["DL-VC-BC-Core", f"{BC_PM}, {BC_TECH_LEAD}, {VC_PO}, {VC_TECH_LEAD}", "Day-to-day email"],
            ["DL-VC-BC-Steerco", f"{BC_CEO_PO}, {VC_PO}, {BC_PM}", "Steerco invite, escalation email"],
            ["DL-VC-BC-Extended", "Core + SME + WS Leads", "Weekly status email distribution"],
        ],
    )

    add_h1(doc, "9. Anti-Patterns (cần tránh)")
    add_bullets(
        doc,
        [
            "Gửi cùng nội dung qua nhiều kênh (email + Teams + DM) → noise + không rõ kênh of-record",
            "Quyết định scope/design chỉ trong DM hoặc voice call không note → không truy được",
            "BCC sponsor mỗi email → mất niềm tin, sponsor bị noise",
            "Status report quá dài (> 3 trang) → không ai đọc → đổi thành dashboard",
            "Họp không có agenda + không có minutes",
            "Sử dụng emoji/icon mơ hồ thay cho RAG status",
            "Báo cáo 'Green' nhưng phía sau có Sev2 chưa giải quyết → mất uy tín",
        ],
    )

    add_h1(doc, "10. Review")
    add_para(
        doc,
        f"Communication Plan được review sau tuần 2 ({PROJECT_START} + 14 ngày) và tại mỗi "
        "milestone review. Vì timeline ngắn, điều chỉnh nhanh nếu cadence không phù hợp. "
        "Phiên bản mới ghi đè tại SharePoint /01_Governance/Communication_Plan/.",
    )

    add_signoff(
        doc,
        [f"{VC_PO}\n({CUSTOMER_SHORT} — Project Owner)",
         f"{BC_PM}\n({VENDOR_SHORT} — PM)"],
    )

    add_footer_note(doc, owner=f"{BC_CEO_PO} (PO)")
    out = OUT / "04_Communication_Plan.docx"
    doc.save(out)
    return out


# ============================================================
if __name__ == "__main__":
    paths = [
        doc_charter(),
        doc_working_agreement(),
        doc_folder_structure(),
        doc_comm_plan(),
    ]
    for p in paths:
        size = p.stat().st_size
        print(f"OK  {p.name}  ({size:,} bytes)")
