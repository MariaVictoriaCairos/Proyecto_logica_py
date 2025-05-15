# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
def suma_lista(numeros=None):
    """
    Suma 3 a cada número de la lista.
    Parámetro por defecto:
      - numeros: [] si no se proporciona
    """
    if numeros is None:
        numeros = []
    return list(map(lambda x: x + 3, numeros))

# --- Entrada por el usuario ---
entrada = input("Introduce una lista de números separados por comas: ").strip()
if not entrada:
    print("Error: No se ingresaron números.")
else:
    try:
        # Normalizar y convertir a int
        lista = [int(x.strip()) for x in entrada.split(",") if x.strip()]
        resultado = suma_lista(lista)
        print(f"Lista original: {lista}")
        print(f"Lista con cada elemento +3: {resultado}")
    except ValueError:
        print("Error: Asegúrate de introducir solo números enteros válidos separados por comas.")
