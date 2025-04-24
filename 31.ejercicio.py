# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.

# función busqueda de nombre en una lista
def Buscar_nombre ():
    
    try: 
        # Entrada de lista de nombre y nombre a buscar
        entrada = input("Introcuce una lista de nombre separados por comas :").upper()
        Nombre_buscar= input("introduce el nombre que deseas buscar : ").strip().upper()
        
        #transforma la entrada en una lista sin espacion y separando por comas
        lista_nombre = [nombre.strip() for nombre in entrada.split(",")]

        # Busqueda del nombre en la lista
        if Nombre_buscar in lista_nombre:
            print(f"El nombre {Nombre_buscar} está en la Lista")
        else:
            raise ValueError(f"El nombre '{Nombre_buscar}' no fue encontrado en la lista.")
    
    except ValueError as e:
        # error en la entrada de datos
        print("Error:", e)


# Llamada a la función
Buscar_nombre()
