#clasificador por edad 

personas = [("cris", 15), ("carlos", 25), ("andres", 88), ("laura", 40)]

for nombre, edad in personas:
    if edad < 18:
        clasificacion = "menor"
    elif edad < 65:
        clasificacion = "adulto"
    else:
        clasificacion = "mayor"

    print(nombre, "-", clasificacion)
    