# frecuencio de palabras 

parrafo = "python es un lenguaje de programacion"
palabras = parrafo.lower().split()
frecuencias = {}

for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra ] += 1
    else:
        frecuencias[palabra] = 1


print(frecuencias)