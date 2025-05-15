# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.

# función para determinar si las palabras son anagramas
def valora_anagrama(variable_1="", variable_2=""):
    """
    Determina si dos palabras son anagramas.
    Parámetros por defecto:
      - variable_1: "" si no se proporciona
      - variable_2: "" si no se proporciona
    """
    # Se verifica que las palabras no estén vacías
    # Se ponen en minusculas
    variable_1 = variable_1.lower()
    variable_2 = variable_2.lower()
    if len(variable_1) != len(variable_2):
        return None # Las palabras no son anagramas por no tener la misma longitud
    else:
        return sorted(variable_1) == sorted(variable_2)


# entrada de la variable 
try: 
    print("Introduce dos palabras separadas por comas que quieras valorar si son anagramas: ")
    entrada_1 = input("Introduce la primera palabra: ").strip()
    entrada_2 = input("Introduce la segunda palabra: ").strip()
    # Se verifica que la cadena no esté vacía   
    if not entrada_1 or not entrada_2:
        raise ValueError("debe introducir ambas palabras para valorar si son anagramas")

    #Visualización y llamada a la función
    resultado = valora_anagrama(entrada_1,entrada_2)
    if resultado is None:
        print("Las palabras no tienen el mismo tamaño, no son anagramas")
    elif resultado is True:
        print(f"las palabras {entrada_1} y la palabra {entrada_2} son  anagramas")
    else:
        print("Las palabras no son anagramas")
except ValueError as e:
    print(f"Error: {e}")