# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas(lista1=None, lista2=None):
    """
    Devuelve una lista con la diferencia elemento a elemento de lista1 menos lista2.
    Parámetros por defecto:
      - lista1: [] (lista vacía)
      - lista2: [] (lista vacía)
    """
    if lista1 is None:
        lista1 = []
    if lista2 is None:
        lista2 = []

    # Normalizar y convertir con map + lambda
    try:
        nums1 = list(map(lambda x: int(str(x).strip()), lista1))
        nums2 = list(map(lambda x: int(str(x).strip()), lista2))
    except ValueError:
        raise ValueError("Todos los elementos deben ser números enteros.")

    # Verificar mismo tamaño
    if len(nums1) != len(nums2):
        raise ValueError("Las listas deben tener el mismo tamaño.")

    # Calcular diferencias usando map + lambda
    return list(map(lambda par: par[0] - par[1], zip(nums1, nums2)))


# --- Uso interactivo ---
print("Para calcular la diferencia, introduce ambas listas del mismo tamaño.")

# strip() en la entrada del usuario
entrada1 = input("Introduce la primera lista de números separados por coma: ").strip()
entrada2 = input("Introduce la segunda lista de números separados por coma: ").strip()

if not entrada1 or not entrada2:
    print("Error: Debes introducir ambas listas.")
else:
    lista1 = entrada1.split(",")
    lista2 = entrada2.split(",")

    try:
        resultado = diferencia_listas(lista1, lista2)
        print(f"La diferencia entre las dos listas es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")