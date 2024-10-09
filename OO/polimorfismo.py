class Animal:
    def fazer_som(self):
        pass #metodo abstrato

class cachorro(Animal):
    def fazer_som(self):
        print("Au Au!")

class gato(Animal):
    def fazer_som(self):
        print("Miau!")

animais = [cachorro(), gato()]

for i in animais:
    i.fazer_som()
