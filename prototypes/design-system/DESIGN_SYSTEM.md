# Latenca — design system

> Tokeny przeniesione **1:1 z projektu 15** (decyzja Artura 2026-07-19, opcja b: nasz system, akcent lawendowy #7C6CF0).
> Wartości nie zmieniamy. **Mobile-first dotyczy UŻYCIA**, nie wartości tokenów.
> Plik tokenów: [`tokens.css`](tokens.css)
> **Design system w akcji = realne ekrany z projektu 15** w [`../reference/prototype-html-15/`](../reference/prototype-html-15/) (Home, Explore, Product, Cart, Collections, Artists…). To one są wzorcem wyglądu — nie osobne demo. Tokeny tu są z nich wyodrębnione 1:1.

## Kolory
| Rola | Light | Dark |
|---|---|---|
| Tło `--bg` | #F6F3ED | #0F0E13 |
| Panel `--panel` / `--panel2` | #FBF9F5 / #F1EDE4 | #17151E / #1E1B26 |
| Tekst `--ink` | #1A1917 | #F2F0EA |
| Wyciszony `--muted` / `--faint` | #6E695F / #8C8578 | #9A94A4 / #6E6879 |
| Linia `--line` | #E7E2D8 | #272432 |
| **Akcent `--accent`** | **#7C6CF0** | #8E7DF3 |
| Akcent-tekst `--accent-ink` | #5F4DE0 | #8E7DF3 |
| Akcent-tło `--accent-soft` | #ECE6FA | #221E33 |
| Media (tło obrazu) `--media` | #E7E0D3 | #1b1826 |
| Status `--ok` / `--err` | #3f9d6d / #c0553f | (err #e0715c) |

Reguła: akcent-**tekst** = `--accent-ink` (kontrast AA); akcent-**wypełnienia/obwódki** = `--accent`.

## Typografia
- Serif nagłówki: **Lora** (`--serif`). Sans UI/tekst: **Inter** (`--sans`).
- Skala: `--fs-2xs:11 · --fs-xs:12 · --fs-sm:13 · --fs-base:14 · --fs-md:16 · --fs-lg:20 · --fs-xl:24 · --fs-2xl:32`.
- Waga: tylko 3 — `--w-normal:400 · --w-medium:500 · --w-semibold:600` (bez 700, „calm").
- Line-height: `--lh-tight:1.2` (nagłówki) · `--lh-base:1.5` (tekst).

## Przestrzeń, promień, przyciski
- Spacing 4pt: `--sp-1..--sp-12` (4/8/12/16/20/24/32/48).
- Promień wg roli: `--r-tile:2` (kafle druku, ostre) · `--r-sm:4` (chipy) · `--r-ui:6` (kontrolki/przyciski) · `--r-full` (pigułki).
- Przyciski — 3 stałe wysokości: `--btn-sm:36 · --btn-md:40 · --btn-lg:48`.
- Ikony touch-first: `--icon:20 · --iconbtn:40`.

## Elewacja, ruch, warstwy
- Cienie: `--shadow-1/2/pop/drawer/bar`. Focus: `--focus-ring:2px solid var(--accent)`.
- Ruch: 3 czasy `--dur-fast/base/slow` + 2 easingi `--ease/--ease-out`. Respektujemy `prefers-reduced-motion`.
- Z-index: `--z-sticky:100 → --z-toast:700`.

## Motyw
`html[data-theme="light"|"dark"]` przełącza tokeny. Oba motywy przetestowane pod WCAG w 15.

---

## Reguły MOBILE-FIRST (to jest nowe w projekcie 18)
Projekt 15 był desktop-first. Tu projektujemy **od 390px w górę**. Zasady (z SPEC §8, 🔬 zweryfikowane):

1. **Projektuj na telefon najpierw.** Bazowy layout = jedna kolumna, 390px. Desktop = progresywne wzbogacenie (`min-width`), nie odwrotnie.
2. **Jedna decyzja na ekran.** Prowadzony przepływ (step-flow), nie gęsta powierzchnia (🔬 Baymard: +do 35% konwersji).
3. **Akcje w dolnej 1/3 ekranu** — zasięg kciuka. Główne CTA = sticky bottom bar (`--shadow-bar`).
4. **Cele dotykowe ≥44px.** Domyślne przyciski na mobile = `--btn-lg` (48) dla głównych akcji; `--btn-md` (40) tylko dla drugorzędnych z zapasem hit-area.
5. **Góra ekranu = strefa nieosiągalna kciukiem** — nie umieszczaj tam akcji krytycznych.
6. **Nie freeform-drag** (🔬 NN/g: touch-drag multi-obiekt = pułapka).
7. **Bezpieczne strefy i jednostki mobilne:** `dvh`/`svh` zamiast `vh`, `env(safe-area-inset-*)` na paskach sticky.
8. **Obrazy:** miniatury pod rozmiar (`srcset`/`sizes`), `loading=lazy`; pełna rozdzielczość tylko do druku (serwer).

## Breakpointy (drabinka)
Bazowo bez media-query (mobile). W górę dokładamy: **460** (mały telefon→standard) · **768** (tablet) · **1024** (laptop/desktop). Prototyp 15 miał gęstszą drabinkę desktop-first (640/820/1024/1100/1440/2100) — w 18 zaczynamy odwrotnie i dokładamy tylko realnie potrzebne progi.
