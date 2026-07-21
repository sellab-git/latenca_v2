# RESEARCH — panel produktu vs doradca: najlepsze wzorce 2026

> Pytanie Artura (2026-07-21): dwa stany prawego panelu (dane produktu ↔ czat) są niespójne — różna wysokość, nieintuicyjne przełączanie, dwa różne markery. Czy warianty, które proponuję, to naprawdę „najlepsze z najlepszych" wzorce 2026? Ten dokument to sprawdza u źródła i **rewiduje** moją pierwszą rekomendację.

## 1. Co jest dziś (diagnoza techniczna)

Prawy panel to **nie jeden panel w dwóch stanach — to dwie osobne karty, które się nawzajem chowają**:

- **Dane produktu** (`.buy`) — karta `flex:1`, rozciąga się na całą wysokość → wysoka.
- **Czat** (`.chat`) — osobna karta ze sztywną wysokością `clamp(430px, 100vh−128px, 720px)` → niższa.
- Skok wysokości = dwa różne mechanizmy wysokości, nie przypadek.

Każda karta ma **własny nagłówek** (produkt: autor „N. Dubois"; czat: „Latenca · picking for one wall") → mózg czyta je jako dwie różne rzeczy.

Dwa **niepasujące przełączniki**:

| kierunek | co widać | pozycja | kolor |
|---|---|---|---|
| produkt → czat | „Not sure about the size… Continue" | góra | fioletowy (accent) |
| czat → produkt | „Poster · 50×70 · $59" | dół | szary (neutral) |

Dolny szary pasek nie wygląda jak przycisk „wróć do produktu" — wygląda jak status. To źródło „nieintuicyjności".

**Sedno:** obecny wzorzec to **twardy mode-switch** — albo kupujesz, albo rozmawiasz, jedno chowa drugie, a przełączniki są zamaskowane i niesymetryczne.

## 2. Co robią liderzy 2026 (u źródła)

