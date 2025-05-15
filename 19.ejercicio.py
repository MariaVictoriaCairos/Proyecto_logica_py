# 19. Crea una función lambda que filtre los números impares de una lista dada.

# entrada de la lista de numeros por el usuario
entrada = input("Introduce una lista de números separados por comas (ej: 5,7,2): ").strip()
if not entrada:
    print("Error: No se ingresó ningún valor.")
else:
    # Normalizar y convertir cada elemento a int
    try:
        # Convertir la entrada en una lista de números
        numeros = [int(x.strip()) for x in entrada.split(",") if x.strip() != ""]
        # Verificar si la lista está vacía
        if not numeros:
            print("Error: La lista de números está vacía.")
            exit(1)
        # Verificar si la lista contiene solo dígitos
        if not all(isinstance(i, int) for i in numeros):
            raise ValueError("La lista debe contener solo números enteros.")
        #filtro de los impares
        # Usar filter para obtener los números impares
        # lambda x: x % 2 != 0 filtra los números impares
        # filter(lambda x: x % 2 != 0, numeros) devuelve un iterador con los números impares
        # Convertir el iterador a una lista
        # list(filter(lambda x: x % 2 != 0, numeros)) convierte el iterador a una lista
        impares = list(filter(lambda x: x%2 !=0, numeros))
        print("los numeros impares son: ")
        for impar in impares:
            print(impar)
    except ValueError:
        print("Error: Asegúrate de ingresar solo números válidos separados por comas.")
        exit(1)
    



