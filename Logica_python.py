# Autora: María Victoria Cairós Gonzalez
# Fecha: 21/03/2025

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.
def contar_frecuencias(cadena):
    frecuencias = {}
    for letra in cadena:
        if letra != ' ':
            letra = letra.lower()  # Para contar sin distinguir mayúsculas
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias
texto= input("Introduzca un texto:")  
frecuencia = contar_frecuencias(texto)
for letra, frecuencia in frecuencia.items(): # Se imprime en vertical por letra de la cadena
    print(f"{letra}: {frecuencia}")
    
    
# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

# la lista de numeros la escribe el usuario
numeros_usuario = input("Introduce la lista de numeros separados por una coma: ")
val_numeros = numeros_usuario.split(",")                    # convierte el input en una lista
if all(numero.strip().isdigit() for numero in val_numeros): # Valida que son números
    numeros = map(int, numeros_usuario.split(","))          # Transforma el input en una lista que separa por la coma
    dobles = list(map(lambda x: x * 2, numeros))            # itera y los duplica

    print(f"El doble de los números que has introducido son {dobles}") 
else:
    print("Los numeros que has introducido no son correctos")

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
# devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def filtrar_por_palabra(lista, objetivo):
    return [palabra for palabra in lista if objetivo in palabra]

palabras = ["ordenador", "ratón", "teclado", "portátil", "tablet", "multiport"]
objetivo = "or"

resultado = filtrar_por_palabra(palabras, objetivo)
print(resultado)

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas(lista1, lista2):
    return list(map(lambda a_b: a_b[0] - a_b[1], zip(lista1, lista2)))


print("Para calcular la diferencia debes introducir ambas listas del mismo tamaño")
Numeros_1 = input("Introduce la primera lista de numeros separados por una coma: ")
Lista_1 = Numeros_1.split(",")                    # convierte el input en una lista
Numeros_2 = input("Introduce la segunda lista de numeros separados por una coma: ")
Lista_2 = Numeros_2.split(",")                    # convierte el input en una lista

if all(numero_1.strip().isdigit() for numero_1 in Lista_1) and all(numero_2.strip().isdigit() for numero_2 in Lista_2):
    if len(Lista_1) == len(Lista_2):    
        
        Lista_1 = list(map(int, map(str.strip, Lista_1)))       # Convertir los elementos de la lista a enteros
        Lista_2 = list(map(int, map(str.strip, Lista_2)))
        
        Calculo= diferencia_listas(Lista_1,Lista_2)
        print(f"La diferencia entre las dos listas es: {Calculo}")
    else:
        print("las listas deben tener el mismo tamaño")
else:
    print("error, introdujo caracteres. solo se pueden calcular diferencia de números") 
    
    
# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.

def calcula_aprobado(notas, nota_aprobado):
    media = sum(notas)/len(notas)
    if media>= nota_aprobado:
        estado="Aprobado"
    else:
        estado="suspenso"
    return(media,estado)

notas = [4,6,7,7]
aprobado= 5
resultado = calcula_aprobado(notas, aprobado)
print(f"La nota media es {resultado[0]:.2f} y el estado es: {resultado[1]}")

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial_recursivo(numero):
    """
    Calcula el factorial de un número de forma recursiva.
    """
    if numero < 0:
        raise ValueError("El número debe ser mayor o igual a cero.")
    elif numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial_recursivo(numero - 1)

# Solicitar un número entero al usuario con validación
entrada = input("Introduce un número entero para calcular su factorial: ")

if entrada.isdigit():  # Solo acepta enteros positivos
    numero_usuario = int(entrada)
    try:
        total = factorial_recursivo(numero_usuario)
        print(f"El factorial de {numero_usuario} calculado de forma recursiva es: {total}")
    except ValueError as e:
        print(f"Error: {e}")
else:
    print("Error: Debes introducir un número entero positivo.")
    
## 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def mi_string(lista):
    return list(map(lambda tupla: " ".join(map(str, tupla)), lista))

# lista de tuplas
mi_lista = [(1, 3), (6, 2), (6, 8)]
# llamada ala función que los convierte
mi_caracter = mi_string(mi_lista)

print(f"Mi lista de tuplas es {mi_lista} al transformarlo en una lista de string, el resultado es {mi_caracter}")
   
   # 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

print("Introduce los dos números que quieres dividir:")

