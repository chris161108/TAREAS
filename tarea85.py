def analizar_numeros(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division_entera = num1 // num2

    return (suma, resta, multiplicacion, division_entera)


res_suma, res_resta, res_mult, res_div = analizar_numeros(20, 3)

print("Suma:", res_suma)
print("Resta:", res_resta)
print("Multiplicación:", res_mult)
print("División Entera:", res_div)