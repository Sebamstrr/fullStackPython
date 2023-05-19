class Usuario:
    def __init__(self, nombre, email, password, balance):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.balance = balance

    def iniciar_sesion(self, email, password):
        if email == self.email and password == self.password:
            print(f"Bienvenido/a, {self.nombre}!")
        else:
            print("Email o contraseña incorrectos.")

    def cerrar_sesion(self):
        print(f"Adiós, {self.nombre}!")

    # NUEVO MÉTODO: hacer_retiro
    def hacer_retiro(self, amount):
        if amount > self.balance:
            print("No puedes retirar más de lo que tienes en tu cuenta.")
        else:
            self.balance -= amount
            print(f"Se ha retirado {amount} de tu cuenta. Nuevo balance: {self.balance}")

    # NUEVO MÉTODO: mostrar_balance_usuario
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}, Balance: ${self.balance}")

    # BONUS: transfer_dinero
    def transfer_dinero(self, other_user, amount):
        if amount > self.balance:
            print("No puedes transferir más de lo que tienes en tu cuenta.")
        else:
            self.balance -= amount
            other_user.balance += amount
            print(f"Se han transferido {amount} a {other_user.nombre}. Nuevo balance de {self.nombre}: {self.balance}. Nuevo balance de {other_user.nombre}: {other_user.balance}")

# Creamos dos instancias de Usuario
usuario1 = Usuario("Juan Pérez", "juan@gmail.com", "contraseña1", 1000)
usuario2 = Usuario("María García", "maria@gmail.com", "contraseña2", 500)

# Probamos el método hacer_retiro en usuario1
usuario1.hacer_retiro(500)
usuario1.hacer_retiro(600) # Esto debería imprimir "No puedes retirar más de lo que tienes en tu cuenta."

# Probamos el método mostrar_balance_usuario en ambas instancias
usuario1.mostrar_balance_usuario() # Esto debería imprimir "Usuario: Juan Pérez, Balance: $500"
usuario2.mostrar_balance_usuario() # Esto debería imprimir "Usuario: María García, Balance: $500"

# Probamos el método transfer_dinero
usuario1.transfer_dinero(usuario2, 200) # Esto debería imprimir "Se han transferido 200 a María García. Nuevo balance de Juan Pérez: 300. Nuevo balance de María García: 700"
usuario1.mostrar_balance_usuario() # Esto debería imprimir "Usuario: Juan Pérez, Balance: $300"
usuario2.mostrar_balance_usuario() # Esto debería imprimir "Usuario: María García, Balance: $700"
