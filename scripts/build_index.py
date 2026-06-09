#!/usr/bin/env python3
"""Generate Docs/codeai/index.html from posts.json."""
import json
import html
from pathlib import Path
from collections import Counter

OUT = Path(__file__).resolve().parent.parent / "Docs" / "codeai"


def main():
    posts = json.loads((OUT / "posts.json").read_text(encoding="utf-8"))
    posts.sort(key=lambda p: p["date"], reverse=True)

    cat_counts = Counter()
    for p in posts:
        for c in p["categories"]:
            cat_counts[c] += 1

    def card(p):
        title = html.escape(p["title"])
        subtitle = html.escape(p.get("subtitle", ""))
        date = p["date"]
        slug = p["slug"]
        cover = html.escape(p.get("cover") or "")
        cats = p["categories"]
        cat_chips = "".join(f'<span class="chip">{html.escape(c)}</span>' for c in cats)
        cover_html = (
            f'<div class="cover"><img src="{cover}" alt="" loading="lazy"></div>'
            if cover
            else '<div class="cover empty"></div>'
        )
        return f"""<article class="card" data-title="{title.lower()}">
  <a class="card-link" href="{slug}.html">
    {cover_html}
    <div class="body">
      <div class="chips">{cat_chips}</div>
      <h2>{title}</h2>
      <p class="subtitle">{subtitle}</p>
      <p class="date"><time datetime="{date}">{date}</time></p>
    </div>
  </a>
</article>"""

    cards_html = "\n".join(card(p) for p in posts)

    out = f"""<!DOCTYPE html>
<html lang="vi" class="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Code AI — Blog Archive (mirror)</title>
<meta name="description" content="Bản lưu trữ offline của blog codeai.zone — {len(posts)} bài viết.">
<style>
  :root {{
    --bg: #18181b;
    --bg-2: #1f1f23;
    --bg-3: #27272a;
    --fg: #f4f4f5;
    --fg-2: #a1a1aa;
    --fg-3: #71717a;
    --accent: #fbbf24;
    --border: #2e2e33;
  }}
  * {{ box-sizing: border-box; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    margin: 0;
    background: var(--bg);
    color: var(--fg);
    font-family: 'Space Grotesk', system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    line-height: 1.5;
  }}
  .container {{ max-width: 80rem; margin: 0 auto; padding: 2rem 1.5rem 6rem; }}

  /* Header */
  header.site {{
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 3rem 1rem 2rem;
    text-align: center;
  }}
  .logo {{
    font-size: clamp(2.5rem, 6vw, 4.5rem);
    font-weight: 400;
    letter-spacing: -0.06em;
    color: var(--fg);
    margin: 0;
  }}
  .logo i {{ font-style: italic; color: #52525b; font-weight: 300; }}
  .tagline {{
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--fg-3);
    margin-top: 0.5rem;
  }}
  .lead {{
    color: var(--fg-2);
    max-width: 36rem;
    text-align: center;
    margin: 1.5rem auto 0;
    font-size: 0.95rem;
  }}
  .stats {{
    display: flex;
    gap: 2rem;
    justify-content: center;
    margin-top: 1.5rem;
    color: var(--fg-3);
    font-size: 0.85rem;
  }}
  .stats b {{ color: var(--accent); font-weight: 600; }}

  /* Grid (desktop) */
  .grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(20rem, 1fr));
    gap: 1.25rem;
    margin-top: 2rem;
  }}
  .card {{
    background: var(--bg-2);
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
    transition: transform .2s, border-color .2s, background .2s;
  }}
  .card:hover {{
    transform: translateY(-3px);
    border-color: #52525b;
    background: #222226;
  }}
  .card-link {{ color: inherit; text-decoration: none; display: block; height: 100%; }}
  .cover {{
    aspect-ratio: 16 / 10;
    background: linear-gradient(135deg, #27272a, #18181b);
    overflow: hidden;
  }}
  .cover img {{
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform .4s;
  }}
  .card:hover .cover img {{ transform: scale(1.04); }}
  .cover.empty {{ background: repeating-linear-gradient(45deg, #27272a 0 12px, #1f1f23 12px 24px); }}

  .body {{ padding: 1rem 1.1rem 1.2rem; }}
  .chips {{ display: flex; flex-wrap: wrap; gap: 0.3rem; margin-bottom: 0.55rem; }}
  .chip {{
    background: var(--bg-3);
    color: var(--fg-2);
    font-size: 0.65rem;
    padding: 0.18rem 0.55rem;
    border-radius: 9999px;
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }}
  h2 {{
    font-size: 1.05rem;
    line-height: 1.3;
    color: var(--fg);
    margin: 0 0 0.4rem;
    font-weight: 600;
  }}
  .subtitle {{
    color: var(--fg-2);
    font-size: 0.85rem;
    margin: 0 0 0.7rem;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }}
  .date {{
    color: var(--fg-3);
    font-size: 0.75rem;
    margin: 0;
    font-variant-numeric: tabular-nums;
  }}

  .hidden {{ display: none !important; }}
  .empty-state {{
    color: var(--fg-3);
    text-align: center;
    padding: 4rem 1rem;
    font-size: 0.9rem;
    grid-column: 1 / -1;
  }}

  footer.site {{
    margin-top: 4rem;
    padding: 2rem 1rem;
    text-align: center;
    color: var(--fg-3);
    font-size: 0.75rem;
    border-top: 1px solid var(--border);
  }}
  footer.site a {{ color: var(--fg-2); }}

  /* Floating action buttons (back-to-top + search) */
  .fab-stack {{
    position: fixed;
    right: 1.25rem;
    bottom: 1.25rem;
    display: flex;
    flex-direction: column;
    gap: 0.65rem;
    z-index: 50;
    align-items: flex-end;
  }}
  .fab {{
    width: 2.75rem;
    height: 2.75rem;
    border-radius: 9999px;
    background: var(--bg-2);
    border: 1px solid var(--border);
    color: var(--fg);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 6px 20px rgba(0,0,0,.45);
    transition: opacity .2s, transform .2s, background .15s, border-color .15s;
    font-family: inherit;
    padding: 0;
  }}
  .fab:hover {{ background: #2a2a2f; border-color: #52525b; }}
  .fab svg {{ width: 1.1rem; height: 1.1rem; stroke: currentColor; fill: none; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }}
  .fab.hidden-fab {{ opacity: 0; pointer-events: none; transform: translateY(0.5rem); }}

  /* Search popover */
  .search-pop {{
    position: fixed;
    right: 1.25rem;
    bottom: 5.5rem;
    background: var(--bg-2);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 0.65rem;
    box-shadow: 0 12px 32px rgba(0,0,0,.55);
    z-index: 49;
    display: none;
    width: min(22rem, calc(100vw - 2.5rem));
  }}
  .search-pop.open {{ display: block; }}
  .search-pop input {{
    width: 100%;
    background: var(--bg-3);
    border: 1px solid var(--border);
    color: var(--fg);
    padding: 0.6rem 0.85rem;
    border-radius: 9999px;
    font-size: 0.9rem;
    outline: none;
    font-family: inherit;
  }}
  .search-pop input:focus {{ border-color: var(--accent); }}
  .search-pop .count {{
    color: var(--fg-3);
    font-size: 0.7rem;
    margin: 0.5rem 0.25rem 0.1rem;
  }}

  /* Mobile: list view, image left / content right */
  @media (max-width: 640px) {{
    .container {{ padding: 1.5rem 1rem 6rem; }}
    .grid {{
      grid-template-columns: 1fr;
      gap: 0.75rem;
    }}
    .card-link {{
      display: grid;
      grid-template-columns: 7.5rem 1fr;
      gap: 0;
      align-items: stretch;
    }}
    .cover {{
      aspect-ratio: 1 / 1;
      height: 100%;
      min-height: 7rem;
    }}
    .body {{ padding: 0.75rem 0.9rem; }}
    .chips {{ margin-bottom: 0.35rem; }}
    .chip {{ font-size: 0.6rem; padding: 0.12rem 0.45rem; }}
    h2 {{
      font-size: 0.92rem;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      margin-bottom: 0.3rem;
    }}
    .subtitle {{
      font-size: 0.75rem;
      -webkit-line-clamp: 2;
      margin-bottom: 0.4rem;
    }}
    .date {{ font-size: 0.68rem; }}
    .card:hover {{ transform: none; }}
    .fab-stack {{ right: 0.9rem; bottom: 0.9rem; }}
  }}
</style>
</head>
<body>
  <header class="site">
    <h1 class="logo">CODE<i>_AI_</i></h1>
    <p class="tagline">Music Producer + Programmer = Vibe-Coder</p>
    <p class="lead">Bản lưu trữ offline của blog <a href="https://codeai.zone/blog" style="color:var(--accent)">codeai.zone/blog</a>. Tất cả nội dung thuộc về tác giả gốc.</p>
    <div class="stats">
      <span><b>{len(posts)}</b> bài viết</span>
      <span><b>{len(cat_counts)}</b> chủ đề</span>
    </div>
  </header>

  <main class="container">
    <div class="grid" id="grid">
      {cards_html}
      <p class="empty-state hidden" id="empty">Không có bài viết nào khớp.</p>
    </div>
  </main>

  <footer class="site">
    <p>Generated {len(posts)} posts &mdash; mirrored from <a href="https://codeai.zone/blog">codeai.zone/blog</a></p>
  </footer>

  <!-- Floating search popover (above the FAB stack) -->
  <div class="search-pop" id="searchPop" role="search">
    <input id="search" type="search" placeholder="Tìm theo tiêu đề..." aria-label="Search">
    <p class="count" id="count">{len(posts)} bài viết</p>
  </div>

  <!-- FAB stack: back-to-top on top, search underneath -->
  <div class="fab-stack" aria-label="Actions">
    <button class="fab hidden-fab" id="toTop" aria-label="Lên đầu trang" title="Lên đầu trang">
      <svg viewBox="0 0 24 24" aria-hidden="true"><polyline points="6 15 12 9 18 15"></polyline></svg>
    </button>
    <button class="fab" id="toggleSearch" aria-label="Tìm kiếm" title="Tìm kiếm">
      <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    </button>
  </div>

  <script>
    (function() {{
      const search = document.getElementById('search');
      const cards = Array.from(document.querySelectorAll('.card'));
      const empty = document.getElementById('empty');
      const count = document.getElementById('count');
      const total = cards.length;

      function apply() {{
        const q = (search.value || '').trim().toLowerCase();
        let visible = 0;
        cards.forEach(c => {{
          const match = !q || c.dataset.title.includes(q);
          c.classList.toggle('hidden', !match);
          if (match) visible++;
        }});
        empty.classList.toggle('hidden', visible > 0);
        count.textContent = visible === total
          ? total + ' bài viết'
          : visible + ' / ' + total + ' bài viết';
      }}
      search.addEventListener('input', apply);

      // Back-to-top
      const toTop = document.getElementById('toTop');
      function onScroll() {{
        toTop.classList.toggle('hidden-fab', window.scrollY < 400);
      }}
      window.addEventListener('scroll', onScroll, {{ passive: true }});
      toTop.addEventListener('click', () => window.scrollTo({{ top: 0, behavior: 'smooth' }}));
      onScroll();

      // Search popover toggle
      const pop = document.getElementById('searchPop');
      const toggle = document.getElementById('toggleSearch');
      toggle.addEventListener('click', e => {{
        e.stopPropagation();
        const open = pop.classList.toggle('open');
        if (open) setTimeout(() => search.focus(), 50);
      }});
      // Close when clicking outside
      document.addEventListener('click', e => {{
        if (!pop.contains(e.target) && e.target !== toggle && !toggle.contains(e.target)) {{
          pop.classList.remove('open');
        }}
      }});
      // Esc closes popover
      document.addEventListener('keydown', e => {{
        if (e.key === 'Escape') pop.classList.remove('open');
      }});
    }})();
  </script>
</body>
</html>
"""
    (OUT / "index.html").write_text(out, encoding="utf-8")
    print(f"index.html written with {len(posts)} posts.")


if __name__ == "__main__":
    main()
