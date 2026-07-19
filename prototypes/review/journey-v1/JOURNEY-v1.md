# Latenca — AI Design Journey (v1)

## What this is
This is the core product, not the website. The user has clicked **"Design my wall"** on the Home screen; this is everything from that click up to the moment they think *"this is exactly what I was looking for"* — right before purchase.

The product is **a consultation with an AI-assisted interior designer.** Deliberately NOT a shop, NOT a chatbot, NOT a configurator. It runs in its own calm, focused environment (no shop chrome) so the user feels they've entered a conversation, not a catalog. Same locked visual system as the Home (Lora serif + Inter, warm palette, lavender accent). It's a clickable prototype; the 16 screenshots are all 8 steps in desktop (1280) and mobile (390).

## Design principles applied to every screen
- **One decision per screen** — never a wall of choices.
- **The designer speaks in first person** ("Then I think this belongs on your wall") — a guiding presence, not a chat bubble.
- **Every decision is explained** — the user always sees *why*.
- **A confidence meter rises through the journey** (72% → 86% → 92% → 93% → 95%), shown in the top bar — it makes progress toward certainty visible.
- **Reassurance throughout** ("nothing is charged", "no sign-up") to remove risk.

## The flow (8 steps)
1. **Your room** — "Which room are we working on?" One warm first choice; sets scale and mood.
2. **Your wall** — "Show me the wall — I'll size everything to fit." Upload a photo (optional) or pick a width; a hint explains it's above a sofa so the piece won't crowd it.
3. **Your taste** — "Pick the ones you're drawn to." A **visual taste calibration** (react to images), the way a stylist reads your eye — not a style questionnaire.
4. **Reading your space** — the AI shows **what it understood**: "Warm natural light → soft pieces glow here", "Oak & linen tones → you lean earthy", "Your picks read minimal & calm", "~2m sofa wall → one larger piece balances best". This is the first trust moment; **the confidence meter appears here (72%)**.
5. **Your style** — "Here's what I'm hearing: **Japandi** — did I get you right?" The user confirms (or nudges tags). The key trust checkpoint before any product is shown. (86%)
6. **Your recommendation** — **one** best piece, **shown on a wall like yours**, with three explained reasons (right scale / picks up your palette / soft & calm) and a "92% match" chip. Inline **refine** nudges (Calmer / Bolder / Warmer / Larger / Different subject) actually rework the piece and the designer responds. "Curated, not crowded." (92%)
7. **Make it yours** — guided fine-tuning of size / frame / finish. Each option carries the designer's **recommendation + reason** ("Oak echoes your furniture", "Matte kills glare from your window light"), with a **live preview on the wall**. A guided decision, not a bare configurator. (93%)
8. **Your wall** — the finished wall in the room, a clear summary (size, frame, finish, total, everything included), and **confidence 95%** — the "exactly what I was looking for" payoff. The CTA "Make it real" is the hand-off to purchase (downstream).

## How it meets the product goals
- *AI understands my space* → Step 4 shows its reading of the room.
- *AI understands my taste* → Steps 3 + 5 (visual calibration + confirmed style profile).
- *AI explains every decision* → reasons on the recommendation and on every customize option.
- *AI guides step by step* → 8 steps, progress bar, one decision at a time.
- *AI removes uncertainty* → rising confidence meter + "nothing charged yet".

## Open questions for feedback
1. Is the flow the right length — should taste (step 3) have more rounds, or is one enough before the analysis?
2. The recommendation shows the art composited on a stock room. Would a real **photo upload → your actual wall** preview meaningfully raise trust, or is "a wall like yours" enough for v1?
3. Should there be a visible **"before → after"** (blank wall → designed wall) moment to dramatize the transformation?
4. Is the confidence meter helpful and credible, or does an explicit percentage feel gimmicky?
5. Where exactly should purchase begin — is "Make it real" on step 8 the right seam, or should price/checkout details start entering earlier?
