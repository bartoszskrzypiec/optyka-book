#!/usr/bin/env python3
"""
Jednorazowy skrypt: tworzy przekierowania pod STARYMI adresami (root-level
rozdzialy/, dodatki/, matematyka/) na strony, ktore przeniosly sie do tom2/
przy okazji podzialu ksiazki na tomy (patrz CLAUDE.md, dev/README.md).

Dla kazdego pliku w tom2/rozdzialy/*.html, tom2/dodatki/*.html i
tom2/matematyka/*.html tworzy w odpowiadajacym katalogu w korzeniu repo
maly plik-zaslepke, ktory:

  - w <head> ma <meta name="redirect-stub" content="tom2/...">, po ktorym
    "scaffold.py sprawdz" i ten skrypt rozpoznaja zaslepke (i nigdy nie
    nadpisuja realnej strony bez tego znacznika),
  - przekierowuje przegladarke natychmiast (meta refresh + location.replace,
    zachowujac location.hash na wypadek linku do konkretnej sekcji),
  - ma <link rel="canonical"> na nowy adres (SEO),
  - i widoczny polski link na wypadek, gdyby JS/refresh nie zadzialal.

Uruchamiane raz, recznie: `python dev/przekierowania.py`. Nie jest krokiem
budowania i nie wchodzi do zadnej petli CI.
"""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (katalog zrodlowy w tom2/, katalog docelowy w korzeniu)
DIRS = [
    ("tom2/rozdzialy", "rozdzialy"),
    ("tom2/dodatki", "dodatki"),
    ("tom2/matematyka", "matematyka"),
]


def stub_html(target_rel):
    """target_rel np. 'tom2/rozdzialy/rozdzial-01-fala-czy-promien.html'."""
    # Stub siedzi w korzeniu, jeden poziom nad tom2/, wiec relatywny link
    # do niego to "../" + target_rel.
    rel = "../" + target_rel.replace("\\", "/")
    return f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="redirect-stub" content="{target_rel}">
<meta http-equiv="refresh" content="0; url={rel}">
<link rel="canonical" href="{rel}">
<title>Strona przeniesiona</title>
<script>
(function () {{
  var target = {rel!r} + (location.hash || "");
  location.replace(target);
}})();
</script>
</head>
<body>
<p>Ta strona przeniosła się do Tomu 2: <a href="{rel}">{rel}</a></p>
</body>
</html>
"""


def is_stub(path):
    if not os.path.isfile(path):
        return None  # nie istnieje
    try:
        with open(path, "r", encoding="utf-8") as f:
            head = f.read(2000)
    except OSError:
        return False
    return "name=\"redirect-stub\"" in head


def main():
    created = []
    skipped_real = []

    for tom_dir, old_dir in DIRS:
        src_abs = os.path.join(ROOT, tom_dir)
        if not os.path.isdir(src_abs):
            continue
        dst_abs = os.path.join(ROOT, old_dir)
        os.makedirs(dst_abs, exist_ok=True)

        for name in sorted(os.listdir(src_abs)):
            if not name.endswith(".html"):
                continue
            target_rel = f"{tom_dir}/{name}".replace("\\", "/")
            stub_path = os.path.join(dst_abs, name)

            existing = is_stub(stub_path)
            if existing is None:
                # nie istnieje jeszcze -> tworzymy
                with open(stub_path, "w", encoding="utf-8", newline="\n") as f:
                    f.write(stub_html(target_rel))
                created.append(os.path.relpath(stub_path, ROOT))
            elif existing is True:
                # juz jest zaslepka -> zostawiamy (idempotentnie), ale
                # odswiezamy tresc na wypadek zmiany szablonu
                with open(stub_path, "w", encoding="utf-8", newline="\n") as f:
                    f.write(stub_html(target_rel))
            else:
                # plik istnieje i NIE jest zaslepka -> prawdziwa strona,
                # nigdy nie nadpisujemy
                skipped_real.append(os.path.relpath(stub_path, ROOT))

    print(f"Utworzono/odswiezono zaslepek: {len(created)}")
    if skipped_real:
        print(f"Pominieto (prawdziwe strony, nie zaslepki): {len(skipped_real)}")
        for p in skipped_real:
            print(f"  - {p}")


if __name__ == "__main__":
    main()
