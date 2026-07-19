# Latenca — zakwestionowanie modelu produktu

> Nie „v2 flow". To dokument decyzyjny: co w obecnym modelu jest błędne u fundamentów, i 5 zupełnie różnych modeli doświadczenia. Ekrany projektujemy dopiero po wyborze modelu.

---

## Punkt wyjścia: czego naprawdę nauczyły nas Figma / Cursor / Perplexity / Midjourney

Żaden z nich nie wygrał „lepszym onboardingiem". Wszystkie zrobiły ten sam ruch:

1. **Pokazały wynik NAJPIERW** (odpowiedź, kod, obraz, projekt), zanim użytkownik cokolwiek wyspecyfikował.
2. **Zastąpiły specyfikację reakcją** — użytkownik nie *opisuje* czego chce, tylko *reaguje* na konkretny artefakt (akceptuj/odrzuć, wariant, remix).
3. **Intencja jest ODKRYWANA w pętli**, nie wydobywana formularzem z góry.
4. **AI ma sprawczość** — proponuje, a nie tylko wykonuje.

Nasz obecny AI Design Journey robi dokładnie odwrotnie: 8 kroków pytań → dopiero potem efekt. To jest bardzo dobry formularz. I dlatego „mógłby go zbudować dowolny startup AI".

**Rdzeń przeprojektowania w jednym zdaniu:** Latenca ma przestać być systemem, który **PYTA** czego chcesz, a stać się systemem, który **POKAZUJE** sztukę na Twojej ścianie i uczy się z tego, po co **sięgasz**. Gust się rozpoznaje, nie opisuje.

---

## Część 1 — Błędne założenia obecnego flow

**O wiedzy i pytaniach**
1. **„Musimy zapytać, żeby zrozumieć."** Większość pytań jest zbędna — jedno zdjęcie ściany zawiera styl, paletę, światło, meble, rozmiar i to, co już wisi. Pytanie o rzeczy, które AI może *zobaczyć*, jest sygnałem, że AI wcale nie jest mądre.
2. **„Użytkownik musi opisać swój gust, zanim cokolwiek zobaczy."** Ludzie nie potrafią nazwać swojego stylu, ale rozpoznają go w ułamku sekundy. Input przed outputem to główna pułapka „formularza".
3. **„Styl trzeba nazwać (Japandi)."** Etykieta to proxy, które bywa błędne i alienujące („to nie ja"). Zmuszamy użytkownika do naszej taksonomii. Styl powinien być *pokazany i strojony wizualnie*, nigdy nazwany.
4. **„Match 94%" — istnieje jedna poprawna odpowiedź.** Gust to przestrzeń preferencji, nie problem klasyfikacji z jedną prawdą. Procent bywa protekcjonalny i sugeruje fałszywą pewność.

**O kolejności i czasie**
5. **„Efekt (sztuka na ścianie) na kroku 6."** Moment „wow" jest odroczony o ~2 minuty. Powinien być w 5. sekundzie. Wow najpierw, dostrajanie potem.
6. **„Flow jest liniowe (1→8)."** Prawdziwe projektowanie jest nieliniowe — skaczesz między „co", „gdzie" i „jak duże". Wizard walczy z tym, jak faktycznie kształtuje się gust.
7. **„Zdjęcie ściany to opcjonalny krok."** Jeśli zdjęcie odblokowuje wszystko (inferencja + podgląd), to nie jest krokiem — jest **drzwiami wejściowymi**, które od razu dają magię.

**O rekomendacji i modelu decyzji**
8. **„Jedna najlepsza rekomendacja = cel" („curated, not crowded")."** Jedna odpowiedź to *werdykt*, który akceptujesz lub odrzucasz. Ale gust rozumiesz przez *kontrast*. Midjourney pokazuje 4, nie 1. „Jedna najlepsza" to znowu myślenie formularzowe (wydobądź dość, by policzyć jedyną słuszną).
9. **„Decyzje podejmuje się przez odpowiadanie."** Alternatywa: przez **manipulację/reakcję** (przeciągnij, podmień, „więcej takich", weto, przypnij). Bezpośrednia manipulacja bije odpowiadanie na pytania.
10. **„AI ma minimalizować błędy."** Model, który czasem pokazuje celowo *rozbieżną* opcję, uczy się Twoich granic szybciej (aktywne uczenie). Bezpieczny strzał uczy wolniej niż „oto dwa skrajne kierunki".
11. **„Rekomendacja pojawia się na końcu procesu poznania."** Powinno być odwrotnie: rekomendacja jest **pierwszym ruchem**, a proces to jej *korygowanie*.

