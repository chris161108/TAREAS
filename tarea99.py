import math
import random

def sistema_navegacion():
    origen = (0, 0)
    destinos = [(random.randint(-20, 20), random.randint(-20, 20)) for _ in range(5)]
    
    rutas = {}
    distancias_unicas = set()
    
    for dest in destinos:
       
        distancia = math.hypot(dest[0] - origen[0], dest[1] - origen[1])
        dist_redondeada = round(distancia, 2)
        
        rutas[dest] = dist_redondeada
        distancias_unicas.add(dist_redondeada)
        
    return rutas, distancias_unicas

rutas_nav, dist_nav = sistema_navegacion()
print(f"9️⃣ Navegación -> Rutas: {rutas_nav}\n Distancias Únicas: {dist_nav}")