# Autora: María Victoria Cairós Gonzalez
# Fecha: 21/03/2025
# Fecha revisión : 14/05/2025

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.
def contar_frecuencias(cadena):
    frecuencias = {}
    # Se eliminan los espacios en blanco al inicio y al final de la cadena
    cadena = cadena.strip()
    # Se verifica que la cadena no esté vacía
    if not cadena:
        print("No se ingresó texto válido.")
        return {}
    for letra in cadena:
        if letra != ' ':
            letra = letra.lower()  # Para contar sin distinguir mayúsculas
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias
texto= input("Introduzca un texto:").strip() # Se pide al usuario que introduzca un texto
# Se llama a la función contar_frecuencias y se imprime el resultado
frecuencia = contar_frecuencias(texto)
if frecuencia:
    print("Frecuencia de letras:")  
    # Se imprime en vertical por letra de la cadena
    for letra, frecuencia in frecuencia.items(): # Se imprime en vertical por letra de la cadena
        print(f"{letra}: {frecuencia}")
    
# ----------------------------------------------------
# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

# la lista de numeros la escribe el usuario
numeros_usuario = input("Introduce la lista de numeros separados por una coma: ").strip()
# Se pide al usuario que introduzca una lista de números separados por comas
# Se eliminan los espacios en blanco al inicio y al final de la cadena
# Se verifica que la cadena no esté vacía
if not numeros_usuario:
    print("La lista de numeros está vacia.")
else:
    numeros_usuario = numeros_usuario.strip()                   # Se eliminan los espacios en blanco al inicio y al final de la cadena
    val_numeros = [x.strip() for x in numeros_usuario.split(",")] # convierte el input en una lista eliminando los espacios
    if all(numero.isdigit() for numero in val_numeros): # Valida que son números
        numeros = map(int, numeros_usuario.split(","))          # Transforma el input en una lista que separa por la coma
        dobles = list(map(lambda x: x * 2, numeros))            # itera y los duplica

        print(f"El doble de los números que has introducido son {dobles}") 
    else:
        print("Los numeros que has introducido no son correctos")
        
# ----------------------------------------------------
# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
# devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def filtrar_por_palabra(lista=None, objetivo=""):
    """
    Devuelve una lista con todas las palabras de 'lista' que contienen 'objetivo'.
    Parámetros por defecto:
      - lista: lista vacía si no se provee
      - objetivo: cadena vacía si no se provee
    """
    # Parámetros por defecto y normalización
    if lista is None:
        lista = []
    objetivo = objetivo.strip().lower()
    if not objetivo:
        return []
    # Filtrar palabras que contienen el objetivo
    return [palabra for palabra in lista if objetivo in palabra] # Filtrar palabras que contienen el objetivo

palabras = ["ordenador", "ratón", "teclado", "portátil", "tablet", "multiport"]
objetivo = "or"

resultado = filtrar_por_palabra(palabras, objetivo)
print(resultado)


# ----------------------------------------------------
# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas(lista1=None, lista2=None):
    """
    Devuelve una lista con la diferencia elemento a elemento de lista1 menos lista2.
    Parámetros por defecto:
      - lista1: [] (lista vacía)
      - lista2: [] (lista vacía)
    """
    if lista1 is None:
        lista1 = []
    if lista2 is None:
        lista2 = []

    # Normalizar y convertir con map + lambda
    try:
        nums1 = list(map(lambda x: int(str(x).strip()), lista1))
        nums2 = list(map(lambda x: int(str(x).strip()), lista2))
    except ValueError:
        raise ValueError("Todos los elementos deben ser números enteros.")

    # Verificar mismo tamaño
    if len(nums1) != len(nums2):
        raise ValueError("Las listas deben tener el mismo tamaño.")

    # Calcular diferencias usando map + lambda
    return list(map(lambda par: par[0] - par[1], zip(nums1, nums2)))



print("Para calcular la diferencia, introduce ambas listas del mismo tamaño.")

# strip() en la entrada del usuario
entrada1 = input("Introduce la primera lista de números separados por coma: ").strip()
entrada2 = input("Introduce la segunda lista de números separados por coma: ").strip()

if not entrada1 or not entrada2:
    print("Error: Debes introducir ambas listas.")
