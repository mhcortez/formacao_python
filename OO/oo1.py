from datetime import date

class Pessoa:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
        
    def AnoNascimento(self):
        ano = date.today().year - self.idade
        print(f"O ano do nascimento de {self.nome} é: " + str(date.today().year - self.idade))
        print(f"O ano do nascimento de {self.nome} é: {ano}")       

pessoa1 = Pessoa("Maria",30)        
print(pessoa1.nome)
print(pessoa1.idade)
pessoa1.apresentar()
pessoa1.AnoNascimento()

'''
pessoa2 = Pessoa("Chico", 40)
print(pessoa2.nome)
print(pessoa2.idade)
pessoa2.apresentar()
pessoa2.AnoNascimento()
'''