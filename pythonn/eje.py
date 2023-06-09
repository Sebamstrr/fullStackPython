
class MathDojo:
    def __init__(self):
        self.result = 0
    
    def sumar(self, *nums):
        for num in nums:
            self.result += num
        return self
    
    def restar(self, *nums):
        for num in nums:
            self.result -= num
        return self

md = MathDojo()

x = md.sumar(2).sumar(2, 5, 1).sumar(4, 4, 6).result
print(x)

y = md.restar(2).restar(3, 1).restar(5, 2, 4).result
print(y)
