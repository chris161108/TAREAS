"""
15. Gestor de Base de Datos de Combo Apple 🍏
Recibes un diccionario de usuarios y sus días de suscripción.
Clasifícalos en "Activos", "Por_Vencer" (< 5 días) y "Expirados" (<= 0).

Requerimientos: función que reciba un diccionario, usar `for ... in dict.items()`,
usar `if-elif-else` y retornar un diccionario con las tres categorías.
"""

from typing import Dict, List


def clasificar_suscriptores(suscriptores: Dict[str, int]) -> Dict[str, List[str]]:
    """Clasifica suscriptores según días restantes.

    - `Activos`: días >= 5
    - `Por_Vencer`: 1 <= días < 5
    - `Expirados`: días <= 0

    Usa un `for` con `.items()` y `if-elif-else`.
    """
    resultado = {"Activos": [], "Por_Vencer": [], "Expirados": []}

    for usuario, dias in suscriptores.items():
        if dias <= 0:
            resultado["Expirados"].append(usuario)
        elif dias < 5:
            resultado["Por_Vencer"].append(usuario)
        else:
            resultado["Activos"].append(usuario)

    return resultado


if __name__ == "__main__":
    ejemplo = {
        "ana": 10,
        "juan": 3,
        "maria": 0,
        "pedro": -1,
        "luisa": 5,
        "carlos": 4,
    }

    clasificacion = clasificar_suscriptores(ejemplo)
    print("Clasificación:")
    for categoria, usuarios in clasificacion.items():
        print(f"- {categoria}: {usuarios}")
