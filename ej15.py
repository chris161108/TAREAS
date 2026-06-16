#suma de matrices 

matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

resultado = [
    [0, 0, 0], 
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    for j in range(3):
        resultado[i][j] = matriz_a[i][j] + matriz_b[i][j]

print(resultado)