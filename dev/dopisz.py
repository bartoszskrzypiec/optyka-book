#!/usr/bin/env python3
"""Dopisuje sekcje do gotowego rozdzialu, tuz przed blokiem "Z praktyki".

    python3 dev/dopisz.py <strona> <plik-z-sekcjami>

Kolejnosc strony jest sztywna (sekcje, potem Z praktyki, Slowniczek, Co dalej),
wiec nowe sekcje moga wejsc tylko w to jedno miejsce. Skrypt odmawia pracy,
jesli go nie znajdzie - lepiej blad niz cicho zepsuta kolejnosc.
"""
import sys, io

MARKER = '  <div class="panel practice">'

page, body = sys.argv[1], sys.argv[2]
html = io.open(page, encoding='utf-8').read()
if MARKER not in html:
    sys.exit('BLAD: %s nie ma bloku "Z praktyki" w oczekiwanym miejscu' % page)
tresc = io.open(body, encoding='utf-8').read().rstrip() + '\n\n'
html = html.replace(MARKER, tresc + MARKER, 1)
io.open(page, 'w', encoding='utf-8').write(html)
print('OK  %s  (+%d znakow)' % (page, len(tresc)))
