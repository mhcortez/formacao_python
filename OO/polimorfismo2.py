class Animal:                   
    def movimento(self):
        pass

class Terreste(Animal):
    def movimento(self):
        print("Andar")

class Aquatico(Animal):
    def movimento(self):
        print("Nadar")

class Aereo(Animal):
    def movimento(self):
        print("Voar")

animais = [Terreste(), Aquatico(), Aereo()]

for i in animais:
    i.movimento()
    