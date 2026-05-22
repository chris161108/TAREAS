# Inventario inicial
inventario = {
    "laptops": 5,
    "mouses": 15,
    "teclados": 8
}

print("Inventario inicial:", inventario)


while True:
    venta = input("\n¿Qué producto quieres vender? (Escribe 'salir' para terminar): ")
    
    if venta == "salir":
        print("Saliendo del simulador de inventario...")
        break
    elif venta in inventario:
        cantidad = int(input("¿Cuántas unidades deseas vender?: "))
        
      
        if inventario[venta] >= cantidad:
            
            inventario[venta] -= cantidad
            print(f"Venta realizada. Stock restante de {venta}: {inventario[venta]}")
        else:
            print(f"No hay suficiente stock. Solo quedan {inventario[venta]} unidades.")
    else:
        print("El producto ingresado no existe en el inventario.")