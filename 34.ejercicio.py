#34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer tronco , nueva rama , crecer ramas , quitar rama e info arbol . El objetivo es implementar estos métodos para
# manipular la estructura del árbol.
# Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método crecer tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método nueva rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método crecer ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método quitar rama para eliminar una rama en una posición específica.
# 6. Implementar el método info arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
# mismas.
# Caso de uso:
# 1. Crear un árbol.
# 2. Hacer crecer el tronco del árbol una unidad.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.

class Arbol:
    def __init__(self):
        self.tronco = 5  # Longitud inicial del tronco
        self.ramas = []  # Lista vacía de ramas

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)  # Cada nueva rama tiene longitud 1

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            del self.ramas[posicion]
        else:
            print(f"No se puede eliminar la rama en la posición {posicion} (índice inválido).")

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

# 1. Crear un árbol
mi_arbol = Arbol()

# 2. Hacer crecer el tronco una unidad
mi_arbol.crecer_tronco()

# 3. Añadir una nueva rama
mi_arbol.nueva_rama()

# 4. Hacer crecer todas las ramas
mi_arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()

# 6. Retirar la rama en la posición 2 (índice 2)
mi_arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol
info = mi_arbol.info_arbol()
print("Información del árbol:")
print(f"Longitud del tronco: {info['longitud_tronco']}")
print(f"Número de ramas: {info['numero_ramas']}")
print(f"Longitudes de las ramas: {info['longitudes_ramas']}")
