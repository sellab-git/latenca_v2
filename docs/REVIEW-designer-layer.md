# REVIEW — warstwa „Latenca jako cyfrowy projektant" (9 hipotez ChatGPT)

> **Co to jest:** krytyczna ocena warstwy 9 hipotez produktowych zaproponowanych przez ChatGPT (rola: senior reviewer), plus rozstrzygnięcia Artura, które z niej wynikły.
> **Autor oceny:** Claude. **Decyzje w sekcji D:** Artur. **Status:** ustalenia robocze — nie są jeszcze wpisem w [`DECISIONS.md`](DECISIONS.md) ani lockiem.
> **Kontekst produktowy:** [`VISION.md`](VISION.md) (MVP = Krok 1 sklep + Krok 2 doradca), [`DECISIONS.md`](DECISIONS.md) (D-020, D-021).
> Data: 2026-07-19.

---

## A. Przyjęte bez zastrzeżeń (§3, §4, §5, §7, §8)

Proces projektowy zamiast chatbota · stan projektu · iteracyjność · rosnąca pewność · uzasadnianie decyzji.

**Dlaczego:** to czysta architektura przepływu — tanie, bez ML, dokładnie to, co D-020 nazywa „dyrygentem". To najmocniejsza część całej warstwy.

**Zastrzeżenia wykonawcze:**
- **Proces ma być w większości niewidoczny.** 7 kroków = 7 wywołań LLM = wolno i drogo. Użytkownik widzi *pewność i uzasadnienie*, nie siedem ekranów ładowania.
- **Iteracja z twardym limitem 2–3 rund** + wyjście awaryjne „po prostu pokaż propozycje". Bez tego użytkownicy odpadają.
- **Pewność musi być zasłużona** — wyliczana z tego, ile ograniczeń faktycznie znamy. Licznik zawsze dobijający do 95% to teatr, czyli dokładnie „udawane AI", którego się zarzekliśmy nie robić.
- **§2 i §8 to jeden mechanizm, nie dwa pomysły.** Uzasadnienie oparte na regule z bazy wiedzy = wiarygodne. Uzasadnienie wymyślone przez LLM w locie = ładnie brzmiąca konfabulacja, gorsza niż jej brak. **Baza wiedzy istnieje po to, żeby AI miało na co się powołać.**

---

## B. Przeramowane

### B1. Designer Knowledge Base (§2) — budujemy, ale to nie jest fosa sama w sobie

Reguły typu „środek obrazu na 145 cm", „galeria 60–80% szerokości sofy" to **wiedza publiczna** — powtarzana w każdym poradniku wnętrzarskim, znana każdemu LLM-owi. Spisanie publicznych reguł do pliku nie tworzy przewagi.

**Fosą jest dopiero: KB × nasz katalog × dane z wyników.**

