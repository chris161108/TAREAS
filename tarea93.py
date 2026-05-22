import math
import random

def procesador_precios():
    productos = ("Laptop", "Mouse", "Monitor", "Teclado", "Audífonos")
    catalogo = {prod: random.randint(30, 120) for prod in productos}
    precios_finales = set()
    
    for producto, precio in catalogo.items():
        if precio > 50:
            precio += precio * 0.15 # Impuesto del 15%
        
        precio_final = math.ceil(precio)
        catalogo[producto] = precio_final
        precios_finales.add(precio_final)
        
    return catalogo, precios_finales

cat, prec_unicos = procesador_precios()
print(f"3️⃣ Precios -> Catálogo: {cat} | Precios Únicos: {prec_unicos}")