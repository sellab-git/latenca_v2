# RESEARCH — Ideogram + Midjourney UX/UI (brief dla Claude Chrome)

> Brief do wklejenia do **Claude Chrome**. Cel: dokładna analiza dwóch generatorów obrazów
> (Ideogram i Midjourney web) po to, by przeprojektować nasze dwa ekrany — **Home** i **Product** —
> w stronę prostszej, „nowoczesnej" logiki, którą oba te produkty mają.
>
> Wyniki wklej z powrotem do rozmowy z Claude Code — zrobię z nich dokument `docs/RESEARCH-generators.md`
> i dopiero na jego podstawie zaprojektuję nową wersję.

---

## Zasady badania (przeczytaj najpierw)

1. **Benchmark, nie kopia.** Nie kopiujemy kodu, tekstów, grafik, brandingu ani nazw. Analizujemy **logikę i wzorce** — co gdzie leży, co się dzieje po kliknięciu, dlaczego wydaje się proste.
2. **Oznaczaj każdą obserwację:**
   - `[KLIK]` = sprawdzone realnie, klikając / przewijając / wpisując.
   - `[WNIOSEK]` = domysł, nie zweryfikowane klikiem.
   Nie zgaduj bez oznaczenia — wolę „nie sprawdziłem" niż ładny opis, który okaże się nieprawdą.
3. **Zawsze porównuj oba naraz.** Dla każdego punktu: *Ideogram robi X, Midjourney robi Y.* Gdzie oba robią to samo → to jest silny wzorzec. Gdzie się różnią → opisz różnicę.
4. **Rób zrzuty ekranu** kluczowych ekranów (desktop i mobile) i opisz co na nich widać. Nazywaj je np. `ideogram-home-desktop`, `mj-product-mobile`.
5. Zakres: **Midjourney = wersja WEB** (`midjourney.com`), nie Discord. Discord pomijamy.

---

## ⚠️ Kluczowa różnica, o której trzeba pamiętać przy KAŻDYM ekranie

**Ideogram i Midjourney GENERUJĄ obrazy. My tego NIE robimy** — mamy gotowy katalog grafik w bazie, a użytkownik z nimi rozmawia przez doradcę.

Dlatego przy każdej sekcji odpowiedz też na jedno dodatkowe pytanie:

> **„Co z tego ma sens, gdy zamiast pola do generowania mamy gotowy katalog + doradcę do wyboru?"**

Konkretnie interesuje mnie odróżnienie:
- ich **górne pole = prompt, który TWORZY nowy obraz** ↔ nasze pole = **rozmowa, która WYBIERA/ZAMIENIA istniejący obraz**;
- ich **feed = cudze wygenerowane obrazy** ↔ nasz katalog = **kurowana oferta na sprzedaż**.

Zaznacz, które ich rozwiązania przenoszą się 1:1, które trzeba przerobić, a które są bez sensu dla nas.

---

## SEKCJA 0 — Dostęp i zakres

0.1 Czy trzeba być zalogowanym, żeby zobaczyć stronę główną / feed / szczegół obrazu? Osobno dla Ideogram i Midjourney. `[KLIK]`
0.2 Czym różni się widok **wylogowany vs zalogowany** na stronie głównej? (co znika, co się pojawia)
0.3 Wypisz wszystkie główne sekcje/zakładki w nawigacji każdego serwisu (nazwy 1:1) — to nasza mapa ekranów do porównania.

---

## SEKCJA 1 — Globalny szkielet (nagłówek, nawigacja, „to jedno pole")

To jest sedno tego, co Arturowi się podoba — sprawdź szczególnie dokładnie.

1.1 **Górne pole wejściowe (prompt bar):**
   - Czy jest **jedno**, czy jest ich kilka w różnych miejscach? `[KLIK]`
   - Czy **zostaje w tym samym miejscu** gdy przewijasz i gdy przechodzisz między stronami? Czy jest przyklejone (sticky) u góry?
   - Dokładna pozycja: góra strony na środku / w nagłówku / pływające na dole?
   - Co jest **wewnątrz i wokół** pola: przyciski, ikony, wybór modelu, proporcje obrazu (aspect ratio), liczba obrazów, ustawienia? Wypisz wszystko.
   - Co się dzieje **po kliknięciu w pole** (focus)? Rozwija się? Pokazuje podpowiedzi/historię?
   - Placeholder — jaki tekst zachęca do wpisania?
