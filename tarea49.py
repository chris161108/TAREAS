from typing import List


def rastreador_frases(dialogos: List[str]) -> List[str]:
	resultados: List[str] = []
	for oracion in dialogos:
		if "valar morghulis" in oracion.lower():
			resultados.append(oracion)
	return resultados


if __name__ == "__main__":
	ejemplos = [
		"Valar Morghulis",
		"valar morghulis",
		"¡VALAR MORGHULIS!",
		"No es la frase",
		"Un saludo: Valar Morghulis, hermano",
		"valAr Morghulis en medio de la frase",
	]

	encontrados = rastreador_frases(ejemplos)
	print("Frases encontradas:")
	for f in encontrados:
		print("-", f)

