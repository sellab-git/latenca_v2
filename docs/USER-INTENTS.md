# USER-INTENTS — synteza: z czym ludzie przychodzą i co z tym robimy

> Cel (Artur, 2026-07-21): zanim zbudujemy więcej, poznać CAŁĄ przestrzeń intencji „z każdej możliwej strony" i rozwiązać ścieżki, żeby nie iść w coś bez sensu.
> Pełny katalog **178 scenariuszy** (6 wymiarów) → `USER-INTENTS-CATALOG.md`. Ten plik to **synteza**: framework, fazy, zwinięcie do realnych flow, sygnały przekrojowe, decyzje. **Mapa, nie decyzje** — do pressure-testu z Arturem i ChatGPT.
> Punkt odniesienia (obecna budowa): landing = katalog; produkt ma wbudowanego doradcę (model D, D-046) na **jednej grafice**; MVP = pojedyncza grafika (D-023); wielo-grafikowe ściany = zapisana luka (D-033 pkt 6).

---

## 1. Odpowiedź na „czy nie ma ich 100?": TAK — i to jest przewidywalne

Intencji nie jest 5. Jest ich **100+**, bo każda realna osoba to **punkt w przestrzeni 6 osi**. Skrzyżuj je, a masz setki:

| Oś | Zakres wartości |
|---|---|
| **A. Stan ściany/przestrzeni** | pusta · częściowo zapełniona · do przeróbki · luka obok posiadanej · nad meblem (sofa/łóżko/konsola/biurko/stół/kominek/TV) · trudna (korytarz/klatka/skos/róg/wysoka/mała/ekstremalny aspekt) · cały pokój |
| **B. Okazja / „dlaczego teraz"** | przeprowadzka · remont · odświeżenie · prezent (×8 typów) · dziecko · biuro · sezon · impreza · downsizing · kamień milowy · żałoba · **biznes (kawiarnia/klinika/salon/biuro/hotel/Airbnb/rebrand)** |
| **C. Kto + głęboka emocja** | lękliwy nowicjusz · pewny dekorator · minimalista · maksymalista · „nie mam gustu" · dający prezent · projektant/B2B · stager · najemca · para w konflikcie · ekspat · downsizer — × emocja: spokój/statement/zakryć wadę/zaimponować/tożsamość/pamięć/„jak w domu"/wypełnić pustkę |
| **D. Stan decyzji** | wie dokładnie · mgliście · zagubiony · „zaskocz mnie" · waliduje wybór · porównuje · „tylko oglądam" · utknął między 3 · żałuje po dodaniu do koszyka |
| **E. Jak wyraża gust** | nazwa stylu · reakcja (cieplej/spokojniej) · lubiany obraz · nastrój · kolor · artysta · temat · „dopasuj do sofy" · inspiracja · lista „czego NIE" |
| **F. Ograniczenia** | budżet · dokładne wymiary · deadline · materiał/finisz · orientacja · dopasować do posiadanej ramy · kraj/VAT · waga/montaż · wilgoć · dostępność |

To jest „każda możliwa strona". Dobra wiadomość: **178 scenariuszy zwija się do ~13 realnych FLOW** (rozdz. 4) — bo build potrzebuje flow, nie 178 wierszy.

---

## 2. Model FAZ — każda intencja przechodzi przez ten sam szkielet

Niezależnie od intencji, człowiek przechodzi (lub przeskakuje) te fazy. To jest kręgosłup, na który mapujemy każdy scenariusz:

