class Calculadora:
    def __init__(self):
        pass

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            print("Error: No se puede dividir entre cero.")
            return None


calculadora = Calculadora()

print("Suma:", calculadora.suma(5, 3))  # Salida: 8
print("Resta:", calculadora.resta(5, 3))  # Salida: 2
print("Multiplicación:", calculadora.multiplicacion(5, 3))  # Salida: 15
print("División:", calculadora.division(10, 2))  # Salida: 5.0
print("División entre cero:", calculadora.division(10, 0))  # Salida: Error: No se puede dividir entre cero.

