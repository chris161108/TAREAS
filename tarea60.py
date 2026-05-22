def optimizador_billetes(monto, denominaciones):
    print(f"Monto a entregar: ${monto}")
    print("-" * 25)
    
    
    for billete in denominaciones:
   
        cantidad = monto // billete
        
        # Si la cantidad es mayor a 0, significa que necesitamos de este billete
        if cantidad > 0:
            print(f"- {cantidad} billete(s) de ${billete}")
        
     
        monto = monto % billete
        
    # Si al final el monto no es 0, significa que faltan billetes o monedas más pequeñas
    if monto > 0:
        print(f"No se pueden entregar ${monto} con las denominaciones dadas.")
    print("-" * 25)


lista_billetes = [20000, 10000, 5000, 2000, 1000]

# Montos de prueba
optimizador_billetes(47000, lista_billetes)
optimizador_billetes(18500, lista_billetes) # En este sobrarán 500