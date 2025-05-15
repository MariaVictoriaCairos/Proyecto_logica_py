# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def lista_palabras(frase=""):
    """
    Devuelve una lista con la longitud de cada palabra en 'frase'.
    Parámetro por defecto:
      - frase: cadena vacía si no se proporciona
    """
    # Parámetro por defecto y normalización
    palabras= frase.split()
    longitudes = list(map(len, palabras))
    return longitudes

entrada = input("Introduce una frase:").strip()
if not entrada:
    print("No se ingresó ninguna frase.")
else:
    # Normalizar y parsear la entrada
    entrada = entrada.strip()
    # Llamada a la función
    longitudes = lista_palabras(entrada)
    print("la longitud de las palabras de tu frase son: ")
    for longitud in longitudes: 
        print(longitud)
    