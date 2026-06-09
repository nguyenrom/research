#!/usr/bin/env python3
"""Scrape codeai.zone/blog into Docs/codeai/ as standalone HTML files."""
from __future__ import annotations

import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

BASE = "https://codeai.zone"
OUT = Path(__file__).resolve().parent.parent / "Docs" / "codeai"
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

POSTS = [
    ("150dsa-ep1-array-hashing-contains-duplicate-ver1", 'Phá đảo 150 DSA Tập 1 - Arrays & Hashing: Contains Duplicate', "2026-04-12", ["Data Structures", "Algorithms"]),
    ("summary-atomic-habits", 'Tóm tắt sách "Atomic Habits - Thói Quen Nguyên Tử"', "2026-03-14", ["Book Summary", "Knowledge"]),
    ("summary-elon-musk-the-quest", 'Tóm tắt sách "Elon Musk: Tesla, SpaceX và sứ mệnh..."', "2026-03-13", ["Book Summary", "Technical"]),
    ("grand-slam-offer", 'GRAND SLAM OFFER - Tóm tắt từ "$100M Offers"', "2026-03-11", ["Startup", "Business", "Sales"]),
    ("dsa-ep11-data-structures-linear-node-circular-linked-list", "Data Structures & Algorithms - Tập 11: Circular Linked List", "2026-03-10", ["Data Structures", "Algorithms"]),
    ("dsa-ep10-data-structures-linear-node-doubly-linked-list", "Data Structures & Algorithms - Tập 10: Doubly Linked List", "2026-03-06", ["Data Structures", "Algorithms"]),
    ("dsa-ep9-data-structures-linear-node-singly-linked-list", "Data Structures & Algorithms - Tập 9: Singly Linked List", "2026-03-03", ["Data Structures", "Algorithms"]),
    ("summary-hard-thing-hard-things", 'Tóm tắt sách "The Hard Thing About Hard Things"', "2026-03-02", ["Business", "Startup", "SaaS"]),
    ("summary-effective-data-analysis", 'Tóm tắt sách "Effective Data Analysis"', "2026-02-28", ["Data Analyst", "Data Science", "Book Summary"]),
    ("reverse-engineering", "Reverse Engineering là gì?", "2026-02-27", ["Technical", "Knowledge"]),
    ("anthropic-agentic-coding-trends-report-2026", "Báo cáo xu hướng Agentic Coding năm 2026 từ Anthropic", "2026-02-25", ["AI Agents", "Productivity"]),
    ("summary-introduction-to-machine-learning", "Giới thiệu về Machine Learning", "2026-02-25", ["AI", "Machine Learning", "Book Summary"]),
    ("dsa-ep8-data-structures-linear-array-circular-buffer", "Data Structures & Algorithms - Tập 8: Circular Buffer", "2026-02-24", ["Data Structures", "Algorithms"]),
    ("summary-the-design-everyday", 'Tóm tắt sách "The Design of Everyday Things"', "2026-02-22", ["Book Summary", "Design", "UX", "UI"]),
    ("summary-the-embedded-entrepreneur", 'Tóm tắt sách "THE EMBEDDED ENTREPRENEUR"', "2026-02-22", ["Book Summary", "Productivity", "SaaS", "Software Development"]),
    ("summary-thinking-in-system", 'Tóm tắt sách "Thinking in System"', "2026-02-20", ["Book Summary", "Productivity", "Learning Method", "Psychology"]),
    ("dsa-ep7-data-structures-linear-array-matrix-2d-array", "Data Structures & Algorithms - Tập 7: Matrix & 2D Array", "2026-02-19", ["Data Structures", "Algorithms"]),
    ("summary-inspired-marty-cagan", 'Tóm tắt sách "INSPIRED" của tác giả Marty Cagan', "2026-02-15", ["Book Summary", "SaaS", "Software Development"]),
    ("curse-of-knowledge", "Lời Nguyền Tri Thức (Curse of Knowledge)", "2026-02-14", ["Psychology", "Learning Method"]),
    ("python-object-oriented-programming", "Lập trình hướng đối tượng (OOP)", "2026-02-13", ["Programming", "Python"]),
    ("dsa-ep6-data-structures-linear-array-dynamic-array", "Data Structures & Algorithms - Tập 6: Dynamic Array", "2026-02-12", ["Data Structures", "Algorithms"]),
    ("dsa-ep5-data-structures-linear-array-string", "Data Structures & Algorithms - Tập 5: String", "2026-02-11", ["Data Structures", "Algorithms"]),
    ("dsa-ep4-data-structures-linear-array-array", "Data Structures & Algorithms - Tập 4: Array", "2026-02-10", ["Data Structures", "Algorithms"]),
    ("dsa-ep3-complex-analyze-space-complex", "Data Structures & Algorithms - Tập 3: Space Complexity", "2026-02-09", ["Data Structures", "Algorithms"]),
    ("dsa-ep1-complex-analyze-big-o-notation", "Data Structures & Algorithms - Tập 1: Big O Notation", "2026-02-06", ["Computer Science", "Comic", "Data Structures", "Algorithms"]),
    ("dsa-ep2-complex-analyze-time-complex", "Data Structures & Algorithms - Tập 2: Time Complexity", "2026-02-06", ["Data Structures", "Algorithms"]),
    ("saas-ep6-code-review", "VIBE CODERS | Software Development & SaaS Tập 6", "2026-02-06", ["SaaS", "Software Development"]),
    ("summary-algorithms-to-live-by-brian-christian", 'Tóm tắt sách "Algorithms to Live By" của Brian Christian', "2026-02-05", ["Algorithms", "Book Summary"]),
    ("how-ai-impacts-skill-formation", "Năng suất không đại diện cho sự tinh thông", "2026-02-02", ["Research", "Productivity", "Learning Method"]),
    ("interview-joel-david-hamkins-godel", "Godel - Định lý Bất toàn (Incompleteness Theorems)", "2026-02-01", ["Mathematic", "Computer Science"]),
    ("agent-skill-with-anthropic", "Hướng dẫn về Agent Skills", "2026-01-31", ["Agent Skills", "Prompt Engineering", "Vibe Coding"]),
    ("grani-markov-chain", "Thuật toán Markov Chain", "2026-01-30", ["Algorithm", "Comic"]),
    ("interview-moltbot-aka-clawdbot-creator", "Phỏng vấn CEO Moltbot aka Clawdbot, OpenClaw", "2026-01-30", ["Interview", "AI Agents"]),
    ("grani-game-theory", "Game Theory: Lý Thuyết Trò Chơi", "2026-01-24", ["Algorithm", "Computer Science", "Comic"]),
    ("saas-ep5-traffic-jam", "VIBE CODERS | Software Development & SaaS Tập 5", "2026-01-20", ["Software Development", "SaaS"]),
    ("just-in-time-learning", "Học tập Đúng lúc (Just-In-Time Learning)", "2026-01-19", ["Learning Method", "Psychology"]),
    ("swe-google", 'Tóm tắt sách "Software Engineering at Google"', "2026-01-18", ["Software Engineering", "Programming", "Book Summary"]),
    ("genius-mind-os", 'Não của những kẻ "xuất chúng" có gì?', "2026-01-17", ["Learning Method", "Psychology"]),
    ("anthropic-how-ai-think", "Interpretability: AI suy nghĩ như thế nào?", "2026-01-15", ["AI", "LLMs", "Psychology"]),
    ("elon-musk-agi", "Phỏng vấn Elon Musk về Tương lai Nhân loại", "2026-01-14", ["Interview", "AI", "LLMs"]),
    ("reddit-tutorial-hell", "Tôi nhận ra mình không biết gì về lập trình", "2026-01-14", ["Programming", "Reddit", "Learning Method"]),
    ("replit-ceo-interview", "Phỏng vấn CEO Replit về Vibe Coding", "2026-01-13", ["Vibe Coding", "Interview", "Programming"]),
    ("phd-learning-method", "Học như một nghiên cứu sinh PhD", "2026-01-12", ["Learning Method", "Psychology"]),
    ("git-easy", "GIT thật đơn giản", "2026-01-11", ["Programming", "Git"]),
    ("timeless-programming-skills", 'Kỹ năng lập trình "Bền Vững"', "2026-01-10", ["Programming", "Reddit"]),
    ("boris-claude-setup", "13 Bước Thiết Lập Claude Code từ Boris Cherny", "2026-01-09", ["Claude Code", "Vibe Coding", "Programming"]),
    ("trust-the-process", "Trust The Process", "2026-01-07", ["Learning Method", "Productivity"]),
    ("summary-refactoring-ui-carousel", 'Tóm tắt sách "Refactoring UI"', "2026-01-06", ["UI", "UX", "Web Development"]),
    ("boris-cherny-claude-code", "Boris Cherny - bộ não đứng sau Claude Code", "2026-01-05", ["Claude Code", "Vibe Coding"]),
    ("500k-codes", "TÔI ĐÃ VIẾT 500.000 DÒNG CODE VỚI AI", "2026-01-04", ["Programming", "Vibe Coding"]),
    ("titan-5-pinterest", "TITANS Tập 5 - PINTEREST", "2026-01-03", ["SaaS", "Pinterest"]),
    ("6-thinking-hats", "6 chiếc mũ tư duy trong vận hành team phát triển phần mềm", "2026-01-01", ["SaaS", "Software Development"]),
    ("code-ai-campaign", "Hành trình 14 ngày tạo nên Code AI Blog", "2025-12-31", ["Programming", "Vibe Coding"]),
    ("karpathy-pivot", "Andrej Karpathy - Cuộc ĐẠI TÁI THIẾT của AI trong lập trình", "2025-12-28", ["Vibe Coding", "Programming", "Software Development"]),
    ("summary-domain-driven-design", 'Tóm tắt sách "Domain Driven Design" của Eric Evans', "2025-12-28", ["Book Summary", "Programming"]),
    ("saas-ep4-tech-debt", "VIBE CODERS | Software Development & SaaS Tập 4", "2025-12-27", ["SaaS", "Software Development"]),
    ("unknown-unknowns", "Bạn kém cỏi hơn bạn nghĩ - Unknown Unknowns", "2025-12-26", ["Learning Method", "Psychology"]),
    ("marketing-to-dev", "Chia sẻ kinh nghiệm tự học CODE cho dân trái ngành", "2025-12-25", ["Learning Method", "Programming", "Vibe Coding"]),
    ("teresa-torres-claude-code", "Tự Động Hoá Cuộc Sống Bằng Claude Code", "2025-12-24", ["Claude Code", "Productivity", "Obsidian"]),
    ("how-to-fix-any-bug", "Kỹ thuật Vibe Debugging của Dan Abramov", "2025-12-23", ["Vibe Coding", "Programming"]),
    ("obsidian-ceo-notes", "Kinh nghiệm quản lý tri thức cá nhân từ CEO Obsidian", "2025-12-21", ["Obsidian", "Learning Method"]),
    ("10-years-code", 'Điều gì vẫn khiến tôi "Kinh Ngạc" sau 10 Năm Code?', "2025-12-19", ["Programming", "Software Development", "Reddit"]),
    ("titan-4-amazon", "TITANS Tập 4 - AMAZON", "2025-12-18", ["Amazon", "SaaS"]),
    ("bloom-aesthetic-dark", "Bloom's Taxonomy Trong Giáo Dục", "2025-12-17", ["Learning Method", "Psychology"]),
    ("google-cloud-console-ver2", "Google Cloud Console cho VIBE-CODERS (ver 2)", "2025-12-17", ["Google Cloud Console", "Tutorial"]),
    ("9-claude-code-tips", '9 PRO TIPS ĐỂ "THUẦN HÓA" CLAUDE CODE', "2025-12-15", ["Claude", "Claude Code", "Reddit"]),
    ("the-way-of-code", "The Way Of Code (Tiếng Việt)", "2025-12-14", ["Book Summary", "Vibe Coding", "Programming"]),
    ("astro-web-dev-blog", "Astro - Framework tối ưu cho dự án Blog", "2025-12-08", ["Astro", "Web Development"]),
    ("saas-ep1-introduction", "VIBE CODERS | Software Development & SaaS Tập 1", "2025-12-07", ["SaaS", "Software Development"]),
    ("claude-code-commands", "Claude Code Commands (Tổng Hợp)", "2025-12-06", ["Claude Code", "Tutorial"]),
    ("clean-architecture", 'Tóm tắt sách "Clean Architecture"', "2025-12-06", ["Programming", "Book Summary"]),
    ("summary-the-art-of-asking", 'Tóm tắt sách "The Art of Asking Essential Questions"', "2025-12-06", ["Book Summary", "Psychology"]),
    ("summary-thinking-fast-slow", 'Tóm tắt sách "Tư Duy Nhanh Và Chậm"', "2025-12-06", ["Book Summary", "Psychology"]),
]


