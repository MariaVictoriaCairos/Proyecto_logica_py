# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.

# función para determinar si las palabras son anagramas
def valora_anagrama(variable_1, variable_2):
    # Se ponen en minusculas
    variable_1 = variable_1.lower()
    variable_2 = variable_2.lower()
    if len(variable_1) != len(variable_2):
        return None # Las palabras no son anagramas por no tener la misma longitud
    else:
        return sorted(variable_1) == sorted(variable_2)


# entrada de la variable 
print("Introduce dos palabras separadas por comas que quieras valorar si son anagramas: ")
entrada_1 = input("Introduce la primera palabra: ")
entrada_2 = input("Introduce la segunda palabra: ")

#Visualización y llamada a la función
resultado = valora_anagrama(entrada_1,entrada_2)
if resultado is None:
    print("Las palabras no son anagramas, no tienen el mismo tamaño")
elif resultado is True:
    print(f"las palabras {entrada_1} y la palabra {entrada_2} son  anagramas")
else:
    print("Las palabras no son anagramas")