# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente


try:
    entrada = input("introduce la puntuación del alumno (del 0 al 100):").strip()
    # Se verifica que la cadena no esté vacía
    
    # Intentamos convertir a float; aquí se detectan '4.5', '10', etc.
    try:
        puntuacion = float(entrada)
    except ValueError:
        raise ValueError("La puntuación debe ser un número válido.")
    
    
    if puntuacion > 0 and puntuacion <=69:
        print("la nota del alumno es : Insuficiente")
    elif puntuacion >=70 and puntuacion <=79:
        print("la nota del alumno es : Bien")
    elif puntuacion >=80 and puntuacion <=89:
        print("la nota del alumno es : Muy Bien")
    elif puntuacion >=90 and puntuacion <=100:
        print("la nota del alumno es : Excelente")
    else:
        print("Puntuación fuera de rango. Debe estar entre 0 y 100.")
except ValueError as e:
    # error en la entrada de datos
    print(f"Error: {e}")