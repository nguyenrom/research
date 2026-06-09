# Voice-of-Customer Mining Protocols

> Reference loaded by `bmad-customer-research-sprint` Phase 2 (Voice of Customer). Concrete sources, query patterns, scraping rules, ranking formula, and persona anti-pattern checklist.

## Source inventory (ranked by signal density)

| Source | Signal density | What you get | Effort |
|--------|---------------|--------------|--------|
| Customer interviews (your own) | Very high | Verbatim language, real switching triggers, true objections | High (need scheduling) |
| Sales call recordings (Gong/Chorus) | Very high | Live objection handling, deal-killer reasons | Medium (need access) |
| Support tickets (Intercom/Zendesk) | High | Recurring frustrations, feature gaps, edge cases | Medium |
| Cancellation surveys | High | Real churn reasons (filtered for honesty) | Low |
| G2 / Capterra / TrustRadius reviews | High | Pros/cons in buyer's words, comparison to competitors | Low |
| AppSumo / Product Hunt comments | Medium | Early-adopter language, feature requests | Low |
| Reddit (relevant subreddits) | High | Unfiltered opinions, alternative-comparison threads | Medium (need scraping) |
| Twitter/X mentions + replies | Medium | Sentiment signals, viral complaints | Medium |
| LinkedIn comments on industry posts | Medium | Decision-maker language (titles, jargon, buying triggers) | Medium |
| Hacker News / specialized forums | Medium-High (technical products) | Deep technical objections, build-vs-buy debates | Medium |
| Blog comments + YouTube comments | Low-Medium | Casual readers, content-fit signals | Low |
| Search query data (GSC, AnswerThePublic) | High | Question phrasing, intent signals | Low |

## Reddit mining query patterns

For each target subreddit, run these queries in order:

```
1. "best [category]"           → comparison threads, alternative discussions
2. "[competitor] vs"           → head-to-head, pain-point reveals
3. "alternative to [competitor]" → switching triggers
4. "[category] for [use case]"   → niche fit
5. "[competitor] sucks"          → unfiltered objections (treat with skepticism)
6. "looking for"                 → unmet needs
7. "[your brand]"                → unprompted mentions
```

**Discovery list of subreddits**: `r/[your category]`, `r/SaaS`, `r/Entrepreneur`, `r/startups`, `r/smallbusiness`, plus 2-3 niche subreddits per persona.

**Ethics**: never post promotional comments while scraping. Read-only. Cite source URLs in mining notes.

## G2 / Capterra review pattern

For each direct competitor's page on G2:

| Filter | Why |
|--------|-----|
| Most recent 12 months | Old reviews are biased toward early version |
| 1-3 star reviews first | Pain points come out clearer in low ratings |
| 4-5 star reviews second | Use to extract what users LOVE — your moat target |
| Filter by industry segment | Only your ICP's reviews matter |
| Filter by company size | SMB reviews don't predict mid-market objections |

For each review extract: pain point, workaround, missing feature, switching trigger, exact phrase.

## Theme ranking formula: frequency × intensity

Raw count of mentions is misleading. Rank by:

```
theme_score = mention_count × avg_intensity

intensity_per_mention:
  1 = casual mention ("would be nice")
  2 = clear preference ("really wish")
  3 = active frustration ("hate that", "deal-breaker")
  4 = deal-killer ("we left because")
  5 = lawsuit-bait ("lost $X because")
```

A theme mentioned 5 times at intensity 4 (score 20) outranks a theme mentioned 30 times at intensity 1 (score 30 — but 30 casual mentions don't justify roadmap shift the way 5 deal-killers do).

Top 5-8 themes by `theme_score` go into `marketing-context.md` Section 4 (Problems) and Section 7 (Objections).

## JTBD synthesis from VOC

For each top theme, synthesize a JTBD statement:

```
When [trigger event],
I want to [job],
So I can [outcome].

But [obstacle / frustration with current solutions],
Which makes me feel [emotion].

I would switch if [shift / new option].
```

## Persona anti-pattern checklist

A persona is wrong if any of these is true:

- [ ] Defined by demographics only (age, gender, location) without behavioral signal.
- [ ] Generic title without specific responsibility ("marketers" instead of "B2B SaaS demand-gen lead at $1-10M ARR companies").
- [ ] Aspirational, not real (the persona you WISH bought your product, not the one who does).
- [ ] Over-broad (covers >40% of population — needs sub-segmentation).
- [ ] Over-narrow (only describes 1-2 actual customers — not a segment).
- [ ] Missing trigger event ("when they want to grow" is not a trigger; "when they hit $10K MRR and need first hire" is).
- [ ] Missing anti-pattern: who looks similar but won't buy.

## Output

`{marketing_artifacts}/customer-research/`:

- `voc-mining.md` — sources used, query log, raw verbatims grouped by theme, ranked by frequency × intensity.
- `jtbd-segments.md` — JTBD statements per primary segment, with switching triggers.
- `personas.md` — 1-3 personas using the schema in `bmad-create-marketing-context/references/twelve-section-template.md` Section 3.
- `persona-anti-patterns.md` — explicit list of who looks similar but is NOT the target.

Cross-references:
- For competitor profiling depth → `bmad-advanced-seo-sprint/references/aso-audit-scorecard.md` (3-tier brand maturity is also a useful frame for competitor positioning).
- For battlecard handoff → `bmad-revops-enablement-sprint/references/sales-enablement-asset-templates.md`.
