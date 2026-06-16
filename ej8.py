#interseccion de datos 

lista_a = [1, 2, 2 ,3 ,4, 5]
lista_b = [3, 4, 5, 5, 6, 7]

set_a = set(lista_a)
set_b = set(lista_b)
comunes = list(set_a & set_b)

print("elementos comunes sin duplicados")
print(comunes)