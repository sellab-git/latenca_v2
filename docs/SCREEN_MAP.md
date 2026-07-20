# Latenca — mapa ekranów (Faza 2, wersja definitywna)

> ⚠️ **Zastępuje pierwszą wersję** (oparta była na 2 mockupach — niepełna). Ta wersja oparta na **WSZYSTKICH 17 mockupach z 17** (obejrzane 2026-07-19) + realne ekrany 15.
> Reguła: **15 = rzemiosło (wygląd/komponenty/design system, akcent lawendowy #7C6CF0), 17 = flow (podróż/framing/koncept).**
> Materiał referencyjny: `reference/mockups-17/` (flow) + `reference/prototype-html-15/` (wygląd).

---

## Najlepsze mockupy 17 (do wzorowania)
- **02_18_49 PM** i **02_09_50 PM** — pełny **15-ekranowy flow**, responsywny (mobile/tablet/desktop). Master-referencja.
- **05_12_26** — kompletna ścieżka 20 ekranów w 5 fazach (z po-zakupie).
- **05_12_28** — czysta, angielska, 10 ekranów, produkcyjna.
- **10_44_00 / 10_34_04** — wersja z **Confidence score** przez całą podróż + AR + „wszystko w cenie".
- **01.06 / 01.07 / 01.08** — najbogatsze Home (ścieżki intencyjne + Trustpilot + kolekcje).

---

## Model: TRZY DRZWI, jeden cel (z 02_09_50)

```
                          HOME
          ┌──────────────┼──────────────┐
   Design My Wall    Browse Collection   Get Inspired
     (DORADCA)          (katalog)        (real homes)
          └──────────────┼──────────────┘
                          ▼
              PRODUKT (pojedynczy LUB Set of N)
                          ▼
              PROJEKT ŚCIANY ("My Living Room Wall")
                          ▼
              KOSZYK → CHECKOUT → SHIPPING → PAYMENT → POTWIERDZENIE
                          ▼
              PO ZAKUPIE (track order · ocena)
```

Wszystkie trzy drzwi schodzą się w tym samym produkcie/projekcie/koszyku → jeden produkt, nie zszyte.

---

## Zasady przewodnie (spójne we WSZYSTKICH mockupach 17 — bierzemy)
1. **AI prowadzi, TY decydujesz** — pewność ponad szybkość.
2. **Jedna najlepsza rekomendacja, wytłumaczona** — nie lista. „Curated, not crowded."
3. **Zaufanie NA POCZĄTKU** — AI pokazuje, jak myśli (Analiza) i co zrozumiał (Style Profile), ZANIM pokaże produkt.
4. **Rosnąca gotowość jako element UI** — ale **bez procentu** (D-026): wewnętrzny `readiness`, a dla użytkownika stan jakościowy nazywający brakującą daną („brakuje mi tylko szerokości ściany, żeby dobrać rozmiar"). *(Mockupy 17 pokazywały tu Confidence score 68%→92%→93% — odrzucone, bo procent sugeruje precyzję statystyczną, której system nie ma.)*
5. **Max 3 opcje na decyzję.** Naturalny język.
6. **Podgląd przed zakupem** — Wall View (v1) / AR Preview (później).
7. **Produkt to często ZESTAW/ściana** — silnik koszyka (COSTS.md).

---

## Ekrany v1 — pełna lista (z master-flow 15 ekranów)

### A. WEJŚCIE
**1. HOME** — „Beautiful walls. Made simple. Curated wall art for every home."
- 3 ścieżki: **Design My Wall** (AI-guided) / **Browse Collection** / **Get Inspired**
- Featured Collections (Japandi/Modern/Classic/Abstract/Botanical) · trust strip (Curated by experts / AI understands you / Quality you can trust)
- **15 (wygląd):** realny Home 15 ma już te sekcje (benefit, browse-by-category, curated sets, featured artists, real homes) — używamy ich komponentów.
- **ZMIANA vs 15:** framing „THE AI ART MARKETPLACE / thousands of AI artworks" → „Beautiful walls. Made simple." + trzy ścieżki (zamiast jednego „Explore the gallery").

### B. ŚCIEŻKA DORADCY (rdzeń — brak w 15, budujemy nowy na naszym design systemie)
**2A. AI Start (intencja)** — „What would you like help with?": *I have a blank wall / I already have artwork / I'm looking for inspiration / I'm not sure — surprise me* (z 01.06–08, miniatury).
**2B. Upload Wall** — „Let's see your wall" + zdjęcie (opcjonalnie) / Skip.
**2C. AI Analysis** — „Analyzing your space… 68%" (Understanding room / Analyzing style / Considering goals / Preparing). ~20s.
**2D. Style Profile** — „Here's your style: **Japandi** — Warm·Minimal·Natural·Calm. Is this right? Yes / Not quite." (stan gotowości: „wystarczy, żeby zaproponować kierunek" — bez procentu, D-026)
**2E. Best Recommendation** — „I think this will look best" + **why** (perfect size / complements colors / creates calm) + *This is perfect / Show another / Feedback*. (stan gotowości: „gotowe do rekomendacji kompozycji" — bez procentu, D-026)
**2F. Iterate** — „What would you like to change?": Brighter / More colorful / Larger / More minimal / Different style / Different mood + wolny tekst.
**2G. Customize** — „Let's make it perfect": **Layout / Size / Frames / Spacing** + suwak odstępu (8cm). Prowadzone dostrajanie, **NIE canvas**.
**2H. Preview** — Wall View / AR Preview + „Looks amazing!" + stan gotowości **„wszystko, czego potrzebuję"** (bez procentu — D-026).
→ Produkt.

### C. ŚCIEŻKA PRZEGLĄDANIA + INSPIRACJI
**3A. Browse Collection** — „Collections" (All/Popular/New/Minimal/Classic): Japandi 54 / Modern 68 / … + katalog (search + Abstract/Nature/Minimal/B&W) z „Need advice? Ask AI Designer".
  - **15 (wygląd):** `Latenca-Explore.html` + `Latenca-Collections.html`.
**3B. Get Inspired** — „Real homes. Real inspiration" (Living Room/Bedroom/Dining, @handles).
  - **15 (wygląd):** sekcja „real homes" + `Latenca-Artists.html` (atrybucja).
→ Produkt.

### D. PRODUKT + ZAKUP (wspólny cel)
**4. Product Detail** — pojedynczy LUB **„Set of 3 Art Prints — $189"**. Size (50×70/70×100/…), Frame (Black/Oak/White/No frame), print options, „AI Designer can help (Will this fit / Show on my wall / Find matching)". Add to project/cart.
  - **15 (wygląd):** `Latenca-Product.html` (bogaty). Pogodzić z osiami z SPEC. Ceny z COSTS.md.
**5. Your Project** — „My Living Room Wall, 3 items" + „Add another item". = obiekt „projekt ściany".
**6. Cart** — pozycje, Subtotal/Shipping(FREE)/Total, „View project". (15: `Latenca-Cart.html`)
**7. Checkout → Shipping → Shipping Method → Payment → Order Confirmed**
  - Shipping method: Standard (5–7 dni) FREE / Express (2–3) $15 / Priority (1–2) $25.
  - Payment: Apple Pay / G Pay / PayPal / karta (zgodne z decyzjami checkoutu).
  - „Thank you, Artur! Order #LTN-45872."

### E. PO ZAKUPIE
**8. Track order** (Order confirmed → In production → Shipped → Out for delivery → Delivered).
**9. Rate** — „How do you feel about your new art?" + feedback (zasila rekomendacje).

---

## Nawigacja dolna (mobile, z 17)
`Home · Browse · Projects · Wishlist · Profile` (AI Designer dostępny kontekstowo „Ask your AI Designer" + jako ścieżka z Home).

## Czego NIE ma w v1
⛔ canvas-builder (zastąpiony krokiem Customize) · ⛔ Creator/upload (marketplace = faza 2; artysta = atrybucja) · ⛔ prawdziwa logika AI (mockup udaje ekranami) · ⛔ prawdziwe AR (v1 = Wall View 2D / upload zdjęcia) · ⛔ backend.

## Kolejność budowy (Faza 3, propozycja)
1. **Home** (trzy drzwi, przeframowany) — pokazuje cały koncept
2. **Ścieżka doradcy 2A→2H** (rdzeń, największy wyróżnik, ze stanami gotowości — D-026)
3. **Product Detail** (+ Set)
4. **Your Project → Cart → Checkout** (zakup)
5. **Browse / Collections / Get Inspired**
6. Track order / Rate (lżejsze)

Każdy ekran: mobile-first (390px), na `design-system/tokens.css`, wygląd z realnych ekranów 15, flow z master-mockupów 17.
