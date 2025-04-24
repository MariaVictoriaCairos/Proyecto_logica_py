# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def listar_tuplas(caracteres):
    caracteres_unicos = set(caracteres)
    resultado = list(map(lambda c: (c.upper(), c.lower()), caracteres_unicos))
    return resultado

# Solicitar entrada al usuario
entrada = input("Introduce un conjunto de caracteres: ")

try:
    Lista_MM = listar_tuplas(entrada)
    for tupla in Lista_MM:
        print(tupla)
except Exception as e:
    print(f"ocurrió un error: {e}")