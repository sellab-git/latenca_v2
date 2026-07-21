# CONCEPT — „the wall" (cała aplikacja jako ściana)

> Pomysł Artura (2026-07-21): cały obszar treści = **biała ściana w domu klienta**. Na każdym ekranie działa jak ściana, na której pokazujemy grafiki — katalog = ściana z wieloma pracami, produkt = ściana z jedną pracą + nałożony panel + elementy. Trochę jak **Figma/Stitch** (płótno + pływające panele) — ale **świadomie NIE super‑narzędzie do projektowania.**
> Pytanie Artura: czy Home ma teraz ten „feeling ściany"?

## Werdykt w jednym zdaniu
**Tak, to mocny i ownable kierunek — ale „ściana" musi znaczyć *powierzchnia + język pływających paneli*, a nie *manipulowalne płótno*.** Inaczej wpadniemy w narzędzie, którego sam nie chcesz. A Home **dziś tego feelingu nie ma** — jest feedem, nie ścianą.

---

## Dlaczego to jest mocne (nie tylko ładne)

1. **Spójność jednej metafory** na wszystkich ekranach: „zawsze patrzysz na ścianę, my pomagamy ją wypełnić". Nikt tak nie ramuje sklepu z grafiką — to jest **do posiadania** (ownable).
2. **To jest wprost nasz wyróżnik.** Jesteśmy „AI wall designer" — więc całe doświadczenie ma być o ścianie, a nie generycznym sklepie. Metafora robi z brandu doświadczenie.
3. **To rozwinięcie tego, co już zablokowaliśmy, nie nowy pomysł z kosmosu:** D‑033 mówi „płaska ściana = powierzchnia wyświetlania". Tu po prostu rozciągamy ją z jednego stage'a produktu na **całą aplikację.**
4. **Potwierdzone u lidera:** Fy! `Flat` = **ściana w kolorze Twojej ściany** (`RESEARCH-wall-display.md`). Dokładnie ta idea — powierzchnia‑ściana — działa w praktyce i jest ich najlepszym trikiem.
5. **Strona produktu JUŻ tak działa.** Obraz pływa na neutralnej powierzchni, panel doradcy/zakupu nałożony po prawej, miniatury i akcje pływają. To nie rewolucja — to **dokończenie** istniejącego wzorca i rozlanie go na resztę.
6. **Tanie jako FEELING** (kluczowe wobec „nie chcę narzędzia"): to warstwa **wizualna** — tło‑ściana, karty z cieniem, grafika z delikatnym cieniem „zawieszenia". **Zero silnika canvas, zero drag‑and‑drop.** Feeling ściany kosztuje kilka reguł CSS, nie budowę Figmy.

---

## Gdzie to się łamie (uczciwie — to jest ważne)

1. **Katalog to „wybieram z wielu", a ściana to „moja, ułożona".** To dwa różne modele mentalne. Gdyby zrobić katalog dosłowną ścianą rozstawionych, oprawionych prac — **zabilibyśmy przeglądalność.** Mixtiles, Displate, Ideogram, Midjourney — wszyscy do *przeglądania* używają **gęstej siatki**, nie ściany. Gęstość = szybkość wyboru.
2. **Płótno + pływające panele to paradygmat NARZĘDZIA, nie sklepu.** Sklepy są przepływem (scroll, sekcje, karty). Pełne pójście w „canvas + panele" grozi dokładnie tym, czego nie chcesz — poczuciem złożonego edytora. Modsy (`ai-graphics-marketplace`/stress‑testy) pokazało, że narzędzie‑do‑projektowania‑wnętrz to cmentarz.

---

## Rozwiązanie napięcia (to jest sedno)

**„Ściana" = POWIERZCHNIA (grunt) + język PŁYWAJĄCYCH PANELI. NIE manipulowalne płótno.**

- **Ściana = tło/grunt**, na którym wszystko siedzi. Ciepły neutralny (nasz `--bg`), docelowo **tintowany kolorem ściany klienta** (trik Fy!, zero ryzyka montażu).
- **Treść zachowuje się per ekran:**
  - **Katalog** = przeglądalna **siatka** grafik *na ścianie* — nadal gęsta i szybka, ale z **delikatnym cieniem „zawieszenia" i odrobiną oddechu**, żeby prace *leżały na powierzchni*, a nie były bezszwowym feedem. (Ostrożnie: nie tracimy gęstości.)
  - **Produkt / doradca** = **jedna praca zawieszona na ścianie**, konfigurowana. To już mamy — trzeba tylko mocniej „dowiesić" (cień, przełącznik flat/pokój, skala).
- **UI (doradca, filtry, panel zakupu, nawet sidebar) = pływające nakładki nad ścianą** (karty z cieniem) — to jest ten „Figma/Stitch chrome". W dużej mierze już tak wygląda.
- **Granica, która trzyma nas po stronie sklepu:** **nie przeciągasz grafik po ścianie, nie układasz dowolnie.** Ty *oglądasz*, AI *układa*. To jest różnica między „sklep z duszą ściany" a „narzędzie do projektowania".

---

## Czy Home ma teraz ten feeling? — NIE

- **Home = feed.** Siatka kafli krawędź‑w‑krawędź, bez cienia, bez „zawieszenia". Czyta się jak **strumień obrazów** (styl Ideogram/MJ), nie jak **grafika na ścianie**.
- **Produkt jest bliżej** (obraz pływa na jasnej powierzchni + pływające panele), ale nawet tam grunt czyta się jako „jasne UI", nie wyraźnie „ściana".
- Czyli: **największa różnica do zrobienia jest właśnie na Home/katalogu** — bo tam efektu nie ma, a potencjał jest największy.

---

## Co by się konkretnie zmieniło (żeby poczuć ścianę)

1. **Grunt treści = powierzchnia „ściany"** — ciepły neutralny z subtelną głębią (cień/tint), docelowo kolor ściany klienta.
2. **Katalog:** grafiki dostają **delikatny cień zawieszenia** + trochę oddechu między nimi → leżą *na* ścianie, nie tworzą bezszwowego feedu. Gęstość zostaje.
3. **Produkt:** wzmocnić czytanie „praca zawieszona na ścianie" (cień, flat/pokój, skala) — w większości już jest.
4. **Panele UI:** czytelnie jako **pływające nakładki** nad ścianą (cienie, zaokrąglenia) — w dużej mierze już są; ujednolicić.

---

## Rekomendacja

**Wejść w to — jako JĘZYK (powierzchnia‑ściana + pływające panele), nie jako narzędzie.** Jest spójne, ownable, tanie do osiągnięcia jako feeling, rozwija D‑033 i jest potwierdzone przez Fy!. **Twarda granica:** katalog zostaje przeglądalną siatką (nie dosłowną rozstawioną ścianą), a użytkownik niczego nie przeciąga — AI układa.

**Następny krok:** zamiast dalej dyskutować — **zaprototypować „wall treatment" na jednym ekranie**, żebyś POCZUŁ różnicę. Proponuję **katalog/Home**, bo tam efekt jest największy i tam go dziś brakuje. Zrobię wariant obok obecnego, porównasz.

---

## Zastosowane (2026-07-21)
Wall‑treatment złożony do produkcyjnych ekranów: **grunt‑ściany** (delikatne światło z góry) wyniesiony do `shared/app.css` → mają go **oba** ekrany (landing i produkt) z jednego źródła. Na landingu kafle „zawieszone" (cień `--art-shadow`, ostre krawędzie, pasek filtrów pełnej szerokości bez kreski); panele (doradca‑hero) pływają (`--shadow-pop`). Cienie w jednym systemie (D‑043). `01-home` v13; `landing-wall.html` zostaje jako snapshot „przed".
