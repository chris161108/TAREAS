import random

numeros_aleatorios = []
pares = []
impares = []


for i in range(15):
    numeros_aleatorios.append(random.randint(1, 50))


for n in numeros_aleatorios:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Lista completa:", numeros_aleatorios)
print("Lista de pares:", pares)
print("Lista de impares:", impares)