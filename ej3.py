#filtrado de positivos 

numeros = [1, -2, -3, 4, -5, -6]
positivos = []

for num in numeros:
    if num > 0:
        positivos.append(num)

print(positivos)