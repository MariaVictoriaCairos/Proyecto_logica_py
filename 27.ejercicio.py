# 27. Crea una función que calcule el promedio de una lista de números.

# función para calcular promedio
def promedio(lista=None):
    """
    Calcula el promedio de una lista de números.
    Parámetro por defecto:
      - lista: [] si no se proporciona
    """
    return sum(lista)/len(lista)

# Lista de número introducida por el usuario
try:
    entrada = input("Introduce números separados por comas: ").strip()
    # Se verifica que la cadena no esté vacía
    if not entrada:
        print("Error: No se ingresaron números.")
        raise ValueError("La lista está vacia")
    lista = [
    float(x.strip()) 
    for x in entrada.strip().split(",") 
    if x.strip()
]
    # Valida que son números
    if not all(isinstance(x, (int, float)) for x in lista):
        raise ValueError("La lista contiene elementos no numéricos")
    
    
    #llamada a la función para calcular el promedio
    resultado = promedio(lista)

    print("El resultado de promedio de la lista es: ", resultado)
except ValueError:
    print("Error: solo se aceptan números")