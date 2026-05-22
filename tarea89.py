import math
import random

punto1 = (random.randint(0, 10), random.randint(0, 10))
punto2 = (random.randint(0, 10), random.randint(0, 10))

def calcular_distancia(p1, p2):

    distancia = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    return distancia

print("Punto 1:", punto1)
print("Punto 2:", punto2)
print("La distancia euclidiana es:", round(calcular_distancia(punto1, punto2), 2))