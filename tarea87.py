# Diccionario con tres estudiantes y sus listas de notas
estudiantes = {
    "Ana": [15, 18, 16],
    "Carlos": [10, 12, 11],
    "Luis": [20, 19, 18]
}


for nombre, notas in estudiantes.items():
    
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {round(promedio, 2)}")