```
1. WEJŚCIE        skąd przyszedł (Google/Pinterest/reel/prezent-link/direct/powrót) i z jaką intencją
2. ORIENTACJA     „co to jest i czy mi pomoże" — w kilka sekund
3. WYRAŻENIE      przekazuje gust/potrzebę (słowo/reakcja/zdjęcie/wymiar/kolor) — albo deleguje
4. PROPOZYCJA     AI proponuje pracę/zestaw + DLACZEGO (rdzeń „pewności")
5. REAKCJA/SWAP   „cieplej/spokojniej/inne" → podmiana w miejscu (pętla)
6. DOPASOWANIE    skala/fit do ściany (true-cm, „za mała ściana = powiem ci")
7. KONFIGURACJA   materiał · rozmiar · rama (zwykły konfigurator)
8. CHECKOUT       cena landed (VAT/wysyłka/termin) · płatność szybka
9. PO ZAKUPIE     track · reklamacja/zwrot · upgrade przed wysyłką · „pochwal się ścianą"
```

**Co obecna budowa (model D) ma:** fazy 4–7 (propozycja, swap, konfiguracja) na jednej grafice, + 1/2/8 przez sklep. **Czego brakuje lub jest słabe:** faza 3 dla nietekstowych wejść (zdjęcie/wymiar/inspiracja), faza 6 (true-cm/„za mała"), faza 9 (post-purchase), i cała gałąź wielo-grafikowa w 4–7.

---

## 3. Twoje 5 przykładów — gdzie są w tej przestrzeni

| Twój przykład | Oś | Status dziś |
|---|---|---|
| Pusta ściana, nie wiem co | A:pusta + D:zagubiony | ✅ single — brak opcji zestawu |
| Mam grafikę, dobrać nową | A:luka-obok + E:lubiany-obraz | 🟡 proponuje jedną, nie komponuje zestawu wokół |
| Kupić jedną grafikę | D:wie + browse | ✅ pełne |
| Wymiary kilku grafik | A:cały-pokój + F:wymiary | ⛔ nieobsłużone (luka SET) |
| Lubię coś, chcę podobne | E:lubiany-obraz/reakcja | ✅ przez rozmowę — brak reverse-image |

---

## 4. ZWINIĘCIE — 178 scenariuszy → 13 flow (to jest to, co się buduje)

| Flow | Co robi | Zasila (przykłady z katalogu) | Status |
|---|---|---|---|
| **1. Browse-and-buy** | zdecydowany: katalog → produkt → koszyk | DEC-3, CH-1..6, WHO-2 | ✅ jest |
| **2. Doradca: jedna praca na ścianę** | pusta/ten-pokój/nastrój/reakcja-swap (rdzeń model D) | SPACE-1..9, DEC-2/4/10, WHO-1/3/5 | ✅ jest (single) |
| **3. Doradca: dobierz do posiadanego** | input posiadanej pracy (zdjęcie/opis) + spójność | SPACE-11/13, CON-7, DEC-6, CH-14 | 🟡 częściowe |
| **4. Doradca: ZESTAW / galeria / pokój** | AI proponuje aranżację-produkt (para/tryptyk/3–5) | SPACE-10/12/19/22/27, WHO-27, DEC-21/22/27, CON-2/20/21/28, CH-3 | ⛔ **luka — sedno** |
| **5. Dopasowanie skali/wymiaru** | true-cm, „za mała ściana = powiem", rozmiar-do-slotu | SPACE-2/18/21/29, CON-3/4/5/24/27, DEC-23 | 🟡 do zrobienia |
| **6. „Więcej jak TA"** (reverse-image) | znajdź podobne do konkretnego obrazu | DEC-3/7/16, CH-7/12 | ⛔ luka |
| **7. Prezent** | wiadomość, wysyłka do obdarowanego, łatwa wymiana, termin | OCC-5/6/7/8/20, WHO-6/7, CH-10 | ⛔ luka |
| **8. B2B / trade** | multi-room, wolumen, faktura VAT, wycena/konto, SLA, duże formaty | OCC-21..28, WHO-16/17 | ⛔ luka (wysoki AOV) |
| **9. Bramki ograniczeń** | budżet · deadline/ships-by · kraj/VAT · materiał-pod-pokój (wilgoć/waga/refleks) · bez-wiercenia | CON-1/2/9/10/14/15/23/29/30, SPACE-23/26 | 🟡 częściowe |
| **10. Powroty / reorder / dobuduj ścianę** | pamięć zamówień/konto | DEC-28, WHO-26, CH-13..17 | ⛔ luka |
| **11. Zapisz na później + ścieżka bez zdjęcia** | wishlist bez wymuszonego konta; kup bez uploadu | DEC-13, CH-27/31 | ⛔ luka |
| **12. Momenty zaufania / obiekcji** | „czemu AI / czemu ta cena / tylko fizyczne / czy będzie jak IRL / człowiek / zwroty" | WHO-24, DEC-12/26, CH-11/19/21/22/23/25/26/32 | 🟡 częściowe |
| **13. Po zakupie** | track · reklamacja/zwrot · upgrade przed wysyłką · „pochwal się ścianą" (silnik ruchu) | CH-17/25/26 | ⛔ luka |

---

## 5. Sygnały PRZEKROJOWE — rzeczy, które psują WIELE scenariuszy naraz

Wszystkich 6 agentów niezależnie wskazało te same nośne braki (kolejność = ile scenariuszy dotyka):

1. **ZESTAWY (wielo-grafika)** — największy; jest naraz rdzeniem wizji, ekonomią (2. sztuka w paczce ~€0,29) i luką. Blokuje flow 4 + kawałki 3/8/10.
2. **True-cm skala + uczciwe „za mała ściana"** — nośne dla całej obietnicy „pewności"; psuje flow 5 i czai się w każdym zakupie fizycznym.
3. **Uczciwy termin dostawy + cena landed (VAT/cło) z góry** — zabija wszystkie deadline'owe i zagraniczne (prezenty, imprezy, cross-border).
4. **Świadomość rozdzielczości-per-obraz i materiału-per-pokój** (wilgoć/waga/refleks/canvas) — nie tylko filtr, ale wiedza doradcy.
5. **Pamięć poprzednich zakupów** — nośna dla powrotów (flow 10); dziś jej nie ma.
6. **Ścieżka bez zdjęcia + wishlist bez wymuszonego konta** — powtarzający się bloker (flow 11).
7. **Narracja „czemu AI / czemu cena / tylko fizyczne" w momencie tarcia** — psuje flow 12.
8. **B2B nie ma domu** — mimo najwyższego AOV (flow 8).
9. **Fallback ludzki + wsparcie/zwroty** — ryzyko skalowania solo-foundera (flow 12/13).
10. **Kody dzielenia pracy/sesji** — napędzają referral (CH-9/10/12), tanie do zbudowania.

---

## 6. Decyzje dla Ciebie (forki — do rozmowy z ChatGPT, nie odpowiadaj na formularz)

Uszeregowane wg wpływu:

1. **ZESTAWY — sedno.** Wchodzą do MVP i JAK (hipoteza: „AI proponuje aranżację jako jeden produkt, akceptujesz/wymieniasz, nigdy nie układasz")? Czy zostajemy przy jednej grafice i świadomie odkładamy flow 4 + ekonomię zestawów?
2. **B2B/trade (flow 8)** — osobny tor teraz, czy świadomie ignorujemy (kłóci się z „jedna sesja, bez profilu", D-024)? Wysoki AOV, ale inny produkt.
3. **Powroty/konto/pamięć (flow 10)** — MVP czy później? (wpływa na model danych JUŻ teraz).
4. **Prezent (flow 7)** i **„więcej jak ta" (flow 6)** — MVP czy backlog?
5. **Które bramki ograniczeń (flow 9)** są MVP (deadline, kraj/VAT są chyba nie-do-uniknięcia) vs później?
6. **Narracja zaufania (flow 12)** — trzeba zaprojektować niezależnie od reszty (tania, wysoki wpływ). Potwierdzasz jako must?
7. **Priorytet „5 Twoich" vs to, co wypłynęło** — czy Twoje 5 to komplet startowy, czy dorzucamy prezent/B2B/powroty?

---

*Następny krok po Twojej reakcji: wybrać podzbiór flow na MVP → dla każdego rozpisać „faza-po-fazie" na konkretne ekrany (na model D + shell/app.css) → przepisać przestarzały `SCREEN_MAP.md`. ChatGPT = senior reviewer tego + katalogu (czyta repo); przygotuję brief. Nie ruszam budowy, dopóki nie uzgodnimy flow.*

---

## 7. Runda 2 — recenzja ChatGPT (2026-07-21) i wynikające ulepszenia

ChatGPT (senior reviewer) pressure-testował mapę. Werdykt: szeroka, ale słabsza jako mapa **stanów systemu i porażek operacyjnych**. Poniżej przyjęte ulepszenia (nie zmieniają decyzji — poprawiają mapę) + jedna decyzja dla Artura.

### 7.1 Nowe braki (realne, tanie do przewidzenia, przyjęte do mapy)
- **Feasibility / substitution engine** — najważniejszy. AI może polecać **tylko z wariantów, które przejdą**: rozmiar, DPI (rozdzielczość per obraz), materiał, kraj/wysyłkę, termin. Nie wolno sprzedać pewności, a potem powiedzieć „środkowy obraz niedostępny/za mała rozdzielczość na 70×100". To **wspólny mechanizm przed rekomendacją**, nie edge-case. (Łączy CON-20/21/26, CH-13, cała gałąź zestawów.)
- **„Nie mam uczciwego dopasowania"** — pełnoprawny wynik doradcy. Przy małym kurowanym katalogu będzie częsty (mała wnęka, ogromna ściana, ekstremalny aspekt, twarde ograniczenia). Bezpośredni test D-002 „trust before sales". Część faz 4/6/9, nie osobny ekran.
- **Taksonomia zestawu** — para/tryptyk/galeria to NIE jedna kategoria: (1) **jeden obraz podzielony na panele** (diptych/triptych z jednego motywu), (2) **coordinated set** (różne prace jako rodzina), (3) **gallery wall** (różne prace + formaty + układ). Różna logika katalogowa/produkcyjna/zakupowa.
- **Perspektywa operatora** (solo) — scenariusze wewnętrzne, bez których zestawy zaprojektujemy idealistycznie: praca wypada z jakości, Gelato wycofuje wariant, zmiana kosztu/dostępności, podmiana elementu we wszystkich aktywnych zestawach, ręczna podmiana uszkodzonego elementu.
- **Częściowa awaria zestawu** — 3 elementy, jeden uszkodzony; dwie paczki w różnych terminach; jeden panel w innym kolorze; zwrot jednego elementu. `ORDER_LINE` musi obsługiwać element osobno, choć klient kupił aranżację jako całość.

### 7.2 13 flow → 5 głównych PODRÓŻY (przyjęte — czystszy model)
ChatGPT słusznie: 13 pozycji było na różnych poziomach abstrakcji. Nowy podział:
- **5 głównych podróży:** 1) Browse-and-buy · 2) Doradca: jedna praca · 3) Dobierz do posiadanej · 4) Kup kuratorowany zestaw · 5) Po-zakupie / support / reorder.
- **Reszta to warstwy, nie osobne podróże:** *wejścia* (Google/Pinterest/reel/prezent-link/powrót, „więcej jak ta"), *capabilities* (**feasibility+skala** — obowiązkowa faza każdego zakupu; similarity), *reguły przekrojowe* (**constraint engine**: budżet/rozmiar/materiał/kraj/deadline/montaż; **warstwa zaufania** = copy w momentach tarcia; **ścieżka bez zdjęcia** = zasada wszystkich flow), *lifecycle/commerce* (wishlist, konto/reorder, prezent-overlay, tracking/zwroty).
- **B2B (dawny flow 8) = osobny produkt operacyjny, nie wariant konsumencki** — backlog. Nie łamie D-024 (może mieć projekt/konto firmowe bez profilu gustu konsumenta).

### 7.3 Zestawy — forma i kolejność (rekomendacja ChatGPT, spójna z naszą)
- **Forma:** „zestaw = jedna kuratorowana aranżacja, którą akceptujesz albo wymieniasz" — poprawna. „Jeden produkt" = **jedna decyzja handlowa** (jedna cena, jedno „Add set to cart", „Show me another"), ale w modelu **wiele elementów** (`SET_ITEM[]`), każdy z własnym wariantem produkcyjnym i osobnym `ORDER_LINE`.
- **Fazy MVP zestawu:** wejście = wybierasz tylko *Para/Tryptyk/Galeria* (+opcjonalnie szerokość ściany, klimat, posiadana praca) — **nie pusty canvas**. Propozycja = jedna gotowa aranżacja na płaskiej ścianie (obrazy, rozmiary, odstępy, całkowita szerokość, „dlaczego"). Reakcja poziom 1 = Keep / Show another / Warmer / Calmer / Bolder; wymiana pojedynczego panelu = **dopiero później** (kombinatoryka niszczy spójność). Dopasowanie = feasibility całości. Konfiguracja MVP = **jeden materiał + jedna rama dla całego zestawu** + 2–3 skale (Compact/Balanced/Statement). Koszyk = jedna karta zestawu (aranżacja, elementy, łączna cena, łączny termin, info o osobnych paczkach).
- **Kolejność typów:** 1) **Para** (najłatwiejsza) → 2) **Tryptyk** (jako zamknięty kuratorowany SKU) → 3) **Gallery wall 3–5** (po parze) → 4) **Dobierz do posiadanej** (v2, wymaga realnego vision).
- **Model danych:** `SET/WALL` jako obiekt od początku — **już przewidziany w `PRODUCT_BIBLE.md` §5** (SET/WALL = centralny obiekt). Minimalny schemat: `WallOrSet{type, source, items[], layout_preset_id, total_w/h_cm, spacing, rationale}` + `SetItem{artwork_id, position, size, material, frame}`. Layout = preset/dane, **nie zapis drag-and-drop**.

