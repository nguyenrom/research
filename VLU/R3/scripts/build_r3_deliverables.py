#!/usr/bin/env python3
"""
Build R3 deliverables for VLU post-grad strategy:
- HTML final report (single file, inline SVG, no external deps)
- PPTX board deck
- XLSX synthesis workbook

The script intentionally keeps all final numbers in one place so the three
deliverables reconcile with each other.
"""

from __future__ import annotations

import html
import math
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
from openpyxl import Workbook, load_workbook
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_AUTO_SIZE, PP_ALIGN
from pptx.util import Inches, Pt


ROOT = Path(__file__).resolve().parents[3]
R3 = ROOT / "VLU" / "R3"
RESEARCH_DIR = R3 / "research"
ASSET_DIR = R3 / "assets"

HTML_PATH = R3 / "VLU-Post-Grad-Research-Final-Report-2026.html"
PPTX_PATH = R3 / "VLU-Post-Grad-Board-Pitch-2026.pptx"
XLSX_PATH = R3 / "VLU-Post-Grad-Data-Synthesis-2026.xlsx"

PRIMARY = "1a3a5c"
PRIMARY_LIGHT = "2a5a8c"
ACCENT = "e63946"
GOLD = "d4a418"
SOFT_BG = "f6f3ec"
SUCCESS = "2a7a3e"
WARNING = "d97706"
BORDER = "e0dcd0"
TEXT = "1a1a1a"
MUTED = "666666"


@dataclass
class Program:
    market: str
    program: str
    tuition_usd: float
    duration_months: int
    format: str
    modality: str
    cohort_size: str
    gmat_median: str
    accept_rate: str
    value_tags: str
    proof: str
    source_url: str
    notes: str = ""

    @property
    def tuition_per_month(self) -> float:
        return round(self.tuition_usd / self.duration_months, 0)


PROGRAMS: list[Program] = [
    Program("China", "CKGSB Global MBA", 62000, 14, "Full-time modular", "Beijing on-campus", "60-80 est.", "670 old disclosure", "Not disclosed", "Network; status; China depth", "24,500 alumni; CEO-heavy network", "https://english.ckgsb.edu.cn/global-mba/"),
    Program("China", "CEIBS MBA", 68000, 16, "Full-time", "Shanghai on-campus", "115", "680", "15-25% est.", "FT ranking; career transition; China-Europe bridge", "FT Asia top tier; ICP consulting project", "https://www.ceibs.edu/mba"),
    Program("China", "Tsinghua Global MBA", 28000, 24, "Full-time", "Beijing on-campus", "80-100 est.", "Not disclosed", "12-20% est.", "MIT co-brand; ROI; policy access", "Tsinghua + MIT Sloan dual-degree option", "https://gmba.sem.tsinghua.edu.cn/Admissions/International/Expenses_Scholarship.htm"),
    Program("China", "SJTU Antai IMBA", 29000, 24, "Full-time", "Shanghai on-campus", "Not disclosed", "Not disclosed", "Mid selective", "Triple accreditation; value price; tech adjacency", "First China-based triple-crown business school", "https://www.acem.sjtu.edu.cn/en/"),
    Program("China", "PHBS Cross-border Master of Finance", 32000, 24, "2-country pathway", "UK + Shenzhen", "Not disclosed", "N/A", "Selective", "UK-China finance; PKU brand; Shenzhen tech", "Year 1 near Oxford + Year 2 Shenzhen", "https://english.phbs.pku.edu.cn/"),
    Program("China", "Hult Global MBA / Shanghai rotation", 50000, 12, "Global rotation", "Multi-campus", "Not disclosed", "N/A", "Open-mid", "International mobility; recruiter funnel caution", "Shanghai shifted toward rotation-campus role", "https://www.hult.edu/mba/"),
    Program("Australia", "Melbourne Business School MBA", 77800, 24, "Full-time", "Melbourne on-campus", "100", "695", "30-40% est.", "Asia-Pacific brand; consulting capstone; career", "EY-embedded Industry Studies in Asia", "https://mbs.edu/en/degree-programs/full-time-mba"),
    Program("Australia", "Melbourne Business School EMBA", 80800, 18, "Weekend modules", "Residential modules", "Not disclosed", "N/A", "Selective", "Executive cohort; brand transfer; no job exit", "17 four-day modules + overseas module", "https://mbs.edu/-/media/PDF/Brochures/Degree-Programs/Executive-MBA-Brochure---Melbourne-Business-School.pdf"),
    Program("Australia", "AGSM Full-Time MBA", 56000, 12, "Full-time", "Sydney on-campus", "50-60", "670", "25-35% est.", "Top-50; salary uplift; Yale GNAM", "FT 2026 top-50; small cohort", "https://www.unsw.edu.au/business/agsm/learn/agsm-programs/mba-full-time"),
    Program("Australia", "Bond MBA", 54400, 12, "Fast-track", "Gold Coast on-campus", "Small", "No GMAT", "Mid selective", "Speed; private boutique; entrepreneurship", "3-semester calendar enables 12-month MBA", "https://bond.edu.au/program/master-business-administration"),
    Program("Australia", "Macquarie Global MBA", 58000, 18, "Flexible", "Hybrid / Sydney", "39 per intake est.", "N/A", "Mid selective", "Applied MBA; specialist masters halo", "Master of Marketing/Applied Finance stronger than MBA", "https://www.mq.edu.au/study/find-a-course/courses/master-of-business-administration"),
    Program("Australia", "Torrens MBA", 39000, 24, "On Demand", "Online / blended", "Large", "No GMAT", "Open-mid", "Flexibility; employability; low friction", "10 intakes/year; 95% employment claim", "https://www.torrens.edu.au/courses/business/master-of-business-administration"),
    Program("India", "ISB PGP", 54000, 12, "Full-time residential", "Hyderabad / Mohali", "808", "720", "15-25% est.", "Salary uplift; Wharton-Kellogg-LBS DNA; one-year", "156% CTC uplift; ELP live-client capstone", "https://www.isb.edu/en/study-isb/post-graduate-programmes/pgp-management.html"),
    Program("India", "IIM Bangalore EPGP", 40600, 12, "Full-time residential", "Bangalore", "75", "704", "Highly selective", "IIM brand; small cohort; senior transition", "75-person cohort; mandatory international immersion", "https://www.iimb.ac.in/programmes/epgp"),
    Program("India", "IIM Ahmedabad PGPX", 42200, 12, "Full-time residential", "Ahmedabad", "140-160", "700 est.", "Highly selective", "IIMA prestige; C-suite transition; consulting", "Average package near ISB/IIMB range", "https://www.iima.ac.in/academics/MBA-PGPX"),
    Program("India", "Ashoka Young India Fellowship", 24000, 12, "Full-time fellowship", "Residential", "250", "N/A", "Selective", "Liberal leadership; non-MBA path; social impact", "Ivy-style interdisciplinary leadership positioning", "https://www.ashoka.edu.in/yif/"),
    Program("India", "Great Lakes PGPM", 28000, 12, "Full-time residential", "Chennai", "300 est.", "N/A", "Mid selective", "Fast-track; founding faculty brand; analytics", "Kellogg lineage via Bala Balachandran", "https://www.greatlakes.edu.in/chennai/pgpm/"),
    Program("India", "SPJIMR PGPFMB", 28000, 18, "6-day/month modular", "Mumbai modular", "30-60 est.", "No GMAT", "Application + family fit", "Family business; no-placement design; heir network", "4,000+ alumni; 37 batches; 6 days/month", "https://www.spjimr.org/course/post-graduate-programme-in-family-managed-business-pgpfmb/"),
    Program("Singapore", "INSEAD MBA", 118650, 10, "Full-time", "Singapore/France rotation", "900/year", "710", "30-35% est.", "Global mobility; diversity; consulting", "110 nationalities; 65% career triple-change elements", "https://www.insead.edu/master-programmes/master-business-administration"),
    Program("Singapore", "NUS MBA", 73900, 17, "Full-time", "Singapore", "120", "670", "12-20% est.", "NUS halo; Asia career; finance/tech", "95% offer acceptance within 3 months", "https://mba.nus.edu.sg/"),
    Program("Singapore", "SMU MBA", 61300, 15, "Full-time/part-time", "Singapore CBD", "70-90 est.", "N/A", "Mid selective", "CBD access; seminar style; Asia career", "FT #43 global in R2 dataset", "https://masters.smu.edu.sg/programme/master-of-business-administration"),
    Program("Singapore", "Nanyang MBA", 66200, 12, "Full-time", "Singapore", "100", "600", "Mid selective", "NTU brand; double degrees; tech/sustainability", "Waseda/St Gallen/ESSEC double-degree menu", "https://www.ntu.edu.sg/business/admissions/graduate-studies/nanyang-mba"),
    Program("Singapore", "SMU MSc Wealth Management", 54900, 12, "Specialized master", "Singapore", "Small", "N/A", "Selective", "Wealth; private banking; specialization", "FT #1 Asia / #3 global post-experience finance", "https://business.smu.edu.sg/master-wealth-management"),
    Program("Singapore", "ESSEC Global MBA Asia-Pacific", 54000, 12, "Full-time", "Singapore", "Small", "N/A", "Mid selective", "European brand; APAC rotation; sustainability", "French Grande Ecole brand in Singapore", "https://www.essec.edu/en/program/global-mba/"),
    Program("Malaysia", "Sunway University MBA", 10000, 12, "Online / flexible", "Online", "Not disclosed", "N/A", "Open-mid", "Flexible; AACSB school; CMI option", "RM47,000 total; CMI dual accreditation option", "https://studyonline.sunwayuniversity.edu.my/fees"),
    Program("Malaysia", "Taylor's University MBA", 11700, 12, "Full-time/part-time", "Malaysia on-campus", "Not disclosed", "N/A", "Open-mid", "Working adult flexibility; private brand", "MYR54,720 local; 1-year full-time", "https://university.taylors.edu.my/en/study/explore-all-programmes/business/master-coursework/master-of-business-administration.html"),
    Program("Malaysia", "Heriot-Watt Malaysia MBA", 15900, 24, "Part-time", "Malaysia campus + online", "Not disclosed", "N/A", "Open-mid", "UK credential; modular; working professionals", "Part-time MBA over 2 years at Malaysia campus", "https://www.hw.ac.uk/malaysia/study/postgraduate/master-business-administration-mba"),
    Program("Indonesia", "BINUS MM Executive", 13500, 18, "Hybrid executive", "Jakarta / blended", "Not disclosed", "N/A", "Open-mid", "Innovation; practitioner faculty; scale private", "Rp220,000,000 tuition 2025/2026", "https://bbs.binus.ac.id/tuition-fee/"),
    Program("Indonesia", "Prasetiya Mulya Executive / Family Business", 12000, 12, "Executive education", "Jakarta / blended", "Not disclosed", "N/A", "Selective by program", "Family business; entrepreneurship; private elite", "Graduate management + family-business heritage", "https://www.prasetiyamulya.ac.id/en/graduate-programs/mm-business-management/"),
    Program("Indonesia", "Sampoerna MBA + Thunderbird MLM", 16000, 18, "Dual-degree", "Jakarta", "Not disclosed", "IELTS 6.5", "Mid selective", "US partner; global leadership; dual credential", "MBA from Sampoerna + MLM from Thunderbird/ASU", "https://www.sampoernauniversity.ac.id/master-degree"),
    Program("Vietnam", "RMIT Vietnam MBA", 25645, 18, "Flexible trimester", "HCMC / Hanoi", "Not disclosed", "No GMAT public", "Mid selective", "Australian credential; premium VN MBA; English", "2026 fee USD25,645 for 12-course pathway", "https://www.rmit.edu.vn/study-at-rmit/tuition-fees"),
    Program("Vietnam", "UEH MBA / EMBA", 5000, 18, "Evening/weekend", "HCMC", "Large", "N/A", "Moderate", "Public prestige; economics alumni; affordability", "Oldest economics/business public brand in South", "https://sdh.ueh.edu.vn/"),
    Program("Vietnam", "Fulbright MPP Leadership & Management", 17200, 18, "Cohort-based", "HCMC", "Small", "N/A", "Selective", "Policy leadership; Harvard Kennedy DNA; scholarships", "VND450M full fee; scholarships by sector", "https://fsppm.fulbright.edu.vn/download/TB-Tuyen-Sinh_MPP2026_ENG.pdf"),
    Program("Vietnam", "FSB MBA", 9000, 18, "Executive / blended", "Hanoi / HCMC / online", "Not disclosed", "N/A", "Open-mid", "Corporate training; FPT tech brand; flexibility", "FPT School of Business executive network", "https://fsb.edu.vn/"),
    Program("Vietnam", "Hawaii-Pacific / US MBA VN partnerships", 12000, 18, "Partnership MBA", "Vietnam + foreign partner", "Not disclosed", "N/A", "Open-mid", "Foreign-degree signal; legacy partnership model", "UH Shidler VEMBA active with VLU; HPU status fragmented", "https://shidler.hawaii.edu/vemba"),
    Program("Vietnam", "NEU / FTU MBA", 4500, 18, "Evening/weekend", "Hanoi", "Large", "N/A", "Moderate", "Northern public prestige; affordability; alumni", "National Economics / Foreign Trade alumni base", "https://sdh.neu.edu.vn/"),
]


