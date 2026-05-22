import random

def cifrado_numerico(lista_numeros):
    clave = random.randint(1, 10)
    diccionario_cifrado = {}
    valores_unicos = set()
    
    for num in lista_numeros:
        if num % 2 == 0:
            cifrado = num + clave
        else:
            cifrado = num - clave
            
        diccionario_cifrado[num] = cifrado
        valores_unicos.add(cifrado)
        
    return (clave, valores_unicos), diccionario_cifrado

tupla_datos, dict_cifras = cifrado_numerico([10, 15, 20, 25, 30])
print(f"5️⃣ Cifrado -> Datos (Clave, Únicos): {tupla_datos} | Mapeo: {dict_cifras}")