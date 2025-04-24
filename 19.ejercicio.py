# 19. Crea una función lambda que filtre los números impares de una lista dada.

# lista de números
numeros= [1,2,3,4,5,6,7,8,9,10]

#filtro de los impares
impares = filter(lambda x: x%2 !=0, numeros)

print("los numeros impares son: ")
for impar in impares:
    print(impar)