# Latenca — sequential vs. spatial (the architecture decision)

You're right that "one future at a time" survived every round unquestioned. So let's not defend it — let's try to break it. The honest way to answer "is there a fundamentally different model hiding here?" is to **decompose "spatial" and see if any version is both (a) genuinely different from sequential and (b) viable for our goal.** If every version collapses, we don't just keep sequential — we *know why* it's forced, and that's real confidence.

## "Spatial" splits into exactly two things. Both collapse.

### (a) User-navigated space — dies on our own foundational truth.
A universe of walls the *user* moves through assumes the user can **steer toward their region.** But our bedrock truth is *taste is recognized, not described.* You cannot navigate toward a place you can't name. So a space hands the **search burden back to a user who can't carry it** — which is the *exact problem the entire product was built to remove.* It's the questionnaire and Scrub returning in a prettier costume: both died because they asked the user to specify/navigate a space they can only *react* to.

And it fights the one goal directly. For a **non-expert, one-time, 10-minute, money-on-the-line decision**, an open field of options is the worst possible structure:
- **Choice overload** → *lower* confidence, *more* regret, *less* likely to decide (this is well-established decision science, not opinion). Our goal is a confident, low-regret purchase; a universe of options actively lowers all three.
- **No natural stop.** A space is wandered forever; sequential has a crescendo and a landing. For a single-session close, closure is oxygen.
- **Effort.** Navigating is work; reacting is effortless. For a casual one-timer, effort is the enemy.
- **It kills the emotion we committed to.** "Surprising-yet-inevitable" is a *reveal* emotion — it requires the wall to be *presented* to you unexpectedly. If you navigated to it yourself, it's a *find*, not a surprise. Spatial trades our entire delight thesis for "I looked around."

### (b) AI-guided space — this *is* sequential, just with scenery.
If the AI flies you through the space (stopping at strong candidates, opening up the direction you like, receding the ones you reject), then the **decision structure is identical to sequential**: the AI leads, you react, it lands. It's opinion-first wearing a spatial *aesthetic*. That's a fine **presentation** choice (it can add the felt sense of a possibility-universe, and some delight) — but it is **not a different architecture.** The spine is still sequential.

### Therefore
There is no "spatial" that is both *different from sequential* and *viable*. It either (a) hands back the search burden — dying on the truth that taste is recognized, not described — or (b) reduces to sequential with nicer scenery. **Sequential/opinion-first is not an unexamined default. It is the forced consequence of our foundational truth.** That's the strong "no" you were hoping we could earn.

## But the challenge earned its keep — it exposed two real weaknesses of *pure* sequential.
Steelmanning spatial surfaces two things pure sequential genuinely lacks, and we should patch them:
1. **No overview → post-purchase FOMO.** A one-time buyer about to spend money wants to feel they've *seen the range* ("did I miss something better?"). A pure crescendo never shows the range → residual regret risk, the enemy of our goal.
2. **No agency for some users.** A minority want to feel they *explored and chose*, not "were led."

**The fix is a spatial *moment*, not a spatial spine.** At the landing — right when the wall becomes "the one," and exactly where regret-risk lives — briefly show a small, curated **"here's the range I explored for you"**: a handful of the genuine alternatives the AI seriously considered, arranged around the chosen wall, visibly *collapsing to it.* Five seconds. It delivers overview (no-FOMO), a beat of agency ("I looked — yes, this is it"), and it makes the choice feel *earned*, **without** front-loading paralysis and **without** becoming a browse-first store. Spatial as a **confirmation lens at the peak**, borrowing its one decisive benefit (no-regret via overview) at the one moment it helps.

## Where spatial genuinely belongs (so we're not blind to it)
Spatial *is* superior — for a **different user.** The ~5% pros (interior designers, Airbnb hosts, developers) are experts, have time, enjoy the process, want control and overview, and come back repeatedly. For them, navigating a possibility space beats being led. That's a future **"pro mode"**, a deliberately different product for a different segment — not the 90% single-session product. Knowing this keeps the door open without polluting the core.

## On novelty (the one legitimate pull toward spatial)
Sequential "one at a time" can look familiar (Tinder, feeds). But **the novelty was never in the topology.** "A designer keeps showing bold, complete walls on *your actual room* until one is inevitable" does not exist. Tinder swipes through other people; Latenca escalates through authored designs of *your space*. The novelty is the grounding + conviction + inevitability. And we can add visual novelty cheaply — spatial-flavored presentation (the AI-flown world) and the closing overview — *on a sequential spine.* We don't need to buy novelty with paralysis.

## Verdict — lock the architecture
- **Spine: sequential / opinion-first.** Forced by "taste is recognized, not described" and by the single-session confident-purchase goal. Confirmed, not assumed.
- **Patch: a spatial confirmation moment at the close** (the "range I explored" collapsing to the chosen wall) to steal spatial's one real benefit — no-regret overview — without its costs.
- **Deferred: spatial "pro mode"** for the ~5% expert/repeat users, as a separate later product.
- **Optional polish:** spatially-flavored *presentation* of the sequential flow for delight; a rendering decision, not an architecture one.

We challenged the last standing assumption and it held — for a precise, defensible reason. I'd now build the blueprint as written, with the one addition of the closing overview moment. Confidence in the architecture is high, and earned.
