# Growth Loop Scorecard

> Reference loaded by `bmad-growth-loops-sprint` Phase 1 (Loop Selection) and Phase 2 (Loop Design). Scoring framework for evaluating 7 loop types, plus per-loop spec templates.

## Why a scorecard

Most growth-loop ideas are bad ideas in expensive disguise. Without a forcing-function rubric, teams build referral programs that nobody uses, free tools that don't fit, communities nobody joins. The scorecard makes the underlying physics explicit.

## The 7 loop types

| Loop | Mechanism | Example |
|------|-----------|---------|
| Free tool | Engineering-as-marketing utility drives signups | HubSpot's Website Grader; Ahrefs' free SEO audit |
| Lead magnet | Gated resource captures email | Salary calculator, ebook, template |
| Referral | Existing users invite new ones, both rewarded | Dropbox referral, Notion 1-month free |
| Affiliate | External promoters earn revenue share | Convertkit creator program |
| Ambassador | Selected creators / power users amplify with brand alignment | Webflow community designers |
| Community | Members create value for each other; brand convenes | dbt community, Indie Hackers |
| Product sharing | Output of using the product is naturally shareable | Calendly invite link, Loom video link |

## The 7-dimension scorecard

For each loop candidate, score 1-10:

| Dimension | What it asks | High score (10) | Low score (1) |
|-----------|--------------|------------------|---------------|
| **ICP pain match** | Does this loop solve a real ICP pain? | Solves a top-3 pain | Tangential / nice-to-have |
| **Distribution reach** | Can this loop expose to many new users? | 100,000+ reachable / cycle | < 1,000 reachable |
| **Repeatability** | Does the same user trigger it again? | Triggers monthly+ | One-time only |
| **Incentive quality** | Is the reward proportional and fair? | Both sides win clearly | Token reward, easy to game |
| **Engineering cost** | Cost to build + maintain | < 1 week dev | 6+ week build with ongoing maintenance |
| **Fraud risk** | Can it be gamed for cash/abuse? | Low (organic structure) | High (cash incentive, easy fake accounts) |
| **Measurement** | Can we instrument loop velocity? | Clean events at every step | Hard to attribute |

**Total score** = sum of 7 dimensions (max 70).

| Total | Verdict |
|-------|---------|
| 56-70 | Top priority — design and ship |
| 42-55 | Strong candidate — refine before ship |
| 28-41 | Marginal — only if no better alternative |
| 0-27 | Skip — physics don't work |

## Per-loop spec templates

### Free tool spec

```yaml
- name: [Tool name]
  job_to_be_done: "Helps [persona] do [task] without [friction]"
  adjacency: "Direct adjacency to [our product's core capability]"
  format: standalone web app | embeddable widget | CLI | desktop
  data_input: [what user provides]
  output: [what user gets]
  capture_point: |
    - Email gate: [yes/no — pros/cons]
    - In-tool conversion: [link to product after value moment]
  distribution:
    - SEO: target keyword [X], create landing page
    - Social: launch via Product Hunt, dev/marketing communities
    - Embed: partners can embed widget
  maintenance: hours/month to keep accurate
  build_decision: native build | no-code | embed third-party
```

**Rule**: free tools must be ADJACENT to the core product. Tangential tools (cool but irrelevant) attract wrong audience.

### Lead magnet spec

```yaml
- name: [Lead magnet]
  buyer_stage: awareness | consideration | decision
  format: guide | template | calculator | checklist | toolkit | course
  match_to_stage:
    awareness: educational guide
    consideration: comparison template / decision matrix
    decision: ROI calculator / RFP template
  gating:
    - Hard gate (email required) — when value is HIGH
    - Soft gate (preview free, full requires email)
    - No gate (drives SEO instead)
  follow_up_sequence: [link to nurture sequence in lifecycle-email]
  attribution_event: lead_magnet_downloaded
```

### Referral program spec

```yaml
- name: [Referral program]
  trigger_moment: "[when user has just hit aha moment]"
  participants:
    referrer_segment: paying customer | free user | trial user
    referred_segment: anyone | matching ICP only
  reward_structure:
    type: one-sided | double-sided | tiered
    referrer_reward: [credit / cash / months free / status]
    referred_reward: [discount / extended trial / bonus credits]
    cap: [per user limit]
  attribution_window: 30d | 60d | 90d
  fraud_controls:
    - Self-referral block (same email domain / device fingerprint)
    - Daily cap on rewards
    - Manual review > $X reward
  tracking_events:
    - referral_link_generated
    - referral_link_clicked
    - referral_signup
    - referral_paid (revenue moment)
  loop_velocity_target: viral coefficient (k) > 0.3
```

