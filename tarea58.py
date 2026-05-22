#!/usr/bin/env python3
"""
Simulador Lógico de Batalla

Función: `simulate_battle(attacker, defender, verbose=True)`
Recibe dos diccionarios con al menos las claves `HP` y `ATK` (o `hp`/`atk`).
Opcional: `NAME` o `name` para mostrar nombres.

La función simula turnos alternos hasta que uno cae y devuelve el nombre
del ganador o la cadena 'Empate' si ambos caen.
"""

from copy import deepcopy


def simulate_battle(p1: dict, p2: dict, verbose: bool = True) -> str:
	a = deepcopy(p1)
	b = deepcopy(p2)

	name_a = a.get('NAME') or a.get('name') or 'A'
	name_b = b.get('NAME') or b.get('name') or 'B'

	hp_a = a.get('HP', a.get('hp', 0))
	hp_b = b.get('HP', b.get('hp', 0))
	atk_a = a.get('ATK', a.get('atk', 0))
	atk_b = b.get('ATK', b.get('atk', 0))

	if verbose:
		print(f"Comienza la batalla: {name_a} (HP={hp_a}, ATK={atk_a}) vs {name_b} (HP={hp_b}, ATK={atk_b})")

	turn = 0
	while hp_a > 0 and hp_b > 0:
		if turn % 2 == 0:
			# p1 ataca a p2
			hp_b -= atk_a
			if verbose:
				print(f"Turno {turn+1}: {name_a} ataca a {name_b} -> -{atk_a} HP (restan {max(hp_b,0)})")
		else:
			# p2 ataca a p1
			hp_a -= atk_b
			if verbose:
				print(f"Turno {turn+1}: {name_b} ataca a {name_a} -> -{atk_b} HP (restan {max(hp_a,0)})")
		turn += 1

	if hp_a <= 0 and hp_b <= 0:
		if verbose:
			print("Resultado: Empate. Ambos han caído.")
		return 'Empate'
	winner = name_a if hp_b <= 0 else name_b
	if verbose:
		print(f"Resultado: {winner} gana en {turn} turnos.")
	return winner


if __name__ == '__main__':
	# Ejemplo simple
	guerrero = {'NAME': 'Guerrero', 'HP': 30, 'ATK': 7}
	dragon = {'NAME': 'Dragón', 'HP': 50, 'ATK': 5}
	simulate_battle(guerrero, dragon)

