# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce()

#importar función reduce()
# la función reduce es parte del módulo functools y se utiliza para aplicar una función de manera acumulativa a los elementos de un iterable, como una lista.
# reduce toma dos argumentos: una función y un iterable. La función se aplica a los elementos del iterable de manera acumulativa, reduciendo el iterable a un solo valor.
# En este caso, se utiliza para calcular el producto total de los valores en la lista.
from functools import reduce

# entrada de los valores por el usuario
valores_usuario = input("Introduce la lista de numeros separados por una coma: ").strip()
# Se eliminan los espacios en blanco al inicio y al final de la cadena
# Se verifica que la cadena no esté vacía
if not valores_usuario:
    print("La lista de numeros está vacia.")
else:
    
    val_numeros = valores_usuario.split(",") # convierte el input en una lista
    # Valida que son números
    if all(numero.strip().isdigit() for numero in val_numeros): # verifica si todos los elementos de la lista son dígitos
        # convierte la lista de cadenas a una lista de enteros
        val_numeros = list(map(int, val_numeros)) # convierte la lista de cadenas a una lista de enteros
        #calculo del producto total
        Producto_total = reduce(lambda x, y: x * y, val_numeros) 
        # reduce(lambda x, y: x * y, val_numeros) calcula el producto total de los valores en la lista
        print(f"El produto total de los valores es: {Producto_total}")
    else:
        print("Los numeros que has introducido no son correctos")
        exit(1)
    
    
