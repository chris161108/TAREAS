"""Implementación del algoritmo de Luhn (validación de tarjetas).

Requerimientos cumplidos:
- Función que recibe un `str` numérico.
- Bucle en reversa y condicionales para duplicar pares.
- Operadores para restar y sumar según la regla de Luhn.

Ejemplo de uso:
>>> validar_luhn('4532015112830366')  # True (Visa de ejemplo)
>>> validar_luhn('1234567812345670')  # True (número con check correcto)
"""

from typing import Optional


def validar_luhn(numero: str) -> bool:
	"""Valida `numero` usando el algoritmo de Luhn.

	Args:
		numero: cadena que contiene sólo dígitos (puede incluir espacios, se ignoran).

	Returns:
		True si el número pasa la comprobación de Luhn, False en caso contrario.

	Lanza ValueError si la cadena no contiene dígitos después de limpiar espacios.
	"""
	if not isinstance(numero, str):
		raise TypeError('Se esperaba un string con dígitos.')

	# Eliminar espacios en blanco comunes
	s = numero.replace(' ', '')

	if not s.isdigit() or len(s) == 0:
		raise ValueError('La entrada debe ser una cadena numérica con al menos un dígito.')

	total = 0
	# Recorremos los dígitos desde la derecha usando enumerate
	for i, ch in enumerate(reversed(s)):
		digit = int(ch)
		# Duplicar cada segundo dígito (i=1,3,5...) según Luhn
		if i % 2 == 1:
			digit *= 2
			# Si el resultado es mayor que 9, restar 9 (equivalente a sumar los dígitos)
			if digit > 9:
				digit -= 9
		total += digit

	return total % 10 == 0


def probar_ejemplos() -> None:
	ejemplos = [
		'4532015112830366',  # Visa de ejemplo
		'49927398716',       # ejemplo clásico (valido)
		'1234567812345670',  # válido
		'1234567812345678',  # no válido
	]

	for n in ejemplos:
		print(f"{n}: {'válida' if validar_luhn(n) else 'inválida'}")


if __name__ == '__main__':
	# Si se ejecuta directamente, mostrar pruebas y permitir entrada rápida
	print('Pruebas de Luhn:')
	probar_ejemplos()

	# Lectura interactiva opcional
	try:
		entrada: Optional[str] = input('\nIntroduce un número de tarjeta (o pulsa Enter para salir): ').strip()
	except (EOFError, KeyboardInterrupt):
		entrada = None

	if entrada:
		try:
			es_valida = validar_luhn(entrada)
		except Exception as e:
			print('Entrada no válida:', e)
		else:
			print('Resultado:', 'válida' if es_valida else 'inválida')

