def saudacao():
    print("Olá , bem vindo(a) à aula de funções em Python! ")
saudacao()
print("-"*90)

def imprime_nome(nome):
    print(f"Nome: {nome}")
imprime_nome("Marcelo")
print("-"*90)

def flor(flor, cor):
    print(f"A cor da {flor} é {cor}")
flor("Rosa", "vermelha")
flor("Orquídea", "Azul")
print("-"*90)

def somar(a, b):
    return a +b
resultado = somar(1, 2)
print(resultado)
print(f"O resultado é : {somar(2,3)}")
print("-"*90)

def saudacao(nome="aluno"):
    print(f"olá, {nome}")
saudacao()
saudacao("carlos")
print("-"*90)

def checar_numero(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "zero"
print(checar_numero(10))
print("-"*90)

def multiplicacao(valor1, valor2): return valor1 * valor2 
print(f"o resultado da multiplicação {multiplicacao(5,2)}")
print("-"*90)

# *Args - Armazena multiplos argumentos numa Tupla
def somar_todos(*args):
    return sum(args)
print(f"O resultado da soma é: {somar_todos(1,2,3,4,5)}")
print("-"*90)

# *Kargs - Armazena multiplos argumentos num dicionario
def exibir_detalhes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
exibir_detalhes(nome="Carlos", idade=30, cidade="Recife")
