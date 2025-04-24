# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente


try:
    entrada = float(input("introduce la puntuación del alumno (del 0 al 100):"))
    
    if entrada > 0 and entrada <=69:
        print("la nota del alumno es : Insuficiente")
    elif entrada >=70 and entrada <=79:
        print("la nota del alumno es : Bien")
    elif entrada >=80 and entrada <=89:
        print("la nota del alumno es : Muy Bien")
    elif entrada >=90 and entrada <=100:
        print("la nota del alumno es : Excelente")
    else:
        print("Puntuación fuera de rango. Debe estar entre 0 y 100.")
except ValueError:
    print("Error: Debes ingresar un número válido.")