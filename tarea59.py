def rle_compress(text: str) -> str:
	"""Comprime la cadena usando Run-Length Encoding.

	Ejemplo: 'AABBC' -> 'A2B2C1'
	"""
	if not text:
		return ""

	resultado = []
	anterior = text[0]
	contador = 1

	for caracter in text[1:]:
		if caracter == anterior:
			contador += 1
		else:
			resultado.append(f"{anterior}{contador}")
			anterior = caracter
			contador = 1

	# añadir el último grupo
	resultado.append(f"{anterior}{contador}")
	return "".join(resultado)


if __name__ == "__main__":
	ejemplos = ["AABBC", "AAAA", "", "ABAB", "aaAA"]
	print("Ejemplos de compresión RLE:")
	for ex in ejemplos:
		print(f"{ex} -> {rle_compress(ex)}")

	entrada = input("\nIntroduce un texto a comprimir (Enter para salir): ")
	if entrada:
		print("Resultado:", rle_compress(entrada))

