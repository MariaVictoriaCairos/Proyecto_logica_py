# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def Mascotas_España(mascotas):
    Mascotas_prohibidas = ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"]
    Mascotas_permitidas = filter(lambda m: m not in Mascotas_prohibidas, mascotas)
    return list(Mascotas_permitidas)

Mascotas = ["perro","gato","pajaro","caballo","Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"]

print(f"Las mascotas permitidas en españa son: {Mascotas_España(Mascotas)}")