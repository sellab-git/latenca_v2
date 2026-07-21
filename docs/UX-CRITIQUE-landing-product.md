# UX CRITIQUE — landing + product (krytyczny przegląd, 2026-07-21)

> Pytanie Artura: *„czy to faktycznie najlepsze z najlepszych UX/UI, jakie możemy mieć?"*
> Metoda: przejść oba ekrany krytycznie, z każdej strony — wracając do Ideogram/Midjourney (`RESEARCH-generators.md`) i Mixtiles/Fy! (`RESEARCH-wall-display.md`) i do **scenariuszy, z jakimi ludzie do nas trafiają**.
> Ton: celowo krytyczny. Co jest dobre — na końcu.

## Werdykt w jednym akapicie

Fundament jest **solidny**: jeden szkielet, czysty katalog, ciepła rozpoznawalna paleta (nie generyczny „AI look"), trafne 3 ekrany, płaska ściana jako powierzchnia (poparte badaniem). Ale **to jeszcze nie „najlepsze z najlepszych"** — z dwóch konkretnych powodów, oba strategiczne, nie kosmetyczne:
1. **Nasz wyróżnik (doradca) jest na landingu prawie niewidoczny.** Wyglądamy jak kolejny sklep z grafiką.
2. **Nie odpowiadamy jeszcze zdecydowanie na blokadę zakupową nr 1 — „czy to będzie dobry rozmiar"** — tak dobrze, jak robią to liderzy jedną prostą rzeczą (nakładka wymiarów).

---

## 1. Scenariusze — z czym ludzie faktycznie lądują i czy ich obsługujemy

| Scenariusz (z czym przychodzą) | Jak częsty | Obsługa dziś | Ocena |
|---|---|---|---|
| „Chcę coś **na konkretne miejsce**" (nad kanapę, nad łóżko) | bardzo częsty | „Room" schowany w „All filters"; doradca to mały link | **słabo** — miejsce to główny motyw wejścia, a jest ukryte |
| „**Poprzeglądam**, znajdę coś, co mi się spodoba" | bardzo częsty | katalog + filtry — dobrze (jak feed Ideogram/MJ) | **dobrze** |
| „Mam **konkretny styl/temat**" | częsty | search + kategorie | **dobrze** |
| „**Nie wiem czego chcę, pomóżcie**" | częsty — to nasz rdzeń | doradca, ale wejście = mały tekst „or let Latenca design your wall" | **słabo** — najważniejszy dla nas scenariusz ma najsłabsze wejście |
| „Trafiłem **z Google prosto na produkt**" | częsty (SEO) | strona produktu + doradca | **ok** |
| „**Prezent**" | średni | brak jakiegokolwiek wątku prezentowego | **brak** (świadomie? do decyzji) |
| „Chcę zobaczyć **w moim pokoju**" (upload) | średni | świadomie nie robimy montażu (D-031/033) | **ok** — słusznie, bo montaż zawodzi (Fy! to potwierdza) |

**Wniosek:** dwa najczęstsze i najważniejsze dla nas motywy wejścia — **„na konkretne miejsce"** i **„pomóżcie wybrać"** — mają dziś **najsłabsze wejście na landingu.** To nie detal, to sedno.

---

## 2. Problem #1 — wyróżnik jest niewidoczny (najważniejsze)

Ideogram i Midjourney **prowadzą swoim wyróżnikiem**: całe ich lądowanie to pole „stwórz". My prowadzimy **wyszukiwarką** (górny pasek), a naszego wyróżnika — doradcę — schowaliśmy do **małego linku tekstowego** pod nagłówkiem.

Skutek: pierwszy odwiedzający widzi *„jeszcze jeden sklep z grafiką z wyszukiwarką i filtrami"*. Nic nie sygnalizuje, że to my **zaprojektujemy z nim ścianę** — a to ma być nasza fosa (D-025). **Sprzedajemy siebie jako commodity, a nie jako to, czym naprawdę jesteśmy.**

Napięcie do rozwiązania (nie łamiąc locków):
- D-022: doradca to „drzwi frontowe, **nigdy bramka**". ✅ zostaje.
- D-036/037: search zostaje wyszukiwarką, doradca osobno. ✅ zostaje.
- ALE „drzwi frontowe" i „mały link w tle" to nie to samo. Wyróżnik może być **wyeksponowany bez bramkowania.**

→ **Rekomendacja (wysoki priorytet):** doradca dostaje **prawdziwe, zapraszające wejście** na landingu — nie tekstowy link, tylko wyraźny element (kafel/pasek „Nie wiesz, co pasuje? Zaprojektujemy ścianę z Tobą →"), obok katalogu. Search zostaje skrótem „wiem, czego chcę". To jedyna zmiana, która realnie sprzedaje to, czym jesteśmy.

---

## 3. Problem #2 — „czy to będzie dobry rozmiar" (blokada zakupowa nr 1)

`RESEARCH-wall-display.md` mówi wprost: skala to **jedyne pytanie**, na które podgląd ma odpowiadać, i liderzy odpowiadają na nie **jedną prostą rzeczą — nakładką wymiarów**:
- **Mixtiles:** ikona „linijki" → etykiety w cm + wymiar całości ze strzałkami („79 × 122 cm"). Karty katalogu też noszą wymiar.
- **Fy!:** przełącznik `Measure` → fizyczne wymiary ze strzałkami na grafice („102 × 76 cm").

My **mamy** prawdziwą skalę w cm (D-035) i pokoje — ale to skala *dorozumiana* (obraz jest we właściwej wielkości względem mebla). **Nie mamy wyraźnej, włączanej nakładki „50 × 70 cm" ze strzałkami** — czyli jawnej odpowiedzi na to jedno pytanie. Liderzy uznali, że dorozumiana skala nie wystarcza; dlatego dołożyli linijkę.

→ **Rekomendacja (wysoki priorytet):** dodać na scenie **przełącznik „Wymiary" (Measure)** — strzałki + „50 × 70 cm" na grafice, jak Mixtiles/Fy!. To najtańsza rzecz, która wprost rozbraja blokadę zakupową nr 1. Input (szerokość ściany) i tak zbieramy w doradcy (D-023) — mamy z czego liczyć.

---

## 4. Mniejsze, ale realne uwagi UX/UI

- **Karty katalogu pokazują tylko tytuł + autora** — zero sygnału o rozmiarze/cenie. Dla sklepu z drukiem, gdzie rozmiar to blokada nr 1, warto dać na karcie choć **wymiar/„od $X"** (Mixtiles daje wymiar). Drobne, ale pomaga.
- **Lead jest bardzo cienki — być może za bardzo.** Ścięliśmy CAŁE zaufanie (D-038). Zimny odwiedzający nie wie, że mamy druk muzealny, produkcję na zamówienie, doradcę. Nie chodzi o powrót starej Home — chodzi o **jedną linię**, która mówi *dlaczego my* (albo eksponuje doradcę — patrz #2).
- **„Set your wall colour" — najlepszy trik Fy!** (`Flat` = ściana w kolorze Twojej ściany, zero ryzyka montażu). Możemy dać prosty wybór koloru ściany dla płaskiej powierzchni — tania personalizacja, którą badanie wskazało jako *działającą*.
- **Search vs doradca konkurują o uwagę** — dziś search wygrywa (jest w pasku), doradca przegrywa (link). Patrz #2: wyeksponować doradcę jako *zaproszenie*, search jako *skrót*.
- **Prezent** — cały wątek nie istnieje. Do świadomej decyzji: czy „na prezent" to nasz scenariusz (POD-giftowe to duży rynek), czy świadomie go pomijamy w MVP.

---

## 5. Co jest naprawdę dobre (uczciwie)

- **Jeden szkielet z jednego źródła** (shell.js + app.css) — zmierzone 0 różnic. To solidny fundament.
- **Katalog** — czysty, gęsty, natychmiastowy; logika Ideogram/MJ w naszym ciepłym systemie, nie kopia ich wyglądu.
- **Płaska ściana jako powierzchnia** (D-033) — poparte obserwacją, że u liderów to prymarna powierzchnia, a render pokoju zawodzi.
- **Doradca jako jeden ekran/dwa stany** (D-034) — elegancko rozwiązuje „skok" advisor↔produkt; reakcja‑nie‑specyfikacja (chipy „cieplejsze/spokojniejsze") to dobry prymityw.
- **3 ekrany** — właściwa minimalna ścieżka.

---

## 6. Rekomendacje wg (wpływ × koszt)

| # | Zmiana | Wpływ | Koszt | Priorytet |
|---|---|---|---|---|
| 1 | **Wyeksponować doradcę na landingu** jako prawdziwe wejście (kafel/pasek), nie link | bardzo wysoki (sprzedaje wyróżnik) | niski | **teraz** |
| 2 | **Nakładka „Wymiary" na scenie produktu** (strzałki + cm) | wysoki (blokada zakupowa nr 1) | niski‑średni | **teraz** |
| 3 | Karty katalogu: dodać wymiar / „od $X" | średni | niski | wkrótce |
| 4 | „Ustaw kolor swojej ściany" dla płaskiej powierzchni | średni | niski‑średni | wkrótce |
| 5 | Jedna linia „dlaczego my" w leadzie (bez powrotu starej Home) | średni | niski | wkrótce |
| 6 | Decyzja: czy obsługujemy scenariusz „prezent" | do rozstrzygnięcia | — | do decyzji |

---

## 7. Jedno strategiczne pytanie do Ciebie

Najgłębszy wybór, który za tym stoi: **czy landing prowadzi katalogiem (sklep), czy doradcą (nasz wyróżnik)?**
- Dziś: katalog‑first, doradca w tle. Bezpieczne, ale ukrywa to, czym jesteśmy.
- Alternatywa: katalog‑first, ale doradca **wyraźnie zaproszony** (rekomendacja #1) — sprzedajemy wyróżnik, nie bramkując.
- Radykalniej: doradca **na górze** jako główne zaproszenie, katalog pod spodem (jak Ideogram prowadzi polem „stwórz"). Odważniejsze, bliższe naszej tezie „AI wall designer", ale doradca jest nieudowodniony.

To jedno pytanie decyduje o kształcie landingu. Reszta (nakładka wymiarów, karty, kolor ściany) to ulepszenia niezależne od tej decyzji.
