
class Usuario:
    # los atributos de clase se definen en la clase
    nombre_banco = "Primer Dojo Nacional"
    # ¡ahora nuestro método tiene 2 parámetros!
    def __init__(self , name, email_address):
    	# los asignamos en consecuencia
        self.name = name
        self.email = email_address
    	# el balance de la cuenta se establece en $0
        self.balance_cuenta = 0

class Usuario:		# esto es lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    # agregando el método de depósito
    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
    	self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido


guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
seba = Usuario("sebita", "guido@python.com")
maty = Usuario("maty", "name")
matias = Usuario("matias", "guido@python.com")

guido.hacer_depósito(100)



print(guido.name)
print(monty.name)
print(f"bueno pal basquet el {seba.name}")
print(f"bueno pa fumar el {maty.name}")
print(f"mi correo es {matias.name}")


