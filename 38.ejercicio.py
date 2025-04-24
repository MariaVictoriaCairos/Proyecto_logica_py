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
