# REVIEW round 3 — konwergencja + gotowe projekty wpisów decyzyjnych

> **Co to jest:** zamknięcie rundy recenzji. Zawiera: wycofanie jednego błędnego zarzutu Claude'a, przyjęcie korekt ChatGPT (w tym trzech korekt brzmienia przed lockiem), oraz **gotowe brzmienia wpisów D-022 … D-029** do wklejenia w [`DECISIONS.md`](DECISIONS.md).
> **Status:** ⚠️ **NIC TU NIE JEST JESZCZE DECYZJĄ.** Zgodnie z D-019 hipoteza nie staje się decyzją po cichu — wpisy poniżej czekają na jedno „tak" Artura.
> Poprzednie rundy: [`REVIEW-designer-layer.md`](REVIEW-designer-layer.md) → [`REVIEW-designer-layer-round2.md`](REVIEW-designer-layer-round2.md).
> Data: 2026-07-19.

---

## A. Wycofuję zarzut o sprzeczności z D-010

W rundzie 2 (§F1) zgłosiłem, że równoległy test dystrybucji jest sprzeczny z zablokowanym D-010. **Sprawdziłem dokładne brzmienie decyzji — myliłem się.**

D-010 „Implications" brzmi dosłownie:

> *„Discovery/traffic must be addressed early in the build (Pinterest anchor, content-as-factory), not deferred."*

Czyli D-010 **wymaga** zajęcia się ruchem wcześnie, w trakcie budowy. Ręczny test redakcyjny nie zastępuje budowy, nie blokuje jej i nie jest bramką „go/no-go" — więc **jest wykonaniem D-010, nie wyjątkiem od niego.**

**Konsekwencja: nie potrzeba żadnego supersede ani odblokowania D-010.** Zarzut wycofany; podziękowanie dla recenzenta za przeczytanie źródła zamiast mojego streszczenia.

---

## B. Przyjęte korekty ChatGPT

### B1. Fosa — to mechanizm docelowy, nie opis stanu obecnego ✅

Przyjmuję. Zapis „fosą Latenca jest…" byłby fałszywym twierdzeniem o przewadze. Poprawne ujęcie: **Latenca nie ma jeszcze fosy — ma projekt mechanizmu, który może ją zbudować.**

| Czynnik | Stan dziś |
|---|---|
| Curated Catalog | częściowo istnieje |
| Designer System | hipoteza / projekt |
| Outcome Data | praktycznie 0 |
| Distribution | praktycznie 0 |

### B2. Pinterest = pierwszy kanał **do testu**, nie zatwierdzony kanał docelowy ✅

Przyjmuję — spójne z moim własnym zastrzeżeniem 🔴 z rundy 2. Lock obejmuje *dystrybucję jako część produktu*, nie *Pinterest jako długoterminowy kanał główny*.

### B3. Metryki — rozdzielić wynik projektowy od komercyjnego ✅

**To najmocniejsza korekta w tej rundzie i przyjmuję ją w całości.** Moje „zakup = główny sygnał" było niechlujne.

Zakup zależy od ceny, dostawy, terminu, zaufania do marki, jakości PDP, checkoutu, dostępności i sytuacji finansowej klienta. **Dobra rekomendacja może nie zostać kupiona; słaba może zostać kupiona z innych powodów.** Mierzenie jakości doradcy zakupem oznaczałoby uczenie systemu na zaszumionym sygnale — czyli dokładnie ten błąd, przed którym sami ostrzegaliśmy.

- **Wynik projektowy** (jakość doradcy): akceptacja w sesji · akceptacja po iteracji · wymiana elementów · odrzucenie kierunku.
- **Wynik komercyjny** (biznes): dodanie do koszyka · zakup · wartość koszyka · zwrot.

### B4. Zakres dokumentów — dokładam `PROJECT_STATUS.md` ✅

Słuszna uwaga: `PROJECT_STATUS.md` ma odzwierciedlać **aktywną pracę**, więc gdy test dystrybucji faktycznie ruszy, trafia tam (liczba materiałów, kanał, status, co mierzymy). `ROADMAP.md` — tylko jeśli test zmieni kolejność prac. `PRODUCT_ARCHITECTURE.md` / `AI_SYSTEM.md` — dopiero przy implementacji.

### B5. Trzy korekty brzmienia przed lockiem ✅

Finalny przebieg recenzji wyłapał trzy sformułowania, które były **szersze niż faktyczna decyzja**. Wszystkie przyjęte i naniesione w sekcji C:

