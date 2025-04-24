# 23. Concatena una lista de palabras.Usa la función reduce().

#importar función reduce()
from functools import reduce
# Lista de palabras
palabras= ["Mi", "profesión", "favorita", "es", "ingeniería", "en", "informática"]
# Función de unir palabras
mensaje= reduce(lambda x, y : x + " " + y, palabras)
# Visualización del mensaje
print(mensaje)