**Amazon Rufus / Alexa for Shopping** (lider kategorii, [aboutamazon](https://www.aboutamazon.com/news/retail/how-to-use-amazon-rufus)):
- Asystent żyje **na stronie produktu**; pole zakupu **zostaje widoczne**. Otwierasz go z jednego, stałego punktu (ikona), rozmawiasz w nakładce, zamykasz — wracasz do produktu. **Nie przełączasz się w tryb, który chowa buy box.**

**Trend PDP 2026** ([insiderone](https://insiderone.com/ai-shopping-assistants/), [algolia](https://www.algolia.com/blog/ecommerce/ai-shopping-assistants)):
- „AI PDP Assistant sits on the product page itself, answering objections at the exact moment a shopper hesitates. **Most competitors park their assistant in a corner widget**" — czyli chowanie/marginalizacja asystenta jest traktowana jako gorszy wzorzec.

**Nielsen Norman Group — 10 wytycznych dla asystentów AI** ([nngroup](https://www.nngroup.com/articles/ai-chatbots-design-guidelines/)):
- **G1 — jeden punkt wejścia.** „Any existing chat options should be consolidated into a single entry point." → nasze **dwa** niepasujące paski łamią to wprost.
- **G2 — stały dostęp.** Asystent ma być widoczny/dostępny, nie znikać. → argument przeciw trybowi, który całkiem chowa doradcę.
- **G3 — pokaż możliwości** przez opening zależny od produktu (Rufus zmienia podpowiedzi pod konkretny produkt). → **już to robimy** (otwarcie nazywa dzieło).
- **G4 — podpowiedzi jako przyciski, nie tekst.** → **już to robimy** (quick-replies „Something warmer / Bolder / Darker").
- **G6 — progresywne ujawnianie**, nie wypychaj treści z widoku.
- **G8 — pozwól powiększyć okno czatu** (gdy treść potrzebuje miejsca).

## 3. Werdykt: to rewiduje moją pierwszą propozycję

Oba warianty, które najpierw dałem — **zakładki `[Kup | Zapytaj]`** i **companion** — to nadal **mode-switch, który chowa buy box**. Liderzy tego unikają (Rufus trzyma zakup, NN/g G1/G2 chcą jednego stałego wejścia). Więc żaden z nich nie jest „best of best".

**Zastrzeżenie specyficzne dla Latenki (ważne):** nasz doradca to **nie** Rufus-owe Q&A na marginesie. To „drzwi frontowe" (D-022) i on **podmienia grafikę na ścianie** — napędza sam wybór. Więc „corner widget" też jest zły w drugą stronę: doradca musi być **wyeksponowany i mieć realne miejsce** (G8), a nie mała ikonka w rogu.

## 4. Rekomendacja — wariant C (ugruntowany)

**„Stały panel produktu + doradca jako otwierana warstwa z jednego punktu wejścia."**

- **Jedna karta, jedna stała wysokość** (na całą wysokość viewportu) → koniec skoku wysokości.
- **Góra karty zawsze ta sama** w obu stanach: tożsamość produktu + **żywa cena** + skrót konfiguracji („Poster · 50×70 · $59"). To jest stały kontekst, który Rufus trzyma na widoku.
- **Domyślnie: konfigurator + „Add to cart"** (jak teraz), w tej stałej karcie.
- **Doradca = wyeksponowany, stały punkt wejścia** przy dole karty (pole w stylu inputu: „Zapytaj Latenca — nie masz pewności co do rozmiaru albo czy pasuje?") + podpowiedzi-przyciski (G3/G4 — już mamy).
- **Klik rozwija rozmowę jako warstwę** nad konfiguratorem (jak drawer Rufusa / bottom-sheet na mobile), a góra (tożsamość + cena) i dostęp do zakupu **zostają przypięte**. Jeden jasny „×/zwiń" chowa warstwę z powrotem — **ten sam element w obie strony**, nie dwa niepasujące paski.

**Dlaczego to zabija wszystkie 3 problemy naraz:**
1. Jedna stała karta → ta sama wysokość zawsze.
2. Otwórz asystenta / zamknij — gest znany z każdej aplikacji AI → od razu zrozumiałe.
3. Jeden symetryczny marker (jedno wejście do doradcy, NN/g G1), zamiast fioletowy-góra vs szary-dół.

**Co zostawiamy (bo już jest zgodne z 2026):** opening nazywający dzieło (G3), quick-replies jako przyciski (G4), cena niesiona do rozmowy. **Co naprawiamy:** dwa paski → jedno wejście; jedna wysokość; jeden nagłówek.

## 5. Rozstrzygnięcie (2026-07-21) — po dopytaniu Artura

Artur doprecyzował: to nie ma być doradca „przywoływany" (Rufus/otwierana warstwa = wzorzec dla *dodatkowego* asystenta), tylko **panel pierwszoplanowy widoczny przez większość czasu** — jak trwały panel w **Figmie / Ideogramie / Fy!**. Te trzy trzymają dużą powierzchnię wizualną po jednej stronie i **trwały panel** po drugiej (poukładany w sekcje, progresywne ujawnianie) — nigdy przełącznik chowający jedną powierzchnię.

**Zbudowany model D (D-046):** lewa = ściana z grafiką (canvas). Prawa = jeden trwały panel: (1) przypięty nagłówek produktu (tytuł/autor/cena/skrót), (2) **doradca = główna powierzchnia** (widoczny przez większość czasu), (3) dok „Options + Add to cart" na dole; pełna konfiguracja = **arkusz wysuwany nad rozmową**, zamykany szewronem. Proporcje: doradca dominuje, konfiguracja kompaktowa w doku, rozwijana na żądanie (Artur wybrał to wyważenie, nie „jeszcze bardziej dominujący" ani „konfiguracja pół na pół"). Zamrożone `04-advisor` v14.

Dodatkowe źródła tej rundy:
- Figma — prawy sidebar (trwały, zakładki + rozwijane sekcje): https://help.figma.com/hc/en-us/articles/360039832014-Design-prototype-and-explore-layer-properties-in-the-right-sidebar
- Fy! (iamfy) — podgląd na ścianie + trwałe sterowanie: https://www.iamfy.co/products/my-cozy-room

## Źródła
- Amazon — How to use Rufus: https://www.aboutamazon.com/news/retail/how-to-use-amazon-rufus
- Amazon — Rufus smarter/personalized: https://www.aboutamazon.com/news/retail/amazon-rufus-ai-assistant-personalized-shopping-features
- InsiderOne — Top AI Shopping Assistants 2026: https://insiderone.com/ai-shopping-assistants/
- Algolia — AI shopping assistants guide: https://www.algolia.com/blog/ecommerce/ai-shopping-assistants
- NN/g — 10 Guidelines for Designing AI Chatbots: https://www.nngroup.com/articles/ai-chatbots-design-guidelines/
- NN/g — conversational interfaces hub: https://www.nngroup.com/topic/conversational-interfaces/

*Uwaga o wiarygodności: mechanika Rufusa opisana z materiałów Amazona + analiz 2026 (nie z bezpośredniego demo); wytyczne NN/g cytowane z ich artykułu. Zasada „buy box zostaje + jedno stałe wejście do asystenta" jest spójna we wszystkich źródłach — to jest twardy grunt. Dokładny piksel-layout (drawer vs bottom-sheet) to już nasza decyzja projektowa, nie cytat.*
