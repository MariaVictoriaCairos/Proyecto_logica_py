# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.
# Excepción personalizada

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.
# Excepción personalizada

class ListaVaciaError(Exception):
    pass

# Función para calcular el promedio
def calcular_promedio(numeros):
    if not numeros:
        raise ListaVaciaError("Error: la lista está vacía, no se puede calcular el promedio.")
    promedio = sum(numeros) / len(numeros)
    return promedio

# Solicitar entrada al usuario
entrada = input("Introduce una lista de números separados por comas (ej: 4, 5.5, 7, 2): ").strip()
if not entrada:
    print("Error: No se ingresó ningún valor.")
else:
    # Normalizar y convertir cada elemento a float
    try:
        # Convertir la entrada en una lista de números
        lista_numeros = [float(x.strip()) for x in entrada.split(",") if x.strip() != ""]

        # Calcular el promedio
        promedio = calcular_promedio(lista_numeros)
        print(f"Tu lista es: {lista_numeros} y el promedio es: {promedio:.2f}")

    except ValueError:
        print("Error: Asegúrate de ingresar solo números válidos separados por comas.")

    except ListaVaciaError as e:
        print(e)
