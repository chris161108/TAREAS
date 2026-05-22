import math
import random

def optimizador_logistico():
    almacenes = {"Zona_A": {"limite": 50, "actual": 0},
                 "Zona_B": {"limite": 40, "actual": 0},
                 "Zona_C": {"limite": 60, "actual": 0}}
    
    zonas_nombres = list(almacenes.keys())
    desbordadas = set()
    
    for _ in range(10):
        zona = random.choice(zonas_nombres)
        carga = random.randint(10, 25)
        
        espacio_disponible = almacenes[zona]["limite"] - almacenes[zona]["actual"]
        
        if carga <= espacio_disponible:
            almacenes[zona]["actual"] += carga
        else:
            desbordadas.add(zona)
         
            sobrante = math.fmod(carga, espacio_disponible if espacio_disponible > 0 else 1)
           
            almacenes[zona]["actual"] = almacenes[zona]["limite"]
            
    return almacenes, desbordadas

estado_inv, desbordes = optimizador_logistico()
print(f"🔟 Logística -> Estado Final: {estado_inv}\n Desbordadas: {desbordes}")