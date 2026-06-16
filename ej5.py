#adivina el numero

numero = 7
intento = 0

while intento != numero:
    intento = int(input("adivina un numero del 1 al 10"))
    if intento != numero:
       print("intenta otra vez ")
    
    print("felicidades, adivinaste.")

