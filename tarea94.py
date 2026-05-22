import math
import random

def geometria_particulas():
    radios = [random.randint(1, 15) for _ in range(10)]
    resultados = {}
    areas_unicas = set()
    
    for i in range(len(radios)):
        radio = radios[i]
        area = math.pi * (radio ** 2)
        resultados[i] = (radio, round(area, 2))
        areas_unicas.add(round(area, 2))
        
    return resultados, areas_unicas

res_particulas, areas_set = geometria_particulas()
print(f"4️⃣ Partículas -> Resultados: {res_particulas}\n Áreas únicas: {areas_set}")