import random
import math

def montecarlo(n):
    licznik = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1:
            licznik += 1
        print('Krok',i+1, '\tbłąd:', abs(math.pi - licznik / (i + 1) * 4))
    return licznik / n * 4

montecarlo(100)