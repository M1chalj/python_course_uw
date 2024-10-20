import argparse
import random
from pathlib import Path
import os
import csv
import json

dni_tygodnia_skroty = {
    'pn': 0,
    'wt': 1,
    'sr': 2,
    'cz': 3,
    'pt': 4,
    'sb': 5,
    'nd': 6
}

dni_tygodnia_nazwy = {
    0: 'poniedziałek',
    1: 'wtorek',
    2: 'środa',
    3: 'czwartek',
    4: 'piątek',
    5: 'sobota',
    6: 'niedziela'
}

pory_dnia_nazwy = {
    'r': 'rano',
    'w': 'wieczorem'
}

modele = ['A', 'B', 'C']

domyslna_pora_dnia = 'rano'


def wczytaj_argumenty():
    parser = argparse.ArgumentParser()
    parser.add_argument('-miesiace',
                        help='lista miesięcy',
                        nargs='+',
                        required=True)
    parser.add_argument('-dni',
                        help='lista dni lub przedziałów dla każdego miesiąca np. pn-wt, pt',
                        nargs='+',
                        required=True)
    parser.add_argument('-pory',
                        help='pory dnia (rano(r)/wieczór(w)) dla każdej kombinacji miesiąc - dzień. Domyślnie rano',
                        nargs='+',
                        required=True)
    parser.add_argument('-t',
                        help='tworzenie plików (domyślnie pliki są odczytywane)',
                        action='store_const',
                        const='t',
                        default='o',
                        dest='tryb')
    parser.add_argument('-j',
                        help='przetwarza pliki o rozszerzeniu json',
                        action='store_true',
                        dest='json')
    parser.add_argument('-c',
                        help='przetwarza pliki o rozszerzeniu csv',
                        action='store_true',
                        dest='csv')
    args = parser.parse_args()

    if not args.json and not args.csv:
        parser.print_help()
        print('Nie podano żadnego formatu plików')
        exit()

    if len(args.miesiace) != len(args.dni):
        parser.print_help()
        print('Liczba miesięcy i dni jest różna')
        exit()

    return args


def daj_liste_dni(zakres):
    wynik = []
    if '-' in zakres:
        lista = zakres.split('-')
        if len(lista) != 2 or lista[0] not in dni_tygodnia_skroty or lista[1] not in dni_tygodnia_skroty:
            print('niepoprawny zakres dni tygodnia')
            exit()

        for i in range(dni_tygodnia_skroty[lista[0]], dni_tygodnia_skroty[lista[1]] + 1):
            wynik.append(dni_tygodnia_nazwy[i])

    else:
        if zakres in dni_tygodnia_skroty:
            wynik.append(dni_tygodnia_nazwy[dni_tygodnia_skroty[zakres]])
        else:
            print('niepoprawny zakres dni tygodnia')
            exit()
    return wynik


def przetworz_listy(miesiace, dni, pory):
    skladowe_sciezek = []
    indeks_pora = 0
    for i in range(len(miesiace)):
        lista_dni = daj_liste_dni(dni[i])
        for dzien in lista_dni:
            if indeks_pora < len(pory):
                if not pory[indeks_pora] in pory_dnia_nazwy:
                    print('niepoprawna pora')
                    exit()
                else:
                    pora = pory_dnia_nazwy[pory[indeks_pora]]
            else:
                pora = domyslna_pora_dnia
            skladowe_sciezek.append([miesiace[i], dzien, pora])
            indeks_pora += 1
    return skladowe_sciezek


def zrob_sciezki(skladowe_sciezek):
    sciezki = []
    for skladowa in skladowe_sciezek:
        sciezka = os.getcwd()
        for folder in skladowa:
            sciezka = os.path.join(sciezka, folder)
            if not Path(sciezka).exists():
                os.mkdir(sciezka)
        sciezki.append(sciezka)

    return sciezki


def zapis_do_csv(sciezki):
    for sciezka in sciezki:
        dane = [['Model', 'Wynik', 'Czas'],
                [random.choice(modele), random.randint(0, 1000), str(random.randint(0, 1000)) + 's']]
        with open(os.path.join(sciezka, 'Dane.csv'), 'w', newline='') as plik:
            pisarz = csv.writer(plik, delimiter=';')
            for wiersz in dane:
                pisarz.writerow(wiersz)


def zapis_do_json(sciezki):
    for sciezka in sciezki:
        dane = {'Model': random.choice(modele),
                'Wynik': random.randint(0, 1000),
                'Czas': str(random.randint(0, 1000)) + 's'}
        with open(os.path.join(sciezka, 'Dane.json'), 'w') as plik:
            json.dump(dane, plik)


def odczyt_z_csv(sciezki, model):
    suma = 0
    for sciezka in sciezki:

        sciezka_do_pliku = os.path.join(sciezka, 'Dane.csv')
        if not Path(sciezka_do_pliku).exists():
            continue

        with open(sciezka_do_pliku, 'r') as plik:
            czytelnik = csv.reader(plik, delimiter=';')
            naglowki = next(czytelnik)
            if 'Model' not in naglowki or 'Czas' not in naglowki:
                print('Błędny plik', sciezka_do_pliku)
                continue
            kolumnaModel = naglowki.index('Model')
            kolumnaCzas = naglowki.index('Czas')
            for wiersz in czytelnik:
                if wiersz[kolumnaModel] == model:
                    suma += int(wiersz[kolumnaCzas][:-1])
    return suma


def odczyt_z_json(sciezki, model):
    suma = 0
    for sciezka in sciezki:
        sciezka_do_pliku = os.path.join(sciezka, 'Dane.json')
        if not Path(sciezka_do_pliku).exists():
            continue
        with open(sciezka_do_pliku, 'r') as plik:
            dane = json.load(plik)
            if not ('Model' in dane or 'Czas' in dane):
                print('Błędny plik', sciezka_do_pliku)
                continue
            if (dane['Model'] == model):
                suma += int(dane['Czas'][:-1])
    return suma


args = wczytaj_argumenty()
sciezki = zrob_sciezki(przetworz_listy(args.miesiace, args.dni, args.pory))
if args.tryb == 't':
    if args.json:
        zapis_do_json(sciezki)
    if args.csv:
        zapis_do_csv(sciezki)
else:
    suma = 0
    if args.json:
        suma += odczyt_z_json(sciezki, 'A')
    if args.csv:
        suma += odczyt_z_csv(sciezki, 'A')
    print('Suma czasów:', suma)
