# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce()

#importar función reduce()
from functools import reduce
#lista de valores
valores= [2,3,2]
#calculo del producto total
Producto_total = reduce(lambda x, y: x * y, valores)
#Visualización del resultado
print(f"El produto total de los valores es: {Producto_total}")
