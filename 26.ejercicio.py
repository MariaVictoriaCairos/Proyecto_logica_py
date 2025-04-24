# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

# Entrada de los numeros
print("introduzca los dos numeros que quiere dividir:")
dividendo = int(input("introduzca el dividendo : "))
divisor = int(input("Introduzca el divisor :"))

# función lambda
resto= lambda dividendo, divisor: dividendo % divisor

# Imprimir el resultado
print(f"el resto es : {resto(dividendo, divisor )}")