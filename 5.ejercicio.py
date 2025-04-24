# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.

def calcula_aprobado(notas, nota_aprobado):
    media = sum(notas)/len(notas)
    if media>= nota_aprobado:
        estado="Aprobado"
    else:
        estado="suspenso"
    return(media,estado)


notas = [4,6,7,7]
aprobado= 5
resultado = calcula_aprobado(notas, aprobado)

print(f"La nota media es {resultado[0]:.2f} y el estado es: {resultado[1]}")