entrada_1 = input("Introduce el primer número: ")
entrada_2 = input("Introduce el segundo número: ")

try:
    numero_1 = float(entrada_1)
    numero_2 = float(entrada_2)

    division = numero_1 / numero_2
    print(f"La división de {numero_1} entre {numero_2} es: {division}")

except ValueError:
    print("Error: Debes introducir valores numéricos válidos.")

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

else:
    print("División realizada con éxito.")
    
# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def Mascotas_España(mascotas):
    Mascotas_prohibidas = ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"]
    Mascotas_permitidas = filter(lambda m: m not in Mascotas_prohibidas, mascotas)
    return list(Mascotas_permitidas)

Mascotas = ["perro","gato","pajaro","caballo","Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"]

print(f"Las mascotas permitidas en españa son: {Mascotas_España(Mascotas)}")

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.
# Excepción personalizada

class ListaVaciaError(Exception):
    pass

# Función para calcular el promedio
def calcular_promedio(numeros):
    if not numeros:
        raise ListaVaciaError("Error: la lista está vacía, no se puede calcular el promedio.")
    promedio = sum(numeros) / len(numeros)
    return promedio

# Solicitar entrada al usuario
entrada = input("Introduce una lista de números separados por comas (ej: 4, 5.5, 7, 2): ")

try:
    # Convertir la entrada en una lista de números
    lista_numeros = [float(x.strip()) for x in entrada.split(",") if x.strip() != ""]

    # Calcular el promedio
    promedio = calcular_promedio(lista_numeros)
    print(f"Tu lista es: {lista_numeros} y el promedio es: {promedio:.2f}")

except ValueError:
    print("Error: Asegúrate de ingresar solo números válidos separados por comas.")

except ListaVaciaError as e:
    print(e)
    
# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.

class MenorQueCero(Exception):
    pass

class MayorQue120(Exception):
    pass

# Solicitar entrada al usuario
entrada = input("Introduce tu edad : ")

try:
    # Convertir la entrada en integer
    edad = int(entrada)
    if edad>=121:
        raise MayorQue120("La edad no es correcta, no puede ser mayor que 120 años.")
    elif edad<0:
        raise MenorQueCero("La edad no puede ser negativa")
    else:
        print(f"La edad del usuario es {edad}")

except ValueError:
    print("Error: Asegúrate de ingresar tu edad correctamente.")

except MenorQueCero as e:
    print(e)
except MayorQue120 as e:
    print(e)
    
# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def lista_palabras(frase):
    palabras= frase.split()
    longitudes = list(map(len, palabras))
    return longitudes

entrada = input("Introduce una frase:")
longitudes = lista_palabras(entrada)
print("la longitud de las palabras de tu frase son: ")
for longitud in longitudes: 
    print(longitud)

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def listar_tuplas(caracteres):
    caracteres_unicos = set(caracteres)
    resultado = list(map(lambda c: (c.upper(), c.lower()), caracteres_unicos))
    return resultado

# Solicitar entrada al usuario
entrada = input("Introduce un conjunto de caracteres: ")

try:
    Lista_MM = listar_tuplas(entrada)
    for tupla in Lista_MM:
        print(tupla)
except Exception as e:
    print(f"ocurrió un error: {e}")

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
# función filter()
def buscar_por_letra(paises, letra):
    return list(filter(lambda pais: pais[0].lower() == letra.lower(), paises))

Lista_paises = ["Argentina", "Brasil", "Canadá", "China", "Egipto", "España", "Colombia", "Estados Unidos", "Francia", "India", "Italia", "Japón", "México", "Nigeria", "Sudáfrica", "Turquía"]

entrada=input("introduce la letra de busqueda : ")


paises_filtro = buscar_por_letra(Lista_paises,entrada)
print(f"Lista de paises que comienzan por la letra '{entrada}': ")
for pais in paises_filtro:
    print(pais)

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
def suma_lista(numeros):
    return list(map(lambda x: x+3, numeros))

# Lista de numeros
entrada= [1,5,3,7,5,9,2]
# llamada a la función
lista_mas3= suma_lista(entrada)

print(lista_mas3)

#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
#todas las palabras que sean más largas que n. Usa la función filter()

# Valida que la entrada no sea 0
class Igual_Cero(Exception):
    pass

# Función para filtrar por el tamaño de la palabra
def filtro_tamaño(lista, tamaño):
    return list(filter(lambda palabra: len(palabra)>tamaño, lista))