def http_get(url: str, binary: bool = False) -> bytes | str | None:
    for attempt in range(3):
        try:
            r = requests.get(url, headers=HEADERS, timeout=30)
            if r.status_code == 200:
                return r.content if binary else r.text
            if r.status_code == 404:
                return None
        except requests.RequestException as e:
            print(f"  retry {attempt+1} for {url}: {e}", file=sys.stderr)
            time.sleep(1 + attempt)
    return None


def safe_filename(url: str) -> str:
    """Strip query/hash, return last segment."""
    p = urlparse(url)
    name = p.path.rstrip("/").rsplit("/", 1)[-1]
    return re.sub(r'[^\w.\-]', '_', name) or "file"


def asset_kind(url: str) -> str:
    """Return one of: css, js, fonts, other."""
    p = urlparse(url).path.lower()
    if p.endswith(".css"):
        return "css"
    if p.endswith((".js", ".mjs")):
        return "js"
    if p.endswith((".woff", ".woff2", ".ttf", ".otf", ".eot")):
        return "fonts"
    return "other"


def download_asset(url: str, cache: dict, base_post_dir: Path = None) -> str | None:
    """Download a shared asset; return relative path for use in HTML."""
    if url in cache:
        return cache[url]
    full = urljoin(BASE, url)
    data = http_get(full, binary=True)
    if data is None:
        cache[url] = url  # leave as-is
        return url
    kind = asset_kind(url)
    fname = safe_filename(url)
    target_dir = OUT / kind
    target_dir.mkdir(parents=True, exist_ok=True)
    # avoid name clashes
    target = target_dir / fname
    if target.exists() and target.read_bytes() != data:
        stem, dot, ext = fname.rpartition(".")
        i = 1
        while target.exists():
            target = target_dir / f"{stem}-{i}.{ext}"
            i += 1
    target.write_bytes(data)
    rel = f"{kind}/{target.name}"
    cache[url] = rel
    # Rewrite font URLs inside CSS to point at local fonts/
    if kind == "css":
        try:
            txt = data.decode("utf-8", errors="ignore")
            new_txt, font_map = rewrite_css(txt, full, cache)
            target.write_text(new_txt, encoding="utf-8")
        except Exception as e:
            print(f"  css rewrite failed for {url}: {e}", file=sys.stderr)
    return rel


