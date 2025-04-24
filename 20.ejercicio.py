# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
# filter()

# lista de elementos
elementos= [2,"f",4,5,4.3,"D"]

elementos_int = filter(lambda x: isinstance(x, int), elementos)

print("Los elementos de la lista que son enteros son : ")
for elemento in elementos_int:
    print(elemento)