| Wpis | Było (za szerokie) | Jest (precyzyjne) | Dlaczego to ważne |
|---|---|---|---|
| **D-022** | „Wszystkie ścieżki muszą kończyć się sprzedażą u nas — nie prowadzimy konsultacji bez zakupu" | Rekomendacje opierają się na katalogu i prowadzą do kupowalnej kompozycji; nie budujemy osobnej usługi konsultacyjnej; **user może zakończyć sesję bez zakupu** | Poprzednie brzmienie dawało się czytać jako „doradca ma wymuszać sprzedaż" — **kolidowało z zablokowanym D-002 (Trust before sales) i D-004 (AI zachowuje się jak projektant, nie sprzedawca)** |
| **D-024** | „Latenca nie pamięta Ciebie" | „Latenca nie buduje między sesjami **profilu gustu** pojedynczego klienta" | Produkt musi pamiętać zamówienia, zgody i dane operacyjne. Hasło jako obietnica prywatności stworzyłoby przyszłą sprzeczność |
| **D-027** | „landing pages per problem (**nie** per styl, **nie** per zestaw)" | Per problem w pierwszym teście i MVP; per styl / per zestaw dopuszczalne później jako warstwa merchandisingowa | Chroni priorytet „problem first", nie zamykając przyszłej architektury commerce (SEO, browse) |

Poprawiona też numeracja w nagłówku dokumentu (było D-022…D-028, jest D-022…D-029).

---

## C. Gotowe projekty wpisów do `DECISIONS.md`

> Do wklejenia **po** zatwierdzeniu przez Artura. Numeracja kontynuuje od D-021.

### D-022 — Kształt produktu: sklep jest podłogą, projektant jest drzwiami frontowymi
**Status:** proponowany
**Decyzja:** Latenca to kurowany sklep z jednym momentem AI. **Sklep = podłoga** (katalog, strona produktu, konfigurator, koszyk) — istnieje zawsze i każda ścieżka w nim ląduje. **Projektant = drzwi frontowe i twarz marki** — bohater strony głównej i główny wyróżnik. **Zasada rozstrzygająca: projektant nigdy nie jest bramką** — zawsze da się go ominąć i kupić bezpośrednio. W nawigacji to jeden produkt, nie dwa równorzędne: ścieżka szybka (*Browse and buy*) i prowadzona (*Design my wall*) kończą się tym samym katalogiem, PDP i checkoutem.
**Powód:** obietnicą marki jest pewność decyzji, ale większość kupujących sztukę na ścianę nie prowadzi „projektu" — zamiana zakupu w obowiązkową konsultację zabiłaby konwersję. Weryfikacja Modsy (~250 projektantów-ludzi, całe pokoje, model nieskalowalny) pokazuje, że groźny jest *koszt ludzki na projekt*, a nie sama warstwa doradcza.
**Implikacje:** reframuje D-001 i D-012 (domyka otwarte pytanie o framing produktu). Wszystkie rekomendacje projektanta opierają się na produktach dostępnych w katalogu Latenca i prowadzą do **kupowalnej kompozycji**; nie budujemy osobnej — płatnej ani bezpłatnej — usługi konsultacyjnej niezwiązanej z ofertą sklepu. **Użytkownik może zakończyć sesję bez zakupu.** Home musi jasno komunikować „możesz kupić bezpośrednio, ale Latenca najlepiej pomaga wybrać" — nie dwa konkurujące CTA o równej wadze.

### D-023 — Jeden Designer Flow; typ projektu jako parametr
**Status:** proponowany
**Decyzja:** Nie budujemy osobnych ścieżek per sytuacja użytkownika. Jeden flow o wspólnym szkielecie (ustal cel → zbierz minimalne dane → hipoteza → propozycja → feedback → dopracowanie → produkt i zakup), w którym **typ projektu jest parametrem** wybieranym jednym tapnięciem na starcie. **MVP = dwa typy: (a) pusta ściana, (b) dołóż / wymień.** Materiał wejściowy (zdjęcie, wymiary, inspiracja) i kontekst (przeprowadzka, remont) to **pola stanu projektu**, nie osobne ścieżki. Dane i reasoning różnią się zależnie od typu; silnik jest jeden.
**Powód:** osiem „punktów wejścia" mieszało trzy różne warstwy; tylko typ projektu rozgałęzia logikę. Budowa wielu ścieżek to pułapka zespołu z budżetem. Pytamy o typ zamiast zgadywać, bo błąd rozpoznania w kroku 1 zatruwa całą sesję.
**Implikacje:** „cały pokój" → v2 (wymaga spójności między ścianami i zbliża produkt do pełnej usługi interior design). Wejścia niekończące się zakupem u nas („powieś mi kupiony gdzie indziej", „dobierz tylko rozmiar") wypadają z MVP.

