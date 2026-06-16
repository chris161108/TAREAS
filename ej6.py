#calculadora de promedios 

notas = {"christopher": [7, 8, 9], "elpepe123": [1, 1, 1], "anuel": [10, 10, 10] }

suma_notas = 0
aprovados = 0

for nota in notas.values():
    suma_notas += sum(nota)
    aprovados += 1


promedio = suma_notas / (aprovados * 3) if aprovados > 0 else 0
print(f"el promedio de las notas es {promedio}")
