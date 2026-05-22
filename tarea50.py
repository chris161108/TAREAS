"""Tarea 50: Validador de Secuencias Numéricas

Función: generar_secuencia(inicio, fin, paso)
- Valida que `paso` no sea 0.
- Si `paso` es positivo, requiere `inicio <= fin`.
- Si `paso` es negativo, requiere `inicio >= fin`.
- Usa un `if` con operadores de comparación para validar, luego un `while`
  para generar la lista de valores.

Ejemplos de uso en la sección __main__.
"""

from typing import List


def generar_secuencia(inicio: int, fin: int, paso: int) -> List[int]:
    """Genera una lista de números desde `inicio` hasta `fin` usando `paso`.

    Validaciones iniciales:
    - `paso` no puede ser 0.
    - Si `paso` > 0 entonces `inicio` debe ser <= `fin`.
    - Si `paso` < 0 entonces `inicio` debe ser >= `fin`.

    La lista incluye tanto `inicio` como `fin` si se alcanza exactamente.
    """
    if paso == 0:
        raise ValueError("El paso no puede ser 0")

    # Validación lógica usando operadores de comparación
    if paso > 0:
        if inicio > fin:
            raise ValueError("Con paso positivo, 'inicio' debe ser <= 'fin'")
    else:  # paso < 0
        if inicio < fin:
            raise ValueError("Con paso negativo, 'inicio' debe ser >= 'fin'")

    resultado: List[int] = []
    actual = inicio

    if paso > 0:
        while actual <= fin:
            resultado.append(actual)
            actual += paso
    else:
        while actual >= fin:
            resultado.append(actual)
            actual += paso

    return resultado


if __name__ == "__main__":
    # Ejemplos de uso
    print("Ejemplo 1 (paso positivo):", generar_secuencia(1, 10, 2))
    print("Ejemplo 2 (paso negativo):", generar_secuencia(10, 0, -3))

    # Ejemplo de validación que lanza error
    try:
        generar_secuencia(5, 1, 2)
    except ValueError as e:
        print("Error esperado:", e)