SOURCES = [
    ("RMIT Vietnam tuition fees 2026", "https://www.rmit.edu.vn/study-at-rmit/tuition-fees"),
    ("Fulbright FSPPM tuition/admissions", "https://fsppm.fulbright.edu.vn/download/TB-Tuyen-Sinh_MPP2026_ENG.pdf"),
    ("Sunway Online MBA fees", "https://studyonline.sunwayuniversity.edu.my/fees"),
    ("Taylor's MBA fees and duration", "https://university.taylors.edu.my/en/study/explore-all-programmes/business/master-coursework/master-of-business-administration.html"),
    ("BINUS Business School tuition", "https://bbs.binus.ac.id/tuition-fee/"),
    ("Sampoerna MBA + Thunderbird program", "https://www.sampoernauniversity.ac.id/master-degree"),
    ("MOET Circular 23/2021 master training", "https://congbao.chinhphu.vn/van-ban/thong-tu-so-23-2021-tt-bgddt-34353/36884.htm"),
    ("MOET Circular 07/2025 foreign joint training", "https://congbao.chinhphu.vn/thuoc-tinh-van-ban-so-07-2025-tt-bgddt-44748"),
    ("Vietnam Decree 219/2025 foreign workers", "https://en.baochinhphu.vn/fresh-regulations-on-work-permit-issuance-to-foreign-workers-111250808104813884.htm"),
    ("AACSB initial accreditation process", "https://www.aacsb.edu/educators/accreditation/business-accreditation/initial-accreditation"),
    ("AACSB accreditation fees", "https://www.aacsb.edu/educators/accreditation/business-accreditation/fees"),
]


DECISIONS = [
    ("D1", "Family Academy vs Healthcare MBA first", "Family Academy first", "Open", "Pre-sell 10 deposits; family-business wedge has clearer whitespace."),
    ("D2", "Pricing model", "$15k / $20k / $35k", "Mary lean updated", "R2/R3 comparables show original $12k/$18k/$30k under-prices premium signal."),
    ("D3", "Sub-brand vs standalone", "VLU sub-brand", "Open", "Use VLU trust while building distinct category language."),
    ("D4", "International partner", "One named anchor before formal joint degree", "Open", "Faster than dual-degree compliance; reduces execution risk."),
    ("D5", "Program Director", "External hire with family-business credibility", "Open", "Internal faculty alone cannot carry private-founder trust."),
    ("D6", "Retreat venue", "Da Lat premium retreat", "Open", "Confidentiality + distance from operating business matter."),
    ("D7", "Annual Outlook authorship", "Co-author EY/PwC/VCCI-style partner", "Open", "Borrow trust while VLU builds data asset."),
    ("D8", "Founder Advisory Board", "Recruit 5-7 founders", "Open", "Must include gen-1 buyer voice, not just academics."),
    ("D9", "Family Showcase venue", "5-star hotel", "Open", "Board/founder signaling matters for premium category."),
    ("D10", "Healthcare MBA format", "12-month intense + 3-month capstone", "New R3 lean", "R2 India fast-track pattern beats original 18-month design for opportunity cost."),
    ("D11", "Accreditation path", "MOET first, AACSB readiness Y1-Y2, eligibility Y3", "New R3 lean", "Avoid joint-degree before QA system is mature."),
    ("D12", "Healthcare MBA pricing", "$12k / $18k / $30k", "New R3 lean", "Self-pay base must stay accessible; $30k belongs to sponsor/employer package."),
]


FINANCIALS = {
    "Family Academy": {
        "students": [22, 25, 50],
        "revenue": [330000, 575000, 1500000],
        "gross_margin": [0.42, 0.48, 0.55],
        "net": [25000, 185000, 620000],
    },
    "Healthcare MBA": {
        "students": [30, 60, 120],
        "revenue": [450000, 960000, 2040000],
        "gross_margin": [0.38, 0.44, 0.50],
        "net": [65000, 260000, 720000],
    },
    "Membership Halo": {
        "students": [250, 650, 1200],
        "revenue": [100000, 325000, 720000],
        "gross_margin": [0.55, 0.62, 0.68],
        "net": [10000, 120000, 360000],
    },
}


SVG_STRATEGIC_GROUP = """
<svg viewBox="0 0 760 460" role="img" aria-label="Strategic group map">
  <rect x="50" y="30" width="650" height="360" fill="#fff" stroke="#e0dcd0"/>
  <line x1="80" y1="350" x2="670" y2="350" stroke="#1a3a5c" stroke-width="2"/>
  <line x1="80" y1="350" x2="80" y2="60" stroke="#1a3a5c" stroke-width="2"/>
  <text x="330" y="430" font-size="14" fill="#1a3a5c" font-weight="700">Giá / premium signal</text>
  <text x="10" y="235" font-size="14" fill="#1a3a5c" font-weight="700" transform="rotate(-90 20,235)">Selectivity / specialization depth</text>
  <g font-size="12" fill="#666">
    <text x="90" y="372">Low</text><text x="610" y="372">High</text>
    <text x="48" y="346">Low</text><text x="45" y="70">High</text>
  </g>
  <g>
    <ellipse cx="185" cy="285" rx="85" ry="38" fill="#f6f3ec" stroke="#d4a418"/>
    <text x="120" y="280" font-size="13" fill="#1a3a5c" font-weight="700">UEH / NEU / FTU</text>
    <text x="122" y="298" font-size="11" fill="#666">Public prestige, low price</text>
  </g>
  <g>
    <ellipse cx="510" cy="230" rx="105" ry="45" fill="#e3f2fd" stroke="#2a5a8c"/>
    <text x="432" y="225" font-size="13" fill="#1a3a5c" font-weight="700">RMIT / Fulbright</text>
    <text x="420" y="244" font-size="11" fill="#666">Premium international / policy</text>
  </g>
  <g>
    <ellipse cx="310" cy="300" rx="82" ry="36" fill="#fff8e1" stroke="#d97706"/>
    <text x="255" y="295" font-size="13" fill="#1a3a5c" font-weight="700">FSB / private MBA</text>
    <text x="252" y="314" font-size="11" fill="#666">Flexible corporate training</text>
  </g>
  <g>
    <ellipse cx="455" cy="120" rx="108" ry="46" fill="#e6f4ea" stroke="#2a7a3e" stroke-width="2"/>
    <text x="372" y="116" font-size="13" fill="#1a3a5c" font-weight="800">VLU Group 5</text>
    <text x="360" y="135" font-size="11" fill="#666">Niche premium applied verticals</text>
  </g>
  <g>
    <circle cx="418" cy="96" r="8" fill="#e63946"/><text x="432" y="101" font-size="12" fill="#1a3a5c">Family Academy</text>
    <circle cx="512" cy="142" r="8" fill="#2a7a3e"/><text x="526" y="147" font-size="12" fill="#1a3a5c">Healthcare MBA</text>
  </g>
</svg>
"""


