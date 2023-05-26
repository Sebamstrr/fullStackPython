class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.balance = 0
    
    def hacer_deposito(self, amount):
        self.balance += amount
    
    def hacer_retiro(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("No hay suficiente saldo en la cuenta.")
    
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}, Balance: ${self.balance}")
    
    def transfer_dinero(self, other_user, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_user.hacer_deposito(amount)
            print(f"Transferencia exitosa. Se transfirieron ${amount} a {other_user.nombre}.")
        else:
            print("No hay suficiente saldo en la cuenta para realizar la transferencia.")

# Ejemplo de uso de la clase Usuario y los métodos adicionales

# Crear dos instancias de Usuario
usuario1 = Usuario("Guido van Rossum")
usuario2 = Usuario("Linus Torvalds")

# Realizar depósitos en las cuentas de los usuarios
usuario1.hacer_deposito(200)
usuario2.hacer_deposito(500)

# Mostrar el balance de las cuentas
usuario1.mostrar_balance_usuario()  # Usuario: Guido van Rossum, Balance: $200
usuario2.mostrar_balance_usuario()  # Usuario: Linus Torvalds, Balance: $500

# Hacer retiro de una cuenta
usuario1.hacer_retiro(50)
usuario1.mostrar_balance_usuario()  # Usuario: Guido van Rossum, Balance: $150

# Transferir dinero entre usuarios
usuario1.transfer_dinero(usuario2, 100)
usuario1.mostrar_balance_usuario()  # Usuario: Guido van Rossum, Balance: $50
usuario2.mostrar_balance_usuario()  # Usuario: Linus Torvalds, Balance: $600
