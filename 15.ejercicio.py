# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
def suma_lista(numeros):
    return list(map(lambda x: x+3, numeros))

# Lista de numeros
entrada= [1,5,3,7,5,9,2]
# llamada a la función
lista_mas3= suma_lista(entrada)

print(lista_mas3)