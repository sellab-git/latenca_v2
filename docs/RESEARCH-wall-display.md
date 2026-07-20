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

⚠️ **Zastrzeżenie do wiarygodności testu Fy!:** narzędzie jest w becie i miało błędy renderowania, a jako „zdjęcie pokoju" użyto zrzutu sceny z Mixtiles, nie prawdziwej fotografii wnętrza. **Nie można w 100% wykluczyć**, że przy czystym zdjęciu tryb `Living Room` robi dosłowny montaż. Do rozstrzygnięcia jednym testem z prawdziwym zdjęciem.

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
| **Nikt nie montuje na zdjęciu użytkownika.** Mixtiles nie daje takiej opcji w ogóle, po latach i milionach zamówień; Fy! prosi o zdjęcie, ale używa go analitycznie | 🟢 **Mocne potwierdzenie D-021.** Zamknięte |
| **Nakładka wymiarów to standard kategorii** — obaj liderzy, ta sama mechanika | 🟢 Mocne. Do wdrożenia |
| **Zdjęcie jako wejście analityczne + uczciwa degradacja** | 🟢 Potwierdzone jako wdrożony wzorzec |
| **Pokój jest opcjonalny przy pojedynczej pracy** | 🟡 Potwierdzone u Mixtiles, ale ich model (własne zdjęcia klienta) różni się od naszego (nieznana sztuka) |
| **Czy Fy! renderuje na prawdziwych pikselach użytkownika** | 🔴 Nierozstrzygnięte — test był skażony |

### Rekomendacje

1. **Dodać nakładkę wymiarów do podglądu** — przełącznik „linijka", strzałki z centymetrami na ścianie, nie tylko liczba w panelu obok. **Najwyższy stosunek wartości do kosztu z całego badania.**
2. **Zdjęcie wyłącznie jako wejście analityczne**, z jawną degradacją w stylu Fy!: gdy nie da się czegoś odczytać, doradca mówi to wprost i dopytuje. Nigdy jako tło do montażu.
3. **Nie budować biblioteki 6–9 pomieszczeń przed walidacją.** Zostawić obecne trzy, dodać **tryb neutralnego tła** (odpowiednik `Flat` u Fy!) i przełącznik — a rozbudowę zestawu uzależnić od tego, czy klienci faktycznie go używają.
4. **Rozstrzygnąć niedokończony test:** wgrać do Fy! prawdziwe zdjęcie pokoju i sprawdzić, czy `Living Room` montuje na realnych pikselach. To jedyne pytanie, które zostało otwarte.

### Otwarte pytanie produktowe (nierozstrzygnięte badaniem)

**Czy przy sprzedaży nieznanej sztuki pokój jest ważniejszy niż przy sprzedaży własnych zdjęć klienta?** Mixtiles może pominąć pokój, bo emocja siedzi w treści. U nas treść jest obca — kontekst może być tym, co przekonuje. **To jest pytanie do przetestowania na klientach, nie do rozstrzygnięcia analizą konkurencji.**

---

## Powiązane
[`DECISIONS.md`](DECISIONS.md) (D-021, D-023, D-030) · [`VISION.md`](VISION.md) · [`../Analizy/Mixtiles/`](../Analizy/Mixtiles/) · [`../Analizy/Iamfy%20-%20Art%20Advisor/`](../Analizy/Iamfy%20-%20Art%20Advisor/)
