# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.

# función para enmascarar texto
def transformar(variable):
    longitud = len(variable)
    if longitud <= 4:
        return None # No hay nada que enmascarar
    else:
        return '#' * (longitud - 4) + variable[-4:]


# entrada de la variable 
entrada = input("Introduce un valor o caracteres que quieras enmascarar con #: ")

#Vusualización y llamada a la función
resultado = transformar(entrada)
if resultado is None:
    print("No hay caracteres que enmascarar, la variable tiene una longitud menor de 4")
else:
    print("Se presentan los caracteres enmascarados con '#' a excepción de los cuatro últimos: ", resultado)
