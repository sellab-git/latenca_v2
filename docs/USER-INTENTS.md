# USER-INTENTS — z czym ludzie przychodzą i co się u nas dzieje

> Cel (Artur, 2026-07-21): zanim zbudujemy więcej, **rozwiązać ścieżki/intencje**, z jakimi ludzie przychodzą — żeby nie iść w coś bez sensu.
> To jest **mapa do reakcji**, nie zbiór nowych decyzji. Oparta na inwentaryzacji tego, co już mamy w repo (nie wymyślam od zera). Do pressure-testu z Arturem i ChatGPT.
> Status obecnej budowy (punkt odniesienia): landing = katalog; strona produktu ma wbudowanego doradcę (model D, D-046) działającego **na jednej grafice naraz**; MVP = pojedyncza grafika (D-023); wielo-grafikowe ściany = zapisana luka (D-033 pkt 6).

---

## 1. Kanon intencji (Twoje 5 + to, co już nazwaliśmy wcześniej)

| # | Intencja (po co przychodzi) | Kto / stan | Które drzwi | Co się dzieje u nas DZIŚ | Status | Źródło |
|---|---|---|---|---|---|---|
| **1** | „Mam pustą ścianę, nie wiem co" | Nowy dom/mieszkanie, zero sztuki | Design my wall / Start designing | Doradca proponuje **jedną** grafikę na płaskiej ścianie + „dlaczego"; konfigurujesz i do koszyka | ✅ obsłużone (1 szt.) — brak opcji zestawu | D-023 typ (a); mockup `firstDesign('empty wall')` |
| **2** | „Mam już grafikę, chcę dobrać nową" | Ma 1+ prac, uzupełnia ścianę | Design my wall | Doradca rekomenduje **jedną** komplementarną; istniejąca sztuka używana tylko „by nie gryzło" (D-031) | 🟡 częściowo — nie komponuje **zestawu wokół** tego, co masz | D-023 typ (b); Fy persona C |
| **3** | „Chcę po prostu kupić jedną grafikę" | Zdecydowany | Explore / szukajka / prosto na produkt | Katalog → produkt (stan kupna) → koszyk; doradca niepotrzebny | ✅ pełne | D-022, D-038(a/c), D-034 |
| **4** | „Mam konkretne wymiary kilku grafik" | Wie, ile miejsca / ile prac | — (brak drzwi) | **Nic** — scena trzyma jedną ramę; wymiary istnieją jako pole, ale flow rozmiaruje jedną pracę | ⛔ **nieobsłużone** — to jest ta luka | D-034/539, D-033 pkt 6 |
| **5** | „Lubię coś konkretnego, chcę podobne" | Ma punkt odniesienia | Doradca (rozmowa) | „coś cieplejszego / pokaż inne / inne" podmienia pracę **w miejscu**; można wgrać lubiany obraz jako sygnał gustu | ✅ przez rozmowę — brak „więcej jak **ta konkretna**" (reverse-image) | D-034, D-031 |

