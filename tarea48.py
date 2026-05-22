def simular_fluctuaciones(pct_list, capital=1000.0):

	for pct in pct_list:
		capital *= (1 + pct)
		if capital < 500:
			break
	return capital


if __name__ == "__main__":
	
	porcentajes = [0.02, -0.15, 0.05, -0.4, 0.01]
	resultado = simular_fluctuaciones(porcentajes)
	print(f"Capital final: ${resultado:.2f}")