### 7.4 Top ryzyka (przyjęte)
1. **Over-build „178 intencji"** → katalog to *taxonomy/testing reference*, nie backlog; każda funkcja musi obsłużyć wiele scenariuszy naraz.
2. **Zestawy wybuchają kombinatorycznie** → zamknięte pary, jeden materiał/rama, 2–3 skale, wymiana całości nie panelu.
3. **„Pewność" bez pewności produkcyjnej** → feasibility PRZED rekomendacją (§7.1).
4. **Zestaw wypiera single** → jednostka (single/pair/set) wynika z **przestrzeni+intencji, nie z marży**; system musi umieć polecić jedną pracę jako najlepszą (chroni WHO-25 minimalistę + D-002).
5. **Pamięć ≠ profil gustu** → od początku trzymać historię zamówień + opcjonalne zapisane zestawy, ale **nie inferować profilu gustu** (D-024 trzyma).

### 7.5 ⚠️ DECYZJA DLA ARTURA (blokuje resztę — wymaga jawnej zmiany D-023/D-030/D-033)
ChatGPT i ja rekomendujemy **formalne rozszerzenie MVP z „pojedyncza grafika" na „single + curated pair"** (para jako zamknięty produkt-zestaw, bez canvasu, bez wymiany paneli). To najtańszy krok do ekonomii zestawów (2. sztuka w paczce ~€0,29) i przybliża produkt do „dobrej ściany", nie „sklepu z plakatami". **To NIE może być ciche rozszerzenie** — potrzebna świadoma zmiana D-023/D-030/D-033.

