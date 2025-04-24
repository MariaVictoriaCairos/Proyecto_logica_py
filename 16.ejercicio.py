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