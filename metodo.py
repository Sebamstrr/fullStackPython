class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.saldo = 0
    
    def hacer_deposito(self, monto):
        self.saldo += monto
        return self
    
    def hacer_retiro(self, monto):
        self.saldo -= monto
        return self
    
    def mostrar_balance_usuario(self):
        print(f"El saldo de {self.nombre} es: {self.saldo}")
        return self

guido = Usuario("Guido")
guido.hacer_deposito(110).hacer_deposito(200).hacer_deposito(200).hacer_retiro(50).mostrar_balance_usuario()