### Dodatkowe intencje, które wypłynęły w dokumentach (Ty decydujesz: w grze / poza)
| # | Intencja | Stan w repo |
|---|---|---|
| 6 | **Inspiracja** („pokaż prawdziwe wnętrza") | Były „trzecie drzwi", ale **wycięte** w obecnej ścieżce (D-038) |
| 7 | **Prezent** | Tylko jako pole kontekstu; **brak flow** prezentowego |
| 8 | **Cała ściana / wiele ścian / pokój** | **Odłożone do v2** (D-023, LOCKS) |
| 9 | **Projektant wnętrz / B2B** (Airbnb, hotel, biuro — kupuje wiele, wraca) | Nazwane w USER_RESEARCH, ale **brak flow** i kłóci się z „jedna sesja, bez profilu" (D-024) |
| 10 | **Budżet** („ściany do $X") | **Nigdzie** nie wspomniane jako intencja |

---

## 2. SEDNO: prawie wszystko schodzi się do jednej nierozwiązanej rzeczy — ZESTAWY

Intencje **2 i 4** (i persona „kompletujący galerię", i cała ekonomia) wskazują na to samo: **wielo-grafikowy zestaw / gallery wall.** A to jest jednocześnie:

- **Rdzeń wizji:** „rdzeniem nie jest pojedyncze dzieło, tylko dobra ściana / zestaw" (VISION, PRODUCT_BIBLE).
- **Ekonomia:** kolejna sztuka w tej samej paczce ~€0,29 → „zestawy to cały biznes"; pojedyncza sprzedaż nie pokrywa CAC (PRODUCT_BIBLE, PROJECT_STATUS).
- **Zapisana luka:** „the one genuine structural gap" (D-033 pkt 6); „sets are the only economics that work".
- **Potrzeba realnych intencji:** #2 i #4 bez tego są nieobsłużone lub połowiczne.

**To jest JEDNA decyzja, która odblokowuje najwięcej.** Reszta (prezent, B2B, budżet, inspiracja) jest wtórna.

**Pytanie do rozstrzygnięcia (Ty + ChatGPT):** czy i JAK wprowadzamy zestawy — przy twardej zasadzie D-033 „**AI układa, Ty oglądasz**" (nie budujemy edytora, w którym user przeciąga prace). Robocza hipoteza do rozbicia: *zestaw = kuratorowana, zaproponowana przez AI aranżacja jako **jeden produkt** (para / tryptyk / gallery wall 3–5), pokazana jako gotowa na ścianie; akceptujesz albo wymieniasz elementy — nigdy nie układasz sam.* Do potwierdzenia lub odrzucenia.

---

## 3. Co jest już zablokowane (żeby nie wracać)

- Jeden flow doradcy; typ projektu = parametr; MVP = 2 typy (pusta ściana; dodaj/wymień); pokój → v2 — **D-023**.
- Sklep to podłoga, doradca drzwiami, **nigdy bramką**; kup-od-ręki zawsze dostępne — **D-022**.
- 3 ekrany MVP: katalog-landing + produkt-z-doradcą + koszyk; „Get inspired" wycięte — **D-038**.
- Doradca + produkt = jeden ekran; wejście wybiera stan startowy — **D-034 → D-046**.
- Wgrania (zdjęcie ściany / lubiana sztuka / inspiracja) = wejście analityczne, opcjonalne, **nigdy canvas** — **D-021, D-031**.
- Bez widocznego % pewności (jakościowa gotowość) — **D-026**. Jedna sesja, bez profilu per-klient — **D-024**. Tylko druk, bez plików cyfrowych — **D-036**.

---

## 4. Dokumenty do wycofania/przepisania (wprowadzają w błąd)

Te opisują świat **sprzed** pivotu na model D i dziś mylą:
- **`SCREEN_MAP.md`** — najbardziej nieaktualny: krok „Upload Wall", ekran „AI Analysis 68%", osobny ekran „Style Profile: Japandi", osobna 8-krokowa podróż 2A→2H, „Set of N / Your Project", „Get Inspired", confidence %. Prawie wszystko z tego jest sprzeczne z D-021/D-026/D-031/D-034/D-038.
- **`PRODUCT-BLUEPRINT-single-session.md`** — „foto → AI maluje ścianę na TWOIM zdjęciu" + zestawy jako pierwszy ruch; sprzeczne z D-021/D-031/D-033 (płaska ściana, nigdy kompozyt na zdjęciu klienta). Sam nagłówek przyznaje, że wymaga przepisania.

Rekomendacja: po ustaleniu mapy — **przepisać SCREEN_MAP do obecnej rzeczywistości** i oznaczyć blueprint jako historyczny.

---

## 5. Otwarte pytania do Ciebie (nie odpowiadaj na formularz — do rozmowy)

1. **Zestawy — sedno:** wchodzimy w wielo-grafikowe zestawy teraz (jako „AI proponuje aranżację-produkt"), czy MVP zostaje przy jednej grafice i świadomie odkładamy #2/#4 + ekonomię zestawów?
2. **Intencja #4** („dokładne wymiary kilku prac") — nasz target czy edge? (dziś zupełnie nieobsłużona)
3. **Prezent (#7), Budżet (#10), Inspiracja (#6)** — któreś w grze na MVP, czy wszystkie później?
4. **B2B/projektanci (#9)** — świadomie ignorujemy na teraz (kłóci się z „jedną sesją")?
5. „Mam już grafikę i chcę dobrać" (#2) — zakładamy, że user **wgra jej zdjęcie/opis**, czy tylko powie słowami?

---

*Następny krok po Twojej reakcji: dla wybranych intencji rozpisać „od drzwi do sprzedaży" na konkretne ekrany (na model D + shell/app.css), oznaczyć MVP vs później, i przepisać SCREEN_MAP. ChatGPT = senior reviewer tego dokumentu (czyta repo); przygotuję mu brief.*
