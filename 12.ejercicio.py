# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def lista_palabras(frase):
    palabras= frase.split()
    longitudes = list(map(len, palabras))
    return longitudes

entrada = input("Introduce una frase:")
longitudes = lista_palabras(entrada)
print("la longitud de las palabras de tu frase son: ")
for longitud in longitudes: 
    print(longitud)
    