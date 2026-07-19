# Latenca — Home SCREEN_01, v3 (product-led rearchitecture)

This is a response to the product-design review. The ask was to stop treating Home like a premium shop and make it read like a **product** — the AI Wall Designer — whose job is to give the user *confidence in a decision*, not to sell images. I kept the visual language, tokens, components, colors, typography and premium/editorial character exactly as approved. Nothing about the look changed. What changed is the **information architecture, UX and narrative.**

Static HTML mockup, desktop-first, fully responsive (sidebar → bottom tab bar on tablet/mobile).

## The core problem I was solving
The previous Home showed the product on ~15% of the page (one "Design my wall" card + a few AI chip labels). The rest — Shop by room, Curated sets, Featured artists, Browse by category, and a large "Discover" masonry gallery — was a **catalog tour**. The Discover gallery in particular ("browse hundreds of images") directly contradicts the product's promise ("you don't have to browse — we'll pick"). So the page still sold **artwork**, not the **result**. AI was decoration on a shop, not the spine.

## New architecture — a question-driven product story
Every section now answers one user question, in order:

| # | Section | Question it answers | What the user should think |
|---|---------|---------------------|----------------------------|
| 1 | **Hero** — "Your AI wall designer" / "Art you'll be sure about" + primary CTA + trust stat | Will someone help me? | "This is a tool that helps me decide, not a shop." |
| 2 | **"How Latenca chooses for you"** — a real intelligence demo | How does it work? Is it actually smart? | "It understands my space — this isn't random." |
| 3 | **"It adapts to your space"** (rooms, reframed) | Will it work in MY space? | "It'll work for my room and taste." |
| 4 | **"People who weren't sure either"** (reviews) + **"The eyes behind your recommendations"** (artists as curators) | Can I trust it? | "People like me trusted it and it worked; real people curate it." |
| 5 | **"You don't get a poster. You get a wall."** (gallery walls + quality band) | What do I get? | "A complete, high-quality wall — not a single poster." |
| 6 | **"Ready to design your wall?"** — final CTA + secondary browse links | How do I start? | "Okay, I'll start." |

## The centerpiece — Section 2 (the intelligence demo)
Instead of generic "how it works" icons, this section demonstrates the product as three real product-UI fragments:
1. **You describe your space** — example answer chips (Living room · Above the sofa · Warm & calm · Oak + linen).
2. **Latenca reads your style** — a "Style profile" card: **Japandi** + tags (Warm · Minimal · Natural · Calm) + a **Style match 92%** confidence bar.
3. **It recommends — with reasons** — a recommendation card: the artwork + a **94% match** chip + three explained reasons ("The right size for a sofa wall", "Complements your oak & linen palette", "Creates the calm you asked for").

This is the answer to "why Latenca isn't just another art shop": it visibly understands the space and recommends *with reasons and confidence* — something Desenio / Poster Store / Etsy can't show.

## What I removed (deliberately)
- **The "Discover" masonry gallery** — the most shop-like block; it contradicts the product promise and is a pure "more products" ecommerce reflex.
- **"Browse by category"** — catalog-navigation reflex.
- The old "Let's design your wall" card + generic "How it works" — their role is now carried by the hero CTA + the real demo.
- The dead JS/data behind those sections.

## What I reframed (same components, product narrative)
- Rooms → "It adapts to your space" (proof of fit, not "shop by room").
- Curated sets → "You don't get a poster. You get a wall." (the outcome).
- Featured artists → "The eyes behind your recommendations" (human-curation credibility, not a browse destination).

## What I kept
The full visual system, all components, and every kept section from the review (three entry paths now live as hero CTAs + secondary links; curated collections; rooms; artists; reviews; quality guarantees).

## Result
The page is ~28% shorter, tells a single story, and closes on the product rather than a gallery. Catalog browsing survives as secondary links for the minority who want to self-serve.

## Open questions for feedback
1. Is Section 2 (the demo) convincing enough as "proof of intelligence", or should it go further (e.g. an interactive-feeling before/after of a blank wall becoming a designed wall)?
2. I put a light trust stat in the hero ("4.8 · 2,400+ walls designed") but kept the full proof section lower — right call, or should heavier proof come earlier?
3. Removing the Discover gallery is the boldest cut. Do you agree the product story is stronger without an on-page "browse hundreds" section?
