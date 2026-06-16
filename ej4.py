# contador de vocales 

texto = input(" ingrese un texto")
contador_de_vocales = 0
vocales = "aeiouAEIOU"

for letra in texto:
    if letra in vocales:
        contador_de_vocales += 1

print(f"el numero de las vocales en el texto es : {contador_de_vocales}")