# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.

def calcula_aprobado(notas=None, nota_aprobado=5):
    """
    Calcula la media de 'notas' y determina si es mayor o igual a 'nota_aprobado'.
    Parámetros por defecto:
      - notas: lista vacía si no se provee
      - nota_aprobado: 5
    Devuelve una tupla (media, estado).
    """
    if notas is None or not notas:
        return 0.0, "suspenso"
    
    # Calcular media
    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado

# Pedimos la lista de notas al usuario
entrada_notas = input("Introduce las notas separadas por comas: ").strip()
if not entrada_notas:
    print("No se ingresaron notas.")
else:
    # Normalizar y convertir cada elemento a float
    lista_notas = [float(x.strip()) for x in entrada_notas.split(",") if x.strip()]
    
    # Pedimos la nota de corte (opcional)
    entrada_corte = input("Introduce la nota de aprobado (por defecto 5): ").strip()
    if entrada_corte:
        try:
            nota_corte = float(entrada_corte)
        except ValueError:
            print("Valor inválido para nota de aprobado. Se usará 5.")
            nota_corte = 5
    else:
        nota_corte = 5

    # Llamada a la función
    media, estado = calcula_aprobado(lista_notas, nota_corte)
    print(f"La nota media es {media:.2f} y el estado es: {estado}")
