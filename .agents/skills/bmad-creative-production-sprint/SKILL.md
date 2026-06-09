---
name: bmad-creative-production-sprint
description: Produce marketing images, video concepts, ad creative variations, social creative, thumbnails, product mockups, banners, and production briefs. Use when the user says "CPS" or needs creative production.
---

# Creative Production Sprint Workflow

**Goal:** Turn campaign strategy into platform-ready creative briefs and variations for ads, social, video, images, thumbnails, product mockups, and listing assets.

**Your Role:** Workflow facilitator coordinating with the Paid Media Buyer, Social Media Strategist, Content Architect, YouTube Strategist, TikTok Creator, Instagram Strategist, and Growth Analyst.

## References

- `references/ad-creative-char-limits.md` — Per-platform char limits (Google RSA, Meta, LinkedIn, X, TikTok, Pinterest, YouTube, Reddit), 8-angle taxonomy, 3-wave generation method (core / extend / wild card), creative quality bar. Required reading for Phase 2 and Phase 3.

## Prerequisites

This workflow consumes the shared marketing context. Before starting, run `bmad-create-marketing-context` (or confirm the file exists). If `{marketing_artifacts}/marketing-context.md` is missing, halt and invoke `bmad-create-marketing-context` first.

## Conventions

- Bare paths resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory.
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{skill-name}` resolves to the skill directory's basename.

## On Activation

### Step 1: Resolve the Workflow Block

Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`

**If the script fails**, resolve the workflow block from base, team, and user customization files using BMad structural merge rules.

### Step 2: Execute Prepend Steps

Execute `{workflow.activation_steps_prepend}`.

### Step 3: Load Persistent Facts

Treat `{workflow.persistent_facts}` as foundational context. Load `file:` entries.

### Step 4: Load Config

Load `{project-root}/_bmad/performance-marketing/config.yaml` and resolve `{user_name}`, `{communication_language}`, `{document_output_language}`, `{company_name}`, `{primary_channel}`, and `{marketing_artifacts}`.

### Step 5: Greet the User

Greet `{user_name}`, speaking in `{communication_language}`. Ask which creative outputs are needed: image, video, ad variations, social graphics, thumbnails, product mockups, banners, or full creative matrix.

### Step 6: Execute Append Steps

Execute `{workflow.activation_steps_append}`.

Activation is complete. Begin the workflow below.

## Paths

- `outputFile` = `{marketing_artifacts}/creative-production-sprint.md`

## Execution

✅ Speak in `{communication_language}` and write artifacts in `{document_output_language}`.

### Phase 1: Creative Brief

**Lead agent:** bmad-paid-media-buyer (collaborates with bmad-content-architect for asset-side input)

1. **Campaign Context** — Capture objective, audience, offer, channel, format, placement, product proof, constraints, and brand rules. → output: `creative-brief.md`
2. **Angle Matrix** — Define 3-5 creative angles with hook, promise, proof, objection, CTA, and hypothesis. Present angles and selected priority for user approval before drafting variants. → output: `creative-angle-matrix.md` → gate: `user_approval`

### Phase 2: Copy & Asset Variations

**Lead agent:** bmad-paid-media-buyer (collaborates with bmad-social-media-strategist for organic adaptations)

1. **Ad Creative Variations** — Produce headlines, primary text, descriptions, CTA variants, and platform-specific adaptations. → output: `ad-creative-variations.md`
2. **Image Briefs** — Produce image prompts/briefs for blog heroes, social graphics, product mockups, profile banners, listing visuals, and ad images. → output: `image-creative-briefs.md`
3. **Video Briefs** — Produce short-form, demo, explainer, ad, UGC, avatar, or programmatic video scripts and shot lists. → output: `video-creative-briefs.md`

### Phase 3: Platform Adaptation

**Lead agent:** bmad-social-media-strategist

1. **Channel Specs** — Adapt creative to X, LinkedIn, Instagram, TikTok, YouTube, Pinterest, Reddit, Discord, Google, Meta, and LinkedIn Ads as needed. → output: `platform-creative-specs.md`
2. **Thumbnail & First-Frame Plan** — For video/social, define thumbnail, first frame, 3-second hook, retention beats, captions, and CTA. → output: `thumbnail-first-frame-plan.md`

### Phase 4: Testing & Production Handoff

**Lead agent:** bmad-growth-analyst

1. **Creative Test Plan** — Define creative hypotheses, test cells, minimum viable variants, measurement, and cut/scale rules. → output: `creative-test-plan.md`
2. **Production Checklist** — Define file names, sizes, aspect ratios, accessibility, compression, alt text, UTM/linking, approval, and QA. Block release until every spec and accessibility item is checked. → output: `creative-production-checklist.md` → gate: `creative_qa`

### Completion

Append a final **Summary** to `outputFile`, then recommend `bmad-paid-acquisition-sprint`, `bmad-social-campaign`, or `bmad-content-pipeline`.

