# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()

#importar función reduce()
from functools import reduce

# función que concatena los números de una lista
def Genera_numero(lista=None):
    """
    Genera un número a partir de una lista de dígitos.
    Parámetro por defecto:
      - lista: [] (lista vacía) si no se proporciona
    """
    if lista is None:
        lista = []
    # Verificar si la lista está vacía
    if not lista:
        return 0
    # Verificar si la lista contiene solo dígitos
    if not all(isinstance(i, int) and 0 <= i <= 9 for i in lista):
        raise ValueError("La lista debe contener solo dígitos (0-9).")
    # Usar reduce para concatenar los dígitos
    # multiplicando por 10 y sumando el siguiente dígito
    # reduce(lambda x, y: x*10 + y, lista) genera el número
    # correspondiente a la lista de dígitos
    return reduce(lambda x, y: x*10 + y, lista)

# Solicitar entrada al usuario
entrada = input("Introduce una lista de números separados por comas (ej: 5,7,2): ").strip()
if not entrada:
    print("Error: No se ingresó ningún valor.")
else:
    # Normalizar y convertir cada elemento a int
    try:
        # Convertir la entrada en una lista de números
        lista_numeros = [int(x.strip()) for x in entrada.split(",") if x.strip() != ""]
        
        # Llamar a la función Genera_numero
        resultado = Genera_numero(lista_numeros)
        print(f"Tu lista es: {lista_numeros} y el número correspondiente es: {resultado}")

    except ValueError:
        print("Error: Asegúrate de ingresar solo números válidos separados por comas.")
