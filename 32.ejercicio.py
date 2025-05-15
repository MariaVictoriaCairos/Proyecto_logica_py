# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.

# Función para buscar el cargo del empleado
def Buscar_empleado(l_empleados=None,nombre_buscar=""):
    # recorre el diccionario
    for nombre, cargo in l_empleados.items():
        # condición 
        if nombre.upper() == nombre_buscar.upper():
            return "El cargo del empleado es : " + cargo
    return "El nombre buscado no es empleado de la empresa"
    
    
# Diccionario con la lista de nombres de empleados y sus cargos
empleados = {
    "Ana Torres": "Gerente de Ventas",
    "Luis Gómez": "Analista de Datos",
    "Carla Ruiz": "Desarrolladora Backend",
    "Pedro Martínez": "Diseñador Gráfico",
    "Sofía Herrera": "Especialista en Recursos Humanos"
}
try:
    # Entrada del nombre que esta buscando
    nombre = input("introduzca el nombre con el primer apellido del empleado que está buscando : ").strip()
    # Se verifica que la cadena no esté vacía
    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")


    # llamada a la función para buscar el nombre del empleado y devolver el cargo
    resultado = Buscar_empleado(empleados, nombre)

    print(resultado)
except ValueError as e:
    # error en la entrada de datos
    print("Error:", e)

