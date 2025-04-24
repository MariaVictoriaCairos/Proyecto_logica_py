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