SVG_PRICING = """
<svg viewBox="0 0 760 360" role="img" aria-label="Pricing comparables">
  <rect x="55" y="25" width="640" height="260" fill="#fff" stroke="#e0dcd0"/>
  <line x1="90" y1="260" x2="660" y2="260" stroke="#1a3a5c" stroke-width="2"/>
  <line x1="90" y1="260" x2="90" y2="55" stroke="#1a3a5c" stroke-width="2"/>
  <text x="300" y="330" fill="#1a3a5c" font-size="14" font-weight="700">Tuition USD</text>
  <g font-size="11" fill="#666">
    <text x="78" y="278">$0</text><text x="204" y="278">$20k</text><text x="337" y="278">$50k</text><text x="492" y="278">$90k</text><text x="615" y="278">$120k</text>
  </g>
  <g>
    <rect x="150" y="205" width="92" height="24" fill="#f6f3ec" stroke="#d4a418"/><text x="158" y="222" font-size="11">VN public</text>
    <rect x="236" y="168" width="110" height="24" fill="#fff8e1" stroke="#d97706"/><text x="244" y="185" font-size="11">VLU lean $15-35k</text>
    <rect x="290" y="124" width="145" height="24" fill="#e6f4ea" stroke="#2a7a3e"/><text x="298" y="141" font-size="11">India/SEA fast-track</text>
    <rect x="430" y="92" width="130" height="24" fill="#e3f2fd" stroke="#2a5a8c"/><text x="438" y="109" font-size="11">Singapore premium</text>
    <rect x="560" y="62" width="86" height="24" fill="#fde8e8" stroke="#e63946"/><text x="568" y="79" font-size="11">Global elite</text>
  </g>
  <line x1="236" y1="55" x2="236" y2="260" stroke="#e63946" stroke-width="2" stroke-dasharray="4 4"/>
  <text x="248" y="67" font-size="12" fill="#e63946" font-weight="700">VLU lower bound</text>
</svg>
"""


def esc(text: object) -> str:
    return html.escape(str(text), quote=True)


def inline_md(text: object) -> str:
    """Escape text, then restore a small safe Markdown subset."""
    s = esc(text)
    s = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        lambda m: f"<a href='{m.group(2)}'>{m.group(1)}</a>",
        s,
    )
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def slug(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return text or "section"


def money(n: float) -> str:
    return f"${n:,.0f}"


def read_optional(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def md_to_html(md: str) -> str:
    """Tiny Markdown subset for local gap appendices."""
    out: list[str] = []
    in_ul = False
    in_ol = False
    in_table = False
    table_rows: list[str] = []

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def flush_table() -> None:
        nonlocal in_table, table_rows
        if not in_table:
            return
        out.append("<div class='table-wrap'><table>")
        for idx, row in enumerate(table_rows):
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if len(cells) <= 1 or all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                continue
            tag = "th" if idx == 0 else "td"
            out.append("<tr>" + "".join(f"<{tag}>{inline_md(c)}</{tag}>" for c in cells) + "</tr>")
        out.append("</table></div>")
        table_rows = []
        in_table = False

    for raw in md.splitlines():
        line = raw.rstrip()
        if not line:
            flush_table()
            close_lists()
            continue
        if line.startswith("|") and line.endswith("|"):
            close_lists()
            in_table = True
            table_rows.append(line)
            continue
        flush_table()
        if line.startswith("### "):
            close_lists()
            out.append(f"<h4>{inline_md(line[4:])}</h4>")
        elif line.startswith("## "):
            close_lists()
            out.append(f"<h3>{inline_md(line[3:])}</h3>")
        elif line.startswith("# "):
            close_lists()
            out.append(f"<h3>{inline_md(line[2:])}</h3>")
        elif line.startswith("- "):
            if not in_ul:
                close_lists()
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline_md(line[2:])}</li>")
        elif re.match(r"^\d+\.\s+", line):
            if not in_ol:
                close_lists()
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline_md(re.sub(r'^\d+\\.\\s+', '', line))}</li>")
        else:
            close_lists()
            out.append(f"<p>{inline_md(line)}</p>")
    flush_table()
    close_lists()
    return "\n".join(out)


def table_html(headers: list[str], rows: Iterable[Iterable[object]]) -> str:
    h = "".join(f"<th>{esc(x)}</th>" for x in headers)
    body = []
    for row in rows:
        body.append("<tr>" + "".join(f"<td>{esc(x)}</td>" for x in row) + "</tr>")
    return f"<div class='table-wrap'><table><thead><tr>{h}</tr></thead><tbody>{''.join(body)}</tbody></table></div>"


def link_table_html(headers: list[str], rows: Iterable[tuple[str, str]]) -> str:
    h = "".join(f"<th>{esc(x)}</th>" for x in headers)
    body = []
    for name, url in rows:
        body.append(f"<tr><td>{esc(name)}</td><td><a href='{esc(url)}'>{esc(url)}</a></td></tr>")
    return f"<div class='table-wrap'><table><thead><tr>{h}</tr></thead><tbody>{''.join(body)}</tbody></table></div>"


def stat_cards(cards: list[tuple[str, str, str]]) -> str:
    return "<div class='stat-row'>" + "".join(
        f"<div class='stat-card {cls}'><div class='num'>{esc(num)}</div><div class='label'>{esc(label)}</div></div>"
        for num, label, cls in cards
    ) + "</div>"


def section(title: str, body: str, sid: str | None = None) -> tuple[str, str, str]:
    sid = sid or slug(title)
    return sid, title, f"<section id='{sid}'><h2>{esc(title)}</h2>{body}</section>"


def build_charts() -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    years = ["Y1", "Y2", "Y3"]
    x = range(len(years))
    fig, ax = plt.subplots(figsize=(7.2, 4.0), dpi=180)
    bottom = [0, 0, 0]
    colors = ["#1a3a5c", "#2a7a3e", "#d4a418"]
    for idx, (name, data) in enumerate(FINANCIALS.items()):
        ax.bar(x, data["revenue"], bottom=bottom, label=name, color=colors[idx])
        bottom = [bottom[i] + data["revenue"][i] for i in range(3)]
    ax.set_xticks(list(x), years)
    ax.set_ylabel("Revenue USD")
    ax.set_title("Triple-stack revenue model")
    ax.legend(loc="upper left", fontsize=8)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(ASSET_DIR / "triple_stack_revenue.png", transparent=False)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7.2, 4.0), dpi=180)
    labels = ["Original\n12/18/30", "Mary lean\n15/20/35", "Parity\n20/30/50"]
    acceptable = [68, 82, 44]
    premium_signal = [55, 78, 91]
    ax.plot(labels, acceptable, marker="o", label="Purchase intent")
    ax.plot(labels, premium_signal, marker="o", label="Premium signal")
    ax.set_ylim(0, 100)
    ax.set_ylabel("Synthetic score")
    ax.set_title("Family Academy pricing scenario")
    ax.legend(loc="lower right", fontsize=8)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(ASSET_DIR / "pricing_scenario.png", transparent=False)
    plt.close(fig)


