# dev/

Narzędzia deweloperskie. **Nie są krokiem budowania** — książka to statyczne
pliki HTML i nic ich nie generuje w locie.

Książka jest podzielona na tomy: dziś istnieje `tom2/` (`rozdzialy/`,
`dodatki/`, `matematyka/`, `index.html`), docelowo dojdzie `tom1/`. Każdy tom
ma własny spis w `dev/spis-tomN.json`. `assets/` zostaje wspólne w katalogu
głównym repo dla obu tomów.

| Skrypt | Do czego |
|---|---|
| `scaffold.py szkielet` | Tworzy brakujące strony z `dev/spis-tomN.json`. Istniejących nie rusza, nigdy. |
| `scaffold.py sprawdz` | Kontrola spójności. Musi przechodzić czysto przed commitem. |
| `stan.py` | Synchronizuje znaczniki „gotowy / w przygotowaniu” w `tomN/index.html` ze stanem stron. |
| `slowa.py` | Licznik prozy w `.section` i wizualizacji. Cel: 1200–1600 słów, 4–6 wiz. |
| `wstaw.py` | Wstawia treść w miejsce `<!-- TRESC -->`. Odmawia, jeśli znacznika już nie ma. Bierze pełną ścieżkę strony (np. `tom2/rozdzialy/x.html`), więc działa na dowolnym tomie bez zmian. |
| `dopisz.py` | Dopisuje sekcje przed blokiem „Z praktyki". Odmawia, jeśli go nie znajdzie. Tak samo bierze pełną ścieżkę strony, więc jest tomowo-niezależny. |

`scaffold.py`, `stan.py` i `slowa.py` przyjmują opcjonalny argument
`--tom N` (np. `python dev/scaffold.py sprawdz --tom 2`). Bez niego
przetwarzają KAŻDY tom, dla którego istnieje `dev/spis-tomN.json` — dziś
tylko `tom2`, `tom1` dołączy się sam, gdy powstanie `dev/spis-tom1.json`
i katalog `tom1/`.

`spis-tomN.json` jest jedynym źródłem struktury danego tomu: części,
rozdziały, dodatki i mapa `EXT OF`. Z jej odwrotności budują się bloki
„Idź głębiej", a `sprawdz` pilnuje, żeby zgadzało się w obie strony —
osobno dla każdego tomu.

Strony testowe silnika 3D (jeśli powstaną) też trafiają tutaj — nie ma do nich
linków ze spisu treści i nie wchodzą do nawigacji. Wymagają serwera, bo widgety
to moduły ES:

    python -m http.server 8000
