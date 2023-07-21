class CuentaBancaria:
    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance

    def deposito(self, cantidad):
        self.balance += cantidad

    def retiro(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
        else:
            print("No hay suficiente dinero en la cuenta.")

    def mostrar_info_cuenta(self):
        print("dinero actual: ", self.balance)
        print("Tasa de interés: ", self.tasa_interes)

    def generar_interes(self):
        intereses = self.balance * self.tasa_interes
        self.balance += intereses



# Crear 2 cuentas
cuenta1 = CuentaBancaria(0.05, 1000)
cuenta2 = CuentaBancaria(0.03, 500)

# Operaciones en la primera cuenta
cuenta1.deposito(100)
cuenta1.deposito(200)
cuenta1.deposito(300)
cuenta1.retiro(400)
cuenta1.generar_interes()
cuenta1.mostrar_info_cuenta()

# Operaciones en la segunda cuenta
cuenta2.deposito(50)
cuenta2.deposito(100)
cuenta2.retiro(75)
cuenta2.retiro(125)
cuenta2.retiro(50)
cuenta2.generar_interes()
cuenta2.mostrar_info_cuenta()