else:
    lista1 = entrada1.split(",")
    lista2 = entrada2.split(",")

    try:
        resultado = diferencia_listas(lista1, lista2)
        print(f"La diferencia entre las dos listas es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")
    
    
# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.

def calcula_aprobado(notas=None, nota_aprobado=5):
    """
    Calcula la media de 'notas' y determina si es mayor o igual a 'nota_aprobado'.
    Parámetros por defecto:
      - notas: lista vacía si no se provee
      - nota_aprobado: 5
    Devuelve una tupla (media, estado).
    """
    if notas is None or not notas:
        return 0.0, "suspenso"
    
    # Calcular media
    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado


# --- Entrada dinámica ---
# Pedimos la lista de notas al usuario
entrada_notas = input("Introduce las notas separadas por comas: ").strip()
if not entrada_notas:
    print("No se ingresaron notas.")
else:
    # Normalizar y convertir cada elemento a float
    lista_notas = [float(x.strip()) for x in entrada_notas.split(",") if x.strip()]
    
    # Pedimos la nota de corte (opcional)
    entrada_corte = input("Introduce la nota de aprobado (por defecto 5): ").strip()
    if entrada_corte:
        try:
            nota_corte = float(entrada_corte)
        except ValueError:
            print("Valor inválido para nota de aprobado. Se usará 5.")
            nota_corte = 5
    else:
        nota_corte = 5

    # Llamada a la función
    media, estado = calcula_aprobado(lista_notas, nota_corte)
    print(f"La nota media es {media:.2f} y el estado es: {estado}")

# ----------------------------------------------------
# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial_recursivo(numero=0):
    """
    Calcula el factorial de un número de forma recursiva.
    Parámetro por defecto: numero=0
    """
    if numero < 0:
        raise ValueError("El número debe ser mayor o igual a cero.")
    if numero in (0, 1):
        return 1
    return numero * factorial_recursivo(numero - 1)

# entrada del usuario
print("Para calcular el factorial de un número, introduce un número entero positivo.")
# strip() en la entrada del usuario para eliminar espacios en blanco
entrada = input("Introduce un número entero para calcular su factorial: ").strip()
# Se verifica que la cadena no esté vacía
if not entrada:
    print("Error: No se ingresó ningún valor.")
else:
    try:
        numero_usuario = int(entrada)
        total = factorial_recursivo(numero_usuario)
        print(f"El factorial de {numero_usuario} calculado de forma recursiva es: {total}")
    except ValueError as e:
        print(f"Error: {e}")

# ----------------------------------------------------    
## 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def mi_string(lista=None):
    """
    Convierte una lista de tuplas en una lista de strings.
    Parámetros por defecto:
      - lista: [] (lista vacía) si no se proporciona
    """
    if lista is None:
        lista = []
    # Para cada tupla: convierte cada elemento a str, strip() y une con espacios
    return list(map(
        lambda tupla: " ".join(map(lambda x: str(x).strip(), tupla)),
        lista
    ))

# --- Entrada del usuario ---
entrada = input("Introduce tus tuplas separadas por ';' (ejemplo: 1,2;  foo, bar; 3 ,4): ").strip()

if not entrada:
    print("No se ingresaron tuplas.")
else:
    # Normalizar y parsear la entrada
    tuplas_raw = [t.strip() for t in entrada.split(";") if t.strip()]
    lista_de_tuplas = []
    for t in tuplas_raw:
        elementos = [e.strip() for e in t.split(",") if e.strip()]
        # Opcional: convertir a int si es dígito
        lista_de_tuplas.append(tuple(
            int(e) if e.isdigit() else e
            for e in elementos
        ))

    # Llamada a la función
    resultado = mi_string(lista_de_tuplas)
    print(f"Mi lista de tuplas es {lista_de_tuplas}, al transformarla en lista de strings el resultado es {resultado}")

# ----------------------------------------------------   
# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

print("Introduce los dos números que quieres dividir:")

# Entrada interactiva con strip()
entrada_1 = input("Introduce el primer número: ").strip()
entrada_2 = input("Introduce el segundo número: ").strip()

# Comprobar que no sean cadenas vacías
if not entrada_1 or not entrada_2:
    print("Error: No se ingresaron números.")
