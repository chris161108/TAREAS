#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def tabulador_multiplicador(base, limite):
	"""Imprime la tabla de multiplicar de `base` hasta `limite`, saltando resultados impares."""
	for i in range(1, limite + 1):
		resultado = base * i
		if resultado % 2 != 0:
			continue
		print(f"{base} x {i} = {resultado}")


if __name__ == "__main__":
	try:
		b = int(input("Base: "))
		l = int(input("Límite: "))
	except ValueError:
		print("Entrada inválida. Usa números enteros.")
	else:
		tabulador_multiplicador(b, l)