def build_html() -> None:
    sections: list[tuple[str, str, str]] = []

    exec_body = f"""
    <p>R3 đóng vai trò vòng tổng hợp cuối trước khi NA trình VLU Board. Báo cáo này nối R1 nền tảng chiến lược, R2 comparative research 4 thị trường, và R3 bổ sung buyer voice Việt Nam, competitor deep-dive, peer markets Malaysia/Indonesia, SPJIMR operational playbook, pricing validation, regulatory/accreditation roadmap.</p>
    {stat_cards([
        ("6", "research gaps đã đóng bằng nguồn công khai + synthesis", "primary"),
        ("36", "program comparables trong Excel workbook", ""),
        ("$15k", "Family Academy entry price Mary's lean", "gold"),
        ("Y3", "breakout year nếu triple-stack chạy đúng cadence", "success"),
    ])}
    <div class='callout callout-success'><strong>Mary's lean:</strong> Commit Family Academy là wedge đầu tiên, thiết kế Healthcare MBA như anchor 12-15 tháng với live-client capstone, và dùng Lifelong Membership như halo để compound network. Không cố đánh generic MBA.</div>
    {table_html(["Stack", "Role", "R3 design choice", "Y3 revenue"], [
        ["Family Enterprise Academy", "Wedge", "15-month modular; 6 ngày/tháng; $15k/$20k/$35k", money(FINANCIALS["Family Academy"]["revenue"][2])],
        ["Healthcare Leadership MBA", "Anchor", "12-month intensive + 3-month capstone; $12k/$18k/$30k", money(FINANCIALS["Healthcare MBA"]["revenue"][2])],
        ["Lifelong Membership", "Halo", "Alumni subscription + short-course network", money(FINANCIALS["Membership Halo"]["revenue"][2])],
    ])}
    """
    sections.append(section("1. Tóm Tắt Điều Hành", exec_body, "exec"))

    methodology_body = """
    <p><strong>Timeline:</strong> R1 tạo foundation context và master HTML report; R2 mở rộng 4 markets China/Australia/India/Singapore; R3 đóng 6 gap còn thiếu để ra decision package.</p>
    <p><strong>Methodology:</strong> desk research từ nguồn chính thức, R2 raw files, R1 planning artifacts, public web, synthetic pricing model. Các inference operational không có nguồn công khai được đánh dấu là inferred operating model.</p>
    """ + table_html(["Round", "Date", "Output", "Use in R3"], [
        ["R1", "2026-05-20", "VLU master report + PRD/product briefs", "Strategic foundation, financial model, triple-stack"],
        ["R2", "2026-05-21", "4-market comparative research", "International steal-list and anti-patterns"],
        ["R3", "2026-05-21", "PPTX + HTML + Excel", "Board decision package"],
    ])
    sections.append(section("2. Timeline R1-R3 & Phương Pháp", methodology_body, "timeline"))

    ai_body = """
    <p>AI làm tri thức codified rẻ đi, nhưng làm <em>judgment, network density, applied wisdom, trust signaling</em> đắt lên. Vì vậy post-grad VLU không nên bán “nội dung MBA” mà bán cộng đồng người ra quyết định, dự án thật, faculty/practitioner feedback, và credential có kiểm định.</p>
    <div class='callout'><strong>AI-resilience test:</strong> Nếu LLM có thể thay học viên làm 80% bài học, module đó phải được thiết kế lại thành live project, peer review, hoặc board-level decision simulation.</div>
    """ + table_html(["Giá trị cũ", "Rủi ro AI", "Thiết kế VLU mới"], [
        ["Lecture-based knowledge", "LLM giải thích rẻ hơn và cá nhân hóa hơn", "Pre-work AI + classroom for judgment"],
        ["Generic case study", "AI tóm tắt case trong vài phút", "VN live-client case với consequence thật"],
        ["Degree as signal", "Credential inflation", "Degree + proof-of-work + advisory-board validation"],
        ["One-off program", "Skill half-life ngắn", "Lifelong membership và refresh modules"],
    ])
    sections.append(section("3. AI x Higher Ed: Bối Cảnh Toàn Cầu", ai_body, "ai-he"))

    markets_rows = [
        ["China", "Network + status + Western co-brand", "CKGSB network, Tsinghua-MIT", "Network is product"],
        ["Australia", "PR pathway + speed/flexibility", "Bond 12-month, Torrens on-demand", "Copy speed, not PR dependence"],
        ["India", "Salary ROI + one-year + family business", "ISB/IIM/SPJIMR", "Copy SPJIMR + fast-track"],
        ["Singapore", "Global mobility + brand stack", "INSEAD/NUS/SMU", "Study capstone/network, not global claims"],
        ["Malaysia", "Private mid-tier professional flexibility", "Sunway, Taylor's, Heriot-Watt", "SEA pricing realism"],
        ["Indonesia", "Private entrepreneurship + family business density", "BINUS, Prasetiya Mulya, Sampoerna", "Closest peer for family-business wedge"],
    ]
    markets_body = table_html(["Market", "Selling DNA", "Anchor examples", "VLU implication"], markets_rows)
    sections.append(section("4. Phân Tích 6 Thị Trường", markets_body, "markets"))

    comp_body = f"""
    <p>VN competitor field chia thành bốn nhóm đã có: public prestige, foreign-premium, policy elite, flexible private MBA. VLU tạo nhóm thứ năm: <strong>niche premium applied verticals</strong>.</p>
    <figure class='chart'><figcaption class='title'>Porter Strategic Group Map mở rộng</figcaption>{SVG_STRATEGIC_GROUP}<figcaption class='source'>R1 Porter map extended with R3 competitor research.</figcaption></figure>
    """ + table_html(["Competitor", "Strength", "Weakness vs VLU triple-stack", "Threat level"], [
        ["RMIT Vietnam MBA", "Australian credential, premium English brand", "Generic MBA; no family/healthcare vertical depth", "High for generic MBA, medium for Healthcare"],
        ["UEH / NEU / FTU", "Public prestige, alumni scale, affordability", "Slower to build boutique premium vertical", "Medium"],
        ["Fulbright FSPPM", "Policy leadership, scholarship trust", "Policy not business succession/healthcare operations", "Low-medium"],
        ["FSB", "Corporate training, FPT tech brand, flexible delivery", "Less academic/regulatory premium; weaker Family Academy fit", "Medium"],
        ["Hawaii/foreign partnerships", "Foreign-degree signal", "Regulatory and brand-fragmentation risk", "Low-medium"],
    ])
    sections.append(section("5. Bản Đồ Cạnh Tranh Việt Nam", comp_body, "competitors"))

    voc_body = """
    <p>Public buyer voice không thay thế primary interviews, nhưng đủ để chốt ba buyer patterns: học thạc sĩ để mở đường thăng tiến, sợ học không đáng tiền, và cần format không phá công việc/gia đình.</p>
    """ + table_html(["Persona", "Core motivation", "Top objection", "VLU close lever"], [
        ["Gen-2 family heir, 22-35", "Credibility trong gia đình + peer confidential network", "Bố/mẹ trả tiền nhưng nghi ngờ academic theory", "Founder dinner + family governance capstone"],
        ["Hospital/pharma exec, 30-45", "Promotion into management without leaving clinical/commercial work", "MBA generic không hiểu ngành y", "Hospital partner capstone + sector faculty"],
        ["SMB founder/owner, 35-55", "Scale company, professionalize team, reduce lonely decision-making", "Không có thời gian; sợ lớp toàn lý thuyết", "Weekend modular + live business diagnosis"],
    ])
    sections.append(section("6. Voice of Vietnamese Buyer", voc_body, "voc"))

    selling_body = """
    <p>R3 đã tách rõ <strong>what to sell</strong> theo từng buyer job. Điểm quan trọng: VLU không nên bán một generic MBA bằng cùng ngôn ngữ với RMIT/UEH/FSB. Mỗi sản phẩm phải có một selling proposition riêng và proof mechanism riêng.</p>
    """ + table_html(["Selling proposition", "Khi nào nên dùng", "VLU application", "Proof cần có", "Không nên claim"], [
        ["Career transition", "Người học muốn đổi vai trò/chức năng/ngành", "Healthcare MBA: clinician/pharma manager chuyển sang hospital ops, quality, strategy", "Promotion stories, capstone ROI, employer sponsorship", "Không claim placement/salary trước cohort 3"],
        ["Career fast-track", "Người học không thể nghỉ 2 năm nhưng cần credential nhanh", "Healthcare MBA 12 tháng + 3 tháng capstone; Family Academy 6 ngày/tháng", "Calendar cụ thể, workload rõ, completion support", "Không biến fast-track thành low-rigor"],
        ["Global network / connections", "Buyer cần mở mạng lưới, mentor, international vocabulary", "Membership halo + ASEAN immersion + visiting faculty + UH/VEMBA adjacency", "Named mentors, partner events, alumni participation", "Không claim global mobility như INSEAD/NUS"],
        ["Local peer network", "Founder/heir/operator cần người cùng bối cảnh Việt Nam", "Family Academy confidential heir cohort; healthcare leader cohort", "Cohort filter, confidentiality protocol, founder dinners", "Không mở admission đại trà"],
        ["Status / signaling", "Gen-1, Board, employer cần thấy program đáng tiền", "Selective admissions, advisory board, annual report, capstone showcase", "Named advisory board, source-backed report, VLU QA", "Không overclaim accreditation"],
        ["Applied transformation", "Buyer nghi ngờ thạc sĩ lý thuyết", "Family Business Transformation Project; Hospital Operations Transformation Project", "Before/after metrics, sponsor sign-off", "Không dùng thesis/de án generic làm main promise"],
    ]) + """
    <div class='callout'><strong>Mary's sales architecture:</strong> Family Academy bán <em>succession confidence + confidential peer network</em>; Healthcare MBA bán <em>career fast-track into healthcare leadership + operating proof</em>; Membership bán <em>continuous access to people, refresh modules, and signals</em>.</div>
    """
    sections.append(section("7. Chiến Lược Bán Post-Grad", selling_body, "selling-strategy"))

    triple_body = table_html(["Stack", "Positioning sentence", "Defensibility lever", "Do not do"], [
        ["Family Academy", "Trường của thế hệ kế nghiệp doanh nghiệp gia đình Việt Nam", "Confidential cohort + annual family-business data asset", "Do not sell placement"],
        ["Healthcare MBA", "MBA quản trị y tế ứng dụng cho người đang vận hành bệnh viện/pharma", "Y + Business + Design + hospital capstone", "Do not make generic MBA with healthcare electives"],
        ["Membership", "Đại học suốt đời cho alumni và executives", "Network effect + refresh modules", "Do not overbuild custom AI platform before 100 active learners"],
    ])
    sections.append(section("8. Triple-Stack Strategy", triple_body, "triple-stack"))

    family_body = """
    <p>SPJIMR PGPFMB là benchmark trực tiếp vì cùng buyer logic: người học không đi tìm placement; họ quay về doanh nghiệp gia đình. Format 6 ngày/tháng bảo vệ operating role, đồng thời tạo đủ immersion để cohort thật sự bonded.</p>
    """ + table_html(["Design layer", "SPJIMR pattern", "VLU adaptation"], [
        ["Calendar", "6 days/month modular", "Thứ Tư-Thứ Hai hoặc Thu-Ba, 1 block/tháng, 15 tháng"],
        ["Admissions", "Family-business fit, interview, no placement promise", "Require ownership/role proof + gen-1 sponsor conversation"],
        ["Capstone", "Family business transformation", "Family Constitution + Succession Roadmap + Growth Initiative"],
        ["Research engine", "CFBE / reports / alumni stories", "VLU Center for Vietnamese Family Enterprise, annual State Report"],
        ["Staffing", "Program director + faculty/practitioner network", "1 external director, 1 admissions BD, 1 alumni/community lead by Y1"],
    ])
    sections.append(section("9. Family Academy Playbook", family_body, "family"))

    healthcare_body = table_html(["Component", "R3 choice", "Reason"], [
        ["Format", "12-month intensive + 3-month capstone", "India one-year opportunity-cost pattern is stronger than 18-month drag"],
        ["Cohort", "30 Y1, 60 Y2, 120 Y3", "Healthcare market is broader than family-business niche"],
        ["Pricing", "$12k standard; $18k sponsored; $30k with ASEAN immersion", "Keeps access for clinical operators while preserving a premium sponsor tier"],
        ["Capstone", "Named hospital/pharma client project", "Defensible only if partner is named and repeated"],
        ["Faculty", "40% academic, 60% practitioner", "Healthcare execs buy applied operating wisdom"],
    ])
    sections.append(section("10. Healthcare MBA Design", healthcare_body, "healthcare"))

    membership_body = table_html(["Layer", "Offer", "Metric"], [
        ["Included alumni layer", "Lifetime cohort community + 2 annual salons", "70% alumni active Y1"],
        ["Paid membership", "Short courses, mentor access, sector roundtables", "250 members Y1"],
        ["AI co-pilot", "Off-shelf Teams + curated prompt/workflow library", "Do not custom-build before demand proof"],
        ["Research flywheel", "Annual reports + pulse surveys", "2 reports/year by Y2"],
    ])
    sections.append(section("11. Lifelong Membership Halo", membership_body, "membership"))

    pricing_body = f"""
    <figure class='chart'><figcaption class='title'>Pricing bands from R2/R3 comparables</figcaption>{SVG_PRICING}<figcaption class='source'>36-program catalog; USD normalized.</figcaption></figure>
    """ + table_html(["Program", "Mary's lean", "Alternative", "Rationale"], [
        ["Family Academy", "$15k / $20k / $35k", "$20k / $30k / $50k after Cohort 2 proof", "Original $12k tier risks cheapening a premium confidential network"],
        ["Healthcare MBA", "$12k / $18k / $30k", "$15k / $18k / $24k if hospital sponsorship weak", "Preserves access for individual healthcare learners while allowing hospital-sponsored premium tier"],
    ])
    sections.append(section("12. Pricing Recommendations", pricing_body, "pricing"))

    reg_body = table_html(["Regulatory item", "What it means for VLU", "Action"], [
        ["Thông tư 23/2021/TT-BGDĐT", "Master programs need admission/training/outcome discipline; application-oriented pathway is viable", "Map every module to learning outcomes + capstone assessment"],
        ["Thông tư 07/2025/TT-BGDĐT", "Foreign joint/dual-degree governance is tighter and time-limited; do not lead with dual degree", "Start with visiting faculty/MOU, delay joint degree to Y3+"],
        ["Decree 219/2025 foreign workers", "Foreign faculty can work via work permit/exemption pathways but paperwork must be planned", "Batch visiting-faculty blocks and legalize credentials early"],
        ["AACSB", "5-7 year credibility path, not launch requirement", "Y1 gap audit, Y2 assurance-of-learning, Y3 eligibility"],
    ])
    sections.append(section("13. Regulatory & Accreditation", reg_body, "regulatory"))

    rows = []
    for name, data in FINANCIALS.items():
        rows.append([name, money(data["revenue"][0]), money(data["revenue"][1]), money(data["revenue"][2]), money(sum(data["net"]))])
    financial_body = table_html(["Stack", "Y1 revenue", "Y2 revenue", "Y3 revenue", "3-year net"], rows)
    sections.append(section("14. Financial Model 3 Năm", financial_body, "financials"))

    def_body = table_html(["Criteria", "Family Academy", "Healthcare MBA", "Membership"], [
        ["Network effect", "5", "4", "5"],
        ["Capability moat", "4", "5", "3"],
        ["Switching cost", "4", "4", "4"],
        ["Brand moat", "5", "4", "3"],
        ["Proof/data moat", "4", "4", "4"],
        ["Total", "22/25", "21/25", "19/25"],
    ])
    sections.append(section("15. Defensibility Framework", def_body, "defensibility"))

    risk_body = table_html(["Risk", "Probability", "Impact", "Mitigation"], [
        ["Cannot recruit credible external program director", "Medium", "High", "Use interim advisory chair + practitioner director; no public launch before hire"],
        ["Family Academy demand overestimated", "Medium", "High", "Run 10-deposit pre-sell and founder dinners before capex"],
        ["Healthcare partners give weak capstones", "Medium", "High", "Require signed capstone LOI with named project owner"],
        ["MOET approval slows specialized naming", "Medium", "Medium", "Launch certificate/executive track while degree paperwork matures"],
        ["RMIT/UEH copy vertical positioning", "Low-medium", "Medium", "Build data/report/advisory board moat in first 18 months"],
    ])
    sections.append(section("16. Risk Register", risk_body, "risks"))

    exec_plan_body = table_html(["Month", "Foundation task", "Owner", "Output"], [
        ["M1", "Capability audit + legal pathway review", "NA + Academic Affairs", "Go/no-go memo"],
        ["M2", "Advisory board target list + 20 warm intros", "NA + BD", "10 meetings booked"],
        ["M3", "Founder dinner 1 + healthcare partner outreach", "Program leads", "5 family leads; 3 hospital LOIs"],
        ["M4", "Curriculum blueprint + faculty roster", "Academic lead", "Module map"],
        ["M5", "Pricing/pre-sell test", "Admissions", "10 Family deposits or LOIs"],
        ["M6", "Board approval checkpoint", "NA", "Final launch budget"],
        ["M7-M12", "Recruit, finalize partners, publish first report", "Program team", "Cohort 0 launch-ready"],
    ])
    sections.append(section("17. Execution Plan 12 Tháng", exec_plan_body, "execution"))

    asks_body = table_html(["Decision ask", "Recommended answer", "Why now"], [
        ["Approve Family Academy as primary wedge", "Yes, with pre-sell gate", "18-24 month response window before competitors notice"],
        ["Approve Healthcare MBA as anchor", "Yes, but redesign to fast-track + capstone", "VLU's Y+Business+Design combo is real capability moat"],
        ["Approve Y0 capability budget", "$150k gross, offset by deposits/sponsors", "Need director, legal, advisory board, capstone BD"],
        ["Approve accreditation path", "MOET-first, AACSB readiness", "Avoid premature dual-degree risk"],
    ])
    sections.append(section("18. Decision Asks", asks_body, "asks"))

    toolkit_body = table_html(["Tool", "Use", "First draft owner"], [
        ["Capability audit checklist", "Verify VLU can deliver before public promise", "Academic Affairs"],
        ["Founder outreach email", "Recruit advisory board and pre-sell cohort", "NA"],
        ["Hospital partner LOI template", "Secure capstone supply", "Healthcare lead"],
        ["Pricing interview guide", "Validate WTP before pricing lock", "Admissions research"],
        ["AACSB readiness tracker", "Start assurance-of-learning discipline early", "QA office"],
    ])
    sections.append(section("19. Action Toolkit", toolkit_body, "toolkit"))

    gap_appendices = []
    for path in sorted(RESEARCH_DIR.glob("gap*.md")):
        gap_appendices.append(f"<h3>{esc(path.name)}</h3>{md_to_html(read_optional(path))}")
    appendices = "\n".join(gap_appendices) or "<p>Gap research appendices were still being finalized at build time; the core synthesis above includes the working findings and source URLs.</p>"
    sources_body = link_table_html(["Source", "URL"], SOURCES)
    sources_body += f"<h3>Research appendices</h3>{appendices}"
    sections.append(section("20. Sources & Methodology", sources_body, "sources"))

    toc = "\n".join(f"<li><a href='#{sid}' data-target='{sid}'>{esc(title.split('. ', 1)[-1])}</a></li>" for sid, title, _ in sections)
    body = "\n".join(s for _, _, s in sections)

    css = f"""
    :root {{ --primary: #{PRIMARY}; --primary-light: #{PRIMARY_LIGHT}; --accent: #{ACCENT}; --gold: #{GOLD}; --bg: #fdfdfb; --text: #{TEXT}; --muted: #{MUTED}; --border: #{BORDER}; --soft-bg: #{SOFT_BG}; --success: #{SUCCESS}; --warning: #{WARNING}; --sidebar-w: 300px; }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; background: var(--bg); color: var(--text); line-height: 1.65; font-size: 16px; }}
    .layout {{ display:flex; min-height:100vh; }}
    .sidebar {{ width:var(--sidebar-w); background:var(--primary); color:white; padding:24px 18px; position:sticky; top:0; height:100vh; overflow-y:auto; flex-shrink:0; }}
    .sidebar h2 {{ font-size:1.1em; margin-bottom:6px; color:var(--gold); }}
    .sidebar .sub {{ font-size:.78em; opacity:.72; margin-bottom:20px; }}
    .sidebar nav ol {{ list-style:none; counter-reset:navi; }}
    .sidebar nav li {{ counter-increment:navi; margin-bottom:4px; }}
    .sidebar nav a {{ display:block; color:rgba(255,255,255,.86); text-decoration:none; padding:7px 10px; border-radius:5px; font-size:.88em; border-left:3px solid transparent; }}
    .sidebar nav a::before {{ content:counter(navi) ". "; opacity:.6; }}
    .sidebar nav a:hover {{ background:rgba(255,255,255,.08); border-left-color:var(--gold); }}
    main {{ flex:1; max-width:calc(100vw - var(--sidebar-w)); overflow-x:hidden; }}
    .container {{ max-width:980px; margin:0 auto; padding:0 28px 64px; }}
    header {{ background:linear-gradient(135deg,var(--primary),var(--primary-light)); color:white; padding:56px 28px 40px; }}
    header h1 {{ font-size:2em; line-height:1.2; margin-bottom:10px; font-weight:800; max-width:920px; }}
    header .subtitle {{ font-size:1.05em; opacity:.95; font-weight:300; max-width:920px; }}
    header .meta {{ margin-top:14px; font-size:.85em; opacity:.85; }}
    header .meta span {{ display:inline-block; margin-right:12px; }}
    h2 {{ font-size:1.55em; color:var(--primary); margin:48px 0 14px; padding-bottom:8px; border-bottom:3px solid var(--gold); font-weight:700; scroll-margin-top:16px; }}
    h3 {{ font-size:1.22em; color:var(--primary); margin:28px 0 10px; font-weight:700; }}
    h4 {{ font-size:1.06em; margin:20px 0 8px; color:#333; font-weight:700; }}
    p {{ margin-bottom:13px; }}
    ul,ol {{ margin:10px 0 16px 24px; }}
    li {{ margin-bottom:5px; }}
    .callout {{ background:var(--soft-bg); border-left:4px solid var(--gold); padding:14px 18px; margin:18px 0; border-radius:4px; }}
    .callout-success {{ border-left-color:var(--success); background:#e6f4ea; }}
    .stat-row {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:10px; margin:18px 0; }}
    .stat-card {{ background:white; border:1px solid var(--border); padding:14px 12px; border-radius:8px; text-align:center; box-shadow:0 1px 2px rgba(0,0,0,.04); }}
    .stat-card .num {{ font-size:1.7em; font-weight:800; color:var(--accent); line-height:1; }}
    .stat-card .label {{ font-size:.8em; color:var(--muted); margin-top:6px; line-height:1.4; }}
    .stat-card.gold .num {{ color:var(--gold); }} .stat-card.success .num {{ color:var(--success); }} .stat-card.primary .num {{ color:var(--primary); }}
    .table-wrap {{ overflow-x:auto; margin:14px 0; }}
    table {{ border-collapse:collapse; width:100%; background:white; font-size:.9em; border:1px solid var(--border); }}
    th,td {{ padding:9px 11px; text-align:left; border-bottom:1px solid var(--border); vertical-align:top; }}
    th {{ background:var(--primary); color:white; font-weight:700; font-size:.85em; }}
    tr:hover td {{ background:#fafafa; }}
    figure.chart {{ background:white; padding:16px; border-radius:8px; border:1px solid var(--border); margin:18px 0; box-shadow:0 1px 2px rgba(0,0,0,.04); }}
    figure.chart figcaption.title {{ font-weight:700; margin-bottom:10px; color:var(--primary); font-size:.98em; }}
    figure.chart figcaption.source {{ font-size:.76em; color:var(--muted); margin-top:8px; font-style:italic; }}
    figure.chart svg {{ width:100%; height:auto; display:block; }}
    .mobile-toc-btn {{ display:none; position:fixed; top:12px; left:12px; z-index:100; background:var(--primary); color:white; border:none; padding:8px 12px; border-radius:5px; font-size:.9em; }}
    a {{ color:var(--primary); word-break:break-word; }}
    @media (max-width:900px) {{ .layout {{ flex-direction:column; }} .sidebar {{ position:fixed; top:0; left:-280px; height:100vh; width:280px; z-index:99; transition:left .25s; }} .sidebar.open {{ left:0; box-shadow:4px 0 12px rgba(0,0,0,.18); }} main {{ max-width:100vw; }} .container {{ padding:0 16px 48px; }} header {{ padding:60px 16px 32px; }} .mobile-toc-btn {{ display:block; }} body {{ font-size:15px; }} table {{ font-size:.84em; }} th,td {{ padding:7px 8px; }} }}
    @media print {{ .sidebar,.mobile-toc-btn {{ display:none; }} main {{ max-width:100%; }} header {{ background:var(--primary) !important; -webkit-print-color-adjust:exact; print-color-adjust:exact; }} }}
    """

    js = """
    document.querySelectorAll('.sidebar a').forEach(a => {
      a.addEventListener('click', () => document.querySelector('.sidebar').classList.remove('open'));
    });
    """
    html_doc = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex, noai, noimageai">
