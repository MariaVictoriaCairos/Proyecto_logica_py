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
