---
name: bmad-social-campaign
description: Plan, create, publish, and analyze a coordinated multi-platform social media campaign. Use when the user says "SC" or "lets run a social campaign".
---

# Social Media Campaign Workflow

**Goal:** Take a social campaign from strategy to platform-specific creation, coordinated publication, and a final performance report.

**Your Role:** Workflow facilitator coordinating with the lead agent (Social Media Strategist) and any specialist agents required.

You will continue to operate with your given name, identity, and communication_style, merged with the workflow facilitator role described below.

## References

- `references/community-flywheel.md` — Identity-first community design, platform selection table, first-100 protocol, health metrics (DAU/MAU > 20% etc.), rituals, anti-spam guardrail. Load when the campaign has a community-marketing phase.

## Prerequisites

This workflow consumes the shared marketing context. Before starting, run `bmad-create-marketing-context` (or confirm the file exists). If `{marketing_artifacts}/marketing-context.md` is missing, halt and invoke `bmad-create-marketing-context` first.

## Conventions

- Bare paths (e.g. `references/guide.md`) resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory (where `customize.toml` lives).
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{skill-name}` resolves to the skill directory's basename.

## On Activation

### Step 1: Resolve the Workflow Block

Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`

**If the script fails**, resolve the `workflow` block yourself by reading these three files in base → team → user order and applying the same structural merge rules as the resolver:

1. `{skill-root}/customize.toml` — defaults
2. `{project-root}/_bmad/custom/{skill-name}.toml` — team overrides
3. `{project-root}/_bmad/custom/{skill-name}.user.toml` — personal overrides

Any missing file is skipped. Scalars override, tables deep-merge, arrays of tables keyed by `code` or `id` replace matching entries and append new entries, and all other arrays append.

### Step 2: Execute Prepend Steps

Execute each entry in `{workflow.activation_steps_prepend}` in order before proceeding.

### Step 3: Load Persistent Facts

Treat every entry in `{workflow.persistent_facts}` as foundational context you carry for the rest of the workflow run. Entries prefixed `file:` are paths or globs under `{project-root}` — load the referenced contents as facts. All other entries are facts verbatim.

### Step 4: Load Config

Load config from `{project-root}/_bmad/performance-marketing/config.yaml` and resolve:
- Use `{user_name}` for greeting
- Use `{communication_language}` for all communications
- Use `{document_output_language}` for output documents
- Use `{company_name}` as the SaaS being marketed
- Use `{primary_channel}` as the default social channel for any social-media phase
- Use `{marketing_artifacts}` for output location

### Step 5: Greet the User

Greet `{user_name}`, speaking in `{communication_language}`. Briefly explain that this workflow ships a coordinated multi-platform campaign from strategy through publication and final report, and ask the user about campaign type (awareness, engagement, traffic, lead-gen, launch), key offer/message, timeline, and which platforms to include before phase 1. Default to `{primary_channel}` if the user does not specify.

### Step 6: Execute Append Steps

Execute each entry in `{workflow.activation_steps_append}` in order.

Activation is complete. Begin the workflow below.

## Paths

- `outputFile` = `{marketing_artifacts}/social-campaign.md`

## Execution

✅ Speak in `{communication_language}` and write artifacts in `{document_output_language}`.

### Phase 1: Campaign Strategy

**Lead agent:** bmad-social-media-strategist

**Steps:**
1. **Campaign Brief** (bmad-social-media-strategist) — Capture objective (awareness, engagement, traffic, leads), audience, key message/offer, timeline, paid budget if any, and success metrics. → output: `campaign-brief.md`
2. **Platform Strategy** (bmad-social-media-strategist) — Determine 2–3 primary platforms, secondary platforms, platform-specific goals, and resource allocation per platform. → output: `platform-strategy.md`
3. **Content Calendar** (bmad-social-media-strategist) — Build the campaign calendar: posting schedule per platform, content themes by day/week, key dates and moments, and hashtag strategy. → output: `content-calendar.md`
4. **Strategy Approval** (bmad-social-media-strategist) — Present strategy to the user, validate the calendar, confirm resources, and obtain approval. → gate: `user_approval`

### Phase 2: Content Creation

**Lead agent:** bmad-social-media-strategist

**Steps:** Run the platform-specific creation step for each selected platform, then consolidate.

1. **Twitter/X Content** (bmad-twitter-ghostwriter) — *if Twitter/X is selected* — Produce 10–20 tweets, 2–3 thread concepts, engagement reply templates, and hashtag sets. → output: `twitter-content.md`
2. **LinkedIn Content** (bmad-linkedin-creator) — *if LinkedIn is selected* — Produce 5–10 posts, carousel concepts, article outlines, and engagement strategy. → output: `linkedin-content.md`
3. **Instagram Content** (bmad-instagram-strategist) — *if Instagram is selected* — Produce 5–10 feed posts, 3–5 reel concepts, story templates, and carousel designs. → output: `instagram-content.md`
4. **TikTok Content** (bmad-tiktok-creator) — *if TikTok is selected* — Produce 5–10 video concepts, trend adaptations, hook variations, and sound selections. → output: `tiktok-content.md`
5. **YouTube Content** (bmad-youtube-strategist) — *if YouTube is selected* — Produce 5–10 Shorts concepts, video scripts, thumbnail briefs, and description templates. → output: `youtube-content.md`
6. **Reddit Content** (bmad-reddit-growth-hacker) — *if Reddit is selected* — Define target subreddits, post concepts, comment templates, and engagement plan. → output: `reddit-content.md`
7. **Discord Content** (bmad-discord-community-manager) — *if Discord is selected* — Produce announcement templates, event concepts, and engagement activities. → output: `discord-content.md`
8. **Pinterest Content** (bmad-pinterest-strategist) — *if Pinterest is selected* — Produce 10–20 pin concepts, board strategy, description templates, and keyword optimization. → output: `pinterest-content.md`
9. **Content Review** (bmad-social-media-strategist) — Consolidate all platform content, verify brand consistency and messaging alignment, present for approval. → gate: `user_approval` → output: `content-package.md`

### Phase 3: Campaign Publication

**Lead agent:** bmad-social-media-strategist

**Steps:**
1. **Schedule Content** (bmad-social-media-strategist) — Load content into scheduling tools, verify posting times, set up cross-platform coordination, and enable monitoring alerts. → output: `scheduling-confirmation.md`
2. **Campaign Launch** (bmad-social-media-strategist) — Activate scheduled posts, monitor initial engagement, respond to early interactions, and document any issues. → output: `launch-report.md`
3. **Daily Engagement** (bmad-social-media-strategist) — Run recurring daily tasks: respond to comments, engage with the audience, monitor mentions, and adjust strategy as needed. → output: `engagement-log.md`

### Phase 4: Campaign Analysis

**Lead agent:** bmad-growth-analyst

**Steps:**
1. **Mid-Campaign Review** (bmad-growth-analyst) — At campaign midpoint, analyze performance vs. targets, top performers, underperforming areas, and optimization recommendations. → output: `mid-campaign-report.md`
2. **Campaign Final Report** (bmad-growth-analyst) — At campaign end, deliver overall performance, platform breakdown, ROI analysis, learnings, and recommendations for the next campaign. → output: `campaign-final-report.md`

### Completion

When all phases are complete:
1. Append a final **Summary** section to `outputFile` listing all artifacts produced.
2. Suggest the next workflow the user might run: `bmad-growth-audit` to roll campaign learnings into the broader growth picture, or another `bmad-social-campaign` to keep momentum.
