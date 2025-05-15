# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.


def contar_frecuencias(cadena):
    frecuencias = {}
    # Se eliminan los espacios en blanco al inicio y al final de la cadena
    cadena = cadena.strip()
    # Se verifica que la cadena no esté vacía
    if not cadena:
        print("No se ingresó texto válido.")
        return {}
    for letra in cadena:
        if letra != ' ':
            letra = letra.lower()  # Para contar sin distinguir mayúsculas
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias
texto= input("Introduzca un texto:").strip() # Se pide al usuario que introduzca un texto
# Se llama a la función contar_frecuencias y se imprime el resultado
frecuencia = contar_frecuencias(texto)
if frecuencia:
    print("Frecuencia de letras:")  
    # Se imprime en vertical por letra de la cadena
    for letra, frecuencia in frecuencia.items(): # Se imprime en vertical por letra de la cadena
        print(f"{letra}: {frecuencia}")