# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.

# función busqueda de nombre en una lista
def Buscar_nombre (lista=None, nombre=None):
    """
    Busca un nombre en una lista.
    Parámetros por defecto:
      - lista: [] si no se proporciona
      - nombre: None si no se proporciona
    """
    if lista is None or nombre is None:
        raise ValueError("La lista o el nombre no pueden ser nulos.")
    
    # Se verifica que la cadena no esté vacía
    if not lista or not nombre:
        raise ValueError("La lista o el nombre no pueden estar vacíos.")
    
    # Se busca el nombre en la lista
    if nombre in lista:
        print(f"El nombre '{nombre}' fue encontrado en la lista.")
    else:
        raise ValueError(f"El nombre '{nombre}' no fue encontrado en la lista.")     
try: 
    # Entrada de lista de nombre y nombre a buscar
    entrada = input("Introcuce una lista de nombre separados por comas :").strip()
    Nombre_buscar= input("introduce el nombre que deseas buscar : ").strip()
    # Se verifica que la cadena no esté vacía
    if not entrada or not Nombre_buscar:
        raise ValueError("Debe introducir La lista de nombres y el nombre que desea buscar")
    
    #transforma la entrada en una lista sin espacion y separando por comas
    lista_nombre = [nombre.strip().lower() for nombre in entrada.split(",")]
    Nombre_buscar = Nombre_buscar.strip().lower()
    Buscar_nombre(lista_nombre, Nombre_buscar)
except ValueError as e:
    # error en la entrada de datos
    print("Error:", e)