Moje rekomendowane odpowiedzi na 5 pytań ChatGPT (do potwierdzenia/korekty przez Artura):
1. **Para = dwie różne, skoordynowane prace** (rodzina), nie jeden obraz podzielony — bo split-image to inna logika produkcyjna i słabiej wyraża kurację. *(rekomendacja)*
2. **Zestaw kupowany jako całość** w v1; kup pojedynczy element z zestawu = później. *(rekomendacja)*
3. **Wymiana całej aranżacji, nie pojedynczego panelu** w v1. *(rekomendacja)*
4. **Jeden materiał + jedna rama dla całego zestawu** jako ograniczenie MVP. *(rekomendacja)*
5. **Tak, rozszerzyć MVP do „single + curated pair"** — jawnie doprecyzować D-023/D-030/D-033. *(rekomendacja — czeka na decyzję Artura)*

Proponowana kolejność budowy (ChatGPT, przyjęta): 1) kręgosłup sklepu + pojedynczy produkt → 2) warstwa skala/feasibility → 3) doradca jednej pracy → 4) **kuratorowana para jako SET/WALL** → 5) baseline zaufania + po-zakupie → 6) tryptyki/galeria → 7) dobierz-do-posiadanej (po teście vision) → 8) reorder/save/prezent → 9) B2B jako osobna decyzja.

