# Latenca — the primitive, one level deeper (Keep)

## You're right about Scrub. Here's exactly why it fails.
Scrub is a **manipulation** primitive: one continuous gesture that navigates the design space. Manipulation primitives (pinch-zoom, drag-pan) only work when the space is **low-dimensional and the axes are obvious** — zoom is one axis, pan is two, everyone knows what they mean.

Wall design is the opposite: number of pieces, composition, scale, mood, framing, material, colour temperature, symmetry, negative space, whether it's even art at all. **High-dimensional, no natural axes.** Flattening that into one drag is an arbitrary projection — which is exactly your "which direction does what?" problem. So Scrub can't be *the* primitive. It's one lossy control.

The lesson generalizes: **for a high-dimensional creative space, the primitive can't be the user navigating it. It has to be the user *ratifying* an AI that navigates it for them.** That's precisely why Cursor is Tab and not a set of sliders.

## The primitive: **Keep**
> The AI makes one design move on your wall, live. You do one thing: **Keep** it (and it builds the next move on top) or **Pass** (and it makes a different move). The wall composes itself out of your Keeps.

That's the whole interaction. One tap. Its inverse (Pass) is its Esc.

You never navigate the space. You never pick an axis. You never specify anything. You watch a designer work in front of you at 10× speed, and your entire creative role is **choosing which of its moves to keep.** The wall is always complete, always one move ahead, always bending toward what you've kept.

This is your intuition made literal: *not changing the wall — continuing the designer's thinking.* Cursor doesn't ask what code to write; it proposes, you press Tab. Latenca doesn't ask what wall you want; it proposes a move, you Keep.

## Fill in the blank
> "Latenca is **the thing where your wall designs itself and you just keep the moves you love.**"

Or shorter, the way people will actually say it: **"you design a wall by saying yes."**

## Why this is Cursor-Tab and not a slot machine
A "next, next, next" feed would be a slot machine. Keep isn't, for three reasons — the same three that make Tab magic:
1. **It accumulates.** Every Keep becomes part of the wall and constrains the next move. Tinder forgets; Cursor *builds*. You're not browsing options — you're compounding a design.
2. **It predicts from context.** The AI doesn't offer a random move; it offers the single **most likely next move for *this* wall given everything you've kept** — the way Tab predicts *your* next keystrokes, not any keystrokes. It's one move ahead of your intent.
3. **Every state is complete.** After the first tap you already have a finished, beautiful wall (wow-first). Each move makes it *more yours*, never "under construction." You can stop at any moment and love where you are.

So the effort is inverted: the AI does the designing; you do the *editing by consent*. High-dimensional intent collapses into a stream of one-tap yeses — which is the only way a normal person can traverse a space they could never describe.

## The moves are the whole point (this is what kills "recommender")
Because the AI proposes *moves*, not *products*, the vocabulary is the entire wall: add a companion piece, go larger, swap to a mirror, warm the palette, introduce a shelf, add moulding, **remove something and leave it breathing empty.** A recommender can only hand you art. Keep lets the AI design the *space* — art is just one kind of move. The purchasable products are resolved only at the very end, as the implementation of the design you kept.

## Does Scrub survive? Honestly — no, not as the primitive.
Keep replaces it. Scrub survives only as an **optional manual override** for the one-in-twenty user who wants to hand-tune a single dimension (e.g. drag to resize the piece they kept). It's a power-user affordance, not the thing people remember. The category is defined by Keep.

## Updated analogy
| Product | The primitive | Its nature |
|---|---|---|
| Tinder | Swipe | ratify (browse) |
| Cursor | Tab | ratify + **accumulate** (build) |
| Midjourney | Vary | select + mutate |
| Google Maps | pinch + drag | manipulate (low-D) |
| ~~Latenca~~ ~~Scrub~~ | ~~drag the wall~~ | ~~manipulate (wrong: high-D)~~ |
| **Latenca** | **Keep** | ratify + accumulate — *design by consent* |

Latenca sits next to Cursor, not Tinder: both are **ratify-and-accumulate**. That's the family that turns "I could never build/design this myself" into "I just kept pressing one key and it appeared."

## One radical alternative I considered and rejected as *the* primitive
**Point-at-inspiration:** aim your camera at any room / painting / colour you love in the world, and your wall becomes a version of *its* spirit. It's genuinely magical — but it's an *input method*, occasional, not the always-on loop. It's a great **companion** to Keep (a way to seed the first move), not the primitive itself. I mention it so you know Keep won on merit, not by default.

## The one thing that makes or breaks it
Keep lives or dies on whether the AI's **next move is genuinely good and genuinely surprising-but-right** — a designer's move, not a safe averaging. If the moves are bland, Keep becomes a chore. If the moves make you go "oh, I wouldn't have thought of that, but yes" — it's the most addictive thing in the category. So the entire bet reduces to one capability: **a model that proposes the next design move like a designer with taste and a point of view.**

## Cheapest test (no screens, no code)
Take one real wall photo. By hand, play "Keep" for a real person: show a complete wall (move 1). They say keep/pass. You reveal the next move you'd make on top (move 2). Keep/pass. Do ~6 moves. Ask: *did it feel like a designer was working with you, one move at a time?* If yes — Keep is the primitive, and the only remaining question is model quality, not interaction design.
