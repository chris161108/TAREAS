def factorial_iterativo(n):
	"""Calcula el factorial de n de forma iterativa.
	Devuelve None si n es negativo.
	"""
	if n < 0:
		return None
	resultado = 1
	i = 1
	while i <= n:
		resultado *= i
		i += 1
	return resultado


if __name__ == "__main__":
	try:
		entrada = input("Ingrese un número entero no negativo: ")
		numero = int(entrada)
	except ValueError:
		print("Entrada inválida: debe ingresar un entero.")
	else:
		if numero < 0:
			print("No se puede calcular el factorial de un número negativo.")
		else:
			print(f"El factorial de {numero} es {factorial_iterativo(numero)}")

