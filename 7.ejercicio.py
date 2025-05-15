## 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def mi_string(lista=None):
    """
    Convierte una lista de tuplas en una lista de strings.
    Parámetros por defecto:
      - lista: [] (lista vacía) si no se proporciona
    """
    if lista is None:
        lista = []
    # Para cada tupla: convierte cada elemento a str, strip() y une con espacios
    return list(map(
        lambda tupla: " ".join(map(lambda x: str(x).strip(), tupla)),
        lista
    ))

# --- Entrada del usuario ---
entrada = input("Introduce tus tuplas separadas por ';' (ejemplo: 1,2;  foo, bar; 3 ,4): ").strip()

if not entrada:
    print("No se ingresaron tuplas.")
else:
    # Normalizar y parsear la entrada
    tuplas_raw = [t.strip() for t in entrada.split(";") if t.strip()]
    lista_de_tuplas = []
    for t in tuplas_raw:
        elementos = [e.strip() for e in t.split(",") if e.strip()]
        # Opcional: convertir a int si es dígito
        lista_de_tuplas.append(tuple(
            int(e) if e.isdigit() else e
            for e in elementos
        ))

    # Llamada a la función
    resultado = mi_string(lista_de_tuplas)
    print(f"Mi lista de tuplas es {lista_de_tuplas}, al transformarla en lista de strings el resultado es {resultado}")

 