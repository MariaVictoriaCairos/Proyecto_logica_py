# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
# función filter()
def buscar_por_letra(paises, letra):
    return list(filter(lambda pais: pais[0].lower() == letra.lower(), paises))

Lista_paises = ["Argentina", "Brasil", "Canadá", "China", "Egipto", "España", "Colombia", "Estados Unidos", "Francia", "India", "Italia", "Japón", "México", "Nigeria", "Sudáfrica", "Turquía"]

entrada=input("introcuce la letra de busqueda : ")


paises_filtro = buscar_por_letra(Lista_paises,entrada)
print(f"Lista de paises que comienzan por la letra '{entrada}': ")
for pais in paises_filtro:
    print(pais)
