# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

#importar función reduce()
from functools import reduce
#lista de numeros
numeros= [2,4,6]

#función para calcular la diferencia
diferencia_total = reduce(lambda x, y: x - y, numeros)

# Visualización del resultado
print(f"la diferencia total de la lista de números {numeros} es {diferencia_total}")

