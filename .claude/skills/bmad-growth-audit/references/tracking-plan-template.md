# Tracking Plan Template

> Reference loaded by `bmad-growth-audit` and `bmad-paid-acquisition-sprint` whenever event tracking is in scope. Owner: `bmad-growth-analyst`.

## What a Tracking Plan IS

An authoritative spec of every analytics event your product/site/marketing emits, with a stable schema. Not a list of analytics tools.

## Naming Convention — Object-Action

`<object>_<action>` in lowercase snake_case, past tense for the action.

Examples:
- `signup_completed` ✅
- `cart_abandoned` ✅
- `pricing_viewed` ✅
- `email_subscribed` ✅
- ❌ `userClickedSignupButton` (mixed case, action-first)
- ❌ `signed up` (no object, ambiguous)

Action vocabulary (use these verbs only):
- `viewed`, `clicked`, `submitted`, `completed`, `started`, `abandoned`, `failed`, `subscribed`, `unsubscribed`, `opened`, `closed`, `created`, `updated`, `deleted`, `shared`, `invited`, `accepted`, `rejected`

## Standard Property Schema (every event)

| Property | Type | Always present | Description |
|---|---|---|---|
| `event_name` | string | yes | The object_action name |
| `event_id` | uuid | yes | Idempotency key for the event |
| `timestamp` | iso-8601 | yes | When the event occurred |
| `user_id` | string \| null | when known | Stable user ID |
| `anonymous_id` | string | yes | Device/session ID, set even when logged in |
| `source` | string | yes | `web` \| `ios` \| `android` \| `email` \| `server` |
| `app_version` | string | yes | Semver of source app/site |
| `utm_*` | strings | when present | Standard UTM set |
| `referrer` | url | when present | The previous URL or referring source |

Plus event-specific properties (per row in tracking plan).

## Tracking Plan Row Format

Single source of truth. CSV or YAML, never spread across tools.

```
| event_name           | trigger location          | required props                              | optional props        | downstream consumer    | owner       | status |
|----------------------|---------------------------|---------------------------------------------|-----------------------|------------------------|-------------|--------|
| signup_completed     | post-form-submit success  | source, signup_method, plan_attempted       | invite_token, ref_id  | growth dashboard, CRM  | growth-eng  | live   |
| pricing_viewed       | /pricing page mount       | source, plan_currently_on, traffic_source   | a_b_variant           | growth dashboard       | growth-eng  | live   |
| paywall_triggered    | feature-gate hit          | feature_id, plan_currently_on, gate_reason  | usage_count           | monetization dashboard | product-eng | live   |
```

## Identity Stitching Decision

| Question | Answer | Implication |
|---|---|---|
| Do we let users use product before login? | Yes | Need anonymous_id always; alias on login |
| Do we have multiple platforms (web + mobile)? | Yes | Server-side identity store (not client-only) |
| Are some events sent server-side (Stripe webhook, cron)? | Yes | Use a server-side stitcher (Segment, Rudderstack, custom) — not GA4-only |
| Strict GDPR / CCPA / consent regime? | Yes | Anonymous_id rotation on consent withdraw; PII separately encrypted |

## Server-side vs Client-side

| Send from | When | Why |
|---|---|---|
| Client (browser/app) | UI interactions, page views | Has full UTM/referrer context |
| Server | Payments, signups, status changes | Source of truth, won't be ad-blocked |
| Both with dedup | Critical conversion events | Resilience + dedup via `event_id` |

Rule: revenue events MUST be server-sent. Client-only payment events under-report by 15-25%.

## Consent Mode Checklist (GA4 + ad pixels)

- [ ] Pre-consent: only set anonymous identifiers, no personal data
- [ ] Post-consent (analytics): activate full analytics tracking
- [ ] Post-consent (ad targeting): activate ad pixels
- [ ] Withdrawal: rotate anonymous_id, drop ad pixel cookies
- [ ] Consent decision logged with timestamp, version of consent banner
- [ ] Region detection: EU/UK get banner, US gets implied consent (configurable)

## UTM Convention

Standardize UTM strings across all marketing surfaces. Variations break attribution.

```
utm_source: <vendor or platform> (lowercase, no spaces) — google, facebook, twitter, hackernews
utm_medium: <type of placement> — cpc, social, email, organic, referral
utm_campaign: <campaign-slug> — q4-launch, founders-webinar
utm_content: <ad variant or link position> — headline-a, footer-cta
utm_term: <keyword bid for search> — only for paid search
```

A misnamed `utm_source=Google` (capital G) creates a separate row. Lowercase enforce.

## GA4 / GTM Setup Checklist

- [ ] One GA4 property per major brand (not per channel)
- [ ] Server-side GTM container OR Segment/Rudderstack pipeline
- [ ] Cross-domain tracking configured if multiple domains
- [ ] Internal traffic filtered (employee IPs)
- [ ] Conversions defined with thresholds (not just every event)
- [ ] BigQuery export enabled (free with GA4)
- [ ] Debug view checked for the 5 most-critical events

## Output

`{marketing_artifacts}/analytics/`:
- `tracking-plan.md` (the row table)
- `event-library.md` (full event-by-event schema)
- `identity-stitching.md` (the decision answers)
- `consent-mode.md` (regional flow)
- `utm-convention.md` (the lowercase rules)
- `ga4-gtm-setup-checklist.md` (the checkboxes, dated)
