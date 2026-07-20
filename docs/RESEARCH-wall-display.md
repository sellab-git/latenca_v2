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

**Wniosek kluczowy: montaż na zdjęciu klienta nie jest „trochę mniej ładny" — jest gorszy niż jego brak.** Ta sama grafika na neutralnej ścianie w **poprawnej skali** byłaby bardziej przekonująca niż „w Twoim pokoju" w skali absurdalnej. Traci się zaufanie, żeby zyskać personalizację, o którą nikt nie prosił.

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
| **Montaż na zdjęciu klienta zawodzi w praktyce.** Mixtiles nie daje takiej opcji w ogóle po latach i milionach zamówień; Fy! próbuje — i na najłatwiejszym możliwym wejściu produkuje render niezdatny do użytku (zła skala, brak kompozycji) | 🟢 **Bardzo mocne potwierdzenie D-021 — dowód bezpośredni, nie z nieobecności.** Zamknięte |
| **Nakładka wymiarów to standard kategorii** — obaj liderzy, ta sama mechanika | 🟢 Mocne. Do wdrożenia |
| **Zdjęcie jako wejście analityczne + uczciwa degradacja** | 🟢 Potwierdzone jako wdrożony wzorzec |
| **Pokój jest opcjonalny przy pojedynczej pracy** | 🟡 Potwierdzone u Mixtiles, ale ich model (własne zdjęcia klienta) różni się od naszego (nieznana sztuka) |
| **Czy Fy! renderuje na prawdziwych pikselach użytkownika** | 🟢 **Rozstrzygnięte: tak, i wychodzi katastrofa** (patrz §1) |

### Rekomendacje

1. **Dodać nakładkę wymiarów do podglądu** — przełącznik „linijka", strzałki z centymetrami na ścianie, nie tylko liczba w panelu obok. **Najwyższy stosunek wartości do kosztu z całego badania.**
2. **Zdjęcie wyłącznie jako wejście analityczne**, z jawną degradacją w stylu Fy!: gdy nie da się czegoś odczytać, doradca mówi to wprost i dopytuje. Nigdy jako tło do montażu.
3. **Nie budować biblioteki 6–9 pomieszczeń przed walidacją.** Zostawić obecne trzy, dodać **tryb neutralnego tła** (odpowiednik `Flat` u Fy!) i przełącznik — a rozbudowę zestawu uzależnić od tego, czy klienci faktycznie go używają.
4. **Przenieść „montaż na zdjęciu pokoju" z BACKLOGU „trudne, odłożone" do „odrzucone z dowodem".** D-021 opierało się na przewidywaniu, że to zawiedzie. Teraz mamy zaobserwowaną porażkę u konkurenta, na najłatwiejszym wejściu. Warunek ewentualnego powrotu jest konkretny: **dopóki nie potrafimy niezawodnie ustalić wymiarów ściany, montaż jest z definicji niemożliwy** — bo bez skali render kłamie w jedynej rzeczy, która ma znaczenie.

### Otwarte pytanie produktowe (nierozstrzygnięte badaniem)

**Czy przy sprzedaży nieznanej sztuki pokój jest ważniejszy niż przy sprzedaży własnych zdjęć klienta?** Mixtiles może pominąć pokój, bo emocja siedzi w treści. U nas treść jest obca — kontekst może być tym, co przekonuje. **To jest pytanie do przetestowania na klientach, nie do rozstrzygnięcia analizą konkurencji.**

---

## Powiązane
[`DECISIONS.md`](DECISIONS.md) (D-021, D-023, D-030) · [`VISION.md`](VISION.md) · [`../Analizy/Mixtiles/`](../Analizy/Mixtiles/) · [`../Analizy/Iamfy%20-%20Art%20Advisor/`](../Analizy/Iamfy%20-%20Art%20Advisor/)
