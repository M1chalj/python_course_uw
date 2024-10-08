import random
import math


def monte_carlo(n, k):
    licznik = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1:
            licznik += 1

        if (i + 1) % k == 0:
            print("Krok", i + 1, "wartość:", licznik / (i + 1) * 4)
    przyblizenie_pi = licznik / n * 4
    print("Wartość po", n, "krokach:", przyblizenie_pi, "błąd:", abs(math.pi - przyblizenie_pi))


monte_carlo(int(input("Podaj liczbę iteracji: ")), int(input("Podaj krok: ")))
