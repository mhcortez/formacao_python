'''
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        print(f'{self.nome} fez algum som')
    
class Cachorro(Animal):
    pass

class Gato(Animal):
    pass
    
dog = Cachorro('Rex')

gato = Gato('Miau')

dog.emitir_som()

gato.emitir_som()
'''

class cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
    
    def pedir_emprestimo(self):
        print(f'{self.nome} pediu um empréstimo')
    
class cliente_especial(cliente):
    pass

class cliente_normal(cliente):
    pass

rico = cliente_especial('Rico', 'rico@gmail.com', '99999999999')
liso = cliente_normal('Liso', 'liso@gmail.com', '99999999999')

rico.pedir_emprestimo()
liso.pedir_emprestimo()