---

## 8. Runda 3 — reframe Artura (2026-07-21): ZMIENNA liczba prac, dwie drogi do ściany

⚠️ Artur odrzucił framing „zamknięta para + jeden materiał" (§7.3/7.5). Poprawiony model:

- **Prymityw = pojedyncza praca** (artwork × rozmiar × materiał × rama). Kup 1 = single.
- **„Ściana" = ZMIENNA liczba prac (1, 2, 3, 10…)** kupowanych razem. Nie ma sztywnej „pary". Trzeba umieć sprzedać dowolne N w spójnej kompozycji/zestawie.
- **Materiały = wszystkie od Gelato** (papier, płótno, akryl, drewno, metal, pianka) — **per praca**, nie zablokowane do jednego na zestaw.
- **Wzorzec prostoty = Mixtiles.** Ich analiza (`Analizy/Mixtiles/docs/UX-FLOW.md`) pokazuje **dwie drogi do ściany**, obie proste:
  - **(A) Gotowe układy „Gallery Walls"** — pre-zaprojektowane kompozycje N prac (nazwa, wymiary, liczba, cena „From", BEST SELLER); wybierasz → wypełniasz → koszyk. Szablon rozwiązuje „nie wiem jak ułożyć", **bez przeciągania** (zgodne z D-033). Nasza VISION już to zakłada: „Kolekcje = gotowe ściany (gallery walls jak Desenio)".
  - **(B) Wolne składanie** — dodajesz dowolną liczbę prac, każda personalizowana osobno, koszyk sumuje na żywo + próg wysyłki/rabatu.