<meta name="referrer" content="no-referrer">
<title>VLU Post-Grad Research Final Report 2026</title>
<style>{css}</style>
</head>
<body>
<button class="mobile-toc-btn" onclick="document.querySelector('.sidebar').classList.toggle('open')">Mục lục</button>
<div class="layout">
<aside class="sidebar"><h2>VLU Research</h2><div class="sub">R3 final package · 2026-05-21</div><nav><ol>{toc}</ol></nav></aside>
<main>
<header><h1>VLU Post-Grad Research<br>Final Decision Package</h1><p class="subtitle">Family Academy · Healthcare Leadership MBA · Lifelong Membership · Board-ready synthesis</p><div class="meta"><span>2026-05-21</span><span>Research by NA</span><span>R3</span></div></header>
<div class="container">{body}</div>
</main>
</div>
<script>{js}</script>
</body>
</html>"""
    HTML_PATH.write_text(html_doc, encoding="utf-8")


def set_cell(ws, cell: str, value, bold=False, fill=None, font_color="000000", align="left"):
    c = ws[cell]
    c.value = value
    c.font = Font(bold=bold, color=font_color)
    if fill:
        c.fill = PatternFill("solid", fgColor=fill)
    c.alignment = Alignment(horizontal=align, vertical="top", wrap_text=True)
    return c


def format_sheet(ws, widths: dict[int, int] | None = None) -> None:
    ws.freeze_panes = "A2"
    header_fill = PatternFill("solid", fgColor=PRIMARY)
    header_font = Font(bold=True, color="FFFFFF")
    thin = Side(style="thin", color=BORDER)
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            cell.border = Border(bottom=thin)
    for cell in ws[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    if widths:
        for idx, width in widths.items():
            ws.column_dimensions[get_column_letter(idx)].width = width
    else:
        for idx in range(1, ws.max_column + 1):
            ws.column_dimensions[get_column_letter(idx)].width = 18


def add_phase_row(ws, row_idx: int, label: str, last_col: int) -> None:
    ws.merge_cells(start_row=row_idx, start_column=1, end_row=row_idx, end_column=last_col)
    c = ws.cell(row=row_idx, column=1)
    c.value = label
    c.font = Font(bold=True, color="FFFFFF")
    c.fill = PatternFill("solid", fgColor=PRIMARY)
    c.alignment = Alignment(horizontal="left", vertical="center")


def build_excel() -> None:
    wb = Workbook()
    wb.remove(wb.active)

    ws = wb.create_sheet("README")
    ws.append(["Mục", "Nội dung"])
    rows = [
        ("Tên workbook", "VLU Post-Grad Data Synthesis 2026"),
        ("Mục đích", "Nguồn dữ liệu tổng hợp cho Board pitch deck và HTML final report R3."),
        ("Refresh date", "2026-05-21"),
        ("Ngôn ngữ", "Tiếng Việt, giữ business terms tiếng Anh khi cần."),
        ("Ràng buộc format", "Không icon, không row-2 descriptions, có phase divider rows ở execution plan."),
        ("File map", "HTML report, PPTX board deck, Excel workbook đều sinh từ cùng script build_r3_deliverables.py."),
    ]
    for r in rows:
        ws.append(r)
    format_sheet(ws, {1: 24, 2: 90})

    ws = wb.create_sheet("Programs Catalog")
    ws.append(["market", "program", "tuition USD", "duration", "format", "modality", "cohort size", "GMAT median", "accept rate", "value prop tag", "key proof point", "source URL", "notes"])
    for p in PROGRAMS:
        ws.append([p.market, p.program, p.tuition_usd, p.duration_months, p.format, p.modality, p.cohort_size, p.gmat_median, p.accept_rate, p.value_tags, p.proof, p.source_url, p.notes])
    format_sheet(ws, {1: 16, 2: 34, 3: 14, 4: 12, 5: 18, 6: 22, 7: 14, 8: 14, 9: 14, 10: 28, 11: 42, 12: 44, 13: 28})

    ws = wb.create_sheet("Pricing Comparables")
    ws.append(["program", "market", "tuition USD", "duration months", "tuition/month", "pricing band", "source"])
    for p in PROGRAMS:
        band = "Low" if p.tuition_usd < 12000 else "Mid" if p.tuition_usd < 30000 else "Premium" if p.tuition_usd < 70000 else "Elite"
        ws.append([p.program, p.market, p.tuition_usd, p.duration_months, p.tuition_per_month, band, p.source_url])
    start = ws.max_row + 3
    ws.cell(start, 1, "Van Westendorp synthetic summary")
    ws.cell(start, 1).font = Font(bold=True, color="FFFFFF")
    ws.cell(start, 1).fill = PatternFill("solid", fgColor=PRIMARY)
    ws.merge_cells(start_row=start, start_column=1, end_row=start, end_column=7)
    ws.append(["program", "scenario", "too cheap", "cheap", "expensive", "too expensive", "Mary lean"])
    for row in [
        ["Family Academy", "$12k/$18k/$30k", 34, 62, 28, 11, "No"],
        ["Family Academy", "$15k/$20k/$35k", 18, 47, 39, 17, "Yes"],
        ["Family Academy", "$20k/$30k/$50k", 8, 29, 58, 37, "Alternative after proof"],
        ["Healthcare MBA", "$12k/$15k/$18k", 22, 55, 34, 13, "Too compressed"],
        ["Healthcare MBA", "$12k/$18k/$30k", 12, 48, 41, 22, "Yes"],
        ["Healthcare MBA", "$15k/$18k/$24k", 13, 44, 43, 19, "Alternative"],
    ]:
        ws.append(row)
    format_sheet(ws, {1: 30, 2: 22, 3: 12, 4: 12, 5: 12, 6: 14, 7: 36})

    ws = wb.create_sheet("6-Layer Matrix")
    ws.append(["market", "career transition", "salary ROI", "network/status", "specialization depth", "brand transfer", "family business", "VLU borrowable"])
    matrix = [
        ["China", 3, 4, 5, 4, 5, 1, "Network-as-product; policy/status signal"],
        ["Australia", 3, 2, 2, 3, 3, 1, "Fast-track and applied capstone, not PR pathway"],
        ["India", 4, 5, 4, 5, 4, 5, "SPJIMR + one-year executive pattern"],
        ["Singapore", 5, 4, 5, 4, 5, 1, "Global network and brand-stack discipline"],
        ["Malaysia", 3, 2, 2, 3, 3, 1, "Private mid-tier affordability and flexibility"],
        ["Indonesia", 3, 2, 3, 4, 3, 4, "Family business + entrepreneurship for peer market"],
        ["Vietnam", 2, 2, 3, 2, 2, 0, "Whitespace for VLU Group 5"],
    ]
    for row in matrix:
        ws.append(row)
    format_sheet(ws, {1: 16, 2: 16, 3: 12, 4: 16, 5: 20, 6: 16, 7: 16, 8: 42})
    ws.conditional_formatting.add("B2:G8", ColorScaleRule(start_type="num", start_value=1, start_color="FDE8E8", mid_type="num", mid_value=3, mid_color="FFF8E1", end_type="num", end_value=5, end_color="E6F4EA"))

    ws = wb.create_sheet("Course DNA Comparison")
    ws.append(["dimension", "China", "Australia", "India", "Singapore", "Malaysia", "Indonesia", "VLU recommendation"])
    dna = [
        ["Duration", "14-24 mo", "12-24 mo", "12 mo exec dominant", "10-17 mo", "12-24 mo", "18 mo exec common", "Family 15 mo modular; Healthcare 12+3 mo"],
        ["Modality", "On-campus + modular", "Hybrid/online more common", "Residential intensity", "On-campus elite", "Flexible private", "Hybrid executive", "On-campus + partner sites"],
        ["Capstone", "Consulting/thesis", "Industry studies", "ELP/live consulting", "Practicum/mission", "Project", "Applied project", "Named live-client capstone"],
        ["Faculty", "Academic + elite guests", "Academic-heavy", "Hybrid", "Academic-heavy", "Practitioner flexible", "Practitioner-heavy", "40/60 academic-practitioner"],
        ["Language", "Chinese/English", "English", "English", "English", "English", "Bahasa/English", "Vietnamese-primary + English terms"],
        ["Admissions", "GMAT/selective", "GMAT for elite", "Highly selective", "Ranking-driven", "Open-mid", "Open-mid", "Application + interview + fit"],
        ["Alumni", "Network sold hard", "Traditional alumni", "Placement/alumni", "Global chapters", "Institutional alumni", "Entrepreneurial alumni", "Membership embedded in tuition"],
        ["Pricing", "$28k-$100k", "$39k-$102k", "$24k-$54k", "$54k-$119k", "$10k-$18k", "$12k-$16k", "$15k-$35k Family; $12k-$30k Healthcare"],
    ]
    for row in dna:
        ws.append(row)
    format_sheet(ws, {1: 20, 2: 22, 3: 22, 4: 24, 5: 22, 6: 22, 7: 22, 8: 42})

    ws = wb.create_sheet("VLU Triple-Stack Scorecards")
    ws.append(["program", "network effect", "capability moat", "switching cost", "brand moat", "proof/data moat", "total", "Y3 revenue", "target metric"])
    score_rows = [
        ["Family Academy", 5, 4, 4, 5, 4, 22, FINANCIALS["Family Academy"]["revenue"][2], "25+ qualified applications before public launch"],
        ["Healthcare MBA", 4, 5, 4, 4, 4, 21, FINANCIALS["Healthcare MBA"]["revenue"][2], "8 signed hospital/pharma capstone LOIs"],
        ["Membership Halo", 5, 3, 4, 3, 4, 19, FINANCIALS["Membership Halo"]["revenue"][2], "250 paid members Y1"],
    ]
    for row in score_rows:
        ws.append(row)
    format_sheet(ws, {1: 24, 2: 14, 3: 14, 4: 14, 5: 14, 6: 14, 7: 10, 8: 16, 9: 46})

    ws = wb.create_sheet("3-Year Financial Model")
    ws.append(["program", "metric", "Y1", "Y2", "Y3", "3-year total"])
    for name, data in FINANCIALS.items():
        ws.append([name, "students/members", *data["students"], sum(data["students"])])
        ws.append([name, "revenue", *data["revenue"], sum(data["revenue"])])
        ws.append([name, "gross margin", *data["gross_margin"], ""])
        ws.append([name, "net contribution", *data["net"], sum(data["net"])])
    ws.append(["TOTAL", "revenue", sum(v["revenue"][0] for v in FINANCIALS.values()), sum(v["revenue"][1] for v in FINANCIALS.values()), sum(v["revenue"][2] for v in FINANCIALS.values()), sum(sum(v["revenue"]) for v in FINANCIALS.values())])
    ws.append(["TOTAL", "net contribution", sum(v["net"][0] for v in FINANCIALS.values()), sum(v["net"][1] for v in FINANCIALS.values()), sum(v["net"][2] for v in FINANCIALS.values()), sum(sum(v["net"]) for v in FINANCIALS.values())])
    format_sheet(ws, {1: 24, 2: 22, 3: 16, 4: 16, 5: 16, 6: 18})
    chart = BarChart()
    chart.title = "Triple-stack revenue"
    data_ref = Reference(ws, min_col=3, max_col=5, min_row=2, max_row=13)
    cats = Reference(ws, min_col=1, min_row=2, max_row=13)
    chart.add_data(data_ref, titles_from_data=False)
    chart.set_categories(cats)
    chart.height = 8
    chart.width = 16
    ws.add_chart(chart, "H2")

    ws = wb.create_sheet("12-Month Execution Plan")
    ws.append(["Tháng", "Pha", "Việc cần làm", "Owner", "Dependency", "Deliverable", "Status"])
    row_idx = 2
    phases = [
        ("FOUNDATION", [
            ["M1", "Foundation", "Capability audit học thuật + legal path MOET", "Academic Affairs", "Board mandate", "Go/no-go memo", "Pending"],
            ["M1", "Foundation", "Map target advisory board 30 người", "NA", "Network list", "Shortlist", "Pending"],
            ["M1", "Foundation", "Define pricing interview script", "Admissions", "Persona draft", "Interview guide", "Pending"],
        ]),
        ("MARKET VALIDATION", [
            ["M2", "Validation", "Founder dinner 1", "NA + BD", "Shortlist", "5 qualified leads", "Pending"],
            ["M3", "Validation", "Healthcare partner outreach", "Healthcare lead", "Partner list", "3 LOIs", "Pending"],
            ["M4", "Validation", "Pricing/pre-sell test", "Admissions", "Founder dinner", "10 deposits/LOIs", "Pending"],
        ]),
        ("BUILD", [
            ["M5", "Build", "Hire/interim Program Director", "Board", "Budget approval", "Signed role", "Pending"],
            ["M6", "Build", "Curriculum + faculty roster", "Program Director", "Director hired", "Module map", "Pending"],
            ["M7", "Build", "First State of VN Family Business outline", "Research center", "Partner sponsor", "Report brief", "Pending"],
        ]),
        ("LAUNCH READINESS", [
            ["M8-M9", "Launch", "Admissions funnel live", "Admissions", "Pricing locked", "Applications", "Pending"],
            ["M10", "Launch", "Capstone partner finalization", "Program leads", "LOIs", "Project briefs", "Pending"],
            ["M11-M12", "Launch", "Board launch checkpoint", "NA", "All evidence", "Launch approval", "Pending"],
        ]),
    ]
    for label, tasks in phases:
        add_phase_row(ws, row_idx, label, 7)
        row_idx += 1
        for task in tasks:
            for col_idx, value in enumerate(task, start=1):
                ws.cell(row_idx, col_idx, value)
            row_idx += 1
    format_sheet(ws, {1: 12, 2: 16, 3: 42, 4: 18, 5: 24, 6: 28, 7: 14})

    ws = wb.create_sheet("Risk Register")
    ws.append(["risk ID", "category", "description", "probability", "impact", "mitigation", "owner"])
    risks = [
        ["R1", "Demand", "Family Academy interest is prestige-curious but not payment-ready", "Medium", "High", "10-deposit pre-sell gate before launch", "NA"],
        ["R2", "Talent", "No credible Program Director", "Medium", "High", "External hire + interim advisory chair", "Board"],
        ["R3", "Partner", "Hospital capstone partners do not allocate real projects", "Medium", "High", "LOI requires named project owner", "Healthcare lead"],
        ["R4", "Regulatory", "Specialized master's naming approval slower than plan", "Medium", "Medium", "Certificate/executive education bridge", "Academic Affairs"],
        ["R5", "Competitive", "RMIT/UEH copy healthcare/family messaging", "Low-medium", "Medium", "Advisory board + annual report + cohort confidentiality", "NA"],
        ["R6", "Quality", "Practitioner-heavy faculty weakens assessment discipline", "Medium", "Medium", "AACSB-style assurance of learning from Y1", "QA office"],
    ]
    for row in risks:
        ws.append(row)
    format_sheet(ws, {1: 10, 2: 16, 3: 48, 4: 14, 5: 12, 6: 46, 7: 18})

    ws = wb.create_sheet("Decision Log")
    ws.append(["decision ID", "question", "Mary lean", "status", "rationale"])
    for row in DECISIONS:
        ws.append(row)
    format_sheet(ws, {1: 12, 2: 42, 3: 34, 4: 16, 5: 56})

    wb.save(XLSX_PATH)


def add_textbox(slide, x, y, w, h, text, size=18, bold=False, color=TEXT, align=PP_ALIGN.LEFT):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
    p = tf.paragraphs[0]
    p.text = text
    p.alignment = align
    for run in p.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.color.rgb = RGBColor.from_string(color)
    return box


def add_title(slide, title: str, subtitle: str | None = None):
    add_textbox(slide, 0.55, 0.25, 8.8, 0.55, title, size=24, bold=True, color=PRIMARY)
    if subtitle:
        add_textbox(slide, 0.58, 0.82, 8.6, 0.35, subtitle, size=11, color=MUTED)
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.55), Inches(1.18), Inches(8.8), Inches(0.03))
    line.fill.solid()
    line.fill.fore_color.rgb = RGBColor.from_string(GOLD)
    line.line.fill.background()


def add_bullets(slide, x, y, w, h, bullets: list[str], size=15):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    for idx, bullet in enumerate(bullets):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.text = bullet
        p.level = 0
        p.font.name = "Arial"
        p.font.size = Pt(size)
        p.font.color.rgb = RGBColor.from_string(TEXT)
        p.space_after = Pt(7)
    return box


def add_footer(slide, n: int):
    add_textbox(slide, 0.55, 7.03, 4.5, 0.25, "VLU Post-Grad Research R3 · Research by NA", size=8, color=MUTED)
    add_textbox(slide, 9.0, 7.03, 0.7, 0.25, str(n), size=8, color=MUTED, align=PP_ALIGN.RIGHT)


def add_table_slide(slide, headers: list[str], rows: list[list[str]], x=0.55, y=1.45, w=8.9, h=4.8, font_size=9):
    table = slide.shapes.add_table(len(rows) + 1, len(headers), Inches(x), Inches(y), Inches(w), Inches(h)).table
    for col_idx, header in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.text = header
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor.from_string(PRIMARY)
        for p in cell.text_frame.paragraphs:
            for r in p.runs:
                r.font.color.rgb = RGBColor(255, 255, 255)
                r.font.bold = True
                r.font.size = Pt(font_size)
    for row_idx, row in enumerate(rows, start=1):
        for col_idx, value in enumerate(row):
            cell = table.cell(row_idx, col_idx)
            cell.text = str(value)
            for p in cell.text_frame.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(font_size)
                    r.font.name = "Arial"
    return table


def build_pptx() -> None:
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]
    slide_no = 1

    def new_slide(title=None, subtitle=None):
        nonlocal slide_no
        slide = prs.slides.add_slide(blank)
        bg = slide.background.fill
        bg.solid()
        bg.fore_color.rgb = RGBColor(253, 253, 251)
        if title:
            add_title(slide, title, subtitle)
        add_footer(slide, slide_no)
        slide_no += 1
        return slide

    slide = prs.slides.add_slide(blank)
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = RGBColor.from_string(PRIMARY)
    add_textbox(slide, 0.7, 1.6, 8.7, 1.0, "VLU Post-Grad Board Pitch 2026", size=32, bold=True, color="FFFFFF")
    add_textbox(slide, 0.72, 2.75, 8.3, 0.9, "Family Academy · Healthcare Leadership MBA · Lifelong Membership", size=18, color="FFFFFF")
    add_textbox(slide, 0.72, 5.6, 6.5, 0.4, "Research by NA · 2026-05-21", size=12, color="FFFFFF")
    add_footer(slide, slide_no)
    slide_no += 1

    slides_content = [
        ("Executive Summary", ["Commit to triple-stack: Family Academy as wedge, Healthcare MBA as anchor, Membership as halo.", "Use $15k/$20k/$35k Family Academy pricing for Cohort 1, with $20k/$30k/$50k reserved for post-proof scale.", "Board ask: approve Y0 capability build with pre-sell gates, not a public launch promise."]),
        ("Why Now", ["AI reduces the value of generic lectures; judgment, network and applied proof become premium.", "Vietnam post-grad demand is still protected demographically for 10-15 years.", "Family succession and healthcare management are urgent operating pains, not abstract education categories."]),
        ("Market Opportunity", ["Family businesses need succession structures; VN has no dedicated master-grade program.", "Healthcare chains and pharma operators need managers who understand both clinical and business systems.", "Mid-career learners want format flexibility without losing peer depth."]),
    ]
    for title, bullets in slides_content:
        slide = new_slide(title)
        add_bullets(slide, 0.8, 1.55, 8.3, 4.8, bullets, size=18)

    slide = new_slide("Post-Grad Selling Strategy")
    add_table_slide(slide, ["Sell", "Use for", "VLU proof"], [
        ["Career transition", "Healthcare leadership moves", "Capstone ROI + employer sponsorship"],
        ["Career fast-track", "Time-poor executives", "12-month/6-day-month calendar"],
        ["Global network", "Premium signal and vocabulary", "ASEAN immersion + visiting faculty"],
        ["Local peer network", "Family heirs and operators", "Selective confidential cohort"],
        ["Applied transformation", "Anti-theory objection", "Family/hospital transformation project"],
    ], font_size=9)

    slide = new_slide("Competitive Landscape", "VLU should create Group 5 instead of fighting existing groups.")
    add_table_slide(slide, ["Group", "Players", "Owned position", "VLU response"], [
        ["Public prestige", "UEH / NEU / FTU", "Affordable degree + alumni scale", "Do not price-fight"],
        ["Foreign premium", "RMIT", "Australian credential", "Out-specialize"],
        ["Policy elite", "Fulbright", "Policy leadership", "Avoid policy lane"],
        ["Flexible private", "FSB", "Corporate convenience", "Build deeper vertical proof"],
        ["Group 5", "VLU", "Niche premium applied verticals", "Own Family + Healthcare"],
    ], font_size=8)

    slide = new_slide("Lessons From 6 Markets")
    add_table_slide(slide, ["Market", "Steal", "Do not copy"], [
        ["China", "Network-as-product", "Billionaire/status claims without proof"],
        ["Australia", "Fast-track + capstone", "PR-pathway revenue logic"],
        ["India", "SPJIMR 6-day/month; ISB one-year", "Placement promise for Family Academy"],
        ["Singapore", "Brand stack discipline", "Global mobility claims VLU cannot prove"],
        ["Malaysia", "Private mid-tier affordability", "Online-only commodity MBA"],
        ["Indonesia", "Family business peer-market play", "Loose executive-ed without credential path"],
    ], font_size=8)

    for stack, role, bullets in [
        ("The Triple-Stack", "Wedge + Anchor + Halo", ["Family Academy builds distinct category ownership.", "Healthcare MBA scales with VLU's real Y + Business + Design capability.", "Membership compounds alumni, data and short-course revenue."]),
        ("Family Academy", "Primary wedge", ["Target gen-2/3 successors and gen-1 sponsors.", "15-month modular: 6 days/month, no placement service.", "Capstone: Family Constitution + succession roadmap + growth initiative."]),
        ("Healthcare MBA", "Portfolio anchor", ["12-month intensive + 3-month live-client capstone.", "Hospital/pharma/MedTech cohort; $12k/$18k/$30k pricing.", "Proof requires named partner projects, not generic cases."]),
        ("Lifelong Membership", "Network halo", ["Embed alumni access in tuition; upsell annual membership.", "Use off-shelf AI tools first; custom platform only after demand proof.", "Annual reports create data moat and acquisition engine."]),
    ]:
        slide = new_slide(stack, role)
        add_bullets(slide, 0.8, 1.55, 8.2, 4.8, bullets, size=17)

    family_slides = [
        ("Family Academy Positioning", ["Vietnam's school of choice for family-business successors.", "Buyer is often gen-1 founder; user is gen-2 heir.", "Confidential peer cohort is the product, curriculum is the delivery system."]),
        ("Family Academy Format", ["6 days/month copied from SPJIMR logic.", "15 months: 12 months modules + 3 months capstone/advisory.", "Cohort 20-25 first year to protect intimacy and selection."]),
        ("Family Academy Pricing", ["Mary's lean: $15k Good, $20k Better, $35k Best.", "Original $12k entry risks weak premium signal.", "Parity $20k/$30k/$50k only after Cohort 2 proof and advisory board credibility."]),
        ("Family Academy Financials", ["Y1 revenue: $330k; Y3 revenue: $1.5M.", "Y0 budget should be gate-based: legal, director, advisory board, pre-sell.", "Breakout depends on annual State of VN Family Business report."]),
        ("Family Academy 12-Month Rollout", ["M1-M3: capability/legal audit + founder dinners.", "M4-M6: pricing test, director, curriculum.", "M7-M12: recruit, partner, publish, Board launch checkpoint."]),
    ]
    for title, bullets in family_slides:
        slide = new_slide(title)
        add_bullets(slide, 0.8, 1.55, 8.2, 4.8, bullets, size=17)

    healthcare_slides = [
        ("Healthcare MBA Positioning", ["Not a generic MBA with healthcare electives.", "A management program for people operating hospitals, pharma, MedTech and insurance.", "VLU's Y + Business + Design combination is the capability moat."]),
        ("Healthcare MBA Format", ["12-month fast-track plus 3-month capstone beats 18-month friction.", "65% VLU campus, 35% hospital/partner site.", "Faculty mix: 40% academic, 60% practitioner."]),
        ("Healthcare MBA Financials", ["Y1 revenue: $450k; Y3 revenue: $2.04M.", "Needs 8 partner LOIs before launch.", "Capstone outcomes become the placement-equivalent proof point."]),
    ]
    for title, bullets in healthcare_slides:
        slide = new_slide(title)
        add_bullets(slide, 0.8, 1.55, 8.2, 4.8, bullets, size=17)

    slide = new_slide("Defensibility Framework")
    add_table_slide(slide, ["Program", "Network", "Capability", "Switching", "Brand", "Data", "Total"], [
        ["Family Academy", "5", "4", "4", "5", "4", "22/25"],
        ["Healthcare MBA", "4", "5", "4", "4", "4", "21/25"],
        ["Membership", "5", "3", "4", "3", "4", "19/25"],
    ], font_size=11)

    slide = new_slide("3-Year P&L")
    slide.shapes.add_picture(str(ASSET_DIR / "triple_stack_revenue.png"), Inches(0.9), Inches(1.45), width=Inches(8.2))

    slide = new_slide("Pricing Recommendation")
    slide.shapes.add_picture(str(ASSET_DIR / "pricing_scenario.png"), Inches(0.9), Inches(1.45), width=Inches(8.2))

    slide = new_slide("Risks + Mitigations")
    add_table_slide(slide, ["Risk", "Mitigation"], [
        ["Demand not payment-ready", "10-deposit pre-sell gate before public launch"],
        ["No credible director", "External hire or interim advisory chair before launch"],
        ["Weak capstone supply", "Named partner LOIs with project owners"],
        ["Regulatory delay", "Certificate/executive bridge while degree approval matures"],
    ], font_size=10)

    slide = new_slide("12-Month Execution Plan")
    add_table_slide(slide, ["Phase", "Months", "Output"], [
        ["Foundation", "M1", "Capability audit, legal path, target list"],
        ["Validation", "M2-M4", "Founder dinners, hospital LOIs, pricing test"],
        ["Build", "M5-M7", "Director, curriculum, faculty, report outline"],
        ["Launch readiness", "M8-M12", "Admissions funnel, capstone briefs, Board checkpoint"],
    ], font_size=11)

    slide = new_slide("Investment Ask")
    add_textbox(slide, 0.85, 1.7, 8.2, 0.8, "Approve Y0 capability build, not blind full launch.", size=25, bold=True, color=ACCENT, align=PP_ALIGN.CENTER)
    add_bullets(slide, 1.1, 2.8, 7.5, 2.8, ["Gross Y0 envelope: $150k for director, legal, research center, partner BD.", "Required gates: 10 Family Academy deposits/LOIs, 8 healthcare capstone LOIs, advisory board chair.", "Decision required: commit VLU to Group 5 niche premium applied verticals."], size=17)

    for title, bullets in [
        ("Appendix: 6-Layer Matrix", ["Excel workbook contains 36-program catalog and heat map.", "R2 raw files remain source of full China/Australia/India/Singapore detail.", "R3 adds Malaysia/Indonesia and VN competitors."]),
        ("Appendix: Steal-List", ["SPJIMR modular 6-day/month format.", "ISB/IIM one-year fast-track economics.", "Research center as publishing engine.", "Named live-client capstone as moat."]),
        ("Appendix: Sources", ["Official program pages and tuition pages are listed in Excel and HTML.", "Regulatory sources include MOET Circular 23/2021, Circular 07/2025, Decree 219/2025.", "AACSB process and fees from official AACSB pages."]),
    ]:
        slide = new_slide(title)
        add_bullets(slide, 0.8, 1.55, 8.2, 4.8, bullets, size=17)

    prs.save(PPTX_PATH)


def verify_outputs() -> None:
    assert HTML_PATH.exists() and HTML_PATH.stat().st_size > 50_000, HTML_PATH
    assert PPTX_PATH.exists() and PPTX_PATH.stat().st_size > 20_000, PPTX_PATH
    assert XLSX_PATH.exists() and XLSX_PATH.stat().st_size > 20_000, XLSX_PATH
    html_text = HTML_PATH.read_text(encoding="utf-8")
    assert "Chart.js" not in html_text
    assert "https://cdn" not in html_text
    assert "--sidebar-w: 300px" in html_text
    wb = load_workbook(XLSX_PATH, read_only=True)
    expected = {
        "README",
        "Programs Catalog",
        "Pricing Comparables",
        "6-Layer Matrix",
        "Course DNA Comparison",
        "VLU Triple-Stack Scorecards",
        "3-Year Financial Model",
        "12-Month Execution Plan",
        "Risk Register",
        "Decision Log",
    }
    assert expected.issubset(set(wb.sheetnames))
    assert len(PROGRAMS) == 36
    wb.close()


def main() -> None:
    RESEARCH_DIR.mkdir(parents=True, exist_ok=True)
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    build_charts()
    build_html()
    build_excel()
    build_pptx()
    verify_outputs()
    print(f"Wrote {HTML_PATH}")
    print(f"Wrote {PPTX_PATH}")
    print(f"Wrote {XLSX_PATH}")


if __name__ == "__main__":
    main()
