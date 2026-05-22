def convertir_y_filtrar_masas(masas_gramos: list[float]) -> list[float]:

	resultado: list[float] = []
	for masa in masas_gramos:
		kg = masa / 1000.0
		if kg >= 0.585:
			resultado.append(kg)
	return resultado


if __name__ == "__main__":
	ejemplo = [100, 585, 600, 1000, 584.9, 700]
	# Notar: los valores en `ejemplo` están en gramos
	filtradas = convertir_y_filtrar_masas(ejemplo)
	print("Entrada (g):", ejemplo)
	print("Salida (kg) >= 0.585:", filtradas)