1.2 **Nagłówek:** co w nim jest (logo, zakładki, konto, kredyty/licznik, ustawienia)? Czy nagłówek jest sticky?
1.3 **Ogólny charakter wizualny** — opisz konkretnie *dlaczego* wydaje się proste i nowoczesne: ile elementów widać naraz, ile pustej przestrzeni, czy kontrolki są schowane do momentu potrzeby (progressive disclosure), czy jest jedno wyraźne główne działanie na ekranie.
1.4 Kolorystyka (jasny/ciemny motyw, akcent), krój pisma (czy szeryfowy/bezszeryfowy), zaokrąglenia, cienie, animacje — krótko, dla obu.

---

## SEKCJA 2 — Strona główna / feed

Artur twierdzi: *„strona główna to tak naprawdę pole do rozmowy, a od razu pod spodem widoczny katalog"*. Zweryfikuj to dla obu.

2.1 Co jest **nad zgięciem** (pierwsze co widać bez przewijania)? Czy to naprawdę: pole + od razu siatka obrazów? Czy jest jakiś hero/baner/tekst powitalny? `[KLIK]`
2.2 **Siatka obrazów pod polem:**
   - ile kolumn, jak gęsto, jakie proporcje kafelków (kwadrat/różne)?
   - co pokazuje **jeden kafelek**: sam obraz? autor? prompt? akcje? polubienia?
   - co się dzieje **po najechaniu** na kafelek (hover)?
   - **nieskończone przewijanie** czy stronicowanie / „pokaż więcej"?
