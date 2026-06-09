# Paid Channel Architecture Presets

> Reference loaded by `bmad-paid-acquisition-sprint` Phase 1 (channel selection) and Phase 2 (campaign architecture). Concrete presets per platform — audience structure, bid strategy, campaign hierarchy, learning-period rules.

## Channel selection — when to pick which

| ICP fit | Channel | Why |
|---------|---------|-----|
| Searches with high commercial intent for category | Google Search | Captures bottom-funnel demand |
| Visual product, broad B2C audience | Meta (Facebook + Instagram) | Detailed targeting, creative-driven |
| B2B mid-market & enterprise, title-targeted | LinkedIn Ads | Highest cost, but only platform with title precision |
| Niche developer / engineer / technical product | X (Twitter), Reddit | Audience hangs out there; low CPM, hard targeting |
| Younger consumer audience (16-30), entertainment products | TikTok | Watch-time-driven, native creative wins |
| Discovery + planning (e-commerce, design, recipe) | Pinterest | Long-tail intent, evergreen pin SEO |

## Google Search Ads preset

### Account hierarchy

```
Account
└── Campaign type: Search (avoid Performance Max for first 60 days)
    ├── Campaign: Brand
    │   └── Ad group: brand keyword variants
    └── Campaign: Non-brand (one per match-type strategy)
        ├── Ad group: [exact] high-intent keywords
        ├── Ad group: [phrase] mid-intent
        └── Ad group: [broad+modifier] research intent
```

### Bid strategy progression

| Phase | Bid strategy | Why |
|-------|-------------|-----|
| 0-30 days | Manual CPC | Build conversion data; learn baseline |
| 30-60 days | Maximize Conversions (no tCPA cap) | Let auto-bidding find conversions |
| 60-90 days | Target CPA (tCPA) at 1.2× actual CPA | Constrain spend to efficient zone |
| 90+ days, scaling | Target ROAS or tROAS | Optimize for revenue, not just signups |

### RSA character limits

- Headlines: 30 chars × up to 15
- Descriptions: 90 chars × up to 4
- Final URL paths: 15 chars × 2

Pin headline 1 to the keyword, headline 2 to the value prop. Don't pin headline 3 — let Google rotate proof points.

### Negative-keyword discipline

Update negatives weekly for first 30 days. Common negatives for SaaS:
- "free" (unless free is your offer)
- "jobs", "salary", "career"
- "tutorial", "course" (research intent, not buyer)
- Competitor product names (decide separately)

## Meta (Facebook + Instagram) preset

### Account hierarchy

```
Account
└── Campaign objective: Sales (or Leads)
    ├── Ad set: Cold audience (broad + interest stack)
    │   └── 3-5 ad creatives (different angles)
    ├── Ad set: Cold audience (lookalike of paying customers, 1%)
    └── Ad set: Warm retargeting (visited /pricing in 30d)
```

### Bid strategy

- **Cold audiences**: lowest cost (start), then bid cap once stable.
- **Warm retargeting**: cost cap = 70% of cold CPA.
- **Daily budget per ad set**: $30-50 minimum to exit learning phase in 7 days.

### Creative requirements

- 1:1 (square), 4:5 (vertical) for feed; 9:16 for Reels/Stories.
- 6 creative variants per ad set (Meta's algo needs creative volume).
- Refresh every 2 weeks — fatigue kicks in fast.
- Primary text < 125 chars (avoids "see more" cut).
- Headline < 27 chars.

## LinkedIn Ads preset

### Account hierarchy

```
Account
└── Campaign: Sponsored Content (start here, NOT Message Ads)
    ├── Campaign group: Job-title cold
    │   └── Audiences: VP Marketing + Director Marketing at [size band] in [vertical]
    ├── Campaign group: Account-list (matched audience from CRM)
    └── Campaign group: Retargeting (engaged with previous content)
```

### Bid strategy

- Cost-per-click manual bid (CPC), NOT CPM. LinkedIn CPM is brutal.
- Daily budget $50-100 minimum per active campaign.
- Bid: aim for top quartile per LinkedIn's bid range (otherwise no impressions).

### Creative requirements

- Single image: 1200×627px, < 100MB.
- Document ads (carousels) outperform single image for B2B by 2-3×.
- Headline < 70 chars; intro text < 150 chars.

### Audience size sweet spot

- 50,000-200,000: enough for stat-sig, not so broad you waste spend.
- < 30,000: wait, audience too small.
- > 500,000: layer additional filters (seniority, function).

## X (Twitter) Ads preset

### When it works

- Founder-led brand with existing audience (5K+ followers).
- Niche dev/technical products.
- Promoted threads (not just single tweets).

### Hierarchy

```
Campaign: Website Clicks or Conversions
├── Ad group: Followers-of-followers (lookalike-like)
├── Ad group: Conversation targeting (people replying to industry conversations)
└── Ad group: Keyword targeting (recent searches/tweets)
```

### Creative

- Promoted threads beat single tweets 3-5×.
- Reply-velocity matters; X amplifies tweets that get fast replies.
- Visuals should NOT look like ads (native UGC tone).

## TikTok Ads preset

### When it works

- B2C or PLG SaaS with consumer-friendly UI.
- Younger audience (16-30 primary, 30-45 secondary).
- You can produce native short-form video (NOT polished ads).

### Hierarchy

```
Campaign: Conversions
└── Ad group: Spark Ads (boost organic-feel content)
    ├── Creative 1: 15-second product walkthrough, native UGC
    ├── Creative 2: Founder-on-camera, 25 seconds
    └── Creative 3: Trend-based, 12 seconds
```

### Creative requirements

- 9:16 vertical only.
- First 3 seconds = hook (no slow intros).
- Native sound trends (use the sound library, NOT licensed music).
- Captions burned in (most users watch with sound off).

## Cut / iterate / scale rules

After learning period (7 days minimum, 14 days ideal):

| Performance | Action |
|-------------|--------|
| CPA > 1.5× target | **Cut** — pause, document, don't iterate the same creative |
| CPA 1.0-1.5× target | **Iterate** — change creative, audience, or LP one at a time |
| CPA 0.7-1.0× target | **Hold** — keep running at current budget, no scaling yet |
| CPA < 0.7× target with stable volume | **Scale** — increase budget 20% every 3-4 days; stop if CPA drifts |

## Learning period & sample size

- Meta: needs 50 conversions per ad set per week to exit learning.
- Google: needs 50 conversions per campaign in 30 days for tCPA stability.
- LinkedIn: 30-50 leads in first 14 days for confidence.
- TikTok: 50 conversions in 7 days.

If volume is below threshold, broaden audience or accept longer learning window. Do NOT panic-pause in week 1.

## Output

`{marketing_artifacts}/paid/`:
- `channel-selection.md` — chosen channels with rationale.
- `<channel>/account-architecture.md` — hierarchy per channel.
- `<channel>/audiences.md` — targeting setup.
- `<channel>/creative-brief.md` — variant plan.
- `<channel>/optimization-cadence.md` — review schedule + cut/iterate/scale rules.

## Cross-references

- For creative variants → `bmad-creative-production-sprint/references/ad-creative-char-limits.md`.
- For tracking plan → `bmad-growth-audit/references/tracking-plan-template.md`.
- For experiment design rigor on creative tests → `bmad-cro-sprint/references/experiment-design.md`.
