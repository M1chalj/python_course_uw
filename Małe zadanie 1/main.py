import random
import math


def pi_monte_carlo(n, k):
    in_cnt = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1:
            in_cnt += 1

        if (i + 1) % k == 0:
            print("Krok", i + 1, "wartość:", in_cnt / (i + 1) * 4)
    estimated_pi = in_cnt / n * 4
    print("Wartość po", n, "krokach:", estimated_pi, "błąd:", abs(math.pi - estimated_pi))


pi_monte_carlo(int(input("Podaj liczbę iteracji: ")), int(input("Podaj krok: ")))
