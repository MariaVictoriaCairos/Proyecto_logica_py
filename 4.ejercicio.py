# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas(lista1, lista2):
    return list(map(lambda a_b: a_b[0] - a_b[1], zip(lista1, lista2)))


print("Para calcular la diferencia debes introducir ambas listas del mismo tamaño")
Numeros_1 = input("Introduce la primera lista de numeros separados por una coma: ")
Lista_1 = Numeros_1.split(",")                    # convierte el input en una lista
Numeros_2 = input("Introduce la segunda lista de numeros separados por una coma: ")
Lista_2 = Numeros_2.split(",")                    # convierte el input en una lista

if all(numero_1.strip().isdigit() for numero_1 in Lista_1) and all(numero_2.strip().isdigit() for numero_2 in Lista_2):
    if len(Lista_1) == len(Lista_2):    
        
        Lista_1 = list(map(int, map(str.strip, Lista_1)))       # Convertir los elementos de la lista a enteros
        Lista_2 = list(map(int, map(str.strip, Lista_2)))
        
        Calculo= diferencia_listas(Lista_1,Lista_2)
        print(f"La diferencia entre las dos listas es: {Calculo}")
    else:
        print("las listas deben tener el mismo tamaño")
else:
    print("error, introdujo caracteres. solo se pueden calcular diferencia de números")
