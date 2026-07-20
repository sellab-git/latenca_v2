# AI — model kosztowy i kontrola wydatków

> **Po co ten dokument:** doradca to jedyny element Latenki, który generuje **koszt zmienny bez gwarancji przychodu** — ktoś może rozmawiać i nie kupić. Ten dokument ustala, ile to realnie kosztuje i jak zabezpieczyć to z każdej możliwej strony.
> **Zasada nadrzędna (Artur, 2026-07-20):** *„nie chcę płacić nie wiem ile za to, że ktoś sobie gada."* Koszt sesji musi mieć **twardy, przewidywalny sufit** — nie „powinien być mały", tylko **nie może przekroczyć X**.
> Kontekst: [`VISION.md`](VISION.md) · [`DECISIONS.md`](DECISIONS.md) (D-020, D-024, D-030) · [`REVIEW-designer-layer-round3.md`](REVIEW-designer-layer-round3.md)
> Data: 2026-07-20. Ceny modeli zweryfikowane; kurs USD/PLN przybliżony (~3,70).

---

## 1. Cennik i wybór modelu

| Model | ID | Wejście / wyjście za 1 mln tokenów |
|---|---|---|
| Opus 4.8 | `claude-opus-4-8` | $5 / $25 |
| Sonnet 5 | `claude-sonnet-5` | $3 / $15 *(promocyjnie $2 / $10 do 2026-08-31)* |
| Haiku 4.5 | `claude-haiku-4-5` | $1 / $5 |

**Wyjście kosztuje 5× więcej niż wejście.** To najważniejsza liczba w całym dokumencie — ograniczanie długości odpowiedzi daje większą oszczędność niż ograniczanie wejścia.

**Strategia:** budujemy na **Opusie** (poprzeczka jakości), potem testujemy, czy Sonnet trzyma poziom. Nie odwrotnie — startując od taniego modelu wyciągniemy fałszywy wniosek, że „doradca jako pomysł nie działa", zamiast „model był za słaby".

---

## 2. Koszt bazowy (jedna normalna sesja)

Sesja = ~6–8 wymian, ~4 tys. tokenów wejścia (w większości z cache), ~300 tokenów odpowiedzi na turę.

| Model | Za sesję (USD) | Za sesję (PLN) |
|---|---|---|
| Sonnet | $0,05–0,15 | ~0,20–0,55 zł |
| Opus | $0,15–0,40 | ~0,55–1,50 zł |

Przy sprzedaży $79–189 (~290–700 zł) i konwersji 1:10 → **koszt AI to ~1–5% wartości zamówienia.** Dla porównania: druk w Gelato to ~40–50% ceny. **W normalnym scenariuszu koszt AI jest szumem.**

---

## 3. ⚠️ Problem: koszt rośnie kwadratowo

W czacie każda tura wysyła **całą dotychczasową rozmowę od nowa**. Tura 50. wysyła 50 poprzednich wymian. Koszt nie rośnie liniowo z długością rozmowy — rośnie **kwadratowo**.

Godzina rozmowy (~60–90 tur):

| Wariant | Koszt godziny (Opus) |
|---|---|
| Naiwnie — cała historia, bez cache | **~25–30 zł** |
| Z prompt-cachingiem | ~5–10 zł |
| **Ze stanem projektu zamiast transkryptu** | **~2–4 zł, i płasko** |

**Haczyk z cache:** domyślny cache żyje **5 minut**. Jeśli ktoś myśli 10 minut między wiadomościami, cache wygasa i każda tura znowu płaci pełną cenę za całą historię. **Powolna, przemyślana rozmowa jest droższa niż szybka** — odwrotnie, niż podpowiada intuicja.

---

## 4. Sześć warstw zabezpieczeń

Wartości startowe do dostrojenia — ale **każda warstwa musi istnieć**, bo każda łapie inny scenariusz.

### Warstwa 1 — Architektura: stan zamiast transkryptu *(usuwa wzrost)*

Najważniejsza warstwa. Zamiast wysyłać modelowi całą rozmowę, wysyłamy **skondensowany stan projektu** (D-024) + ostatnie 2–3 wymiany. Wszystko starsze jest już zawarte w stanie.

- Stan ma **stały budżet rozmiaru** (np. ≤1500 tokenów) — nie puchnie
- Verbatim tylko **ostatnie 3 wymiany**
- Efekt: **tura 80. kosztuje tyle samo co tura 3.** Ryzyko z kwadratowego staje się płaskie

### Warstwa 2 — Limity sesji *(sufit na jedną rozmowę)*

| Limit | Wartość startowa | Zachowanie po przekroczeniu |
|---|---|---|
| Liczba tur | **12** | Doradca domyka: *„Krążymy. Decyduję za Ciebie — oto najlepsza propozycja."* |
| Budżet tokenów na sesję | **~150 tys.** | Sesja kończy się z gotowym projektem, nie błędem |
| Bezczynność | **30 min** | Sesja wygasa; powrót = nowa sesja |
| Czas trwania | **60 min** | Twardy koniec |

