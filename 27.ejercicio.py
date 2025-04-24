# 27. Crea una función que calcule el promedio de una lista de números.

# función para calcular promedio
def promedio(lista):
    if not lista:
        return "La lista está vacia"
    return sum(lista)/len(lista)

# Lista de número introducida por el usuario
try:
    entrada = input("Introduce números separados por comas: ")
    lista = [float(x) for x in entrada.split(",")]
    #llamada a la función para calcular el promedio
    resultado = promedio(lista)

    print("El resultado de promedio de la lista es: ", resultado)
except ValueError:
    print("Error: solo se aceptan números")