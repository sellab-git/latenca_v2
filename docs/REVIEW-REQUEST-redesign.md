# REVIEW REQUEST — redesign Home + Product (dla ChatGPT)

> Do wklejenia ChatGPT-owi (senior reviewer czytający repo `sellab-git/latenca_v2`).
> Rola: skrytykuj i doradź w 3 konkretnych decyzjach — nie przebudowuj, nie wychodź poza zakres.

## Co masz zrobić

Przeczytaj w repo, w tej kolejności:
1. `docs/REDESIGN-proposal.md` — propozycja zmian + 3 otwarte decyzje (to główny przedmiot recenzji).
2. `docs/RESEARCH-generators.md` — badanie Ideogram + Midjourney (wnioski + obserwacje z realnych zrzutów).
3. Kontekst wiążący: `docs/PROJECT_STATUS.md`, `docs/DECISIONS.md`, `docs/LOCKS.md`.

Potem odpowiedz **konkretnie na 3 decyzje** (rekomendacja + uzasadnienie na każdą) i wskaż, czego nie dostrzegliśmy.

## Trzy decyzje do rozstrzygnięcia

1. **Home — jak radykalnie:** A) pełny generator (pole + siatka, nic więcej) / B) hybryda (pole + katalog na górze, cienka warstwa zaufania niżej) / C) zachowawczo (bogata Home + trwałe pole). *(Nasza rekomendacja: B.)*
2. **Pole na Home — czym jest:** A) doradca‑jako‑wyszukiwarka (brak osobnego search, doradca JEST wyszukiwarką) / B) zwykłe wyszukiwanie na Home, doradca dopiero na produkcie. *(Nasza rekomendacja: A jako cel; w MVP pole może startować jako proste wyszukiwanie i „urastać".)*
3. **Pole na mobile — gdzie:** A) dół (jak Midjourney, kciukowo) / B) góra (jak Ideogram, stały nagłówek). *(Nasza rekomendacja: A.)*

## Kontekst wiążący — NIE proponuj wbrew temu

- **Latenca = kurowany SKLEP z drukami na ścianę**, jeden moment AI (doradca, D‑030). Sklep działa bez doradcy; rozmiar/materiał/rama to zwykłe parametry produktu, nie AI.
- **Grafiki pozyskujemy z różnych/publicznych źródeł**; artyści = na razie sama atrybucja (marketplace docelowo). **Nie sprzedajemy plików cyfrowych** (D‑036 — publiczne źródła czynią sprzedaż pliku słabą i niejasną prawnie).
- **Twórca to solo, nietechniczny founder** budujący z Claude Code. Rozwiązania **muszą być do zbudowania w pojedynkę.** Nie proponuj infrastruktury/procesów zespołowych.
- **Generatory studiujemy jako benchmark, nie kopiujemy** kodu/wyglądu/brandingu. Zostaje **nasz** system wizualny (kremowe tło #F6F3ED + lawenda #7C6CF0, serif Lora). Ich biało‑czarna surowość to nie my.
- **Kolejność prac: system (makiety) → prawdziwy kod MVP → dystrybucja.** **Dystrybucja/CAC są ZAMKNIĘTE** — nie doradzaj o kanałach, mimo że to ryzyko nr 1.
- **Materiał determinuje, które rozmiary i ceny istnieją** (to NIE Mixtiles) — nie sugeruj cięcia liczby materiałów ani „rozmiar najpierw".
- **Doradca = D‑034** (jeden ekran, dwa stany: rozmowa lub panel zakupu; ten zamknięty zwija się do linii, nigdy nie znika). **Jedna rozmowa na ekran** (D‑036). Stan rozmowy musi żyć NAD stroną produktu w drzewie, inaczej miękka nawigacja go zabije.
- **Powierzchnia wyświetlania = płaska ściana** (D‑033); pokoje to tylko przełącznik do porównania.
- Cel doradcy to jakość rekomendacji, nie sprzedaż na siłę; koszt AI zabezpieczony (maks. ~1 zł/sesja), model wymienialny.

## Czego konkretnie od Ciebie chcę

1. Rekomendacja na każdą z 3 decyzji + krótkie uzasadnienie.
2. **Największe ryzyko, którego nie dostrzegliśmy** — zwłaszcza czy „doradca‑jako‑wyszukiwarka" (Decyzja 2A) to dobry wyróżnik czy pułapka (musi ogarniać zapytania „pokaż mi…", nie tylko „doradź mi").
3. Czy z wzorców generatorów bierzemy **za dużo albo za mało** czegokolwiek.
4. Czy propozycja **nie łamie żadnej zablokowanej decyzji** z `DECISIONS.md`/`LOCKS.md`.

Odpowiedz zwięźle i wprost. Jeśli się z naszą rekomendacją zgadzasz — powiedz to krótko i przejdź dalej; poświęć miejsce tam, gdzie się różnisz.