**O roli AI i użytkownika**
12. **„AI to neutralny ekstraktor, który pyta i wykonuje."** Świetny projektant ma *zdanie* — proponuje, broni wyboru, czasem się nie zgadza („zaufaj mi"). Nasze AI jest służalcze. Produkt kategorii ma gust i sprawczość.
13. **„AI prowadzi, użytkownik podąża."** Być może odwrotnie: użytkownik *eksploruje i bawi się*, a AI kuratoruje w tle (jak Perplexity robi robotę, ale to ty prowadzisz pytania). Sprawczość buduje pewność.
14. **„Pewność to liczba, którą AI raportuje."** Pewność powinna być czymś, co użytkownik *czuje*, widząc rzecz na swojej ścianie — nie procentem, który AI ogłasza.

**O produkcie i jednostce wartości**
15. **„Wynikiem jest jeden produkt (oprawiony druk) na końcu."** Prawdziwe zadanie to „ściana, która czuje się dobrze" — czasem jeden obraz, czasem para, czasem galeria, ewoluująca w czasie. Jednostką jest **kompozycja ściany**, nie „plakat".
16. **„To sesja z końcem (zakup)."** Ściany się *żyje*; gust i pory roku się zmieniają. Może produkt to trwała, ucząca się relacja z Twoją przestrzenią, a nie jednorazowy lejek.
17. **„Doświadczenie jest jednoosobowe."** Decyzje o ścianie w domu są często wspólne (partner, rodzina). Model może być współdzielony/asynchroniczny (insight Figmy).
18. **„Wartością jest rekomendacja."** Może wartością jest samo **widzenie** — moc zobaczenia dowolnej sztuki na *Twojej* ścianie, w Twoim świetle, w prawdziwej skali. Jeśli to jest wystarczająco magiczne, użytkownik sam staje się pewnym siebie projektantem.
19. **„Musi być czuć, że to AI."** Najlepsze narzędzia czynią AI niewidzialnym — czujesz się genialnym projektantem, nie „użytkownikiem AI". (To już nasz insight z Home: niewidzialny kurator.)

---

## Część 2 — Pięć zupełnie różnych modeli

Każdy ma inny *rdzenny mechanizm*, nie kosmetykę. Nie wykluczają się — zwycięski produkt pewnie je łączy — ale warto je rozdzielić jako hipotezy.

