# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo"
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

def Calcula_area(tipo, valores):
    # función para calcular el área
    base, altura = valores
    if tipo=="Rectángulo":
        area = base * altura
    elif tipo =="Triangulo":
        area = (base * altura)/2
    return area
    
datos = (3,4) # valores para calcular el área

# Cálcula el área de un triangulo
print(f"El area de un triangulo de {datos[0]} de base por {datos[1]} de altura es :" , Calcula_area("Triangulo", datos))

# Cálcula el área de un Rectángulo
print(f"El area de un Rectángulo de {datos[0]} de base por {datos[1]} de altura es :" , Calcula_area("Rectángulo", datos))