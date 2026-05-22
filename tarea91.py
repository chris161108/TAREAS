import math
import random

def analisis_muestras(n):
  
    lista_numeros = [random.randint(1, 100) for _ in range(n)]
    
 
    conjunto_unicos = set(lista_numeros)
    

    maximo_valor = max(conjunto_unicos)
    raiz = math.sqrt(maximo_valor)
    
    return {
        "lista_original": lista_numeros,
        "conjunto": conjunto_unicos,
        "raiz_del_maximo": round(raiz, 2)
    }

print("1️⃣ Muestras:", analisis_muestras(10))