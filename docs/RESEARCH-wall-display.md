# RESEARCH — jak liderzy pokazują grafikę na ścianie (Mixtiles + Fy!)

> **Skąd to jest:** Artur przeklikał pełne ścieżki obu serwisów w Claude Chrome (2026-07-20), z rozróżnieniem sprawdzone / wnioskowane. To nie jest analiza z drugiej ręki — to obserwacja działającego produktu.
> **Po co:** rozstrzygnąć, na czym pokazujemy grafikę i jak odpowiadamy na pytanie *„czy to będzie dobry rozmiar"* — czyli na blokadę zakupową numer jeden.
> Kontekst: [`DECISIONS.md`](DECISIONS.md) D-021 (neutralna ściana, zdjęcie pokoju opcjonalne) · D-023 (jedna praca, nie galeria) · D-030 (granica MVP)
> Data: 2026-07-20.

---

## 1. Co znaleziono (fakty)

### Mixtiles

| Obszar | Ustalenie |
|---|---|
| **Edytor pojedynczego kafla** | **Brak pokoju.** Grafika pływa na jednolitym jasnym tle z delikatnym cieniem imitującym zawieszenie. Bez mebli, bez człowieka |
| **Gallery Walls (gotowe zestawy)** | Każdy zestaw ma **własny, przypisany render pokoju** — to nie jest biblioteka teł do wyboru. Karuzela 6 zdjęć na produkt. Wszystkie sceny jasne (skandynawsko-mid-century) |
| **Wgranie własnego zdjęcia pokoju** | **Nie istnieje.** Jedyny upload to grafika **do druku**, nie tło. Nigdzie nie proszą o zdjęcie wnętrza |
| **Skala** | **Nakładka linijki** (ikona w rogu): każdy kafel dostaje etykietę w cm, a cały układ wymiar całości ze strzałkami (**79 cm × 122 cm**) — na tle pokoju z fotelem i komodą |
| **Technika podglądu** | Statyczny render z nałożonymi grafikami. Zero AR, zero przeciągania po ścianie. Interakcja: rama / rozmiar / efekt / border, zoom, przełącznik linijki |
| **Katalog** | Filtr Small / Medium / Large, każda karta z wymiarem całości („122cm x 79cm") |

### Fy! (Art Advisor, oznaczony „IN BETA")

| Obszar | Ustalenie |
|---|---|
| **Główny podgląd** | Przełącznik **`Flat` \| `Living Room`**. `Flat` = ramka na neutralnym beżowym tle studyjnym. `Living Room` = scena pokoju |
| **Skala** | Przełączniki **`Measure`** i **`Grid`**. Po włączeniu `Measure` — wymiary fizyczne ze strzałkami na grafice (**102 cm × 76 cm**) |
| **Zdjęcie pokoju** | Proszą: *„Upload a photo — Room, wall, or art you love"*, opisane jako **OPTIONAL** |
| **Do czego używają zdjęcia** | ① wyciągają **paletę barw** (box „FROM YOUR ROOM", 5 próbek) ② próbują **zmierzyć ścianę** ③ zapisują kontekst („Living Room saved") |
| **Gdy analiza zawodzi** | *„We couldn't measure your wall confidently — tell us your wall size for an accurate fit."* |
| **Czy montują na zdjęciu użytkownika** | W obserwowanej sesji **nie** — tryb `Living Room` pokazywał generyczną scenę, nie piksele użytkownika |

### ✅ Domknięcie: Fy! **próbuje** montażu na zdjęciu — i wychodzi katastrofa

Pierwszy test był skażony, więc powtórzono go z czystym zdjęciem wnętrza *(użyto naszej własnej próbki `cupboard.webp` — jednolita ściana, równomierne światło, wyraźny mebel odniesienia, czyli **najłatwiejszy możliwy przypadek**)*.

**Wynik: Fy! faktycznie nakłada grafiki na zdjęcie użytkownika. Efekt jest niezdatny do użytku.** Cztery prace wielkości znaczków pocztowych, rozrzucone losowo po ścianie.

| Co zawiodło | Dlaczego to fatalne |
|---|---|
| **Skala całkowicie nietrafiona** — prace ~15×20 cm na ścianie ~3 m | Skala to **jedyne pytanie**, na które podgląd ma odpowiadać. Zawiódł w swojej jedynej funkcji |
| **Zero logiki kompozycji** — różne wysokości, brak wyrównania i grupowania, brak związku z meblem pod spodem | To ma być narzędzie *projektanckie*; żaden projektant tak by nie powiesił |
| **Brak obsługi planów** — praca ląduje na roślinie zamiast za nią | Widać, że to montaż |
| **Podważa własną obietnicę** | Doradca ma dawać pewność; ten render odbiera ją bardziej, niż dawał podgląd na neutralnej ścianie |

### ⚠️ Korekta po trzecim teście — wniosek powyżej był przedwczesny

Po dłuższej zabawie z narzędziem Fy! wyprodukowało render **dobrej jakości**: cztery prace 100×70, **wyrównane na jednej wysokości, równo rozstawione, w poprawnej skali** względem komody. To nie jest ta sama jakość co przy pierwszej próbie.

**Rewizja wniosku: bramką jakości nie jest technologia montażu, tylko jedna informacja — wymiary ściany.**

- **Bez wymiarów** system zgaduje skalę i produkuje śmieci (znaczki pocztowe, patrz wyżej)
- **Z wymiarami** produkuje wiarygodny render
- Potwierdza to ich **własny komunikat**: *„We couldn't measure your wall confidently — tell us your wall size for an accurate fit."* Oni sami znają ten warunek

**Ciekawe dla nas:** szerokość ściany to dokładnie **nasze „jedno zasłużone pytanie"** w doradcy (D-023). Kluczowy input mielibyśmy więc już w ręku.

**Co nadal zawodzi — i to jest ta droga część:** Fy! **edytuje zdjęcie pokoju**, wycinając rośliny na pierwszy plan, żeby grafiki mogły się za nimi chować. To realna praca na obrazie (segmentacja, plany głębi) i **widocznie jeszcze glitchuje** — prace niepoprawnie znikają za roślinami. Samo nałożenie prostokąta na płaską ścianę jest łatwe; **wiarygodne wpasowanie w scenę z planami — nie.**

> **Uczciwa uwaga metodologiczna:** wniosek „gorsze niż brak" postawiony po pierwszym, nieudanym renderze był **za mocny na podstawie jednego przypadku**. Drugi test go obalił w ciągu kilkunastu minut. Zapis zostawiony celowo — jako przypomnienie, żeby nie hartować wniosków na pojedynczej obserwacji.

### Katalog zaobserwowanych trybów awarii

Cztery próby, jeden sukces. Bilans i warunki:

| # | Wejście | Wynik | Tryb awarii |
|---|---|---|---|
| 1 | Zrzut sceny z Mixtiles (skażone) | ❌ | Test nieważny |
| 2 | Czyste zdjęcie frontalne, **bez podanych wymiarów** | ❌ | **Skala** — prace wielkości znaczków |
| 3 | To samo zdjęcie, **po podaniu informacji** | ✅ | — (dobry render) |
| 4 | Zdjęcie **w perspektywie** (ściana pod kątem) | ❌ | **Perspektywa** — grafiki wklejone jako płaski prostokąt na wprost, nieleżący w płaszczyźnie ściany; dodatkowo **wklejone na istniejące obrazy w ramach**, zamiast je uwzględnić |

**Trzy niezależne tryby awarii:**
1. **Brak wymiarów ściany** → błędna skala *(rozwiązywalne — wystarczy zapytać)*
2. **Plany sceny** → rośliny/meble na pierwszym planie, glitchujące przesłanianie *(trudne — segmentacja)*
3. **Perspektywa** → grafika nie leży w płaszczyźnie ściany *(trudne — estymacja płaszczyzny i homografia)*
4. *(pochodna 3.)* **Istniejące obrazy na ścianie** — wklejane „po wierzchu", nie wykrywane

### 🔑 Wniosek praktyczny: okno warunków, w którym to działa, jest wąskie

Montaż zadziałał **wyłącznie** przy: zdjęciu **frontalnym**, **dobrze oświetlonym**, ściana **pusta**, bez przedmiotów na pierwszym planie, **plus podane wymiary**.

**To jest opis zdjęcia studyjnego.** A zdjęcie studyjne pustej ściany to dokładnie to, czym jest **gotowe pomieszczenie przykładowe**.

> **Jeśli montaż wymaga warunków zbliżonych do studia, to równie dobrze można użyć zdjęcia studyjnego — czyli własnego, kontrolowanego pomieszczenia.** Zyskujesz wtedy pewność renderu bez żadnej pracy na obrazie.

To jest praktyczne uzasadnienie D-021 — mocniejsze niż „to trudne". Realne zdjęcia od klientów **z reguły** są robione pod kątem (bo inaczej pokój nie mieści się w kadrze) i zawierają meble oraz rośliny na pierwszym planie. Czyli **typowe wejście wpada w tryby awarii 2 i 3**, a nie w wąskie okno sukcesu.

---

## 2. Trzy rzeczy, które wywracają nasze wcześniejsze założenia

### ⚠️ 2.1. Mixtiles **nie pokazuje pojedynczej pracy w pokoju** — pokazuje ją na neutralnym tle

To jest najbardziej zaskakujące ustalenie. Zakładaliśmy, że lider kategorii zawsze renderuje w pomieszczeniu. **Nie robi tego.** Pokój pojawia się **wyłącznie przy gotowych zestawach wieloelementowych**, i to jako render przypisany do konkretnego produktu — nie jako wybieralne tło.

**Konsekwencja dla nas:** rekomendowałem wcześniej zbudowanie biblioteki **6–9 pomieszczeń** rozpiętych na osiach stylu. **To było przeinżynierowane.** Nasze MVP to **jedna praca** (D-023) — czyli dokładnie ten przypadek, w którym lider kategorii pokoju **nie używa**.

🟡 **Ale uwaga na różnicę modeli biznesowych — nie kopiujmy bezmyślnie.** Mixtiles sprzedaje **Twoje własne zdjęcia**. Emocja siedzi w treści, nie w pokoju; neutralne tło niczego nie odbiera. My sprzedajemy **nieznaną klientowi sztukę** — tu kontekst może znaczyć *więcej*, nie mniej. To jest realna niewiadoma, nie rozstrzygnięta tym badaniem.

### 2.2. Skalę rozwiązuje się **liczbami na obrazie**, nie fotorealizmem

Obaj liderzy robią to samo: **nakładka wymiarów ze strzałkami**, przełączana. Mixtiles: 79 cm × 122 cm na tle mebla. Fy!: 102 cm × 76 cm.

To bezpośrednio odpowiada na obawę, którą zgłosiłem wcześniej („skala musi być skalibrowana, inaczej podgląd kłamie"). **Odpowiedź branży nie jest fotograficzną kalibracją — jest jawnym podaniem centymetrów.** Znacznie tańsze i uczciwsze: nie udajesz precyzji renderu, tylko mówisz wprost, ile to ma.

**To jest najtańsza funkcja o najwyższej wartości, której nam brakuje.** Nasz mockup podaje „70×100 cm" jako tekst w panelu obok. Nikt nie łączy tego ze ścianą.

### 2.3. Pomysł Artura „zdjęcie do analizy, nie do wyświetlania" **jest wdrożoną praktyką**

Fy! robi dokładnie to: wyciąga z fotografii **paletę barw** i próbuje **zmierzyć ścianę** — a gdy się nie udaje, **przyznaje się i pyta**: *„We couldn't measure your wall confidently — tell us your wall size."*

To nie jest już hipoteza. To działający wzorzec, łącznie z **uczciwą degradacją**, gdy wnioskowanie zawiedzie — a to jest dokładnie zachowanie zgodne z naszym zakazem udawania AI.

---

## 3. Co z tego wynika dla Latenki

| Wniosek | Siła dowodu |
|---|---|
| **Montaż na zdjęciu klienta jest wykonalny, ale zabramkowany na wymiarach ściany.** Bez nich — render niezdatny do użytku; z nimi — wiarygodny. Mixtiles nie oferuje tego w ogóle; Fy! oferuje, z widocznymi problemami przy planach (rośliny) | 🟡 D-021 **stoi** (neutralna ściana domyślnie), ale uzasadnienie się zmienia: nie „to nie działa", tylko **„to wymaga danych i pracy na obrazie, których na MVP nie mamy"** |
| **Nakładka wymiarów to standard kategorii** — obaj liderzy, ta sama mechanika | 🟢 Mocne. Do wdrożenia |
| **Zdjęcie jako wejście analityczne + uczciwa degradacja** | 🟢 Potwierdzone jako wdrożony wzorzec |
| **Pokój jest opcjonalny przy pojedynczej pracy** | 🟡 Potwierdzone u Mixtiles, ale ich model (własne zdjęcia klienta) różni się od naszego (nieznana sztuka) |
| **Czy Fy! renderuje na prawdziwych pikselach użytkownika** | 🟢 **Rozstrzygnięte: tak, i wychodzi katastrofa** (patrz §1) |

### Rekomendacje

1. **Dodać nakładkę wymiarów do podglądu** — przełącznik „linijka", strzałki z centymetrami na ścianie, nie tylko liczba w panelu obok. **Najwyższy stosunek wartości do kosztu z całego badania.**
2. **Zdjęcie wyłącznie jako wejście analityczne**, z jawną degradacją w stylu Fy!: gdy nie da się czegoś odczytać, doradca mówi to wprost i dopytuje. Nigdy jako tło do montażu.
3. **Nie budować biblioteki 6–9 pomieszczeń przed walidacją.** Zostawić obecne trzy, dodać **tryb neutralnego tła** (odpowiednik `Flat` u Fy!) i przełącznik — a rozbudowę zestawu uzależnić od tego, czy klienci faktycznie go używają.
4. **Montaż na zdjęciu pokoju zostaje w BACKLOGU — ale z jasno nazwanym warunkiem odblokowania.** *(Wcześniejsza rekomendacja w tym dokumencie, żeby przenieść go do „odrzucone z dowodem", została **wycofana** po trzecim teście — patrz §1.)*
   Warunek nie jest już mglisty („trudne"), tylko rozbity na dwa mierzalne składniki:
   - **(a) Wymiary ściany** — bez nich skala zgaduje i render kłamie w jedynej rzeczy, która ma znaczenie. **Ten składnik już mamy** — pytamy o szerokość ściany w doradcy (D-023)
   - **(b) Obsługa planów sceny** — wycinanie mebli i roślin na pierwszy plan. Realna praca na obrazie, **u Fy! wciąż glitchuje**. **Nie mamy, na MVP nie budujemy**
   - **(c) Estymacja płaszczyzny ściany i perspektywy** — bez tego grafika nie leży na ścianie, tylko na zdjęciu. **Nie mamy, na MVP nie budujemy**

   Czyli: nie „może kiedyś", tylko **„gdy (b) i (c) staną się niezawodne i tanie"**. Oba to praca na obrazie, nie orkiestracja cudzego API — czyli **inny rodzaj przedsięwzięcia niż to, co opisuje D-020**.

### Otwarte pytanie produktowe (nierozstrzygnięte badaniem)

**Czy przy sprzedaży nieznanej sztuki pokój jest ważniejszy niż przy sprzedaży własnych zdjęć klienta?** Mixtiles może pominąć pokój, bo emocja siedzi w treści. U nas treść jest obca — kontekst może być tym, co przekonuje. **To jest pytanie do przetestowania na klientach, nie do rozstrzygnięcia analizą konkurencji.**

---

## Powiązane
[`DECISIONS.md`](DECISIONS.md) (D-021, D-023, D-030) · [`VISION.md`](VISION.md) · [`../Analizy/Mixtiles/`](../Analizy/Mixtiles/) · [`../Analizy/Iamfy%20-%20Art%20Advisor/`](../Analizy/Iamfy%20-%20Art%20Advisor/)
