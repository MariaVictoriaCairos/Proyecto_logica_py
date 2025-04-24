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
