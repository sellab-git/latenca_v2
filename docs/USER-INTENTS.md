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
