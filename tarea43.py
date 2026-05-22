def sum_pares(limite: int) -> int:

	if limite < 1:
		return 0

	total = 0
	for n in range(1, limite + 1):
		if n % 2 == 0:
			total += n
	return total


if __name__ == "__main__":
	try:
		entrada = input("Ingrese el límite (entero positivo): ")
		limite = int(entrada)
	except ValueError:
		print("Entrada inválida. Por favor ingrese un número entero.")
	else:
		resultado = sum_pares(limite)
		print(f"Suma de pares entre 1 y {limite}: {resultado}")

