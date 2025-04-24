# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

# la lista de numeros la escribe el usuario
numeros_usuario = input("Introduce la lista de numeros separados por una coma: ")
val_numeros = numeros_usuario.split(",")                    # convierte el input en una lista
if all(numero.strip().isdigit() for numero in val_numeros): # Valida que son números
    numeros = map(int, numeros_usuario.split(","))          # Transforma el input en una lista que separa por la coma
    dobles = list(map(lambda x: x * 2, numeros))            # itera y los duplica

    print(f"El doble de los números que has introducido son {dobles}") 
else:
    print("Los numeros que has introducido no son correctos")