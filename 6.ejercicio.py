# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial_recursivo(numero=0):
    """
    Calcula el factorial de un número de forma recursiva.
    Parámetro por defecto: numero=0
    """
    if numero < 0:
        raise ValueError("El número debe ser mayor o igual a cero.")
    if numero in (0, 1):
        return 1
    return numero * factorial_recursivo(numero - 1)

# entrada del usuario
print("Para calcular el factorial de un número, introduce un número entero positivo.")
# strip() en la entrada del usuario para eliminar espacios en blanco
entrada = input("Introduce un número entero para calcular su factorial: ").strip()
# Se verifica que la cadena no esté vacía
if not entrada:
    print("Error: No se ingresó ningún valor.")
else:
    try:
        numero_usuario = int(entrada)
        total = factorial_recursivo(numero_usuario)
        print(f"El factorial de {numero_usuario} calculado de forma recursiva es: {total}")
    except ValueError as e:
        print(f"Error: {e}")