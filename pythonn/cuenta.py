class CuentaBancaria:
    def __init__(self, tasa_interes, balance=0):
        self.tasa_interes = tasa_interes
        self.balance = balance
    
    def deposito(self, amount):
        self.balance += amount
    
    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
    
    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}")
    
    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interes

cuenta1 = CuentaBancaria(0.02, 500)
cuenta2 = CuentaBancaria(0.05)

cuenta1.deposito(100).deposito(200).deposito(300).retiro(50).generar_interes().mostrar_info_cuenta()
cuenta2.deposito(50).deposito(100).retiro(20).retiro(30).retiro(40).retiro(50).generar_interes().mostrar_info_cuenta()

