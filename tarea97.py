import math
import random

def motor_batalla():
    jugador = {"hp": 100, "defensa": 10}
    enemigo = {"hp": 100, "defensa": 8}
    historial = []
    
    while jugador["hp"] > 0 and enemigo["hp"] > 0:
        # Daño del jugador al enemigo
        dano_base_j = random.randint(15, 30)
        mitigacion_e = math.ceil(enemigo["defensa"] / 2)
        dano_final_j = max(1, dano_base_j - mitigacion_e)
        enemigo["hp"] -= dano_final_j
        historial.append(f"Jugador ataca con {dano_final_j} pts.")
        
        if enemigo["hp"] <= 0: break
        
        # Daño del enemigo al jugador
        dano_base_e = random.randint(15, 30)
        mitigacion_j = math.ceil(jugador["defensa"] / 2)
        dano_final_e = max(1, dano_base_e - mitigacion_j)
        jugador["hp"] -= dano_final_e
        historial.append(f"Enemigo ataca con {dano_final_e} pts.")
        
    ganador = "Jugador" if jugador["hp"] > 0 else "Enemigo"
    return (ganador, historial)

ganador_rpg, log_rpg = motor_batalla()
print(f"7️⃣ RPG -> Ganador: {ganador_rpg} | Turnos jugados: {len(log_rpg)}")