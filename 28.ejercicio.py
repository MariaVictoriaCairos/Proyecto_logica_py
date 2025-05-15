# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

# función para buscar duplicado
def duplicado (lista=None):
    """
    Busca el primer elemento duplicado en una lista.
    Parámetro por defecto:
      - lista: [] si no se proporciona
    """
    if lista is None:
        lista = []
    # Se inicializa un conjunto para almacenar los elementos vistos
    # y se itera sobre la lista
    elementos_vistos = set() # Conjunto para almacenar elementos únicos
    # Iterar sobre la lista
    # y verificar si el elemento ya ha sido visto
    # Si es así, se devuelve el elemento duplicado
    # Si no se encuentra duplicado, se devuelve None
    for elemento in lista:
        if elemento in elementos_vistos:
            return elemento
        elementos_vistos.add(elemento)
    return None

try:
    entrada = input("Introduce números separados por comas: ").strip()
    if not entrada:
        raise ValueError("La lista está vacía.")
    
    # Normalizar y convertir
    lista = [float(x.strip()) for x in entrada.split(",") if x.strip()]
    
    resultado = duplicado(lista)
    if resultado is None:
        print("No hay elementos duplicados en la lista.")
    else:
        print(f"El primer elemento duplicado de la lista es: {resultado}")

except ValueError as e:
    print(f"Error: {e}")