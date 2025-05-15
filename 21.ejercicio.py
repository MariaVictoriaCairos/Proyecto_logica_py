#21. Crea una función que calcule el cubo de un número dado mediante una función lambda

#entrada del valor
valor = input("introduce el número para calcular el cubo : ").strip()
#verifica que la cadena no esté vacía
if not valor:
    print("Error: No se ingresó ningún valor.")
    exit(1)
#verifica que el valor sea un número entero
try:
    valor = int(valor)
    #verifica que el valor sea mayor o igual a cero
    if valor < 0:
        print("Error: El número debe ser mayor o igual a cero.")
        exit(1)
    #función lambda en una línea para calcular el cubo
    cubo = (lambda x: x ** 3)(valor)
    # visualización del resultado
    print(f"El cubo del valor es: {cubo}")
except ValueError:
    print("Error: Asegúrate de ingresar un número entero válido.")
    exit(1)
