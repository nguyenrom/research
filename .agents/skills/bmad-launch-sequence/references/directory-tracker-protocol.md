# Directory & Backlink Submission Protocol

> Reference loaded during `bmad-launch-sequence` Phase 2 (Pre-Launch Asset Production) and Phase 4 (J+7 Retention/Compounding). Owner: `bmad-launch-coordinator`.

## 3 Hard Rules

1. **Foundation first.** Do not submit anywhere until destination pages are ready (homepage, key alternative pages, key use-case pages, public roadmap, change log). A successful submission to a low-quality destination is wasted backlink equity.
2. **Destination pages drive ROI.** A directory backlink only matters if the linked page is destination-quality. Hierarchy of value:
   1. Alternative-to / vs pages (highest — captures bottom-funnel intent)
   2. Use-case / job-specific pages
   3. Templates / tools / free utility pages
   4. Listicle / category pages
   5. Integrations / app marketplace pages
3. **Tier-specific positioning.** A submission to Product Hunt, G2, and Reddit cannot use the same copy. Each tier has its own taste rules (see Tier Matrix below).

## Tier Matrix

| Tier | Examples | Purpose | Time horizon | Copy positioning |
|---|---|---|---|---|
| Tier 0 — Hero launches | Product Hunt, Hacker News Show HN | Awareness spike + hard launch | Day 0 | Bold, narrative, founder-voice |
| Tier 1 — High-authority directories | G2, Capterra, AlternativeTo, Crunchbase | Long-term SEO + buyer research | First 14 days | Buyer-focused, comparison-friendly |
| Tier 2 — Niche directories | StackShare, BetaList, IndieHackers, FutureTools | Discovery in target audience | First 30 days | Practitioner-focused, technical |
| Tier 3 — Generic directories | SaaS lists, Reddit /r/<niche>, micro listicles | Long-tail SEO | Ongoing | Lightweight, link-only |

## 10-in-30 Review Protocol

To unlock the G2/Capterra "trending" boost and earn social proof: secure **10 customer reviews in the first 30 days post-launch**.

| Day | Action |
|---|---|
| J+0 | Email the top 25 happiest customers asking for honest review on G2/Capterra. Include direct review URL. |
| J+3 | Personal Slack/text follow-up to the 10 most engaged who haven't responded |
| J+7 | Cross-post launch testimonials from internal channels — "would you mind putting this on G2?" |
| J+14 | Mid-window check: how many reviews so far? Iterate on ask language |
| J+21 | Second wave: incentivize with company swag (NOT discount — that biases the review) |
| J+30 | Quality check: any 1-2 star reviews? Address publicly, do NOT delete |

## Reddit 90/10 Rule

In subreddits relevant to your ICP:
- **90% of activity** = genuine value contribution (answer questions, share insight, no link)
- **10% of activity** = self-promotion (Show & Tell threads, scheduled launch posts)

Violators get shadowbanned within 60 days. Mods notice posting ratios.

## Tracker Schema

Every directory submission tracks 8 fields:

```yaml
- directory: <name>
  url: <submission url>
  tier: 0|1|2|3
  destination_page: <which of our pages we linked to>
  positioning_used: <brief copy summary>
  submitted_at: <date>
  status: submitted|approved|live|rejected
  backlink_live_at: <date or null>
  notes: <anything weird>
```

Save tracker to `{marketing_artifacts}/launch/directories/tracker.csv`.

## Product Hunt 3-Week Timeline

| Week | Action |
|---|---|
| W-3 | Pick a launch day (Tue-Thu best). Draft maker comment. Assemble 50+ "hunters" (existing customers / community willing to comment in first 4 hours). Create high-quality gallery images (5-7) and a short demo video. |
| W-2 | Soft DMs to community: "We're launching on PH on <date>, would love your support on launch day." Schedule launch day morning Slack/Discord blast. |
| W-1 | Final asset review. Test launch flow internally. Write maker comment, top-3 FAQ, and 2-3 reply templates for comments. Pre-write press release / blog post / Twitter thread / LinkedIn post for launch day. |
| W-0 | Launch at 12:01 AM PT. Maker comment within first 5 minutes. Active in comments for first 4 hours. Twitter/LinkedIn cross-post immediately. End-of-day: blog post recap. |

## Output

Phase 2 produces `directory-asset-bundle.md` with: maker description, 5 image variants, demo video brief, hunter outreach list, maker comment draft.
Phase 4 produces `directory-tracker.csv` populated with Tier 0-3 submissions.
