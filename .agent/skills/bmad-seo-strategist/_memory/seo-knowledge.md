# SEO Knowledge Base

> Working SEO checklists and guidelines for Quincy Crawler. Loaded alongside instructions.md.

---

## Core Web Vitals — Checklist

### LCP (Largest Contentful Paint) < 2.5s
- [ ] Optimize images (WebP, lazy loading)
- [ ] Preload critical resources
- [ ] CDN for static assets
- [ ] Eliminate render-blocking resources

### FID (First Input Delay) < 100ms / INP < 200ms
- [ ] Minimize third-party JavaScript
- [ ] Code splitting
- [ ] Defer non-critical JS
- [ ] Web Workers for heavy tasks

### CLS (Cumulative Layout Shift) < 0.1
- [ ] Explicit width/height on images and videos
- [ ] Reserve space for ads / embeds
- [ ] Avoid dynamic injections above the fold
- [ ] `font-display: swap` for web fonts

---

## E-E-A-T Guidelines

### Experience
- Content created by someone with direct hands-on experience of the topic.
- Evidence of using / testing the products being recommended.
- Personal anecdotes and insights (not generic).

### Expertise
- Author with verifiable credentials.
- Citations of authoritative sources.
- Technical depth appropriate for the audience.

### Authoritativeness
- Backlinks from domain-relevant reference sites.
- Mentions in trade press.
- Complete author profiles with bios.

### Trustworthiness
- HTTPS required.
- Clear privacy policy.
- Visible contact information.
- Citations that resolve to verifiable sources.

---

## Technical Audit — Full Checklist

### Indexation
- [ ] `robots.txt` accessible and correct.
- [ ] XML sitemap submitted to Google Search Console.
- [ ] No important pages set to `noindex`.
- [ ] Canonical tags resolve correctly.

### Architecture
- [ ] Logical, flat URL structure.
- [ ] Breadcrumbs implemented.
- [ ] Coherent internal linking.
- [ ] No orphan pages.

### On-Page
- [ ] Title unique, < 60 characters.
- [ ] Meta description unique, < 160 characters.
- [ ] One H1 per page.
- [ ] Logical H1–H6 hierarchy.
- [ ] Alt text on images.

### Performance
- [ ] TTFB < 200ms.
- [ ] Page weight < 3MB.
- [ ] Requests < 100.
- [ ] GZIP / Brotli compression.

### Mobile
- [ ] Mobile-first indexing ready.
- [ ] Viewport meta tag set.
- [ ] Touch targets > 48px.
- [ ] No content hidden on mobile.

---

## Topic Cluster Template

```
                    [PILLAR PAGE]
                    /     |     \
                   /      |      \
            [CLUSTER]  [CLUSTER]  [CLUSTER]
              /|\        /|\        /|\
             / | \      / | \      / | \
           [Interconnected sub-topics]
```

### Recommended structure
- **Pillar:** 3,000–5,000 words, covers the topic in breadth.
- **Clusters:** 1,500–2,500 words, deep-dive a single aspect.
- **Links:** Pillar ↔ Clusters (bidirectional).
- **Anchors:** varied, natural, descriptive.

---

## Search Intent Classification

| Intent | Signals | Content type |
|--------|---------|--------------|
| **Informational** | how, why, what is | Guide, tutorial, article |
| **Navigational** | [brand] + login / site / app | Product page, homepage |
| **Transactional** | buy, price, best, comparison | Landing page, comparison |
| **Commercial** | review, vs, alternative to | Review, comparison |

---

## Quick Wins — Common Categories

### Easy (< 1 day)
- Optimize titles / meta descriptions of top 20 pages.
- Add missing alt text.
- Fix broken internal links.
- Add basic schema markup.

### Medium (1–3 days)
- Build strategic internal-linking pass.
- Optimize images (compression, WebP).
- Improve Core Web Vitals.
- Enrich thin content.

### High Impact
- Pages ranking position 4–10 → push to top 3.
- Pages with low CTR vs. position (rewrite title / description).
- Keywords with high volume + low difficulty.
- Content gaps vs. direct competitors.

---

## Key Metrics to Track

| Metric | Tool | Frequency |
|--------|------|-----------|
| Positions | GSC, Ahrefs | Weekly |
| Organic traffic | GA4 | Weekly |
| Core Web Vitals | PageSpeed Insights | Monthly |
| Backlinks | Ahrefs, Moz | Monthly |
| Indexation | GSC | Weekly |
| CTR per page | GSC | Monthly |

For deeper experiment design, cross-reference `bmad-cro-sprint/references/experiment-design.md` (hypothesis, ICE, MDE, sample-size math).
For advanced surfaces (AI SEO, pSEO, schema, ASO), cross-reference `bmad-advanced-seo-sprint/`.
