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