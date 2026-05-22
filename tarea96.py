import math
import random

def analisis_estaciones():
    estaciones = {
        "Norte": tuple(random.randint(-5, 45) for _ in range(5)),
        "Sur": tuple(random.randint(-5, 45) for _ in range(5))
    }
    
    promedios = {}
    anomalias = set()
    
    for estacion, temps in estaciones.items():
        suma = 0
        for t in temps:
            suma += t
            if t < 0 or t > 40:
                anomalias.add(t)
        
        promedios[estacion] = math.floor(suma / len(temps))
        
    return promedios, anomalias

proms, anom = analisis_estaciones()
print(f"6️⃣ Clima -> Promedios: {proms} | Anomalías: {anom}")