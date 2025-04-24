# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
# devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def filtrar_por_palabra(lista, objetivo):
    return [palabra for palabra in lista if objetivo in palabra]

palabras = ["ordenador", "ratón", "teclado", "portátil", "tablet", "multiport"]
objetivo = "or"

resultado = filtrar_por_palabra(palabras, objetivo)
print(resultado)