CSS_URL_RE = re.compile(r'url\(\s*["\']?([^"\')]+)["\']?\s*\)')


def rewrite_css(css: str, css_url: str, cache: dict) -> tuple[str, dict]:
    """Inline font references in a CSS file: download them and rewrite as ../fonts/x."""
    font_map = {}

    def repl(m):
        ref = m.group(1).strip()
        if ref.startswith("data:") or ref.startswith("#"):
            return m.group(0)
        absurl = urljoin(css_url, ref)
        # only fetch our own host
        if urlparse(absurl).netloc and urlparse(absurl).netloc not in ("codeai.zone", "www.codeai.zone"):
            return m.group(0)
        kind = asset_kind(absurl)
        if kind == "fonts":
            rel = download_asset(absurl, cache)
            if rel and rel.startswith("fonts/"):
                # css file is at css/x.css; reference fonts/ as ../fonts/...
                return f'url("../{rel}")'
        elif kind == "other":
            rel = download_asset(absurl, cache)
            if rel:
                return f'url("../{rel}")'
        return m.group(0)

    return CSS_URL_RE.sub(repl, css), font_map


def download_post_image(img_url: str, slug: str) -> str:
    """Download an image into images/{slug}/; return relative path."""
    full = urljoin(BASE, img_url)
    data = http_get(full, binary=True)
    if data is None:
        return img_url
    dest_dir = OUT / "images" / slug
    dest_dir.mkdir(parents=True, exist_ok=True)
    fname = safe_filename(img_url)
    target = dest_dir / fname
    target.write_bytes(data)
    return f"images/{slug}/{fname}"


