# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo"
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

def Calcula_area(tipo=None, valores=None):
    # función para calcular el área
    """
    Calcula el área de un rectángulo o triángulo.
    Parámetros:
      - tipo: "Rectángulo" o "Triangulo"
      - valores: una tupla con base y altura
    """
    base, altura = valores
    if tipo=="Rectángulo":
        area = base * altura
    elif tipo =="Triangulo":
        area = (base * altura)/2
    return area
    
#entrada de la figura
try:
    figura = input("Introduce la figura (Rectángulo o Triangulo): ").strip()
    if figura.lower() not in ["rectángulo", "triangulo"]: # validación de la figura en minusculas
        raise ValueError("Figura no válida. Debe ser 'Rectángulo' o 'Triangulo'.")

    # entrada de los datos
    datos = input("Introduce los datos (base, altura) separados por comas: ").strip()
    if not datos:
        raise ValueError("Los datos no pueden estar vacíos.")
    # Se transforma la entrada en una tupla de números
    datos = tuple(map(float, datos.split(",")))
    if len(datos) != 2:
        raise ValueError("Debe introducir exactamente dos números.")
    # Cálcula el área de un triangulo
    area = Calcula_area(figura, datos)
    # Visualiza el resultado
    print(f"El area de un {figura} de {datos[0]} de base por {datos[1]} de altura es :" , area)
except ValueError as e:
    print(f"Error: {e}")
    # valores por defecto   


