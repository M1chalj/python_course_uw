import math


class Ułamek:
    def __init__(self, licznik, mianownik):
        assert mianownik != 0

        self.__licznik = licznik
        self.__mianownik = mianownik
        self.skróć()

    def skróć(self):
        gcd = math.gcd(self.__licznik, self.__mianownik)
        self.__licznik //= gcd
        self.__mianownik //= gcd

        if self.__mianownik < 0:
            self.__licznik *= -1
            self.__mianownik *= -1

        if self.__licznik == 0:
            self.__mianownik = 1

    def __add__(self, other):
        wynik = Ułamek(self.__licznik * other.__mianownik + self.__mianownik * other.__licznik,
                       self.__mianownik * other.__mianownik)
        wynik.skróć()
        return wynik

    def __sub__(self, other):
        wynik = Ułamek(self.__licznik * other.__mianownik - self.__mianownik * other.__licznik,
                       self.__mianownik * other.__mianownik)
        wynik.skróć()
        return wynik

    def __mul__(self, other):
        wynik = Ułamek(self.__licznik * other.__licznik, self.__mianownik * other.__mianownik)
        wynik.skróć()
        return wynik

    def __truediv__(self, other):
        wynik = Ułamek(self.__licznik * other.__mianownik, self.__mianownik * other.__licznik)
        wynik.skróć()
        return wynik

    def __eq__(self, other):
        return self.__licznik == other.__licznik and self.__mianownik == other.__mianownik

    def __gt__(self, other):
        return self.__licznik * other.__mianownik > other.__licznik * self.__mianownik

    def __ge__(self, other):
        return self.__licznik * other.__mianownik >= other.__licznik * self.__mianownik

    def __str__(self):
        return str(self.__licznik) + '/' + str(self.__mianownik)

    def __repr__(self):
        return str(self)


połowa = Ułamek(1, 2)
ćwierć = Ułamek(1, 4)
setna = Ułamek(1, 100)
zero = Ułamek(0,10)
zero2 = Ułamek(0, 17)

print(połowa, '+', ćwierć, '=', połowa + ćwierć)
assert połowa + ćwierć == Ułamek(3, 4)

print(połowa, '-', ćwierć, '=', połowa - ćwierć)
assert połowa - ćwierć == ćwierć

print(setna, '*', ćwierć, '=', setna * ćwierć)
assert setna * ćwierć == Ułamek(1, 400)

print(setna, '/', ćwierć, '=', setna / ćwierć)
assert setna / ćwierć == Ułamek(4, 100)

print(ćwierć, '-', połowa, '=', ćwierć - połowa)
assert ćwierć - połowa == zero - ćwierć

assert setna < połowa
assert ćwierć < połowa
assert setna < ćwierć
assert połowa <= połowa
assert setna <= połowa
assert zero == zero2

# błąd = Ułamek(10, 0)
