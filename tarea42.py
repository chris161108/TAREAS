def count_pass_fail(notas, minimo=10):

	aprobados = 0
	reprobados = 0
	for n in notas:
		if n >= minimo:
			aprobados += 1
		else:
			reprobados += 1
	return aprobados, reprobados


if __name__ == "__main__":
	ejemplo = [9, 10, 12, 7, 15, 10, 8, 20, 11, 5]
	apro, repro = count_pass_fail(ejemplo)
	print(f"Ejemplo notas: {ejemplo}")
	print(f"Aprobados: {apro}, Reprobados: {repro}")