Lista_paises = ["Argentina", "Brasil", "Canadá", "China", "Egipto", "España", "Colombia", "Estados Unidos", "Francia", "India", "Italia", "Japón", "México", "Nigeria", "Sudáfrica", "Turquía"]

# Entrada del tamaño máximo de la palabra
entrada =input("Introduce el tamaño máximo de la palabra : ")

try:
    tamaño_palabra = int(entrada)
    if tamaño_palabra >= 0:
        palabras= filtro_tamaño(Lista_paises,tamaño_palabra)
        print(f"las palabras que son mas largas de {tamaño_palabra} son :")
        for palabra in palabras:
            print(palabra)
    else:
        raise Igual_Cero("El tamaño no puede ser menor que 1")
        
        
except ValueError:
    print("Error: Asegúrate de ingresar un tamaño de palabra numérico y mayor de 0")
    
except Igual_Cero as e:
    print(e)


# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()

#importar función reduce()
from functools import reduce

# función que concatena los números de una lista
def Genera_numero(lista):
    return reduce(lambda x, y: x*10 + y, lista)

numeros= [2,5,3]

resultado = Genera_numero(numeros)
print(resultado)

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
    
# 19. Crea una función lambda que filtre los números impares de una lista dada.

# lista de números
numeros= [1,2,3,4,5,6,7,8,9,10]

#filtro de los impares
impares = filter(lambda x: x%2 !=0, numeros)

print("los numeros impares son: ")
for impar in impares:
    print(impar)
    
# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
# filter()

# lista de elementos
elementos= [2,"f",4,5,4.3,"D"]

elementos_int = filter(lambda x: isinstance(x, int), elementos)

print("Los elementos de la lista que son enteros son : ")
for elemento in elementos_int:
    print(elemento)

#21. Crea una función que calcule el cubo de un número dado mediante una función lambda

#entrada del valor
valor = input("introduce el número para calcular el cubo : ")
valor = int(valor)

#función lambda en una línea para calcular el cubo
cubo = (lambda x: x ** 3)(valor)

# visualización del resultado
print(f"El cubo del valor es: {cubo}")

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce()

#importar función reduce()
from functools import reduce

#lista de valores
valores= [2,3,2]

#calculo del producto total
Producto_total = reduce(lambda x, y: x * y, valores)

#Visualización del resultado
print(f"El produto total de los valores es: {Producto_total}")

# 23. Concatena una lista de palabras.Usa la función reduce().

#importar función reduce()
from functools import reduce
# Lista de palabras
palabras= ["Mi", "profesión", "favorita", "es", "ingeniería", "en", "informática"]
# Función de unir palabras
mensaje= reduce(lambda x, y : x + " " + y, palabras)
# Visualización del mensaje
print(mensaje)

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

#importar función reduce()
from functools import reduce
#lista de numeros
numeros= [2,4,6]

#función para calcular la diferencia
diferencia_total = reduce(lambda x, y: x - y, numeros)

# Visualización del resultado
print(f"la diferencia total de la lista de números {numeros} es {diferencia_total}")

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def cuenta_caracteres(cadena):
    caracteres_total = len(cadena)
    caracteres_sin_espacios = caracteres_total - sum(c.isspace() for c in cadena)
    letras = sum(c.isalpha() for c in cadena)
    numeros = sum(c.isdigit() for c in cadena)
    espacios = sum(c.isspace() for c in cadena)

    return caracteres_total, caracteres_sin_espacios, letras, numeros, espacios


# Solicitar una cadena al usuario
entrada = input("Introduce el texto al que le quieres calcular los caracteres: ")

# Obtener los resultados
total, sin_espacios, letras, numeros, espacios = cuenta_caracteres(entrada)

# Mostrar resultados de forma clara
print("\nEl contenido de la cadena que has introducido tiene:")
print(f"- Total de caracteres (con espacios): {total}")
print(f"- Total de caracteres (sin espacios): {sin_espacios}")
print(f"- Letras: {letras}")
print(f"- Dígitos numéricos: {numeros}")
print(f"- Espacios: {espacios}")

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

# Entrada de los numeros
print("introduzca los dos numeros que quiere dividir:")
dividendo = int(input("introduzca el dividendo : "))
divisor = int(input("Introduzca el divisor :"))

# función lambda
resto= lambda dividendo, divisor: dividendo % divisor