### Co zostało do WYJAŚNIENIA (otwarte, do rozstrzygnięcia z Arturem)
1. **Dwie drogi — obie na MVP czy jedna?** Gotowe układy (A) i/lub wolne składanie (B). *(rek.: obie — A daje pewność i AOV bez wysiłku usera, B daje elastyczność; A prostsza do udania w makiecie.)*
2. **Kto układa kompozycję (przy N>1)?** Szablon (wybierasz+wypełniasz) / AI proponuje układ / brak układu (lista, sam wieszasz). *(rek.: szablon + AI-proponuje, NIGDY drag — D-033.)*
3. **Podgląd ściany:** pokazujemy N prac razem na płaskiej ścianie w konkretnym układzie (dla pewności), czy tylko siatkę? Czy układ w podglądzie jest tylko wizualny (i tak sam wieszasz, nie wpływa na to, co wysyłamy)? *(rek.: podgląd na ścianie, układ = wizualna pewność.)*
4. **Spójność vs dowolność per praca:** wszystkie materiały dostępne per sztuka (potwierdzone). Czy doradca NUDGE-uje spójność (np. „ta sama rama dla ściany"), czy pełna dowolność jak Mixtiles? *(rek.: dowolność + delikatny nudge spójności.)*
5. **Cennik przy N:** per-praca sumowane na żywo (Mixtiles). Dokładamy rabat/próg za większą ścianę (ekonomia €0,29/kolejna sztuka), żeby zachęcić do N>1? *(rek.: tak, próg free-shipping / rabat od 2–3 szt.)*
6. **Gdzie N prac „żyje" w UI:** model D = jedna praca + doradca. Przy N potrzeba powierzchni „ściana/projekt". Czy „ściana" to osobny ekran/projekt, czy rozszerzony koszyk-jako-ściana (Mixtiles)? *(rek.: „ściana" jako lekki projekt/koszyk, nie ciężki edytor.)*
7. **Rola doradcy przy N:** proponuje CAŁĄ ścianę N naraz (feasibility per praca + logika kompozycji), czy zawsze jedną, a Ty dokładasz? *(otwarte — wpływa na złożoność.)*
8. **Feasibility przy N:** „czy się zmieści" liczy całkowitą szerokość N + odstępy, nie jedną. *(potwierdzić że silnik z §7.1 to obejmuje.)*
9. **Kuracja gotowych ścian:** układy (A) ktoś (operator/AI) musi skomponować z katalogu z góry — praca kuratorska. Ile na start? *(otwarte.)*
10. **„10 prac" = 10 różnych** (galeria) — czy dopuszczamy wielokrotności tej samej? *(edge, rek.: różne.)*

