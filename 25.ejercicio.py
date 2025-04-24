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