**Limit tur ma podwójne uzasadnienie.** Mamy zablokowane: single-session, 10–15 minut, iteracja 2–3 rundy. **Godzinna rozmowa to sygnał awarii produktu, nie sukcesu** — doradca nie zbiega do decyzji. Limit jest jednocześnie tańszy i lepszy dla UX.

### Warstwa 3 — Limity na użytkownika *(sufit na nadużycia)*

- **Sesje na urządzenie/IP na dobę:** 5 *(potem: „wróć jutro albo przeglądaj katalog")*
- **Minimalny odstęp między wiadomościami:** 2 s *(blokuje skryptowe pompowanie)*
- **Cooldown po wyczerpaniu limitu sesji**

⚠️ **Uczciwie:** bez logowania rate-limiting nigdy nie jest szczelny (VPN, tryb prywatny). Dlatego warstwa 6 (globalny sufit) jest obowiązkowa, a nie opcjonalna.

### Warstwa 4 — Walidacja wejścia *(sufit na pojedyncze zapytanie)*

- **Maks. długość wiadomości:** ~500 znaków — obcinamy **przed** wysłaniem do API, nie po
- **Zdjęcia:** obraz w wysokiej rozdzielczości to **do ~4 800 tokenów za sztukę** — czyli jedno zdjęcie może kosztować więcej niż cała tekstowa tura. Limit: **1 zdjęcie na sesję, zmniejszane po naszej stronie przed wysłaniem**
- Odrzucamy oczywiste śmieci (pusta wiadomość, sam spam znaków) bez dotykania API

### Warstwa 5 — Dyscyplina modelu *(sufit na turę)*

- **`max_tokens` przykręcone** — np. 500 na turę sterującą. Wyjście kosztuje 5× wejścia, więc to tu są największe pieniądze
- **„Myślenie" modelu włączone tylko na pierwszą propozycję**, gdzie faktycznie trzeba pomyśleć. Na „coś spokojniejszego" — wyłączone. Oszczędza koszt *i* czas odpowiedzi
- **Prompt caching** na bazie wiedzy i instrukcjach *(ta sama treść w każdej turze → ~10% ceny)*
- Rozważyć tańszy model do prostych tur klasyfikujących, gdy zmierzymy, że jakość nie spada

### Warstwa 6 — Monitoring i wyłącznik bezpieczeństwa *(sufit globalny)*

- **Twardy dzienny limit wydatków** na całe konto — po przekroczeniu doradca **wyłącza się sam**
- Log kosztu każdej sesji + alert przy odchyleniach
- Ręczny wyłącznik doradcy niezależny od limitów

---

## 5. Ostateczne zabezpieczenie: sklep działa bez doradcy

To wynika wprost z **D-022 („projektant nigdy nie jest bramką")**: katalog, strona produktu, konfigurator i koszyk **nie zależą od AI**.

**Jeśli koszty kiedykolwiek wymkną się spod kontroli, wyłączamy doradcę i nadal mamy działający sklep.** Nie ma scenariusza, w którym rachunek za AI zatrzymuje sprzedaż. To jest właściwy powód, dla którego hybryda ze sklepem-jako-podłogą była dobrą decyzją — nie tylko UX, ale i odporność biznesowa.

---

## 6. Najgorszy przypadek z włączonymi limitami

Z warstwą 1 (płaski koszt) + warstwą 2 (12 tur):

- **Maks. koszt jednej sesji: ~$0,25–0,30 (~1 zł)** — twardo, niezależnie od tego, jak długo ktoś siedzi
- Osoba wyczerpująca dzienny limit: 5 sesji × 1 zł = **~5 zł**
- Przy globalnym dziennym suficie **cały scenariusz „ktoś sobie gada" jest ograniczony z góry i przewidywalny**

**To jest różnica między „koszt powinien być mały" a „koszt nie może przekroczyć X."** Wymagana jest ta druga wersja.

---

## 7. Czego nie kontrolujemy w pełni

- **Anonimowe nadużycie** — rate-limiting bez logowania jest obchodliwy. Łagodzi to globalny sufit (warstwa 6)
- **Ceny modeli** — mogą się zmienić; promocja Sonneta kończy się 2026-08-31
- **Realny rozkład długości sesji** — wartości startowe to szacunki. **Zmierzyć na pierwszych 100 sesjach i dostroić**

Doradca odpowiada wyłącznie o dobór sztuki na ścianę, więc **nie nadaje się do „farmienia" darmowego AI** — to zawęża motywację do nadużyć, ale jej nie zeruje.

---

## 8. Co z tego wynika dla budowy

Kolejność wdrożenia — od tego, co najtaniej ratuje najwięcej:

1. **Stan projektu zamiast transkryptu** — bez tego reszta łata objawy, nie przyczynę
2. **Limit tur + domykanie decyzji** — jednocześnie oszczędność i lepszy UX
3. **`max_tokens` + myślenie tylko na pierwszą propozycję**
4. **Prompt caching**
5. **Globalny dzienny sufit + wyłącznik** — zanim ruszy publiczny ruch
6. Limity per-IP, walidacja wejścia, monitoring

**Punkty 1–2 to nie optymalizacja — to warunek, żeby w ogóle uruchomić doradcę publicznie.**
