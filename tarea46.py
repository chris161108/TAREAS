def contar_vocales(frase: str) -> int:
	vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
	contador = 0
	for ch in frase:
		if ch in vocales:
			contador += 1
	return contador


if __name__ == '__main__':
	ejemplos = [
		'Hola Mundo',
		'Árbol',
		'¡Buenos días! ¿Cómo estás?',
		'',
		'XYZ'
	]
	for s in ejemplos:
		print(f'"{s}" -> {contar_vocales(s)}')

