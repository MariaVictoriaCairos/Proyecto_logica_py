# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
# 90. Usa la función filter()

# Lista de diccionarios con información de estudiantes
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificación": 95},
    {"nombre": "Luis", "edad": 22, "calificación": 88},
    {"nombre": "María", "edad": 19, "calificación": 92},
    {"nombre": "Pedro", "edad": 21, "calificación": 76},
    {"nombre": "Laura", "edad": 20, "calificación": 90}
]

# Función que filtra estudiantes con calificación >= 90
estudiantes_destacados = list(filter(lambda est: est["calificación"] >= 90, estudiantes))

# Mostrar los estudiantes filtrados
print("Estudiantes con calificación mayor o igual a 90:")
for estudiante in estudiantes_destacados:
    print(estudiante)