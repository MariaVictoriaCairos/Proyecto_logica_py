# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
# devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def filtrar_por_palabra(lista=None, objetivo=""):
    """
    Devuelve una lista con todas las palabras de 'lista' que contienen 'objetivo'.
    Parámetros por defecto:
      - lista: lista vacía si no se provee
      - objetivo: cadena vacía si no se provee
    """
    # Parámetros por defecto y normalización
    if lista is None:
        lista = []
    objetivo = objetivo.strip().lower()
    if not objetivo:
        return []
    # Filtrar palabras que contienen el objetivo
    return [palabra for palabra in lista if objetivo in palabra] # Filtrar palabras que contienen el objetivo

palabras = ["ordenador", "ratón", "teclado", "portátil", "tablet", "multiport"]
objetivo = "or"

resultado = filtrar_por_palabra(palabras, objetivo)
print(resultado)
