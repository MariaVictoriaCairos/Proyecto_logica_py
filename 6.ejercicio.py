# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial_recursivo(numero):
    """
    Calcula el factorial de un número de forma recursiva.
    """
    if numero < 0:
        raise ValueError("El número debe ser mayor o igual a cero.")
    elif numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial_recursivo(numero - 1)

# Solicitar un número entero al usuario con validación
entrada = input("Introduce un número entero para calcular su factorial: ")

if entrada.isdigit():  # Solo acepta enteros positivos
    numero_usuario = int(entrada)
    try:
        total = factorial_recursivo(numero_usuario)
        print(f"El factorial de {numero_usuario} calculado de forma recursiva es: {total}")
    except ValueError as e:
        print(f"Error: {e}")
else:
    print("Error: Debes introducir un número entero positivo.")