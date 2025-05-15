# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

try:
    # Entradas del usuario
    lista1 = input("Introduzca la primera lista de valores separados por comas: ").strip()
    lista2 = input("Introduzca la segunda lista de valores separados por comas: ").strip()
    # veificar que no estén vacías
    if not lista1 or not lista2:
        raise ValueError("Las listas no pueden estar vacías.")
    # Convertir las entradas en listas
    lista1 = [int(x.strip()) for x in lista1.split(",")] 
    lista2 = [int(x.strip()) for x in lista2.split(",")] 
    # Lambda que suma elementos correspondientes de dos listas
    # Lambda que suma elementos correspondientes de dos listas
    sumar_listas = lambda l1, l2: list(map(lambda a, b: a + b, l1, l2))

    # Llamar a la función lambda
    resultado = sumar_listas(lista1, lista2)
    print(f"Suma elemento a elemento: {resultado}")


except ValueError as e:
    print("Error: Asegúrate de introducir solo numeros separados por comas. ", e)