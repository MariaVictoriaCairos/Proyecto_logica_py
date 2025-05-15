# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

# Entrada de los numeros
try:
    # Se pide al usuario que introduzca dos números
    # Se eliminan los espacios en blanco al inicio y al final de la cadena
    # Se pide al usuario que introduzca dos números
    print("introduzca los dos numeros que quiere dividir:")
    dividendo = input("introduzca el dividendo : ").strip()
    divisor = input("Introduzca el divisor :").strip()
    
    if not dividendo or not divisor:
        raise ValueError("Los números no pueden estar vacíos.")
    # Se transforman los números a enteros
    dividendo = int(dividendo)
    divisor = int(divisor)
    # Se verifica que el divisor no sea cero
    if divisor == 0:
        raise ValueError("El divisor no puede ser cero.")
    # Se verifica que el dividendo no sea cero
    if dividendo == 0:
        raise ValueError("El dividendo no puede ser cero.")
    # Se verifica que el dividendo y el divisor sean números enteros
    if not isinstance(dividendo, int) or not isinstance(divisor, int):
        raise ValueError("Los números deben ser enteros.")
    # Se verifica que el dividendo y el divisor sean números enteros
    
    # función lambda
    resto= lambda dividendo, divisor: dividendo % divisor

    # Imprimir el resultado
    print(f"el resto es : {resto(dividendo, divisor )}")
    # Se verifica que la cadena no esté vacía
    
except ValueError as e:
    print(f"Error: {e}")
    exit()