*Ten reframe unieważnia „curated pair jako pierwszy krok" z §7.5. Nowa jednostka to zmienne N. Decyzje z §7.5 (materiał/rama, para) zastąpione powyższymi. Po rozstrzygnięciu 1–10 → projekt decyzji D-047 (jednostka = 1..N, dwie drogi) + przepisanie SCREEN_MAP.*

### Pomysł Artura (2026-07-21, do zapamiętania) — STRONA PRODUKTU = ŚCIANA
Kandydat na odpowiedź do otwartych #3 (gdzie N żyje) i #6 (osobny ekran vs koszyk):
**Nie ma osobnego ekranu „ściana" — strona produktu NIĄ jest.** Wchodzisz na jedną pracę (model D: praca na środku + czat po prawej). Gdzieś prompt „dodaj kolejną pracę / zbuduj z tego ścianę". Scena **rośnie w bok w rząd prac** — jak Mixtiles: kafle obok siebie, przesuwają się lewo/prawo, skalują, zmieniają ramki per sztuka — a **czat doradcy zostaje po prawej** (to, czego Mixtiles nie ma). Czerwone pola po bokach centralnej pracy = miejsce na kolejne.
- **Mocne:** unifikuje model D ze ścianą (zero nowego ekranu), N=1 płynnie rośnie do N>1, Mixtiles-prostota + nasz czat = przewaga.
- **Zgodność z D-033 (skorygowane przez Artura 2026-07-21):** Mixtiles **NIE** pozwala dowolnie przeciągać kafli — one same przesuwają się w rzędzie zależnie od kliknięcia (fokus). Czyli **układ trzyma system (rząd), nie user** — to nie canvas. User zmienia tylko rzeczy per-praca, które MY już mamy w model D (rozmiar/rama). Więc napięcie z D-033 jest **małe**: pozycji się nie przeciąga, system/AI trzyma układ, Ty oglądasz i podmieniasz prace. To ewolucja D-033 w duchu zasady, nie złamanie.
- Status: **zaparkowane jako wiodący kierunek dla powierzchni ściany** — potwierdzić przy rozstrzyganiu #1–#3.

### Model przepływu (Artur, 2026-07-21) — JEDNA powierzchnia = ściana, chooser intencji, wiele ścieżek
To rozwija pomysł „strona produktu = ściana" w pełny przepływ. **Rozstrzyga otwarte #1 (obie drogi), #2 (system/AI układa), #3/#6 (produkt = ściana).**

