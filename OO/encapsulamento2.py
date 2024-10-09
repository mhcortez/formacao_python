class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
           
    @property #get
    def nome(self):
        return self.__nome
    
    @property #get
    def idade(self):
        return self.__idade   
    
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome,str) and novo_nome.strip():
            self.__nome = novo_nome
        else:
            print("nome invalido")
            
    @idade.setter
    def idade(self, nova_idade):
        if isinstance(nova_idade,int) and nova_idade > 0:
            self.__idade = nova_idade
        else:
            print("idade invalido")
    
        
pessoa = Pessoa("Alice", 30)        
print(pessoa.nome)
print(pessoa.idade)

#print(pessoa.__nome)