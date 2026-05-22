def analizar_palabras(lista1, lista2):
  
    set1 = set(lista1)
    set2 = set(lista2)

    en_ambas = set1 & set2
    
    exclusivas_primera = set1 - set2
    
    print("Palabras en ambas listas:", en_ambas)
    print("Palabras exclusivas de la primera lista:", exclusivas_primera)


palabras_a = ["python", "codigo", "computadora", "teclado"]
palabras_b = ["raton", "codigo", "pantalla", "python"]

analizar_palabras(palabras_a, palabras_b)