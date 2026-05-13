# ASO Audit Scorecard

> Reference loaded by `bmad-advanced-seo-sprint` Phase 5 step 3 (ASO Audit). Owner: `bmad-seo-strategist`.

## 6-Dimension Weighted Scorecard

Each dimension scored 0-100. Weighted total tells you where to invest.

| Dimension | Weight | What it measures |
|---|---|---|
| Title & Subtitle | 20% | Indexable copy, value prop, keyword presence |
| Visuals (icon, screenshots, preview video) | 25% | First-impression conversion + tap-through rate |
| Keyword Indexability | 15% | Apple/Google algorithm coverage |
| Reviews & Ratings | 20% | Trust signal, rating cap, response cadence |
| Conversion Path | 10% | Description, in-app preview, on-app-page CTAs |
| Localization | 10% | Per-region listings, ranking in non-home regions |

Total = Σ (dimension_score × weight).

| Total | Verdict |
|---|---|
| 80-100 | Listing is competitive |
| 60-79 | Top quartile within category |
| 40-59 | Mid-tier; clear improvements available |
| 0-39 | Underperforming; visuals + title are usually the problem |

## 3-Tier Brand Maturity (modifies scoring rules)

ASO advice depends on how recognizable your brand is. The scoring rule changes:

### Tier 1 — Dominant (Apple, Notion, ChatGPT)
- Brand IS the keyword. Title can be brand only.
- Visuals can be minimalist; brand recognition does the work.
- Keyword fields matter less; users search by name.
- Focus shifts to localization + alternative searches.

### Tier 2 — Established (mid-market SaaS, recognized indie apps)
- Title = brand + value-prop keyword combo.
- Visuals must communicate value clearly + show core UI.
- Keyword fields mid-importance; mix brand-keywords + category-keywords.

### Tier 3 — Challenger (new launch, < 6 months in store)
- Title = value-prop FIRST, brand last (e.g., "Recipe Planner — by Acme").
- Visuals must educate; user doesn't know the brand.
- Keyword fields HIGH importance; this is the only discovery surface.

Diagnose tier first, then audit accordingly. A Tier 3 app graded by Tier 1 rules will always look bad.

## Apple App Store vs Google Play — Indexing Matrix

| Field | Apple indexes? | Google indexes? | Notes |
|---|---|---|---|
| App name | yes (high) | yes (high) | 30 char Apple, 50 char Google |
| Subtitle (Apple) | yes | n/a | 30 char, second priority for Apple keywords |
| Short description (Google) | n/a | yes (high) | 80 char, first paragraph |
| Long description | NO | yes (med) | Apple does NOT index this — write for conversion only |
| Keyword field (Apple) | yes (high) | n/a | 100 char, comma-separated, no spaces |
| Promotional text (Apple) | NO | n/a | Update freely; not indexed |
| Subtitle = Google "category" tags | n/a | yes (low) | Pick correct category + tags |
| Reviews and review responses | weak | yes (med) | Both pass review keywords through algorithm |

Implication: Apple ASO front-loads keywords into title + subtitle + keyword field. Google ASO front-loads into title + short description + long description. Cannot copy-paste between stores.

## Tier-Conditional Flag List

Run the audit, then check tier-specific flags:

### Tier 1 Dominant flags
- [ ] Localized in top 10 regions for the category
- [ ] Promotional text rotates 1×/quarter for content marketing
- [ ] Custom product page experiments live
- [ ] Featured-app outreach to Apple/Google curation team

### Tier 2 Established flags
- [ ] Title combines brand + 1 high-volume value keyword
- [ ] Top 3 screenshots show CORE feature in use, not generic UI
- [ ] Star rating ≥ 4.5; ratings count > 100
- [ ] Reviews from past 90 days outweigh older reviews
- [ ] Subtitle (Apple) hits 28-30 chars (max value)
- [ ] Short description (Google) front-loads value prop in first 80 chars

### Tier 3 Challenger flags
- [ ] Title: value-prop keyword in FIRST 30 chars (Apple) / 50 chars (Google)
- [ ] Keyword field (Apple) packed with non-overlapping single keywords (no spaces, no plurals if singular present)
- [ ] First 3 screenshots have ON-IMAGE TEXT that re-states value prop
- [ ] Preview video set up (boosts conversion 25-35% on Apple)
- [ ] At least 50 reviews via in-app prompt at moment of "win"
- [ ] Long description (Google) first paragraph re-states value prop

## A/B Testing (Apple Custom Product Pages, Google Experiments)

Apple supports up to 35 Custom Product Pages — use for paid-channel-specific landing.
Google Play Experiments supports listing/icon/short-description tests.

Tests to prioritize:
1. Icon (single biggest visual lever)
2. First screenshot
3. Title value-prop wording
4. Subtitle / short description first 30 chars
5. Preview video first 5 seconds

## Output

`{marketing_artifacts}/aso/`:
- `audit-report.md` (6-dim scorecard with scores and weighted total)
- `tier-classification.md` (your maturity tier + reasoning)
- `apple-vs-google-mapping.md` (the indexing matrix populated for your app)
- `flag-list.md` (tier-conditional checklist with checks)
- `experiment-plan.md` (next 3 ASO tests prioritized)
