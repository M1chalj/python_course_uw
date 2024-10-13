aktywnosci = {}


def dodaj():
    nazwa = input("Podaj nazwę: ")
    czas = int(input("Podaj czas: "))
    if nazwa not in aktywnosci.keys():
        aktywnosci[nazwa] = []
    aktywnosci[nazwa].append(czas)
    print("Dodano")


def sumuj_czas(aktywnosc):
    czas = 0
    for t in aktywnosci[aktywnosc]:
        czas += t
    return czas


def pokaz_czas():
    nazwa = input("Podaj nazwę: ")
    if nazwa not in aktywnosci.keys():
        print("Niepoprawna nazwa")
    else:
        print("Całkowity czas:", sumuj_czas(nazwa))


def pokaz_top():
    ranking = []
    for nazwa in aktywnosci.keys():
        ranking.append((sumuj_czas(nazwa), nazwa))
    ranking.sort(reverse=True)
    for i in range(min(3, len(ranking))):
        print(i + 1, ". ", ranking[i][1], ": ", ranking[i][0], sep="")


def koniec():
    exit(0)


funkcje = {
    "dod": dodaj,
    "pok": pokaz_czas,
    "top": pokaz_top,
    "wyj": koniec
}
opisy = {
    "dod": "Dodaj aktywność",
    "pok": "Pokaż czas",
    "top": "Pokaż top",
    "wyj": "Wyjście"
}

while True:
    print("Dostępne funkcje:")
    for skrot, opis in zip(opisy.keys(), opisy.values()):
        print(skrot, ": ", opis, sep="")

    func = input("Co chcesz zrobić: ")
    while func not in funkcje.keys():
        func = input("Niepoprawny kod, spróbuj jeszcze raz: ")

    funkcje[func]()
