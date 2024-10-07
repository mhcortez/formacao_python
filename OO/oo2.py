class Circulo:
    pi = 3.14159

    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return self.pi * self.raio ** 2

Circulo1 = Circulo(10)
Circulo1.calcular_area()
print(Circulo1.calcular_area())