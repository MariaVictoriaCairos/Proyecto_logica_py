# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
# filter()
# Lectura y normalización de la entrada
entrada = input("Introduce una lista de elementos separados por comas: ").strip()
if not entrada:
    print("La lista de elementos está vacía.")
else:
    # Crear lista de cadenas limpias, sin elementos vacíos
    elementos_raw = list(filter(None, map(str.strip, entrada.split(","))))
    if not elementos_raw:
        print("La lista de elementos está vacía.")
    else:
        # Parsear cada elemento a int, float o str
        elementos = []
        for e in elementos_raw:
            try:
                elementos.append(int(e))
            except ValueError:
                try:
                    elementos.append(float(e))
                except ValueError:
                    elementos.append(e)

        # Filtrar solo los enteros usando filter()
        enteros = list(filter(lambda x: isinstance(x, int), elementos))
        if enteros:
            print("Los elementos de la lista que son enteros son:")
            for n in enteros:
                print(n)
        else:
            print("No hay elementos enteros en la lista.")
