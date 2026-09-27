#!/usr/bin/env python3
"""Synchronizuje znaczniki stanu w index.html z rzeczywistoscia.

    python dev/stan.py
    python dev/stan.py --tom 2

Bez --tom skrypt przelicza kazdy tom, dla ktorego istnieje
dev/spis-tomN.json (dzis tylko tom2), aktualizujac tomN/index.html.

Spis tresci wymienia wszystkie strony od pierwszego dnia, wiec bez znacznika
czytelnik nie ma jak odroznic rozdzialu napisanego od szkieletu - klika
i trafia na pusta strone. Ten skrypt czyta kazda strone, sprawdza, czy jest
w niej jeszcze <!-- TRESC -->, i dopisuje do wiersza spisu odpowiedni stan.

To NIE jest krok budowania. tomN/index.html pozostaje plikiem utrzymywanym
recznie; ten skrypt tylko poprawia jedno pole, ktore inaczej rozjezdza sie
przy kazdym napisanym rozdziale. "scaffold.py sprawdz" pilnuje, zeby nie
zostal zapomniany.
"""

import io
import os
import re
import sys

sys.dont_write_bytecode = True

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GOTOWY = '<span class="stan stan--gotowy">gotowy</span>'
SZKIELET = '<span class="stan">w przygotowaniu</span>'


def find_volumes():
    """Numery tomow, dla ktorych istnieje dev/spis-tomN.json."""
    ns = []
    dev_dir = os.path.join(ROOT, 'dev')
    for fn in os.listdir(dev_dir):
        m = re.match(r'spis-tom(\d+)\.json$', fn)
        if m:
            ns.append(int(m.group(1)))
    return sorted(ns)


def index_path(n):
    return os.path.join(ROOT, f'tom{n}', 'index.html')


def czy_napisana(sciezka):
    """Strona jest napisana, gdy nie ma juz w niej znacznika szkieletu."""
    if not os.path.exists(sciezka):
        return False
    return '<!-- TRESC -->' not in io.open(sciezka, encoding='utf-8').read()


def stan_wierszy(n):
    """Mapa: href wiersza spisu tomu n -> True/False (napisana)."""
    idx = index_path(n)
    html = io.open(idx, encoding='utf-8').read()
    base = os.path.dirname(idx)
    out = {}
    for href in re.findall(r'<a class="index-row" href="([^"]+)"', html):
        out[href] = czy_napisana(os.path.join(base, href.replace('/', os.sep)))
    return out


def przelicz_tom(n, popraw=True):
    idx = index_path(n)
    html = io.open(idx, encoding='utf-8').read()
    stany = stan_wierszy(n)
    zmiany, rozjazdy = [], []

    def podmien(m):
        href, num_inner = m.group(1), m.group(2)
        czysty = re.sub(r'\s*<span class="stan[^"]*">.*?</span>', '', num_inner).strip()
        chciany = GOTOWY if stany.get(href) else SZKIELET
        obecny = re.search(r'<span class="stan[^"]*">.*?</span>', num_inner)
        if not obecny or obecny.group(0) != chciany:
            (zmiany if popraw else rozjazdy).append(href)
        return ('<a class="index-row" href="%s">\n        <span class="index-num">%s %s</span>\n'
                '        <span class="index-title">' % (href, czysty, chciany))

    # Kotwiczymy na nastepnym <span class="index-title">, bo .index-num moze juz
    # zawierac zagniezdzony <span class="stan"> — bez tej kotwicy niezachlanne
    # (.*?)</span> ucina sie na zamknieciu tego zagniezdzonego spana i kazdy
    # wiersz wyglada na rozjechany.
    nowy = re.sub(
        r'<a class="index-row" href="([^"]+)">\s*<span class="index-num">(.*?)</span>\s*'
        r'<span class="index-title">',
        podmien, html, flags=re.S)

    if popraw:
        if nowy != html:
            io.open(idx, 'w', encoding='utf-8', newline='\n').write(nowy)
        gotowe = sum(1 for v in stany.values() if v)
        print('tom%d/index.html: %d z %d stron oznaczonych jako gotowe (%d wierszy poprawionych)'
              % (n, gotowe, len(stany), len(zmiany)))
    return rozjazdy


def przelicz(tom=None):
    tomy = [tom] if tom is not None else find_volumes()
    rozjazdy = []
    for n in tomy:
        rozjazdy += [(n, href) for href in przelicz_tom(n, popraw=True)]
    return rozjazdy


def sprawdz(tom=None):
    """Uzywane przez scaffold.py sprawdz — zwraca liste (numer_tomu, href) rozjechanych wierszy."""
    tomy = [tom] if tom is not None else find_volumes()
    out = []
    for n in tomy:
        out += [(n, href) for href in przelicz_tom(n, popraw=False)]
    return out


def sprawdz_tom(n):
    """Jak sprawdz(), ale dla jednego, juz znanego tomu — zwraca same href."""
    return przelicz_tom(n, popraw=False)


if __name__ == '__main__':
    argv = sys.argv[1:]
    tom = None
    i = 0
    while i < len(argv):
        if argv[i] == '--tom':
            tom = int(argv[i + 1])
            i += 2
        else:
            i += 1
    przelicz(tom)
