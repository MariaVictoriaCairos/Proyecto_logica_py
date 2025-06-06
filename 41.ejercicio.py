# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
# siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
# a cero). Por ejemplo, descuento de 15€.
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
# programa de Python.

try:
    #introduce el precio como variable numerica con decimales
    entrada = input("Introduzca el precio del artículo: ").strip()
    # Se verifica que la cadena no esté vacía
    if not entrada:
        raise ValueError("El precio no puede estar vacío.")
    # Se verifica que el precio sea un número
    if not entrada.replace('.', '', 1).isdigit():
        raise ValueError("El precio debe ser un número válido.")
    # Se transforma la entrada en un número
    # Se reemplaza la coma por un punto para convertir a float
    if ',' in entrada:
        entrada = entrada.replace(',', '.')
    # Se transforma la entrada en un número
    precio = float(entrada.replace(',', '.'))
    # introduce si tiene un cupón y se guarda en una variable booleana
    respuesta = input("¿Tiene cupón de descuento? indique si o no :").strip().lower()
    # Se verifica que la cadena no esté vacía
    if not respuesta:
        raise ValueError("La respuesta no puede estar vacía.")
    # Se verifica que la respuesta sea válida   
    if respuesta not in ["si", "no"]:
        raise ValueError("Debes responder al cupón con 'si' o 'no'")
    Cupon = respuesta == "si"
    
    # Solicitud del valor del cupón
    valor_cupon=0
    if Cupon:
        entrada= input("Introduce el valor del cupón : ").strip()
        # Se verifica que la cadena no esté vacía
        if not entrada:
            raise ValueError("El valor del cupón no puede estar vacío.")
        # Se verifica que el valor del cupón sea un número
        if not entrada.replace('.', '', 1).isdigit():
            raise ValueError("El valor del cupón debe ser un número válido.")
        # Se transforma la entrada en un número
        valor_cupon= float(entrada.replace(',', '.')).s
        # el valor no puede ser negativo
        if valor_cupon < 0:
            raise ValueError("El valor del cupón no puede ser negativo.")
    
    # calculo del precio final   
    precio_final = precio-valor_cupon
    
    print(f"El precio final de la compra es: {precio_final:.2f} €")
        
except ValueError as e:
    print(f"Error en el valor: {e}")