### Affiliate program spec

Similar to referral but EXTERNAL promoters:

```yaml
- name: [Affiliate program]
  participant_profile: bloggers | YouTubers | newsletter creators | agencies
  vetting: open | application-based | invite-only
  commission:
    rate: 10-30% recurring revenue (SaaS norm)
    cookie_window: 30-90 days
    payout: monthly | quarterly
  asset_kit:
    - Banner ads (multiple sizes)
    - Email swipe copy
    - Video assets / screenshots
    - Tracking links + UTMs
  fraud_controls:
    - Refund clawback (if customer churns within 60d)
    - Self-affiliate prevention
    - Quality threshold (deactivate affiliates with > X% refund rate)
```

### Ambassador program spec

Differs from affiliate by curation + brand alignment + non-cash motivation:

```yaml
- name: [Ambassador program]
  selection: curated, application-based
  size: 20-100 ambassadors max (quality > quantity)
  motivation:
    - Status / community access
    - Early product access
    - Co-marketing (feature them)
    - Modest cash / swag (NOT primary motivation)
  expectations:
    - Quarterly content piece (post / video / talk)
    - Beta-testing new features
    - Monthly community participation
  offboarding: clear criteria for inactivity / misalignment
```

### Community flywheel spec

Cross-reference: `bmad-social-campaign/references/community-flywheel.md` is the canonical reference. Use it for community-led growth design.

### Product sharing loop spec

```yaml
- name: [Product sharing loop]
  share_moment: "[when user creates / completes / publishes X]"
  shared_artifact: [URL, image, video, embed]
  sharer_motivation: [why they share — utility, status, collaboration]
  receiver_experience:
    - Sees: branded preview / signup CTA
    - Lands on: branded page (not generic homepage)
    - Friction to signup: [as low as possible]
  branding_balance:
    - Visible enough: receivers know what tool was used
    - Not obnoxious: doesn't make sharer cringe
  measurement:
    - shares_per_active_user (target > 0.5/week)
    - signup_rate_from_share (target > 5%)
```

Calendly is the gold standard: every invite link drives the brand without the sharer thinking about it.

## Loop velocity math

```
Loop velocity = (signups per cycle × conversion rate × avg invites per converter) / cycle time

Viral coefficient (k) = avg invites per user × conversion rate per invite

If k > 1: pure viral growth (rare; reserve for B2C with strong sharing utility)
If k 0.3-1: meaningful augmentation; should still complement other channels
If k < 0.3: loop exists but not load-bearing
```

For loops with paid component (referral cash incentive):

```
Loop CAC = total reward paid / new acquired users
Loop CAC must be < blended CAC for the loop to be profitable.
```

## Kill / iterate / scale rules

| Signal | Action |
|--------|--------|
| Loop velocity > target after 60 days | Scale: increase distribution, broaden eligibility |
| Loop velocity 50-100% of target | Iterate: tweak incentive, message, or trigger moment |
| Loop velocity < 50% of target after 90 days | Kill: physics didn't work; document learnings |
| High volume but high fraud rate | Iterate: add controls before scaling |
| Volume good, retention of acquired users low | Iterate: the loop attracts wrong audience; tighten ICP fit |

## Output

`{marketing_artifacts}/growth-loops/`:
- `loop-scorecard.md` — all candidates scored on 7 dimensions.
- `<loop-type>-spec.md` — selected loops fully specified using the templates above.
- `loop-tracking-plan.md` — events, dashboards, viral coefficient calc.
- `kill-iterate-scale-rules.md` — pre-committed decisions.

## Cross-references

- For community design → `bmad-social-campaign/references/community-flywheel.md`.
- For lead-magnet follow-up → `bmad-lifecycle-email-sprint/references/email-sequence-archetypes.md`.
- For tracking event taxonomy → `bmad-growth-audit/references/tracking-plan-template.md`.
- For experiment rigor on loop tests → `bmad-cro-sprint/references/experiment-design.md`.
