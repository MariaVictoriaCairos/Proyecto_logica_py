#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
#todas las palabras que sean más largas que n. Usa la función filter()

# Valida que la entrada no sea 0
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