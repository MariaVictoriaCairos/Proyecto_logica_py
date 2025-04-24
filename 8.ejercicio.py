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
