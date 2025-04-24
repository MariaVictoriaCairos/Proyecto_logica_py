#21. Crea una función que calcule el cubo de un número dado mediante una función lambda

#entrada del valor
valor = input("introduce el número para calcular el cubo : ")
valor = int(valor)

#función lambda en una línea para calcular el cubo
cubo = (lambda x: x ** 3)(valor)

# visualización del resultado
print(f"El cubo del valor es: {cubo}")