else:
    try:
        # Intentar convertir directamente a float
        numero_1 = float(entrada_1)
        numero_2 = float(entrada_2)

        # Intentar la división
        division = numero_1 / numero_2
    except ValueError:
        print("Error: Debes introducir valores numéricos válidos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    else:
        print(f"La división de {numero_1} entre {numero_2} es: {division}")
    
# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def Mascotas_Espana(mascotas=None):
    """
    Filtra de la lista 'mascotas' aquellas no permitidas en España.
    Parámetro por defecto:
      - mascotas: [] (lista vacía) si no se proporciona
    Devuelve una lista usando filter().
    """
    if mascotas is None:
        mascotas = []
    prohibidas = {"mapache", "tigre", "serpiente pitón", "cocodrilo", "oso"}
    # Primero normalizamos con strip(), luego filtramos con filter()
    mascotas_norm = map(lambda m: m.strip(), mascotas)
    permitidas = filter(
        lambda m: m and m.lower() not in prohibidas,
        mascotas_norm
    )
    return list(permitidas)

# --- Entrada interactiva ---
entrada = input("Introduce una lista de mascotas separadas por comas: ").strip()

if not entrada:
    print("No se ingresaron mascotas.")
else:
    lista_mascotas = [m for m in entrada.split(",")]
    permitidas = Mascotas_Espana(lista_mascotas)
    if permitidas:
        print(f"Las mascotas permitidas en España son: {permitidas}")
    else:
        print("No hay mascotas permitidas en la lista proporcionada.")

# ----------------------------------------------------
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
entrada = input("Introduce una lista de números separados por comas (ej: 4, 5.5, 7, 2): ").strip()
if not entrada:
    print("Error: No se ingresó ningún valor.")
else:
    # Normalizar y convertir cada elemento a float
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
    
# ----------------------------------------------------
# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.

class MenorQueCero(Exception):
    pass

class MayorQue120(Exception):
    pass

# Solicitar entrada al usuario
entrada = input("Introduce tu edad : ").strip()
if not entrada:
    print("Error: No se ingresó ningún valor.")
else:
    # Normalizar y convertir cada elemento a float
    try:
        # Convertir la entrada en una lista de números
        lista_numeros = [float(x.strip()) for x in entrada.split(",") if x.strip() != ""]
    except ValueError:
        print("Error: Asegúrate de ingresar solo números válidos separados por comas.")
        exit(1)
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
        
# ----------------------------------------------------    
# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def lista_palabras(frase=""):
    """
    Devuelve una lista con la longitud de cada palabra en 'frase'.
    Parámetro por defecto:
      - frase: cadena vacía si no se proporciona
    """
    # Parámetro por defecto y normalización
    palabras= frase.split()
    longitudes = list(map(len, palabras))
    return longitudes

entrada = input("Introduce una frase:").strip()
if not entrada:
    print("No se ingresó ninguna frase.")
else:
    # Normalizar y parsear la entrada
    entrada = entrada.strip()
    # Llamada a la función
    longitudes = lista_palabras(entrada)
    print("la longitud de las palabras de tu frase son: ")
    for longitud in longitudes: 
        print(longitud)

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def listar_tuplas(caracteres=None):
    """
    Devuelve una lista de tuplas con cada letra en mayúsculas y minúsculas.
    Parámetro por defecto:
      - caracteres: cadena vacía si no se proporciona
    """
    # Parámetro por defecto y normalización
    if caracteres is None:
        caracteres = ""
    caracteres = caracteres.strip()
    caracteres_unicos = set(caracteres)
    resultado = list(map(lambda c: (c.upper(), c.lower()), caracteres_unicos))
    return resultado

# Solicitar entrada al usuario
entrada = input("Introduce un conjunto de caracteres: ").strip()
if not entrada:
    print("No se ingresaron caracteres.")
else:
    # Normalizar y parsear la entrada
    try:
        entrada = entrada.strip()
        # Llamada a la función
        Lista_MM = listar_tuplas(entrada)
        for tupla in Lista_MM:
            print(tupla)
    except Exception as e:
        print(f"ocurrió un error: {e}")

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
# función filter()
# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
# función filter()
def buscar_por_letra(paises=None, letra=""):
    """
    Filtra una lista de 'paises' que comienzan con la letra 'letra'.
    Parámetros por defecto:
      - paises: lista vacía si no se proporciona
      - letra: cadena vacía si no se proporciona
    """
    # Parámetro por defecto y normalización
    if paises is None:
        paises = []
    if letra is None:
        letra = ""
    letra = letra.strip().lower()
    return list(filter(lambda pais: pais[0].lower() == letra.lower(), paises))

Lista_paises = ["Argentina", "Brasil", "Canadá", "China", "Egipto", "España", "Colombia", "Estados Unidos", "Francia", "India", "Italia", "Japón", "México", "Nigeria", "Sudáfrica", "Turquía"]

entrada=input("introcuce la letra de busqueda : ").strip()
if not entrada:
    print("No se ingresó ninguna letra.")
else:
    # Normalizar y parsear la entrada
    entrada = entrada.strip()
    # Llamada a la función
    paises_filtro = buscar_por_letra(Lista_paises,entrada)
    print(f"Lista de paises que comienzan por la letra '{entrada}': ")
    for pais in paises_filtro:
        print(pais)

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
def suma_lista(numeros=None):
    """
    Suma 3 a cada número de la lista.
    Parámetro por defecto:
      - numeros: [] si no se proporciona
    """
    if numeros is None:
        numeros = []
    return list(map(lambda x: x + 3, numeros))

# --- Entrada por el usuario ---
entrada = input("Introduce una lista de números separados por comas: ").strip()
if not entrada:
    print("Error: No se ingresaron números.")
else:
    try:
        # Normalizar y convertir a int
        lista = [int(x.strip()) for x in entrada.split(",") if x.strip()]
        resultado = suma_lista(lista)
        print(f"Lista original: {lista}")
        print(f"Lista con cada elemento +3: {resultado}")
    except ValueError:
        print("Error: Asegúrate de introducir solo números enteros válidos separados por comas.")# Valida que la entrada no sea 0
class Igual_Cero(Exception):
    pass

# Función para filtrar por el tamaño de la palabra
def filtro_tamaño(lista=None, tamaño=0):
    """
    Filtra una lista de 'lista' que son más largas que 'tamaño'.
    Parámetros por defecto:
      - lista: lista vacía si no se proporciona
      - tamaño: 0 si no se proporciona
    """
    # Parámetro por defecto y normalización
    if lista is None:
        lista = []
    if not isinstance(tamaño, int):
        raise ValueError("El tamaño maximo de la palabra debe ser un número entero")
    
    if tamaño < 0:
        raise ValueError("El tamaño no puede ser menor que 0")
    # Filtrar palabras que son más largas que el tamaño
    # Se utiliza filter() para filtrar las palabras
    # Se utiliza lambda para definir la función de filtrado
    # Se utiliza len() para obtener la longitud de cada palabra
    # Se utiliza list() para convertir el resultado de filter() en una lista
    return list(filter(lambda palabra: len(palabra)>tamaño, lista))

Lista_paises = ["Argentina", "Brasil", "Canadá", "China", "Egipto", "España", "Colombia", "Estados Unidos", "Francia", "India", "Italia", "Japón", "México", "Nigeria", "Sudáfrica", "Turquía"]

# Entrada del tamaño máximo de la palabra
entrada =input("Introduce el tamaño máximo de la palabra : ").strip()
if not entrada:
    print("No se ingresó ningún tamaño.")
else:
    try:
        tamaño_palabra = int(entrada)
        if tamaño_palabra >= 0:
            palabras= filtro_tamaño(Lista_paises,tamaño_palabra)
            print(f"las palabras que son mas largas de {tamaño_palabra} son :")
            for palabra in palabras:
                print(palabra)
        else:
            raise        Igual_Cero("El tamaño no puede ser menor que 1") 
    except ValueError:
        print("Error: Asegúrate de ingresar un tamaño de palabra numérico y mayor de 0")
    
    except Igual_Cero as e:
        print(e)     
# ----------------------------------------------------
# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()

#importar función reduce()
from functools import reduce

# función que concatena los números de una lista
def Genera_numero(lista=None):
    """
    Genera un número a partir de una lista de dígitos.
    Parámetro por defecto:
      - lista: [] (lista vacía) si no se proporciona
    """
    if lista is None:
        lista = []
    # Verificar si la lista está vacía
    if not lista:
        return 0
    # Verificar si la lista contiene solo dígitos
    if not all(isinstance(i, int) and 0 <= i <= 9 for i in lista):
        raise ValueError("La lista debe contener solo dígitos (0-9).")
    # Usar reduce para concatenar los dígitos
    # multiplicando por 10 y sumando el siguiente dígito
    # reduce(lambda x, y: x*10 + y, lista) genera el número
    # correspondiente a la lista de dígitos
    return reduce(lambda x, y: x*10 + y, lista)

# Solicitar entrada al usuario
entrada = input("Introduce una lista de números separados por comas (ej: 5,7,2): ").strip()
if not entrada:
    print("Error: No se ingresó ningún valor.")
else:
    # Normalizar y convertir cada elemento a int
    try:
        # Convertir la entrada en una lista de números
        lista_numeros = [int(x.strip()) for x in entrada.split(",") if x.strip() != ""]
        
        # Llamar a la función Genera_numero
        resultado = Genera_numero(lista_numeros)
        print(f"Tu lista es: {lista_numeros} y el número correspondiente es: {resultado}")

    except ValueError:
        print("Error: Asegúrate de ingresar solo números válidos separados por comas.")

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
    
    
# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
# filter()

# Lectura y normalización de la entrada
entrada = input("Introduce una lista de elementos separados por comas: ").strip()
if not entrada:
    print("La lista de elementos está vacía.")
else:
    # Crear lista de cadenas limpias, sin elementos vacíos
    elementos_raw = list(filter(None, map(str.strip, entrada.split(","))))
    if not elementos_raw:
        print("La lista de elementos está vacía.")
    else:
        # Parsear cada elemento a int, float o str
        elementos = []
        for e in elementos_raw:
            try:
                elementos.append(int(e))
            except ValueError:
                try:
                    elementos.append(float(e))
                except ValueError:
                    elementos.append(e)

        # Filtrar solo los enteros usando filter()
        enteros = list(filter(lambda x: isinstance(x, int), elementos))
        if enteros:
            print("Los elementos de la lista que son enteros son:")
            for n in enteros:
                print(n)
        else:
            print("No hay elementos enteros en la lista.")

#21. Crea una función que calcule el cubo de un número dado mediante una función lambda

#entrada del valor
valor = input("introduce el número para calcular el cubo : ").strip()
#verifica que la cadena no esté vacía
if not valor:
    print("Error: No se ingresó ningún valor.")
    exit(1)
#verifica que el valor sea un número entero
try:
    valor = int(valor)
    #verifica que el valor sea mayor o igual a cero
    if valor < 0:
        print("Error: El número debe ser mayor o igual a cero.")
        exit(1)
    #función lambda en una línea para calcular el cubo
    cubo = (lambda x: x ** 3)(valor)
    # visualización del resultado
    print(f"El cubo del valor es: {cubo}")
except ValueError:
    print("Error: Asegúrate de ingresar un número entero válido.")
    exit(1)

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce()

from functools import reduce

# entrada de los valores por el usuario
valores_usuario = input("Introduce la lista de numeros separados por una coma: ").strip()
# Se eliminan los espacios en blanco al inicio y al final de la cadena
# Se verifica que la cadena no esté vacía
if not valores_usuario:
    print("La lista de numeros está vacia.")
else:
    
    val_numeros = valores_usuario.split(",") # convierte el input en una lista
    # Valida que son números
    if all(numero.strip().isdigit() for numero in val_numeros): # verifica si todos los elementos de la lista son dígitos
        # convierte la lista de cadenas a una lista de enteros
        val_numeros = list(map(int, val_numeros)) # convierte la lista de cadenas a una lista de enteros
        #calculo del producto total
        Producto_total = reduce(lambda x, y: x * y, val_numeros) 
        # reduce(lambda x, y: x * y, val_numeros) calcula el producto total de los valores en la lista
        print(f"El produto total de los valores es: {Producto_total}")
    else:
        print("Los numeros que has introducido no son correctos")
        exit(1)

# 23. Concatena una lista de palabras.Usa la función reduce().

#importar función reduce()
from functools import reduce
# Lista de palabras
palabras= ["Mi", "profesión", "favorita", "es", "ingeniería", "en", "informática"]
# Función de unir palabras
mensaje= reduce(lambda x, y : x + " " + y, palabras)
# Visualización del mensaje
print(mensaje)

# -----------------------------------------------------
# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

from functools import reduce

# entrada de los valores por el usuario
valores_usuario = input("Introduce la lista de numeros separados por una coma: ").strip()
# Se eliminan los espacios en blanco al inicio y al final de la cadena
# Se verifica que la cadena no esté vacía
if not valores_usuario:
    print("La lista de numeros está vacia.")
else:
    val_numeros = valores_usuario.split(",")
    # Valida que son números
    if all(numero.strip().isdigit() for numero in val_numeros):
        # convierte la lista de cadenas a una lista de enteros
        numeros = list(map(int, val_numeros))
        #función para calcular la diferencia
        diferencia_total = reduce(lambda x, y: x - y, numeros)
        # Visualización del resultado
        print(f"la diferencia total de la lista de números {numeros} es {diferencia_total}") 

# -----------------------------------------------------
# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.


def cuenta_caracteres(cadena=""):
    """
    Cuenta el número de caracteres en una cadena de texto.
    Parámetro por defecto: cadena=""
    """
    caracteres_total = len(cadena) # Contar caracteres totales
    caracteres_sin_espacios = caracteres_total - sum(c.isspace() for c in cadena) # Contar caracteres sin espacios
    letras = sum(c.isalpha() for c in cadena) # Contar letras
    numeros = sum(c.isdigit() for c in cadena) # Contar dígitos numéricos
    espacios = sum(c.isspace() for c in cadena) # Contar espacios

    return caracteres_total, caracteres_sin_espacios, letras, numeros, espacios


# Solicitar una cadena al usuario
entrada = input("Introduce el texto al que le quieres calcular los caracteres: ").strip()
# Se eliminan los espacios en blanco al inicio y al final de la cadena
# Se verifica que la cadena no esté vacía
if not entrada:
    print("No se ingresó texto válido.")
else:
    # Obtener los resultados
    total, sin_espacios, letras, numeros, espacios = cuenta_caracteres(entrada)

    # Mostrar resultados de forma clara
    print("\nEl contenido de la cadena que has introducido tiene:")
    print(f"- Total de caracteres (con espacios): {total}")
    print(f"- Total de caracteres (sin espacios): {sin_espacios}")
    print(f"- Letras: {letras}")
    print(f"- Dígitos numéricos: {numeros}")
    print(f"- Espacios: {espacios}")

# -----------------------------------------------------
# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

# Entrada de los numeros
try:
    # Se pide al usuario que introduzca dos números
    # Se eliminan los espacios en blanco al inicio y al final de la cadena
    # Se pide al usuario que introduzca dos números
    print("introduzca los dos numeros que quiere dividir:")
    dividendo = input("introduzca el dividendo : ").strip()
    divisor = input("Introduzca el divisor :").strip()
    
    if not dividendo or not divisor:
        raise ValueError("Los números no pueden estar vacíos.")
    # Se transforman los números a enteros
    dividendo = int(dividendo)
    divisor = int(divisor)
    # Se verifica que el divisor no sea cero
    if divisor == 0:
        raise ValueError("El divisor no puede ser cero.")
    # Se verifica que el dividendo no sea cero
    if dividendo == 0:
        raise ValueError("El dividendo no puede ser cero.")
    # Se verifica que el dividendo y el divisor sean números enteros
    if not isinstance(dividendo, int) or not isinstance(divisor, int):
        raise ValueError("Los números deben ser enteros.")
    # Se verifica que el dividendo y el divisor sean números enteros
    
    # función lambda
    resto= lambda dividendo, divisor: dividendo % divisor

    # Imprimir el resultado
    print(f"el resto es : {resto(dividendo, divisor )}")
    # Se verifica que la cadena no esté vacía
    
except ValueError as e:
    print(f"Error: {e}")
    exit()

# -----------------------------------------------------
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
    
# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

# función para buscar duplicado
# función para buscar duplicado
def duplicado (lista=None):
    """
    Busca el primer elemento duplicado en una lista.
    Parámetro por defecto:
      - lista: [] si no se proporciona
    """
    if lista is None:
        lista = []
    # Se inicializa un conjunto para almacenar los elementos vistos
    elementos_vistos = set() # Conjunto para almacenar elementos únicos
    # Se itera sobre la lista
    for elemento in lista:
        if elemento in elementos_vistos:
            return elemento
        elementos_vistos.add(elemento)
    return None

try:
    entrada = input("Introduce números separados por comas: ").strip()
    if not entrada:
        raise ValueError("La lista está vacía.")
    
    # Normalizar y convertir
    lista = [float(x.strip()) for x in entrada.split(",") if x.strip()]
    
    resultado = duplicado(lista)
    if resultado is None:
        print("No hay elementos duplicados en la lista.")
    else:
        print(f"El primer elemento duplicado de la lista es: {resultado}")

except ValueError as e:
    print(f"Error: {e}")
    
# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.

# función para enmascarar texto
def transformar(variable=""):
    """
    Enmascara todos los caracteres de la variable con '#' excepto los últimos cuatro.
    Parámetro por defecto: variable=""
    """
    longitud = len(variable)
    if longitud <= 4:
        return None # No hay nada que enmascarar
    else:
        return '#' * (longitud - 4) + variable[-4:]


# entrada de la variable 
try:
    entrada = input("Introduce un valor o caracteres que quieras enmascarar con #: ").strip()

    entrada = str(entrada)
    # Se verifica que la cadena no esté vacía
    if not entrada:
        raise ValueError("La variable está vacia")          

    #Visualización y llamada a la función
    resultado = transformar(entrada)
    if resultado is None:
        print("No hay caracteres que enmascarar, la variable tiene una longitud menor de 4")
    else:
        print("Se presentan los caracteres enmascarados con '#' a excepción de los cuatro últimos: ", resultado)
except ValueError as e:
    print(f"Error: {e}")
    
# -----------------------------------------------------
# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.

# función para determinar si las palabras son anagramas
def valora_anagrama(variable_1="", variable_2=""):
    """
    Determina si dos palabras son anagramas.
    Parámetros por defecto:
      - variable_1: "" si no se proporciona
      - variable_2: "" si no se proporciona
    """
    # Se verifica que las palabras no estén vacías
    # Se ponen en minusculas
    variable_1 = variable_1.lower()
    variable_2 = variable_2.lower()
    if len(variable_1) != len(variable_2):
        return None # Las palabras no son anagramas por no tener la misma longitud
    else:
        return sorted(variable_1) == sorted(variable_2)


# entrada de la variable 
try: 
    print("Introduce dos palabras separadas por comas que quieras valorar si son anagramas: ")
    entrada_1 = input("Introduce la primera palabra: ").strip()
    entrada_2 = input("Introduce la segunda palabra: ").strip()
    # Se verifica que la cadena no esté vacía   
    if not entrada_1 or not entrada_2:
        raise ValueError("debe introducir ambas palabras para valorar si son anagramas")

    #Visualización y llamada a la función
    resultado = valora_anagrama(entrada_1,entrada_2)
    if resultado is None:
        print("Las palabras no tienen el mismo tamaño, no son anagramas")
    elif resultado is True:
        print(f"las palabras {entrada_1} y la palabra {entrada_2} son  anagramas")
    else:
        print("Las palabras no son anagramas")
except ValueError as e:
    print(f"Error: {e}")
    
# -----------------------------------------------------   
# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.

# función busqueda de nombre en una lista
def Buscar_nombre (lista=None, nombre=None):
    """
    Busca un nombre en una lista.
    Parámetros por defecto:
      - lista: [] si no se proporciona
      - nombre: None si no se proporciona
    """
    if lista is None or nombre is None:
        raise ValueError("La lista o el nombre no pueden ser nulos.")
    
    # Se verifica que la cadena no esté vacía
    if not lista or not nombre:
        raise ValueError("La lista o el nombre no pueden estar vacíos.")
    
    # Se busca el nombre en la lista
    if nombre in lista:
        print(f"El nombre '{nombre}' fue encontrado en la lista.")
    else:
        raise ValueError(f"El nombre '{nombre}' no fue encontrado en la lista.")     
try: 
    # Entrada de lista de nombre y nombre a buscar
    entrada = input("Introcuce una lista de nombre separados por comas :").strip()
    Nombre_buscar= input("introduce el nombre que deseas buscar : ").strip()
    # Se verifica que la cadena no esté vacía
    if not entrada or not Nombre_buscar:
        raise ValueError("Debe introducir La lista de nombres y el nombre que desea buscar")
    
    #transforma la entrada en una lista sin espacion y separando por comas
    lista_nombre = [nombre.strip().lower() for nombre in entrada.split(",")]
    Nombre_buscar = Nombre_buscar.strip().lower()
    Buscar_nombre(lista_nombre, Nombre_buscar)
except ValueError as e:
    # error en la entrada de datos
    print("Error:", e)

# -----------------------------------------------------
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

# -----------------------------------------------------
# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

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


try:
    entrada = input("Introduzca la hora con formato HH:MM: ").strip()
    # 1) No vacío
    if not entrada:
        raise ValueError("La hora no puede estar vacía.")
    # 2) Formato básico: 5 caracteres y ":" en medio
    if len(entrada) != 5 or entrada[2] != ":":
        raise ValueError("Formato de hora incorrecto. Debe ser HH:MM.")
    h_str, m_str = entrada.split(":")
    # 3) Sólo dígitos
    if not (h_str.isdigit() and m_str.isdigit()):
        raise ValueError("Formato de hora inválido. HH y MM deben ser números enteros.")
    hora = int(h_str)
    minuto = int(m_str)
    # 4) Rangos válidos
    if not (0 <= hora < 24):
        raise ValueError("La hora debe estar entre 00 y 23.")
    if not (0 <= minuto < 60):
        raise ValueError("Los minutos deben estar entre 00 y 59.")

    if 6 <= hora < 12:
        print("Es de mañana ")
    elif 12 <= hora < 20:
        print("Es de tarde ")
    else:
        print("Es de noche ")

except ValueError as e:
    print(f"Error: {e}")
    
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
    
# ------------------------------------------------------
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
    
# ------------------------------------------------------
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
    entrada = input("Introduzca el precio del artículo: ").strip()
    # Se verifica que la cadena no esté vacía
    if not entrada:
        raise ValueError("El precio no puede estar vacío.")
    # Se verifica que el precio sea un número
    if not entrada.replace('.', '', 1).isdigit():
        raise ValueError("El precio debe ser un número válido.")
    # Se transforma la entrada en un número
    # Se reemplaza la coma por un punto para convertir a float
    if ',' in entrada:
        entrada = entrada.replace(',', '.')
    # Se transforma la entrada en un número
    precio = float(entrada.replace(',', '.'))
    # introduce si tiene un cupón y se guarda en una variable booleana
    respuesta = input("¿Tiene cupón de descuento? indique si o no :").strip().lower()
    # Se verifica que la cadena no esté vacía
    if not respuesta:
        raise ValueError("La respuesta no puede estar vacía.")
    # Se verifica que la respuesta sea válida   
    if respuesta not in ["si", "no"]:
        raise ValueError("Debes responder al cupón con 'si' o 'no'")
    Cupon = respuesta == "si"
    
    # Solicitud del valor del cupón
    valor_cupon=0
    if Cupon:
        entrada= input("Introduce el valor del cupón : ").strip()
        # Se verifica que la cadena no esté vacía
        if not entrada:
            raise ValueError("El valor del cupón no puede estar vacío.")
        # Se verifica que el valor del cupón sea un número
        if not entrada.replace('.', '', 1).isdigit():
            raise ValueError("El valor del cupón debe ser un número válido.")
        # Se transforma la entrada en un número
        valor_cupon= float(entrada.replace(',', '.')).s
        # el valor no puede ser negativo
        if valor_cupon < 0:
            raise ValueError("El valor del cupón no puede ser negativo.")
    
    # calculo del precio final   
    precio_final = precio-valor_cupon
    
    print(f"El precio final de la compra es: {precio_final:.2f} €")
        
except ValueError as e:
    print(f"Error en el valor: {e}")
    