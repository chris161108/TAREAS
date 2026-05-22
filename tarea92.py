import random

def loteria_matematica(numeros_usuario):
 
    ganadores_temp = set()
    while len(ganadores_temp) < 3:
        ganadores_temp.add(random.randint(1, 20))
    tupla_ganadores = tuple(ganadores_temp)
    
    aciertos = set(numeros_usuario).intersection(tupla_ganadores)
    cantidad_aciertos = len(aciertos)
    
    premio_base = 5000
    if cantidad_aciertos == 3:
        premio = premio_base * 10
    elif cantidad_aciertos == 2:
        premio = premio_base * 2
    elif cantidad_aciertos == 1:
        premio = premio_base // 2
    else:
        premio = 0
        
    return f"Ganadores {tupla_ganadores} | Aciertos: {aciertos} | Premio: ${premio}"

print("2️⃣ Lotería:", loteria_matematica([5, 12, 18]))