# Imprimir el resultado
print(f"el resto es : {resto(dividendo, divisor )}")

# 27. Crea una función que calcule el promedio de una lista de números.

# función para calcular promedio
def promedio(lista):
    if not lista:
        return "La lista está vacia"
    return sum(lista)/len(lista)

# Lista de número introducida por el usuario
try:
    entrada = input("Introduce números separados por comas: ")
    lista = [float(x) for x in entrada.split(",")]
    #llamada a la función para calcular el promedio
    resultado = promedio(lista)

    print("El resultado de promedio de la lista es: ", resultado)
except ValueError:
    print("Error: solo se aceptan números")
    
# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

# función para buscar duplicado
def duplicado (lista):
    elementos_vistos = set()
    for elemento in lista:
        if elemento in elementos_vistos:
            return elemento
        elementos_vistos.add(elemento)
    return None

try:
    # Lista de número introducida por el usuario
    entrada = input("Introduce números separados por comas: ")
    lista = [float(x) for x in entrada.split(",")]
    
    #llamada a la función para duscar el primer duplicado
    resultado = duplicado(lista)

    print("El primer elemento duplicado de la lista es: ", resultado)
except ValueError:
    print("Error: solo se aceptan números")
    
# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.

# función para enmascarar texto
def transformar(variable):
    longitud = len(variable)
    if longitud <= 4:
        return None # No hay nada que enmascarar
    else:
        return '#' * (longitud - 4) + variable[-4:]


# entrada de la variable 
entrada = input("Introduce un valor o caracteres que quieras enmascarar con #: ")

#Vusualización y llamada a la función
resultado = transformar(entrada)
if resultado is None:
    print("No hay caracteres que enmascarar, la variable tiene una longitud menor de 4")
else:
    print("Se presentan los caracteres enmascarados con '#' a excepción de los cuatro últimos: ", resultado)

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.

# función para determinar si las palabras son anagramas
def valora_anagrama(variable_1, variable_2):
    # Se ponen en minusculas
    variable_1 = variable_1.lower()
    variable_2 = variable_2.lower()
    if len(variable_1) != len(variable_2):
        return None # Las palabras no son anagramas por no tener la misma longitud
    else:
        return sorted(variable_1) == sorted(variable_2)


# entrada de la variable 
print("Introduce dos palabras separadas por comas que quieras valorar si son anagramas: ")
entrada_1 = input("Introduce la primera palabra: ")
entrada_2 = input("Introduce la segunda palabra: ")

#Visualización y llamada a la función
resultado = valora_anagrama(entrada_1,entrada_2)
if resultado is None:
    print("Las palabras no son anagramas, no tienen el mismo tamaño")
elif resultado is True:
    print(f"las palabras {entrada_1} y la palabra {entrada_2} son  anagramas")
else:
    print("Las palabras no son anagramas")
    
# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.

# función busqueda de nombre en una lista
def Buscar_nombre ():
    
    try: 
        # Entrada de lista de nombre y nombre a buscar
        entrada = input("Introcuce una lista de nombre separados por comas :").upper()
        Nombre_buscar= input("introduce el nombre que deseas buscar : ").strip().upper()
        
        #transforma la entrada en una lista sin espacion y separando por comas
        lista_nombre = [nombre.strip() for nombre in entrada.split(",")]

        # Busqueda del nombre en la lista
        if Nombre_buscar in lista_nombre:
            print(f"El nombre {Nombre_buscar} está en la Lista")
        else:
            raise ValueError(f"El nombre '{Nombre_buscar}' no fue encontrado en la lista.")
    
    except ValueError as e:
        # error en la entrada de datos
        print("Error:", e)


# Llamada a la función
Buscar_nombre()

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.

# Función para buscar el cargo del empleado
def Buscar_empleado(l_empleados,nombre_buscar):
    # recorre el diccionario
    for nombre, cargo in l_empleados.items():
        # condición 
        if nombre.upper() == nombre_buscar:
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

# Entrada del nombre que esta buscando
nombre = input("introduzca el nombre con el primer apellido del empleado que está buscand : ").upper()

# llamada a la función para buscar el nombre del empleado y devolver el cargo
resultado = Buscar_empleado(empleados, nombre)

print(resultado)

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

def agregar_elementos(lista, entrada):
    # Convierte la entrada en una lista, eliminando espacios
    elementos = [item.strip() for item in entrada.split(",")]
    return lista + elementos  # Devuelve una nueva lista combinada

