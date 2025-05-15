# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def Mascotas_Espana(mascotas=None):
    """
    Filtra de la lista 'mascotas' aquellas no permitidas en España.
    Parámetro por defecto:
      - mascotas: [] (lista vacía) si no se proporciona
    Devuelve una lista usando filter().
    """
    if mascotas is None:
        mascotas = []
    prohibidas = {"mapache", "tigre", "serpiente pitón", "cocodrilo", "oso"}
    # Primero normalizamos con strip(), luego filtramos con filter()
    mascotas_norm = map(lambda m: m.strip(), mascotas)
    permitidas = filter(
        lambda m: m and m.lower() not in prohibidas,
        mascotas_norm
    )
    return list(permitidas)

# --- Entrada interactiva ---
entrada = input("Introduce una lista de mascotas separadas por comas: ").strip()

if not entrada:
    print("No se ingresaron mascotas.")
else:
    lista_mascotas = [m for m in entrada.split(",")]
    permitidas = Mascotas_Espana(lista_mascotas)
    if permitidas:
        print(f"Las mascotas permitidas en España son: {permitidas}")
    else:
        print("No hay mascotas permitidas en la lista proporcionada.")