2.3 Czy nad siatką są **zakładki / filtry / sortowanie** (np. Top / Nowe / Śledzone / kategorie)? Wypisz je.
2.4 Czy są sekcje tematyczne / kategorie / „nastroje" (mood) do przeglądania?
2.5 **Nasze pytanie kuracji:** gdyby te kafelki były produktami na sprzedaż (a nie cudzymi generacjami) — co na kafelku byłoby zbędne, a czego brakuje (cena, rozmiar, „na ścianie")?

---

## SEKCJA 3 — Pole wejściowe w akcji (ich generowanie ↔ nasz doradca)

To najważniejsza sekcja do przełożenia na naszego doradcę.

3.1 Wpisz prompt i zatwierdź. **Co się dzieje?** `[KLIK]`
   - przechodzisz na inny URL, czy zostajesz na miejscu?
   - gdzie **pojawia się wynik** — pod polem, na osobnej stronie, w panelu z boku?
   - czy pole **zostaje na miejscu** po wysłaniu, gotowe na kolejny wpis?
3.2 Czy to jest **rozmowa (chat, ciąg tur)**, czy raczej **pojedyncze strzały** (prompt → 4 obrazy → nowy prompt od zera)? To ważne — Artur odbiera to jako „rozmowę", chcę wiedzieć czy naprawdę nią jest. Opisz osobno dla Ideogram i Midjourney.
3.3 Jak **poprawia się / zmienia** wynik: warianty (variations), przerób (remix/edit), „bardziej jak ten", zmiana ustawień i ponów? Wypisz mechanizmy.
3.4 Czy da się **odnieść do konkretnego obrazu i powiedzieć „chcę coś podobnego / cieplejszego"**? Jak dokładnie działa ten flow? (to nasz rdzeń — zamiana obrazu na cieplejszy)
3.5 Historia rozmowy / poprzednich promptów — gdzie jest, jak się do niej wraca?
3.6 Czy jest **osobne pole „szukaj"** obok pola „generuj/prompt", czy to **to samo pole**? Krytyczne dla nas — mamy zasadę „jedno okno rozmowy na ekran" i nie chcemy trzech pól, w które nie wiadomo w co klikać. Sprawdź to bardzo dokładnie na obu. `[KLIK]`

---

## SEKCJA 4 — Strona produktu / szczegół obrazu

Artur: *„strony produktu mają podobny UX do tego, co my mamy teraz"*. Opisz ich dokładnie, żebym mógł porównać z naszym `04-advisor`.

4.1 Jak się **wchodzi** na szczegół obrazu (klik w kafelek)? Czy zmienia się URL? Czy to pełna strona, czy nakładka (modal/lightbox)? `[KLIK]`
4.2 **Układ szczegółu:** obraz na środku? panel z boku? co jest w panelu?
4.3 Jakie **akcje** przy obrazie: pobierz, warianty, remix, zapisz, udostępnij, „użyj jako referencji", zgłoś? Wypisz wszystkie.
4.4 Jakie **metadane** pokazują: prompt, autor, model, ustawienia, data, polubienia?
4.5 **Nawigacja między obrazami** w szczególe: strzałki lewo/prawo? przewijanie? czy URL się zmienia przy każdym? Czy przycisk „wstecz" wraca do feedu w tym samym miejscu? (u nas: zmiana obrazu ma NIE dodawać wpisu do historii — sprawdź jak oni to robią)
4.6 Czy pod obrazem są **podobne / powiązane** obrazy? Jak dobrane?
4.7 **Nasze pytanie kuracji:** gdyby to była strona sprzedaży druku (rozmiar, materiał, rama, cena, podgląd na ścianie, dodaj do koszyka) — co z ich układu zostaje, a co trzeba dołożyć?

---

## SEKCJA 5 — Szukanie i eksploracja

5.1 Jak działa **wyszukiwanie**? Po tekście? Po obrazie (upload/„podobne do")? Podpowiedzi? `[KLIK]`
5.2 Filtry przy wynikach — jakie (styl, kolor, proporcje, model, autor)?
5.3 Czy jest osobny ekran **Explore/Feed** różny od strony głównej, czy to jedno i to samo?

---

## SEKCJA 6 — Mobile

Zmniejsz okno / otwórz na telefonie i sprawdź:

6.1 Gdzie ląduje **górne pole** na wąskim ekranie — nadal góra? na dole? chowane? `[KLIK]`
6.2 Czy jest **dolny pasek nawigacji** (bottom tabbar)? Jakie ikony?
6.3 Ile kolumn ma siatka na telefonie? Jak wygląda szczegół obrazu na mobile?
6.4 Co znika / upraszcza się względem desktopu?

---

## SEKCJA 7 — Co się NIE przełoży na nas (ważne)

7.1 Wypisz elementy UI, które **istnieją tylko dlatego, że oni generują** i dla nas (katalog + doradca) są zbędne lub mylące: wybór modelu, liczba obrazów, seed, aspect ratio jako *input*, kredyty/koszt generacji, „upscale", galeria cudzych generacji jako społeczność itd.
7.2 Gdzie ich prostota wynika z tego, że **nie sprzedają fizycznego produktu** (brak rozmiaru/materiału/ramy/wysyłki/koszyka)? To rzeczy, których u nas nie da się usunąć — chcę wiedzieć, gdzie nasza strona z konieczności będzie „bogatsza" niż ich.

---

## SEKCJA 8 — Trzy tezy Artura do bezpośredniej weryfikacji

Odpowiedz wprost PRAWDA/FAŁSZ + dowód `[KLIK]`, osobno dla Ideogram i Midjourney:

8.1 „Jest **jedno** pole u góry, które **nie zmienia położenia** co chwilę." → ?
8.2 „Strona główna to **pole do rozmowy, a od razu pod spodem katalog**." → ?
8.3 „Ich strony **produktu** są podobne do zwykłej strony produktu (obraz + panel z akcjami z boku)." → ?

---

## SEKCJA 9 — Podsumowanie od Claude Chrome

Na koniec, w kilku zdaniach:

9.1 **Co konkretnie sprawia, że oba wydają się proste i nowoczesne** — 3–5 mechanizmów (nie „ładne", tylko *dlaczego*: np. jedno główne działanie, kontrolki schowane, dużo światła, natychmiastowy wynik pod polem).
9.2 **Największa różnica** między Ideogram a Midjourney w podejściu do tego samego problemu.
9.3 Jeśli coś Cię zaskoczyło albo wygląda inaczej niż opis powyżej — powiedz. Nie dopasowuj obserwacji do moich pytań.

---

### Format odpowiedzi, którego potrzebuję z powrotem

Dla każdej sekcji: krótkie punkty, **Ideogram vs Midjourney obok siebie**, każdy z tagiem `[KLIK]` lub `[WNIOSEK]`, plus nazwy zrzutów ekranu, które zrobiłeś. Nie musi być pięknie — ma być prawdziwe i kompletne.
