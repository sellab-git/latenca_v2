# BRIEF (Claude Chrome) — kompletny zrzut logiki „Gallery Walls" Mixtiles

**Status: mechanizm ZWALIDOWANY (2026-07-22). Zostaje: zmierzyć wszystkie 45 ścian.**
**Decyzja Artura: przechodzimy WSZYSTKIE 45, krok po kroku — 100% pewności, zero zgadywania.**

**Cel:** kompletny, zmierzony zestaw danych → odtworzyć logikę u nas na naszych 9 rozmiarach Gelato.
**Zasada IP:** zbieramy wzorce + wymiary + opcje (fakty). Nie kopiujemy ich zdjęć/kodu/brandu/rozmiarów.
**Zrzuty ich ekranów:** wrzucaj Arturowi w czacie (albo lokalny folder) — **NIE commitujemy ich obrazów do publicznego repo.** W repo trzymamy tylko NASZE zmierzone/wyliczone dane (liczby) → plik `docs/mixtiles-layouts-data.json`.

## Nasze rozmiary (na to mapujemy — NIE zmieniamy)
Pion 30×40·50×70·70×100 · Poziom 40×30·70×50·100×70 · Kwadrat 30×30·50×50·70×70

---

## ZWALIDOWANE (potwierdzone klikając — NIE trzeba powtarzać)
- **Jeden flow:** wybierasz nazwaną, SZTYWNĄ ścianę i wypełniasz zdjęciami. **Brak** „zbuduj z N zdjęć / auto‑generuj układ".
- **Kompozycje sztywne, ZERO reflow.** Odznaczenie zdjęcia → dana komórka pusta w miejscu, układ się NIE przesuwa. Liczba ramek stała (klik w pustą = tylko „Upload Photo/Import"). Puste ramki dozwolone (kontur).
- **S/M/L to TRZY OSOBNE KOLEKCJE różnych produktów**, nie skala jednego produktu. Listy się nie pokrywają: Small ~20 ścian, Medium ~18, Large ~7 = **~45 unikatowych ścian, każda ma JEDEN stały wymiar**. (Stąd w schemacie: `sizeBand` + jeden `overallCm`, nie trzy warianty.)
- **Frame (potwierdzone 1:1):** Frameless, Black, White, Oak +$48, Wide Black +$96, Wide White +$96, Wide Walnut +$96, Earthy Blend +$48, Classic Blend +$48, Harmony Mix +$30. („Blend/Mix" miesza kolory ramek na jednej ścianie.)
- **Border:** None/Shallow/Medium/Deep = wewnętrzne passe‑partout; **zewnętrzny rozmiar ramki stały, kurczy się pole zdjęcia** (Deep = duży biały margines). ➜ **DO ZMIERZENIA W CM (raz):** margines dla Shallow/Medium/Deep.
- **Effect:** Original/Silver/Noir/Vivid/Dramatic.
- **Referencyjny rekord (linijka):** *16 Snapshots* — 97×97 cm, siatka 4×4, każda ramka 21×21 cm (kwadrat), gap ≈ 4,3 cm. (Wpisany już w `mixtiles-layouts-data.json` jako wzorzec formatu.)

---

## ROBOTA: zmierz wszystkie 45 ścian (Small + Medium + Large)

### Metoda per ściana (szybka, bez szacowania pozycji):
1. Otwórz ścianę w builderze.
2. **Linijka:** zapisz **wymiar całkowity (W×H cm)**.
3. **Linijka:** zapisz **rozmiar każdej ramki w cm + orientację** (P pion / L poziom / S kwadrat). Jeśli wszystkie identyczne — napisz „×N, 21×21 S".
4. **Linijka:** zapisz **gap** (odstęp między ramkami w cm) — albo policz z całości.
5. **Pozycje — bez zrzutów (mój Playwright NIE dosięga ich buildera, sprawdzone):**
   - `uniform-grid` / `row` → nic nie podajesz, pozycje policzę z liczb (overall + rozmiar kafla + count).
   - **każdy inny typ** (`symmetric-center` / `staggered-cluster` / `mixed-cluster`) → dodaj per ramka **`centerPct: {x, y}`** = środek ramki jako % szerokości/wysokości CAŁEJ ściany (0–100). Masz już piksele środków → podziel przez wymiar ściany. Z tego + cm policzę dokładny `box`. (Zrzut niepotrzebny.)
6. Zapisz: `name`, `sizeBand` (z której kolekcji), `bestSeller?`, `frameCount`, `compositionType`.

### Typy kompozycji (`compositionType`) — nazwij jednym z:
`uniform-grid` · `row` · `column` · `symmetric-center` (małe wokół dużej środkowej) · `staggered-cluster` (schodkowy, luźny) · `mixed-cluster` (różne orientacje/rozmiary bez siatki)

### Format wyniku = dopisujesz obiekt do `walls[]` w `docs/mixtiles-layouts-data.json`:
```json
{
  "name": "16 Snapshots",
  "sizeBand": "Medium",
  "bestSeller": true,
  "frameCount": 16,
  "compositionType": "uniform-grid",
  "overallCm": { "w": 97, "h": 97 },
  "gapCm": 4.3,
  "frames": [
    { "orientation": "S", "cm": { "w": 21, "h": 21 }, "count": 16 }
  ],
  "screenshot": "16-snapshots-empty (wrzucony Arturowi w czacie)",
  "confidence": { "cm": "ruler", "gap": "derived" }
}
```
- `frames[]`: dla `uniform-grid`/`row` użyj `count` (bez pozycji — policzę z liczb). Dla `symmetric-center`/`staggered-cluster`/`mixed-cluster` — jeden obiekt na ramkę z `orientation` + `cm` + **`centerPct:{x,y}`** (środek jako % ściany). Przykład:
```json
{ "orientation": "P", "cm": { "w": 50, "h": 69 }, "centerPct": { "x": 75, "y": 29 } }
```
- **Nie wypełniaj `box{x,y,w,h}` — wyliczę go z `centerPct` + `cm` + `overallCm`.** Żadnych zrzutów.

### Checklist (przechodź systematycznie, zaznaczaj):
- **Small (~20):** Wild Visuals, Parallel Triplet, Offbeat Set, 6 Enduring Pictures, Bold Statement, Timeless Quartet, Harmony In Four, Embraced By Warmth, Boundless Moments, Dancing Lights, Captured Affection, Frame By Frame, The Joyful Five, The Sweet Seven, Cozy Trio, Drifting Shapes, Soft Melodies, Beautiful Lines, 12 Memories, Symphony Of Frames … (dodaj każdą, którą znajdziesz).
- **Medium (~18):** 16 Snapshots ✅, Mirrored Memories, Lifting Spirits, The Memory Mosaic, Bright And Cherished, The Perfect Four … (reszta).
- **Large (~7):** Timeless Bonds (221×107), Framed Connections (160×185) … (reszta).

## Uzupełnij też sekcję `config` w JSON (raz):
- `borders`: zmierz margines w cm dla None(0)/Shallow/Medium/Deep.
- (`frames` + `effects` już potwierdzone — są w pliku).
- Mapowanie zdjęcie→kafel: potwierdź jak liczą „Add N Photos" vs liczba kafli (prefill demo?), i **jak przycina zdjęcie pionowe do kafla kwadratowego** (środek? da się przesunąć kadr?).

---

## CO JA Z TYM ZROBIĘ
Ze zrzutów pustych ramek policzę dokładne pozycje (`box{x,y,w,h}%`), połączę z Twoimi cm/orientacjami, zbuduję matrycę `LAYOUTS` (per liczba × typ), zmapuję ich rozmiary → nasze 9 Gelato, wepnę do `05-wall`. Zero zgadywania — każda pozycja z piksela, każdy rozmiar z linijki.