# Entradas del usuario
entrada_frutas = input("Introduzca las frutas que desea añadir a la lista separadas por comas: ")
entrada_verduras = input("Introduzca las verduras que desea añadir a la lista separadas por comas: ")

# Listas originales
frutas = ["mango", "plátano", "fresa"]
verduras = ["cebolla", "ajo", "peregil"]

# Aplicar la función
nuevas_frutas = agregar_elementos(frutas, entrada_frutas)
nuevas_verduras = agregar_elementos(verduras, entrada_verduras)

# Imprimir resultados
print(f"La lista de frutas es: {nuevas_frutas}")
print(f"La lista de verduras es: {nuevas_verduras}")

#34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer tronco , nueva rama , crecer ramas , quitar rama e info arbol . El objetivo es implementar estos métodos para
# manipular la estructura del árbol.
# Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método crecer tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método nueva rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método crecer ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método quitar rama para eliminar una rama en una posición específica.
# 6. Implementar el método info arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
# mismas.
# Caso de uso:
# 1. Crear un árbol.
# 2. Hacer crecer el tronco del árbol una unidad.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.

class Arbol:
    def __init__(self):
        self.tronco = 5  # Longitud inicial del tronco
        self.ramas = []  # Lista vacía de ramas

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)  # Cada nueva rama tiene longitud 1

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            del self.ramas[posicion]
        else:
            print(f"No se puede eliminar la rama en la posición {posicion} (índice inválido).")

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

# 1. Crear un árbol
mi_arbol = Arbol()

# 2. Hacer crecer el tronco una unidad
mi_arbol.crecer_tronco()

# 3. Añadir una nueva rama
mi_arbol.nueva_rama()

# 4. Hacer crecer todas las ramas
mi_arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()

# 6. Retirar la rama en la posición 2 (índice 2)
mi_arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol
info = mi_arbol.info_arbol()
print("Información del árbol:")
print(f"Longitud del tronco: {info['longitud_tronco']}")
print(f"Número de ramas: {info['numero_ramas']}")
print(f"Longitudes de las ramas: {info['longitudes_ramas']}")

# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
# agregar dinero al saldo.
# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False.
# 2. Implementar el método retirar dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
# poder hacerse.
# 3. Implementar el método transferir dinero para realizar una transferencia desde otro usuario al usuario actual.
# Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar dinero para agregar dinero al saldo del usuario.
# 
# Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
# PROYECTO LÓGICA: Katas de Python 2
# 2. Agregar 20 unidades de saldo de "Bob"
# .
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# 4. Retirar 50 unidades de saldo a "Alicia".

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, dinero):
        try:
            if not self.cuenta_corriente:
                raise PermissionError(f"{self.nombre} no tiene cuenta corriente. No puede retirar dinero.")
            if dinero > self.saldo:
                raise ValueError("El saldo de su cuenta no es suficiente.")
            self.saldo -= dinero
            print(f"{self.nombre} retiró {dinero}. Saldo actual: {self.saldo}")
        except (ValueError, PermissionError) as e:
            print(f"Error al retirar dinero: {e}")

    def transferir_dinero(self, dinero, otro_usuario):
        try:
            if not self.cuenta_corriente or not otro_usuario.cuenta_corriente:
                raise PermissionError("Ambos usuarios deben tener cuenta corriente para transferencias.")
            if dinero > otro_usuario.saldo:
                raise ValueError(f"{otro_usuario.nombre} no tiene saldo suficiente para transferir.")
            otro_usuario.saldo -= dinero
            self.saldo += dinero
            print(f"{otro_usuario.nombre} transfirió {dinero} a {self.nombre}.")
        except (ValueError, PermissionError) as e:
            print(f"Error al transferir dinero: {e}")

    def agregar_dinero(self, dinero):
        if dinero > 0:
            self.saldo += dinero
            print(f"{self.nombre} recibió {dinero}. Saldo actual: {self.saldo}")
        else:
            print("No se puede agregar una cantidad negativa o cero.")

# casos de uso
# 1. Crear dos usuarios
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 unidades al saldo de Bob
bob.agregar_dinero(20)  # Saldo de Bob ahora: 70

# 3. Transferir 80 unidades de Bob a Alicia
alicia.transferir_dinero(80, bob)  # Saldo de Bob: -10 no permitido, así que da error si no tiene saldo suficiente

