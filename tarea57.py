def cifrado_cesar(texto: str, salto: int) -> str:
	"""Devuelve el texto cifrado con un desplazamiento `salto`.

	- Mantiene mayúsculas y minúsculas.
	- No altera espacios ni signos de puntuación.
	- Usa `isalpha()`, `ord()`, `chr()` y `% 26`.
	"""
	resultado = []
	for ch in texto:
		if ch.isalpha():
			if ch.isupper():
				base = ord('A')
			else:
				base = ord('a')
			nuevo = chr((ord(ch) - base + salto) % 26 + base)
			resultado.append(nuevo)
		else:
			resultado.append(ch)
	return ''.join(resultado)


if __name__ == "__main__":
	ejemplos = [
		("hola mundo", 3),
		("Abc, XYZ!", 4),
		("En un lugar de La Mancha.", 7),
	]
	for txt, s in ejemplos:
		print(f"Texto: {txt} | Salto: {s} -> {cifrado_cesar(txt, s)}")

