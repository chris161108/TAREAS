def calcular_total_suscripcion(precio_mensual, meses):
    total = precio_mensual * meses
    if meses >= 6:
        total *= 0.85  
    return total


precio_ingresado = float(input("Introduce el precio mensual: "))
meses_ingresados = int(input("Introduce la cantidad de meses: "))


total_final = calcular_total_suscripcion(precio_ingresado, meses_ingresados)
print(f"El total a pagar es: {total_final}")