**Wejście:** Home → „Start design" → powierzchnia‑ściana. Prawa = czat (jak model D). Środek, przed wyborem = **kafelki‑chooser intencji**. Po wyborze środek ładuje jedną ze ścieżek; wszystko dzieje się dalej na tej samej ścianie z czatem po prawej. Całość ma być **mega prosta i interaktywna** (Mixtiles‑prostota + nasz czat).

**Ścieżki po wyborze intencji (Artur):**
1. Jedna praca na środku (← mamy, model D).
2. Wybrana ściana z pustymi slotami → dobiera prace rozmawiając w czacie.
3. Wgrał zdjęcie → pojawia się wybrana przez AI praca startowa.
4. Wybrał konkretny układ + wgrał zdjęcie → ściana od razu z wypełnionymi pracami.
5. Pojedyncza praca → AI „może warto dodać 2gą" → klik OK → druga praca obok (każda kolejna obok, rząd rośnie).
6. Wcześniej wybrał układ → sloty się pokazują; np. 2 wypełnione, 3ci ze schematu pusty → klikasz pusty i dobierasz dalej.

**Kafelki‑chooser — PROPOZYCJA (Artur: „nie wiem"; propozycja grounded w mapie intencji, do korekty):**
- **„Jedna praca"** → ścieżka 1 (single).
- **„Zaprojektuj ścianę"** → gotowe układy + AI składa; ścieżki 2/6.
- **„Wgraj zdjęcie"** → od Twojej przestrzeni albo pracy, którą masz; ścieżki 3/4 (+ „dobierz do posiadanej").
- **„Nie wiem — zaskocz mnie"** → AI decyduje i startuje (delegacja).
- *(opcjonalnie 5ty: „Przeglądaj gotowe ściany" — albo to = Kolekcje w nawigacji.)*
Zasada: max 4–5 kafli, opisane konkretnie (NN/g G3/G4). Wejście z katalogu na konkretną pracę **pomija chooser** → od razu ścieżka 1.

**Małe do dogrania (później):** kiedy pali się upsell „dodaj 2gą" (po akceptacji pracy? po rozmiarze?); jak dokładnie działa klik w pusty slot; jak rząd się „sam przesuwa" na fokus (Mixtiles).

### Mechanika ściany + prawy panel (Artur, 2026-07-21)
- **Katalog i designer = ta sama powierzchnia i ten sam PROJEKT.** Wejście z katalogu ląduje na 1 pracy, ale ma identyczne możliwości (pomija tylko chooser). Jedna praca → dodawanie → układy = **kolejne fazy jednego projektu ściany**.
- **Układy = biblioteka presetów per liczba prac** (np. 10 układów dla 4 prac, 10 dla 5…). Zmiana układu dynamiczna. Zejście z N na N‑1 → nadmiarowa praca ląduje **w zapasie** (nie znika). **Zero przeciągania prac po ścianie** — układ trzyma system (D‑033‑safe, tanie: układ = dane).
- **Rozmiary należą do UKŁADU** (slot = pozycja + rozmiar; „1 duża + 4 małe" definiuje układ). Praca wrzucona w slot bierze rozmiar slotu. „Inny rozmiar" = „inny układ", nie dowolne skalowanie → brak wybuchu kombinatoryki. *(Do potwierdzenia: czy rozmiar pojedynczej pracy można zmieniać niezależnie od układu — rek.: NIE; per praca zmieniasz materiał/ramę i którą grafikę.)*
- **Prawy panel = dwa poziomy** (naturalne rozszerzenie model D):
  - **Poziom PRACY (fokus):** klik w pracę na ścianie → panel pokazuje jej config (materiał, rama, podmiana grafiki). Config zawsze dotyczy 1 zaznaczonej pracy.
  - **Poziom ŚCIANY (zawsze):** czat (o całej ścianie), **łączna cena**, **„dodaj ścianę do koszyka"**, **przełącznik układu**, liczba prac + zapas.
  - Mapowanie na model D: dzisiejszy header/config = poziom pracy; czat + dok (total + add) = poziom ściany, tylko rozszerzony o total całości i przełącznik układu.