Ujęcie Artura (trafniejsze od pierwotnego zarzutu Claude'a): **publiczna wiedza to ziarno, nie produkt.** Spisujemy ją raz — tanio i szybko — a potem **specjalizujemy pod nas**: pod nasz katalog, nasze formaty i rozmiary, realne pokoje naszych klientów. Po 200 projektach nie mamy już „galeria 60–80% szerokości sofy", tylko *„przy sofie 220 cm w tym stylu najlepiej działa ten układ z tych 12 naszych prac"*. Tego nikt nie skopiuje, bo to wiedza **o naszym katalogu**, nie o wnętrzach w ogóle.

| Warstwa KB | Kiedy |
|---|---|
| A. Zasady · B. Heurystyki · D. Wzorce projektowe | **Teraz** — zwykły plik, natychmiastowa wartość |
| C. Wyjątki | Teraz, cienko |
| E. Przypadki (case studies) | Wymaga zrealizowanych projektów |
| F. Confidence / liczba użyć / skuteczność | **Wymaga wolumenu.** Przy kilkunastu zamówieniach „skuteczność 73%" to szum, nie dana |

**Powód budowy KB: robi doradcę dobrym, przewidywalnym i zdolnym do argumentacji od dnia 1** — nie „bo to fosa". Fosą staje się przez używanie.

### B2. Korekta faktograficzna do §1 — Modsy (ostrzeżenie wycofane)

Claude wielokrotnie ostrzegał przed „cmentarzyskiem Modsy". Po weryfikacji **ostrzeżenie w tej formie zostaje wycofane.**

Fakty: Modsy działało na sieci **~250 własnych projektantów-ludzi**, robiło renderingi 3D **całych pokoi** z meblami znanych marek, i zamknęło usługę projektową w czerwcu 2022. Podana przyczyna: **łączenie ludzkich projektantów z softwarem było kapitałochłonne i nie skalowało się rentownie** (potem pivot do SaaS dla projektantów).

To był **cały pokój + ludzie w pętli**, nie AI. Nasz model jest strukturalnie inny: **mikro-wycinek (jedna ściana z obrazami) + AI (marginalny koszt bliski zeru) + sprzedaż z własnego katalogu.** Dwie rzeczy, które zabiły Modsy — koszt pracy ludzkiej na projekt i wyciek klienta do cudzych mebli — są u nas dużo słabsze.

**Co z lekcji zostaje (realne):**
1. **Nigdy nie dokładać człowieka do pojedynczego projektu.** Żadnego „nasz projektant to sprawdzi" — tam umarło Modsy.
2. **Poprzeczka jakości jest wysoka.** Ludzie płacili Modsy za *ludzki osąd*. Nasze AI musi dawać poczucie prawdziwej porady, inaczej jest gadżetem.

Źródła: [TechCrunch](https://techcrunch.com/2022/06/29/modsy-shuts-down-design-services-cutting-roles-and-disrupting-orders/) · [Fortune](https://fortune.com/2022/06/29/modsy-interior-design-startup-shutting-down-design-business-splitting-with-designers/) · [Business of Home](https://businessofhome.com/articles/modsy-abruptly-shuts-down)

---

## C. Odrzucone lub odłożone

### C1. Osiem ścieżek wejścia (§6) → jeden flow

Te 8 wejść to **nie 8 ścieżek**, bo wymieszały się trzy różne warstwy:

| Warstwa | Przykłady | Rozgałęzia logikę? |
|---|---|---|
| **Typ projektu** | pusta ściana · dołóż do istniejącego · cały pokój | ✅ tylko to |
| **Materiał wejściowy** | zdjęcie ściany · wymiary · inspiracja z internetu · zdjęcia moich obrazów | ❌ pole w stanie projektu |
| **Kontekst** | przeprowadzka · remont · prezent | ❌ pole w stanie projektu |

**Rozwiązanie: JEDEN flow, typ projektu jako parametr w jednym kroku, reszta to dane.** Budowanie 8 osobnych ścieżek to wprost pułapka „zespół z budżetem".

### C2. Pętla uczenia (§9) — nie teraz; log od dnia 1

Kierunek prawidłowy (i jedyny, który realnie buduje fosę), ale pętla potrzebuje **wolumenu** — przy pierwszych kilkudziesięciu projektach uczysz się na szumie i utrwalasz przypadki.

**Tania, uczciwa wersja: nie buduj pętli — buduj log.** Zapisuj od dnia 1 każdą decyzję (co zaproponowane / przyjęte / odrzucone / poprawione / kupione), żeby dane **już były**, gdy wolumen przyjdzie.

### C3. Pozostałe
- **„Cały pokój" jako typ projektu → v2** (wymaga spójności między wieloma ścianami = skokowo trudniejsze; później to powtórzenie flow ściany × N).
- **Wejścia niekończące się sprzedażą u nas** („kupiłem gdzie indziej, powieś mi", „dobierz tylko rozmiar") — wypadają z MVP.

---

## D. Rozstrzygnięcia Artura

1. **Pamięć: nie profil pojedynczego klienta, tylko system uczący się z całej puli klientów.**
   > **Latenca nie pamięta Ciebie. Latenca pamięta, co działa.**

   Pamięcią produktu jest **baza wiedzy**, nie profil użytkownika. **Zgodne z zablokowanym single-session**, bez problemów z prywatnością, a efekt uczenia zostaje. *(To rozwiązuje zgłoszony konflikt: stan projektu obowiązuje w obrębie sesji; pamięci między sesjami dla jednego klienta nie budujemy.)*

2. **Hybryda, nie wybór — sklep i projektant to dwa światy, które łączymy:**
   - **Sklep = podłoga.** Katalog, strona produktu, konfigurator, koszyk. Istnieje zawsze; każda ścieżka w nim ląduje.
   - **Projektant = drzwi frontowe i twarz marki.** To widać pierwsze i o tym opowiadamy.
   - **Zasada rozstrzygająca: projektant nigdy nie jest bramką.** Zawsze da się go ominąć i kupić w 2 minuty — ale to on jest bohaterem strony głównej.

   *(To rozwiązuje zgłoszony konflikt z D-007 / D-012. Po weryfikacji Modsy hybryda jest bezpieczna: warstwa projektowa nic nie kosztuje na klienta i prowadzi do własnego katalogu.)*

3. **Wszystkie ścieżki muszą kończyć się sprzedażą u nas.** Nie robimy konsultacji doradczych bez zakupu.

4. **Typy projektu w MVP: dwa** — (a) pusta ściana, (b) dołóż / wymień. Wybór **jednym tapnięciem na starcie**: pytamy, zamiast zgadywać, bo błąd rozpoznania w kroku 1 zatruwa całą sesję. Wnioskowanie przez AI = późniejsze ulepszenie.

---

## E. Otwarte pytania do ChatGPT

1. Czy hybryda **„projektant jako drzwi, nigdy jako bramka"** się broni, czy rozmywa oba światy?
2. Co realnie ma napędzać **licznik pewności**, żeby był uczciwy, a nie dekoracyjny?
3. Jaka jest **minimalna baza wiedzy**, przy której porada przestaje brzmieć generycznie już w dniu 1?
4. Czy **dwa typy projektu** wystarczą na start, czy „cały pokój" jest potrzebny od razu ze względu na wartość koszyka?
5. **Żadna z 9 hipotez nie dotyka dystrybucji** — a to jest ryzyko nr 1. Jak produkt ma sam produkować treść do kanału, który dowiezie pierwszych obcych klientów?

---

## Powiązane
[`VISION.md`](VISION.md) · [`DECISIONS.md`](DECISIONS.md) · [`LOCKS.md`](LOCKS.md) · [`REVIEW_WORKFLOW.md`](REVIEW_WORKFLOW.md) · [`../Analizy/`](../Analizy/)
