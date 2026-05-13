# Step 02 — Pre-Launch (J-7 to J-1)

**Phase:** 2
**Lead agent:** bmad-launch-coordinator
**Timebox:** J-7 → J-1
**Gate at end:** `go_no_go`

## Steps

1. **Teaser Campaign** (bmad-social-media-strategist) — *J-7 to J-1* — Execute daily teaser posts, J-7 email teaser, countdown content, and audience warming. → output: `teaser-execution.md`
2. **Influencer/Partner Outreach** (bmad-launch-coordinator) — *J-7 to J-3* — Coordinate influencer briefings, partner notifications, press outreach, and affiliate preparation. → output: `outreach-status.md`
3. **Technical Readiness** (bmad-launch-coordinator) — *J-2* — Verify landing-page live check, analytics tracking, email automation, payment processing if applicable, and server capacity. → output: `technical-checklist.md`
4. **Team Briefing** (bmad-launch-coordinator) — *J-1* — Final alignment on launch-day schedule, role assignments, communication channels, escalation procedures, and the **go/no-go decision**. → gate: `go_no_go` → output: `team-briefing.md`

## References for this step

- `references/directory-tracker-protocol.md` — Tier 1-2 submissions can begin during this window so backlinks are live for J-Day search/social discovery.

## Gate `go_no_go` decision rule

Block launch if ANY of these fail:
- Landing page returns 5xx in any region
- Analytics events not firing in QA
- Payment / signup flow failing in QA
- A critical hire/owner unavailable for J-Day window
- Legal/compliance review pending

If gate fails: postpone J-Day by minimum 48h, return to Step 02 step 3.