# 4. Retirar 50 unidades de Alicia
alicia.retirar_dinero(50)

# 5. Ver el saldo de Alicia y de bob
print(f"El saldo final de {alicia.nombre} es {alicia.saldo}")
print(f"El saldo final de {bob.nombre} es {bob.saldo}")

# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
# reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
# de la función procesar_texto.
#
# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
# que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra
# nueva . Tiene que devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
# eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
# número de argumentos variable según la opción indicada.
#
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto

def contar_palabras(texto):
    # Cuenta el número de veces que aparece cada palabra en el texto.
    # Devuelve un diccionario con la palabra como clave y su frecuencia como valor.
    
    palabras = texto.lower().split()    # transforma todo en minusculas y separa por palabra
    conteo = {}                         # inicializa el diccionario
    for palabra in palabras:
        palabra = palabra.strip(".,;:!?()[]\"'")  # quitar signos de puntuación
        conteo[palabra] = conteo.get(palabra, 0) + 1  # .get metodo para buscar
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    # Reemplaza todas las apariciones de palabra_original por palabra_nueva en el texto.
    # Devuelve el texto modificado.
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    # Elimina todas las apariciones exactas de palabra_a_eliminar del texto.
    # Devuelve el texto resultante.

    palabras = texto.split() # separa por palabra para hacer una lista
    resultado = []

    for palabra in palabras:
        palabra_limpia = palabra.strip(".,;:!?()[]\"'") # elimina caracteres en las palabras 
        if palabra_limpia != palabra_a_eliminar:
            resultado.append(palabra)
    
    return ' '.join(resultado)  # une la lista en un solo string


def procesar_texto(texto, opcion, *args):
    # Procesa un texto según la opción especificada:
    # - "contar": cuenta las palabras.
    # - "reemplazar": reemplaza una palabra por otra.
    # - "eliminar": elimina una palabra.
    
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar" and len(args) == 2:
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar" and len(args) == 1:
        return eliminar_palabra(texto, args[0])
    else:
        return "Opción no válida o número incorrecto de argumentos."

texto = "El sol brilla y el cielo está azul. El sol calienta la tierra. La tierra respira mientras el cielo observa en silencio."
print("texto: "+ texto)
# Contar palabras
resultado = procesar_texto(texto, "contar")
print("El conteo de palabras es:")
for palabra, cantidad in resultado.items():
    print(f"{palabra}: {cantidad}")

# Reemplazar palabra
print("Se remplaza la palabra cielo por mar y el texto resultante es:", procesar_texto(texto, "reemplazar", "cielo", "mar"))

# Eliminar palabra
print("Se elmina del texto la palabra tierra y el resultado es: ", procesar_texto(texto, "eliminar", "tierra"))

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
import datetime as dt

entrada = input("Introduzca la hora con formato HH:MM: ")

try:
    hora_objeto = dt.datetime.strptime(entrada, "%H:%M")  # convierte el texto a objeto hora
    hora = hora_objeto.hour  # extrae la hora

    if 6 <= hora < 12:
        print("Es de mañana 🌅")
    elif 12 <= hora < 20:
        print("Es de tarde ☀️")
    else:
        print("Es de noche 🌙")

except ValueError:
    print("Formato incorrecto. Por favor use el formato HH:MM (por ejemplo, 08:30)")
    
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

# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
# siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
# a cero). Por ejemplo, descuento de 15€.
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
# programa de Python.

try:
    #introduce el precio como variable numerica con decimales
    precio = float(input("Introduzca el precio del artículo: ").replace(',', '.'))

    # introduce si tiene un cupón y se guarda en una variable booleana
    respuesta = input("¿Tiene cupón de descuento? indique si o no :").strip().lower()
    if respuesta not in ["si", "no"]:
        raise ValueError("Debes responder al cupón con 'si' o 'no'")
    Cupon = respuesta == "si"
    
    # Solicitud del valor del cupón
    valor_cupon=0
    if Cupon:
        valor_cupon= float(input("Introduce el valor del cupón : ").replace(',', '.'))
        # el valor no puede ser negativo
        if valor_cupon < 0:
            raise ValueError("El valor del cupón no puede ser negativo.")
    
    # calculo del precio final   
    precio_final = precio-valor_cupon
    
    print(f"El precio final de la compra es: {precio_final:.2f} €")
        
except ValueError as e:
    print(f"Error en el valor: {e}")
    