### Model A — „Żywa ściana" (Twoja ściana jest płótnem, nie formularzem)
**Mechanizm.** Wchodzisz i od razu jesteś *w widoku swojej ściany* (zdjęcie albo pokój-szablon). AI robi pierwszy ruch — sztuka pojawia się na niej, w skali, w Twoim świetle. Dalej **nie ma pytań ani kroków**. Żyjesz w widoku ściany i *manipulujesz*: swipe = podmień pracę (talia kuratorowana, zbiega się), pinch = rozmiar, drag = pozycja, tap „więcej takich / nie to". AI uczy się z podmian i czasu patrzenia — nigdy nie pyta. Ściana to trwały dokument, do którego wracasz.
**Dlaczego to inna kategoria.** Od „odpowiedz na pytania, dostań rekomendację" do „graj na swojej realnej ścianie; AI kuratoruje talię, którą przeglądasz". (Midjourney selekcja + płótno Figmy, dla Twojej ściany.)
**Za 5 lat:** „Latenca sprawiła, że wybieranie sztuki przestało być zakupem, a stało się *aranżowaniem* — jak przesuwanie mebli, tylko na ekranie."
**Ryzyko.** Bez struktury część ludzi się gubi („zbyt otwarte"); potrzebna kuratorska talia, żeby swipe się zbiegał, a nie był nieskończony.

### Model B — „Dwie drogi" (rozbieżność → zbieżność; gust przez kontrast)
**Mechanizm.** AI nigdy nie pyta — *proponuje*. Otwiera dwie celowo różne, kompletne aranżacje na Twojej ścianie (np. „cicha i ciepła" vs „mocna i graficzna") — bez nazw stylów, po prostu pokazane. Wybierasz tę, która ciągnie (albo „coś pomiędzy", albo „żadna, idź dziwniej"). Każdy wybór rodzi dwoje rozbieżnych dzieci. W 3–4 rozwidleniach zbiegasz do ściany, którą kochasz — robiąc wyłącznie odruchowe „to albo to" na *swoim pokoju*. Kontrolowany błąd jest wbudowany: jedna z dwóch to zawsze strzał w bok, żeby szybko zmapować Twoje granice.
**Dlaczego to inna kategoria.** Gust wyłania się z drzewa turniejowego pełnych wizualizacji, nie z opisu atrybutów. Aktywne uczenie jako UX.
**Za 5 lat:** „Latenca nie pytała cię o gust. Pokazywała dwie ściany i patrzyła, po którą sięgasz — i po pięciu wyborach wiedziała lepiej niż ty."
**Ryzyko.** Zmęczenie wyborem, jeśli drzewo za głębokie; trzeba twardo zbiegać (3–4 forki max).

### Model C — „Partner ze zdaniem" (rówieśnik, nie wizard)
**Mechanizm.** AI z ekstraktora staje się **opiniotwórczym współprojektantem z gustem**. Robi śmiały pierwszy ruch i *broni go* („dałem duże i spokojne — masz w pokoju sporo dziejącego się, więc ściana ma oddychać"). Ty odpychasz naturalnie i reaktywnie („za bezpieczne", „cieplej", „mam zieloną kanapę, której nie widać"). Ono argumentuje, dostraja, czasem grzecznie się nie zgadza („odradzałbym mniejsze — oto dlaczego, ale Twoja decyzja"). Dialog propozycji i reakcji, nie Q→A. Produktem jest *relacja* — projektant, który cię rozumie i ma zdanie.
**Dlaczego to inna kategoria.** Od wydobywania do prawdziwej współpracy; AI ma sprawczość i gust. (Cursor „szkicuje, ty sterujesz, ma zdanie" — dla wnętrz.)
**Za 5 lat:** „Latenca dała każdemu projektanta wnętrz z charakterem — takiego, który się z tobą spiera, a nie tylko wykonuje."
**Ryzyko.** Najtrudniejsze do dobrego wykonania (jakość „zdania" AI); ryzyko irytacji, jeśli AI za bardzo się upiera.

### Model D — „Najpierw wow" (efekt przed inputem, magia potem korekta)
**Mechanizm.** Zero pytań na start. Dajesz JEDNO — zdjęcie ściany (albo wybierasz pokój podobny do swojego) — i **natychmiast** widzisz gotową, piękną, zaprojektowaną ścianę w swojej przestrzeni. Kropka. To jest cały pierwszy ekran: transformacja. Dopiero po „wow" pojawiają się korekty, i tylko jako reakcje na to, co widać („kocham / cieplej / inny klimat") — każda opcjonalna. Wielu kupi z pierwszego lub drugiego widoku.
**Dlaczego to inna kategoria.** Czas-do-magii skrócony do ~5 sekund; inferencja ze zdjęcia zastępuje formularz w całości; dostrajanie jest opcjonalnym szlifem, nie wymaganym lejkiem. (Perplexity: odpowiedź najpierw.)
**Za 5 lat:** „Latenca pokazała ci twoją nową ścianę, zanim zdążyłeś o cokolwiek zapytać. Reszta konkurencji dalej robiła quizy."
**Ryzyko.** Jeśli pierwszy strzał chybi (bez żadnego kontekstu), „wow" zamienia się w „no nie". Stawia wszystko na jakość inferencji ze zdjęcia.

### Model E — „Ambient" (żywa, ewoluująca przestrzeń, którą posiadasz)
**Mechanizm.** Nie sesja z końcem. Latenca staje się trwałym modelem Twojej przestrzeni i gustu. Twoja ściana to *miejsce, które masz* w aplikacji; ono proponuje pomysły w czasie (sezonowo, nowi artyści, „to zagra z tym, co masz"), reagujesz od czasu do czasu, ono uczy się ciągle, a zakup to po prostu „tak, zrób to naprawdę", gdy propozycja trafia.
**Dlaczego to inna kategoria.** Od transakcji/lejka do trwającej relacji i żywej przestrzeni; model gustu się kumuluje; ściany ewoluują. („Discover Weekly" dla Twoich ścian.)
**Za 5 lat:** „Latenca nie sprzedała ci obrazu. Została projektantem twojego domu na lata."
**Ryzyko.** Słabszy pierwszy „aha"; wymaga masy i czasu, by relacja miała wartość; trudniejszy start dla nowego użytkownika.

---

## Część 3 — Moja rekomendacja

**Jeden rdzenny zakład, na którym stoi cała reszta:** *inferencja ze zdjęcia ściany* + *nauka z reakcji, nie z pytań*. To jest wspólny mianownik modeli A, B, D i to jest to, „czego dziś nie ma".

Rekomendowana fuzja jako v1 nowej kategorii:
- **Wejście = Model D** (zdjęcie → natychmiastowe „wow" na Twojej ścianie; zero pytań).
- **Eksploracja = Model B** (jeśli pierwszy strzał nie trafia idealnie: dwie rozbieżne drogi zamiast cofania do formularza).
- **Sterowanie = Model A** (żyjesz w widoku ściany; podmiana/skala/pozycja bezpośrednią manipulacją).
- **Głos = Model C** (AI z lekkim zdaniem tłumaczy *dlaczego* — ale niewidzialnie, nie jako chatbot).
- **Model E** to faza 2 (retencja/LTV), nie start.

Czego **nie** przenoszę z obecnego flow: nazywania stylu, procentu „match", liniowych 8 kroków, pytań o rzeczy widoczne na zdjęciu, „jednej najlepszej" jako jedynej ścieżki.

**Najtańszy test, zanim cokolwiek zbudujemy (żeby nie zaprojektować pięknej hipotezy, która nie działa):**
1. Weź 5 realnych zdjęć ścian (znajomi/mieszkania z sieci).
2. Ręcznie (ja + ty) zróbmy dla każdej: (a) jeden „wow" strzał [test Modelu D] i (b) dwie rozbieżne drogi [test Modelu B].
3. Pokaż 5 osobom: czy „wow" trafia bez żadnych pytań? Czy „dwie drogi" szybciej trafiają w gust niż nasz obecny 8-krokowy flow?
To rozstrzyga, czy inferencja-ze-zdjęcia jest wystarczająco dobra, żeby na niej postawić — zanim zbudujemy ekrany.

---

## Bezpośrednie odpowiedzi na Twoje pytania
- **8 kroków?** Nie. Docelowo 0 pytań na wejściu; reszta jako opcjonalna reakcja.
- **Tyle pytań?** Nie — większość jest inferowalna ze zdjęcia.
- **AI może wywnioskować samo?** Tak, ~80% (styl, paleta, światło, skala, istniejąca sztuka) z jednego zdjęcia.
- **Kolejność?** Odwrócona: efekt najpierw, kontekst potem i opcjonalnie.
- **Rekomendacja za późno?** Tak — powinna być pierwszym ruchem, nie finałem.
- **Efekt przed odpowiedziami?** Tak (Model D).
- **Liniowe?** Nie — eksploracyjne (A/B).
- **Rozmowa?** Tak, ale reaktywna i niewidzialna, nie chatbot (C).
- **Współprojektowanie?** Tak — manipulacja na płótnie (A) + zdanie AI (C).
- **Kilka hipotez zamiast jednej?** Tak (B) — kontrast uczy szybciej niż werdykt.
- **Kontrolowany błąd?** Tak — wbudowany w „dwie drogi" (jedna to celowy strzał w bok).
- **Inny model niż questionnaire?** Tak — cztery różne powyżej.
