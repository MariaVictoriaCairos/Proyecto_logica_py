# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

# función para buscar duplicado
def duplicado (lista):
    elementos_vistos = set()
    for elemento in lista:
        if elemento in elementos_vistos:
            return elemento
        elementos_vistos.add(elemento)
    return None

try:
    # Lista de número introducida por el usuario
    entrada = input("Introduce números separados por comas: ")
    lista = [float(x) for x in entrada.split(",")]
    
    #llamada a la función para duscar el primer duplicado
    resultado = duplicado(lista)

    print("El primer elemento duplicado de la lista es: ", resultado)
except ValueError:
    print("Error: solo se aceptan números")