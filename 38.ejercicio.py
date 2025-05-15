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
