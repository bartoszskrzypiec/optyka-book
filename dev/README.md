# dev/

Narzędzia deweloperskie. **Nie są krokiem budowania** — książka to statyczne
pliki HTML i nic ich nie generuje w locie.

| Skrypt | Do czego |
|---|---|
| `scaffold.py szkielet` | Tworzy brakujące strony z `dev/spis.json`. Istniejących nie rusza, nigdy. |
| `scaffold.py sprawdz` | Kontrola spójności. Musi przechodzić czysto przed commitem. |
| `stan.py` | Synchronizuje znaczniki „gotowy / w przygotowaniu” w spisie treści ze stanem stron. |
| `slowa.py` | Licznik prozy w `.section` i wizualizacji. Cel: 2000–3500 słów, 5–8 wiz. |
| `wstaw.py` | Wstawia treść w miejsce `<!-- TRESC -->`. Odmawia, jeśli znacznika już nie ma. |
| `dopisz.py` | Dopisuje sekcje przed blokiem „Z praktyki". Odmawia, jeśli go nie znajdzie. |

`spis.json` jest jedynym źródłem struktury książki: części, rozdziały,
dodatki i mapa `EXT OF`. Z jej odwrotności budują się bloki „Idź głębiej",
a `sprawdz` pilnuje, żeby zgadzało się w obie strony.

Strony testowe silnika 3D (jeśli powstaną) też trafiają tutaj — nie ma do nich
linków ze spisu treści i nie wchodzą do nawigacji. Wymagają serwera, bo widgety
to moduły ES:

    python -m http.server 8000
