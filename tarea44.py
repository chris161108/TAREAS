def validar_contrasena(texto):
	if len(texto) > 8 and '@' in texto:
		return True
	return False


if __name__ == "__main__":
	texto = input("Introduce la contraseña: ")
	print(f"{texto!r}: {validar_contrasena(texto)}")

