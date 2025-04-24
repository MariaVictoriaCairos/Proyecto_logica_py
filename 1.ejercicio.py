# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.


def contar_frecuencias(cadena):
    frecuencias = {}
    for letra in cadena:
        if letra != ' ':
            letra = letra.lower()  # Para contar sin distinguir mayúsculas
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias
texto= input("Introduzca un texto:")  
frecuencia = contar_frecuencias(texto)
for letra, frecuencia in frecuencia.items(): # Se imprime en vertical por letra de la cadena
    print(f"{letra}: {frecuencia}")