### D-024 — Uczenie na poziomie puli, nie pojedynczego klienta
**Status:** proponowany
**Decyzja:** W MVP **nie budujemy między sesjami pamięci preferencji ani profilu estetycznego pojedynczego klienta.** System uczy się z **całej puli projektów**, żeby kolejnym doradzać lepiej. Pamięcią doradczą produktu jest **baza wiedzy (KB)**, nie profil użytkownika: *„Latenca nie buduje między sesjami profilu gustu pojedynczego klienta — system zachowuje zagregowaną wiedzę o tym, co działa."* Stan projektu obowiązuje **w obrębie sesji**. *(Uwaga: to nie blokuje danych operacyjnych — zamówień, zgód, ani ewentualnego zapisywania projektów w późniejszym etapie.)* KB budujemy od razu w warstwach **A (zasady) / B (heurystyki) / D (wzorce)**; warstwy **E (case studies) i F (skuteczność)** wymagają wolumenu. **Od dnia 1 logujemy decyzje; automatycznej pętli uczenia nie budujemy**, dopóki nie ma wolumenu.
**Powód:** zgodne z zablokowanym single-session, bez ryzyka prywatności, a efekt uczenia zostaje. Pętla ucząca się na kilkudziesięciu projektach uczy się szumu i utrwala przypadki.
**Implikacje:** KB jest **warunkiem jakości od dnia 1** i źródłem uzasadnień — uzasadnienie oparte na regule KB jest wiarygodne, wymyślone przez LLM w locie jest konfabulacją. Człowiek pracuje **nad systemem** (KB, katalog, audyty na próbkach), nigdy **nad pojedynczym projektem** — moment, w którym koszt ludzki rośnie z każdą sesją, to powtórzenie błędu Modsy.

### D-025 — Fosa jest mechanizmem docelowym, nie stanem obecnym
**Status:** proponowany
**Decyzja:** Docelowy mechanizm budowania przewagi: **Curated Catalog × Designer System × Outcome Data × Distribution**. Zapis multiplikatywny jest celowy — brak jednego czynnika zeruje całość. **Latenca nie posiada dziś fosy**: Outcome Data i Distribution wynoszą praktycznie 0, Designer System jest projektem, katalog istnieje częściowo.
**Powód:** reguły projektowe (145 cm, 60–80% szerokości mebla) są wiedzą publiczną — sama KB nie jest przewagą. Unikalne staje się dopiero mapowanie reguł na **nasz** katalog, formaty i realne wyniki. Zapis „fosą Latenca jest…" byłby fałszywym twierdzeniem o przewadze.
**Implikacje:** dystrybucja jest **nierozwiązanym problemem, nie aktywem** — i pozostaje ryzykiem nr 1. Bez ruchu nie ma projektów, bez projektów nie ma danych, bez danych KB nigdy się nie specjalizuje.

### D-026 — Bez widocznego procentu pewności
**Status:** proponowany
**Decyzja:** W MVP **nie pokazujemy użytkownikowi procentowego „confidence score"**. Wewnętrznie liczymy `readiness` z kompletności danych (geometria ściany, kontekst kotwiczący, cel projektu, sygnał estetyczny) **oraz z pokrycia rekomendacji w katalogu i regułach KB** — nie sam licznik wypełnionych pól. Użytkownik widzi **stan jakościowy i brakującą informację**, np. *„Brakuje mi tylko szerokości ściany, żeby dobrać rozmiar."*
**Powód:** procent sugeruje precyzję statystyczną, której system nie ma — czyli jest „udawanym AI", którego zakazaliśmy. Wersja jakościowa jest jednocześnie uczciwa i użyteczna (mówi, co zrobić dalej).
**Implikacje:** `prototypes/mockups/02-design-journey.html` ma dziś licznik 72% → 95% — **wymaga przebudowy** na stany gotowości.

