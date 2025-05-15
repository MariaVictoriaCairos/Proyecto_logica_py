# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

# la lista de numeros la escribe el usuario
numeros_usuario = input("Introduce la lista de numeros separados por una coma: ").strip()
# Se pide al usuario que introduzca una lista de números separados por comas
# Se eliminan los espacios en blanco al inicio y al final de la cadena
# Se verifica que la cadena no esté vacía
if not numeros_usuario:
    print("La lista de numeros está vacia.")
else:
    numeros_usuario = numeros_usuario.strip()                   # Se eliminan los espacios en blanco al inicio y al final de la cadena
    val_numeros = [x.strip() for x in numeros_usuario.split(",")] # convierte el input en una lista eliminando los espacios
    if all(numero.isdigit() for numero in val_numeros): # Valida que son números
        numeros = map(int, numeros_usuario.split(","))          # Transforma el input en una lista que separa por la coma
        dobles = list(map(lambda x: x * 2, numeros))            # itera y los duplica

        print(f"El doble de los números que has introducido son {dobles}") 
    else:
        print("Los numeros que has introducido no son correctos")
