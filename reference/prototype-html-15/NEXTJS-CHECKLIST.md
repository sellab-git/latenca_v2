# Latenca — checklista do realnego builda (Next.js)

> Prototyp (HTML/CSS w `C:\AI biznes\15. Latenca\`) ma **kompletny, spójny system wizualny** (typografia, kolory, odstępy, przyciski, pola, focus, ruch, z-index, cienie, breakpointy, badge, stany, WCAG AA light+dark, responsywność). Poniżej **warstwy, których statyczny prototyp NIE mógł objąć** — do zrobienia przy przepisywaniu na Next.js + Tailwind/shadcn + Supabase.
>
> Legenda priorytetu: 🔴 krytyczne (blokuje jakość/prawo) · 🟡 ważne · 🟢 dopieszczenie
> Stan na: 2026-07-07 · po ukończeniu prototypu (Explore v56 · Product v54 · Cart v28 · Creator v23)

---

## 1. Semantyczny HTML i komponenty
- 🔴 Zamień prototypowe `<span>`/`<a>` udające przyciski na prawdziwe `<button>` / `<Link>` (kafle, pigułki filtrów, nav, „Sort", „All filters"). W prototypie nie są osiągalne z klawiatury — w realnym kodzie muszą być.
- 🔴 Chrome (topbar, sidebar, search, tabbar) = **jeden współdzielony komponent** `<TopBar/>`/`<Sidebar/>`/`<TabBar/>`, nie kopiuj-wklej (prototyp miał 4 kopie → ryzyko dryfu, które sami łataliśmy).
- 🟡 Landmarki: `<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>` z `aria-label`.
- 🟡 Skip-link („Przejdź do treści") na początku `<body>`.

## 2. Dostępność (poza kolorem/focusem — te są zrobione)
- 🔴 **Klawiatura**: pełny tab-order, focus-trap w modalach/panelu filtrów, `Esc` zamyka, focus wraca do triggera.
- 🔴 **ARIA**: role/`aria-label`/`aria-expanded`/`aria-selected` na dropdownach, tabach, segmented, panelu filtrów, koszyku.
- 🔴 **Alt-texty**: każdy obraz dzieła = sensowny `alt` (tytuł + autor); dekoracyjne = `alt=""`.
- 🔴 **Formularze**: `<label for>` ↔ `id`, `aria-invalid`, `aria-describedby` do komunikatu błędu (`.msg` wzorzec gotowy w prototypie).
- 🟡 **Czytnik ekranu**: przetestuj przepływ zakupu (NVDA/VoiceOver).
- 🟡 **Reduced-motion**: prototyp wyłącza `transition` i `.skeleton`; w realnym kodzie wyłącz też animacje wejścia/room-zoom przy `prefers-reduced-motion`.
- 🟡 **Target size** (WCAG 2.5.8): przyciski 36–48 OK, ale sprawdź drobne ikony/„×"/qty na dotyku (≥24px).
- 🟢 Automatyczny audyt `axe` w CI.

## 3. Treść, stany i formularze
- 🔴 **Walidacja** (Zod na wejściu wg reguł projektu): email, adres, kod pocztowy — wpięcie w gotowy wzorzec `.field.err` + `.msg`.
- 🟡 **Stany** — wzorce są w prototypie (`.skeleton`, `.alert.ok/.err`, empty-state), trzeba je **wpiąć w realne dane**: loading galerii/produktu, błąd płatności, pusty koszyk/wyniki/brak prac twórcy.
- 🟡 **Toasty**: potwierdzenia akcji (dodano do koszyka, zapisano) — spójny system.
- 🟢 **UX writing**: przejście przez cały tekst (ton, etykiety-czasowniki: „Add to cart"→toast „Added"); i18n-ready (nie wklejać tekstu w obrazki/logikę).
- 🟢 **Formatery**: `formatCurrency()`/`formatDate()` z `lib/locale.ts` — nie hardcoduj `$`/`zł`/dat (reguła projektu). Prototyp ma częściowo `tabular-nums`.

## 4. Wydajność (Core Web Vitals 2026)
- 🔴 **Obrazy**: `next/image` — AVIF/WebP, `srcset`/`sizes`, `loading="lazy"`, `priority` na hero, placeholdery blur/LQIP (thumbhash). Prototyp ładuje surowo z Unsplash.
- 🔴 **Czcionki**: self-host (`next/font`) Lora+Inter, `font-display:swap`, subset — zamiast `<link>` do Google Fonts (usuwa FOUT „skoku logo", który ręcznie łataliśmy).
- 🟡 **CLS**: rezerwuj wymiary obrazów (aspect-ratio) — masonry musi mieć znane proporcje kafli.
- 🟡 **LCP/INP**: hero jako priorytet; virtualizacja długiej galerii (react-virtuoso) zamiast renderu wszystkiego.
- 🟢 Bundle: code-splitting panelu filtrów/lightboxa; sprawdź rozmiar.

## 5. Responsywność / techniczne
- 🟡 **Container queries** zamiast globalnych `@media` tam, gdzie komponent ma być niezależny od viewportu (karty, kafle). Prototyp używa media queries (6 breakpointów: 460/640/820/1024/1100/1440/2100).
- 🟡 **Safe-area** (iOS notch): tabbar już ma `env(safe-area-inset-bottom)`; sprawdź resztę sticky.
- 🟢 Test na **realnych urządzeniach** (nie tylko emulacja) — iOS Safari, Android Chrome, tablet.

## 6. Motywy / i18n
- 🟡 **Dark mode**: wykrywanie `prefers-color-scheme` + zapis wyboru (localStorage/cookie) + brak migotania (blocking script). Prototyp ma pełny dark (WCAG AA), ale przełącznik jest ręczny.
- 🟢 **i18n/RTL**: kod jest i18n-ready, ale angielski jest na sztywno; przy dodaniu języków — logical properties (`margin-inline`), `dir="rtl"` test.

## 7. SEO / meta (marketplace = ruch z Google)
- 🔴 `metadata` per strona: `<title>`, `description`, Open Graph, canonical.
- 🟡 **Structured data**: `Product`/`Offer`/`BreadcrumbList` JSON-LD (bogate wyniki dla dzieł).
- 🟡 `sitemap.xml`, `robots.txt`, obrazy OG per produkt/twórca.
- 🟢 Czytelne slugi URL (`/art/nebula-bloom`, `/creator/aria-vela`).

## 8. Migracja design-systemu (to jest gotowe — tylko przenieść)
- 🟢 Przenieś `:root` (bajt-identyczny w 4 plikach) do **jednego** źródła: `globals.css` CSS vars + `tailwind.config` (mapowanie tokenów). Wszystkie wartości już zdecydowane i zmierzone vs Ideogram/Displate/WCAG.
- 🟢 Systemy jako klasy/komponenty shadcn: Button (36/40/48), Input (40), Badge, Alert, Skeleton, Card (`--card-pad`).
- 🟢 Skrypty transformacji (`scratchpad/ds_*.py`) dokumentują KAŻDĄ decyzję tokenową — trzymać jako referencję.

## 9. Testowanie / jakość
- 🟡 Testy `lib/` (formatery, walidatory Zod) — reguła projektu.
- 🟡 Lighthouse + axe w CI (perf + a11y jako bramka).
- 🟢 Visual regression (Playwright screenshots) — mamy już nawyk weryfikacji pomiarowej.

---

### Czego NIE trzeba robić od nowa
Cały **system wizualny jest zdecydowany, spójny i sprawdzony** (16 warstw tokenów + stany + karty, WCAG AA light+dark, mobile/tablet/desktop bez overflow). Przepisanie = mechaniczne przeniesienie tokenów + owinięcie w prawdziwe komponenty React. Nie wymyślaj wartości od nowa — są w `:root` i w skryptach `ds_*.py`.