### D-027 — Dystrybucja jest częścią produktu
**Status:** proponowany
**Decyzja:** Dystrybucja przestaje być „marketingiem na później" i staje się warstwą produktu. Pętla: *katalog + KB → projekt / scenariusz redakcyjny → gotowa ściana + uzasadnienie → kanał → landing konkretnego problemu → sesja doradcy → zakup → log wyników*. Zasady: **w pierwszym teście dystrybucji i w MVP główne landing pages tworzymy per problem projektowy** — bo tak wygląda realne wyszukiwanie („sztuka nad beżową sofą"). Strony per styl i per zestaw pozostają dopuszczalne jako **późniejsza warstwa merchandisingowa**, ale nie są podstawą pierwszego testu. Dalej: **zakaz automatycznej publikacji danych i zdjęć klientów** (materiał = scenariusze redakcyjne i neutralne mockupy; realizacje klientów wyłącznie za dobrowolną zgodą); **Pinterest = pierwszy kanał do TESTU**, nie zatwierdzony kanał docelowy.
**Powód:** to najsłabszy czynnik w D-025 i ryzyko nr 1. Treść prowadząca na ogólny home daje ruch, a nie konwersję.
**Implikacje:** metadane pod wyszukiwanie pracują jednocześnie na SEO i na kanał. Zasięg organiczny Pinteresta nie jest darmowy — kanał pozostaje 🔴 hipotezą.

### D-028 — Ręczny test dystrybucji równolegle z Krokiem 1 (wykonanie D-010)
**Status:** proponowany
**Decyzja:** Równolegle z budową Kroku 1 uruchamiamy **ręczny, redakcyjny test dystrybucji: 20–30 materiałów, zero automatyzacji.** Test odpowiada na trzy pytania: czy problemowe treści ścienne zdobywają uwagę · które problemy generują zapis/klik/wejście · czy użytkownik przechodzi od inspiracji do intencji rozwiązania ściany. **Nie próbuje dowodzić CAC ani konwersji zakupowej** — bez gotowego produktu nie jest to uczciwie mierzalne. Generator content-packów powstaje dopiero, jeśli kanał zadziała.
**Powód:** **to jest wykonanie D-010, nie wyjątek od niego** — D-010 wymaga wprost, by discovery/traffic były adresowane wcześnie w trakcie budowy („Pinterest anchor, content-as-factory, not deferred"). Test nie zastępuje budowy, nie blokuje jej i nie jest bramką go/no-go.
**Implikacje:** D-010 **nie wymaga** supersede ani odblokowania. Gdy test ruszy, trafia do `PROJECT_STATUS.md` (liczba materiałów, kanał, status, co mierzymy). Automatyzacja kanału, który jeszcze nie działa, byłaby czystą stratą.

### D-029 — Metryki: wynik projektowy oddzielony od komercyjnego
**Status:** proponowany
**Decyzja:** Rozdzielamy dwie warstwy pomiaru. **Wynik projektowy** (jakość doradcy): akceptacja w sesji · akceptacja po iteracji · wymiana elementów · odrzucenie kierunku. **Wynik komercyjny** (biznes): dodanie do koszyka · zakup · wartość koszyka · zwrot. **Główny sygnał biznesowy = zakup. Główny obserwowalny sygnał dopasowania rekomendacji = akceptacja w sesji.** Zwrot to sygnał negatywny, ale nie dowód błędu projektowego. **„Brak późniejszej zmiany" odrzucony jako niemierzalny.** Automatyczne uczenie na tych danych pozostaje odłożone do osiągnięcia wolumenu.
**Powód:** zakup zależy od ceny, dostawy, terminu, zaufania, PDP, checkoutu i sytuacji klienta. Dobra rekomendacja może nie zostać kupiona, słaba może zostać kupiona z innych powodów — mierzenie jakości doradcy zakupem uczyłoby system na zaszumionym sygnale.

---

## D. Co się dzieje po „tak" Artura

1. Wpisy **D-022 … D-029** trafiają do [`DECISIONS.md`](DECISIONS.md); [`LOCKS.md`](LOCKS.md) dostaje odpowiednie statusy.
2. [`VISION.md`](VISION.md) — aktualizacja formuły fosy (jako mechanizmu docelowego) + dystrybucja jako warstwa produktu.
3. [`prototypes/mockups/02-design-journey.html`](../prototypes/mockups/02-design-journey.html) — licznik 72% → 95% zamieniony na stany gotowości.
4. [`PROJECT_STATUS.md`](PROJECT_STATUS.md) — dopiero gdy test dystrybucji faktycznie ruszy.
5. `ROADMAP.md` — tylko jeśli test zmieni kolejność prac. `PRODUCT_ARCHITECTURE.md` / `AI_SYSTEM.md` — przy implementacji.
