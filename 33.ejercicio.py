# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

def agregar_elementos(lista=None, entrada=None):
    # Convierte la entrada en una lista, eliminando espacios
    elementos = [item.strip() for item in entrada.split(",")]
    return lista + elementos  # Devuelve una nueva lista combinada

try:
    # Entradas del usuario
    entrada_frutas = input("Introduzca las frutas que desea añadir a la lista separadas por comas: ").strip()
    entrada_verduras = input("Introduzca las verduras que desea añadir a la lista separadas por comas: ").strip()
    if not entrada_frutas and not entrada_verduras:
        raise ValueError("No se ingresaron frutas ni verduras.")
    if not entrada_frutas:
        raise ValueError("No se ingresaron frutas.")
    if not entrada_verduras:
        raise ValueError("No se ingresaron verduras.")
    
    # Listas originales
    frutas = ["mango", "plátano", "fresa"]
    verduras = ["cebolla", "ajo", "peregil"]

    # Aplicar la función
    nuevas_frutas = agregar_elementos(frutas, entrada_frutas)
    nuevas_verduras = agregar_elementos(verduras, entrada_verduras)

    # Imprimir resultados
    print(f"La lista de frutas es: {nuevas_frutas}")
    print(f"La lista de verduras es: {nuevas_verduras}")
except ValueError as e:
    print("Error: Asegúrate de introducir solo cadenas de texto válidas separadas por comas. ", e)