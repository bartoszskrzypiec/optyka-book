#!/usr/bin/env python3
"""Wstawia tresc w miejsce znacznika <!-- TRESC --> w szkielecie strony.

    python3 dev/wstaw.py <sciezka-strony> <sciezka-pliku-z-trescia>

Uzywane jednorazowo przy pisaniu kazdej strony. Po wstawieniu znacznik
znika, wiec ponowne uruchomienie na tej samej stronie zglosi blad zamiast
po cichu nadpisac recznie dopracowana tresc.
"""
import sys, io

page, body = sys.argv[1], sys.argv[2]
html = io.open(page, encoding='utf-8').read()
if '<!-- TRESC -->' not in html:
    sys.exit(f'BLAD: {page} nie ma juz znacznika <!-- TRESC --> (tresc wstawiona wczesniej)')
tresc = io.open(body, encoding='utf-8').read().rstrip() + '\n'
io.open(page, 'w', encoding='utf-8').write(html.replace('  <!-- TRESC -->\n', tresc))
print(f'OK  {page}  (+{len(tresc)} znakow)')
