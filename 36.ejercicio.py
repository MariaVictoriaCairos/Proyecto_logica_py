# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
# agregar dinero al saldo.
# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False.
# 2. Implementar el método retirar dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
# poder hacerse.
# 3. Implementar el método transferir dinero para realizar una transferencia desde otro usuario al usuario actual.
# Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar dinero para agregar dinero al saldo del usuario.
# 
# Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
# PROYECTO LÓGICA: Katas de Python 2
# 2. Agregar 20 unidades de saldo de "Bob"
# .
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# 4. Retirar 50 unidades de saldo a "Alicia".

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, dinero):
        try:
            if not self.cuenta_corriente:
                raise PermissionError(f"{self.nombre} no tiene cuenta corriente. No puede retirar dinero.")
            if dinero > self.saldo:
                raise ValueError("El saldo de su cuenta no es suficiente.")
            self.saldo -= dinero
            print(f"{self.nombre} retiró {dinero}. Saldo actual: {self.saldo}")
        except (ValueError, PermissionError) as e:
            print(f"Error al retirar dinero: {e}")

    def transferir_dinero(self, dinero, otro_usuario):
        try:
            if not self.cuenta_corriente or not otro_usuario.cuenta_corriente:
                raise PermissionError("Ambos usuarios deben tener cuenta corriente para transferencias.")
            if dinero > otro_usuario.saldo:
                raise ValueError(f"{otro_usuario.nombre} no tiene saldo suficiente para transferir.")
            otro_usuario.saldo -= dinero
            self.saldo += dinero
            print(f"{otro_usuario.nombre} transfirió {dinero} a {self.nombre}.")
        except (ValueError, PermissionError) as e:
            print(f"Error al transferir dinero: {e}")

    def agregar_dinero(self, dinero):
        if dinero > 0:
            self.saldo += dinero
            print(f"{self.nombre} recibió {dinero}. Saldo actual: {self.saldo}")
        else:
            print("No se puede agregar una cantidad negativa o cero.")

# casos de uso
# 1. Crear dos usuarios
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 unidades al saldo de Bob
bob.agregar_dinero(20)  # Saldo de Bob ahora: 70

# 3. Transferir 80 unidades de Bob a Alicia
alicia.transferir_dinero(80, bob)  # Saldo de Bob: -10 no permitido, así que da error si no tiene saldo suficiente

# 4. Retirar 50 unidades de Alicia
alicia.retirar_dinero(50)

# 5. Ver el saldo de Alicia y de bob
print(f"El saldo final de {alicia.nombre} es {alicia.saldo}")
print(f"El saldo final de {bob.nombre} es {bob.saldo}")
        

        
        
   