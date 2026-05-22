import random


numero_secreto = random.randint(1, 10)
print("¡Adivina el número del 1 al 10! Tienes 3 intentos.")


for intento in range(3):
    jugada = int(input(f"Intento {intento + 1} - Ingresa tu número: "))
    
  
    if jugada == numero_secreto:
        print("¡Acertaste! Adivinaste el número.")
        break
    else:
        print("Fallaste.")
else:
   
    print(f"Te quedaste sin intentos. El número secreto era {numero_secreto}")