def process_post(slug: str, title: str, date: str, cats: list[str], asset_cache: dict) -> dict | None:
    url = f"{BASE}/blog/{slug}"
    print(f"[+] {slug}")
    html = http_get(url)
    if not html:
        print(f"  FAILED to fetch {url}", file=sys.stderr)
        return None
    soup = BeautifulSoup(html, "lxml")

    # Extract the main <article> (the post body)
    article = soup.find("article")
    if not article:
        print(f"  no <article> in {slug}", file=sys.stderr)
        return None

    # Remove "Back to Blog" navigation and newsletter form & footer pieces inside main
    for sel in [
        'a[href="/blog"]',
        "#newsletter-form",
    ]:
        for el in article.select(sel):
            el.decompose()
    # Remove newsletter section (the form wrapper)
    for sec in article.find_all("section"):
        if sec.find("form", id="newsletter-form") or "newsletter" in (sec.get("class") and " ".join(sec.get("class")) or "").lower():
            sec.decompose()

    # Find description text near header
    h1 = article.find("h1")
    subtitle_el = h1.find_next("p") if h1 else None
    subtitle = subtitle_el.get_text(strip=True) if subtitle_el else ""

    # Process images inside the article
    cover_local = None
    for img in article.find_all("img"):
        src = img.get("src") or ""
        if not src:
            continue
        if src.startswith("/blog/") or src.startswith(f"{BASE}/blog/"):
            local = download_post_image(src, slug)
            img["src"] = local
            if cover_local is None:
                cover_local = local
        else:
            local = download_asset(src, asset_cache)
            if local:
                img["src"] = local

    # Process linked stylesheets and module scripts in <head>
    head = soup.find("head")
    asset_links_html = []
    if head:
        for link in head.find_all("link", rel="stylesheet"):
            href = link.get("href")
            if href:
                rel = download_asset(href, asset_cache)
                link["href"] = rel
        for link in head.find_all("link", rel="preload"):
            href = link.get("href")
            if href and link.get("as") in ("font", "style"):
                rel = download_asset(href, asset_cache)
                if rel:
                    link["href"] = rel
        for script in head.find_all("script", src=True):
            src = script["src"]
            if src.startswith("http") and "codeai.zone" not in src:
                # external analytics - drop
                script.decompose()
                continue
            rel = download_asset(src, asset_cache)
            if rel:
                script["src"] = rel

    # Build standalone HTML page using just the article
    inline_head_style = ""
    if head:
        for tag in head.find_all("style"):
            inline_head_style += tag.decode_contents() + "\n"

    css_links = ""
    if head:
        for link in head.find_all("link", rel="stylesheet"):
            css_links += str(link) + "\n"
        for link in head.find_all("link", rel="preload"):
            if link.get("as") == "font":
                css_links += str(link) + "\n"

    article_html = str(article)

    page = f"""<!DOCTYPE html>
<html lang="vi" class="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Code AI (mirror)</title>
<meta name="description" content="{subtitle}">
{css_links}
<style>{inline_head_style}</style>
<style>
  body {{ background:#18181b; color:#f4f4f5; font-family: 'Space Grotesk', system-ui, sans-serif; max-width: 64rem; margin: 0 auto; padding: 2.5rem 1.5rem; min-height: 100vh; }}
  .topbar {{ display:flex; justify-content:space-between; align-items:center; margin-bottom:2rem; padding-bottom:1rem; border-bottom:1px solid #27272a; }}
  .topbar a {{ color:#a1a1aa; text-decoration:none; font-size:.875rem; }}
  .topbar a:hover {{ color:#f4f4f5; }}
  .logo {{ font-size:1.5rem; font-weight:600; letter-spacing:-0.05em; }}
  .logo i {{ color:#52525b; font-style:italic; }}
  .meta-footer {{ margin-top:3rem; padding-top:1.5rem; border-top:1px solid #27272a; color:#71717a; font-size:.75rem; text-align:center; }}
</style>
</head>
<body>
<header class="topbar">
  <a href="index.html"><span class="logo">CODE<i>_AI_</i></span></a>
  <a href="index.html">← Quay lại danh sách bài viết</a>
</header>
<main>
{article_html}
</main>
<footer class="meta-footer">
  <p>Bản lưu trữ local của <a href="{url}" style="color:#a1a1aa">{url}</a></p>
  <p>© Code AI — mirrored for offline reading</p>
</footer>
</body>
</html>
"""
    (OUT / f"{slug}.html").write_text(page, encoding="utf-8")
    return {
        "slug": slug,
        "title": title,
        "date": date,
        "categories": cats,
        "subtitle": subtitle,
        "cover": cover_local or "",
    }


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    asset_cache: dict[str, str] = {}
    results = []
    # Sequential to be respectful (and asset_cache is shared)
    for slug, title, date, cats in POSTS:
        try:
            info = process_post(slug, title, date, cats, asset_cache)
            if info:
                results.append(info)
        except Exception as e:
            print(f"  ERROR on {slug}: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc(file=sys.stderr)
    # Persist a JSON manifest the index generator will consume
    (OUT / "posts.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nDone. {len(results)}/{len(POSTS)} posts saved.")


if __name__ == "__main__":
    main()
