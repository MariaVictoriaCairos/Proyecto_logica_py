# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()

#importar función reduce()
from functools import reduce

# función que concatena los números de una lista
def Genera_numero(lista):
    return reduce(lambda x, y: x*10 + y, lista)

numeros= [2,5,3]

resultado = Genera_numero(numeros)
print(resultado)
