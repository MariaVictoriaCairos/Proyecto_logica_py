# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

#importar función reduce()
from functools import reduce

# entrada de los valores por el usuario
valores_usuario = input("Introduce la lista de numeros separados por una coma: ").strip()
# Se eliminan los espacios en blanco al inicio y al final de la cadena
# Se verifica que la cadena no esté vacía
if not valores_usuario:
    print("La lista de numeros está vacia.")
else:
    val_numeros = valores_usuario.split(",")
    # Valida que son números
    if all(numero.strip().isdigit() for numero in val_numeros):
        # convierte la lista de cadenas a una lista de enteros
        numeros = list(map(int, val_numeros))
        #función para calcular la diferencia
        diferencia_total = reduce(lambda x, y: x - y, numeros)
        # Visualización del resultado
        print(f"la diferencia total de la lista de números {numeros} es {diferencia_total}")        

