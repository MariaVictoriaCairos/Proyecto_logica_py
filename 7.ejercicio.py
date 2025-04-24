## 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def mi_string(lista):
    return list(map(lambda tupla: " ".join(map(str, tupla)), lista))

# lista de tuplas
mi_lista = [(1, 3), (6, 2), (6, 8)]
# llamada ala función que los convierte
mi_caracter = mi_string(mi_lista)

print(f"Mi lista de tuplas es {mi_lista} al transformarlo en una lista de string, el resultado es {mi_caracter}")
 