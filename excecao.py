'''
try:
    arquivo= open('dados.txt', 'r')
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo nao existe")
else:
    print(conteudo)
finally:
    print("Operação finalizada")
'''

'''
try:
    resultado = int(input("Digite um DIVISOR")
    resultado = 10/0
except ValueError:
    print("Erro: Voce deve digitar um numero inteiro")
except ZeroDivisionError:
    print("Erro: Não é permitido divisão por 0")
else:
    print(f"O resultado é {resultado}")
finally:
    print("Obrigado pela atenção")
'''
'''
idade = int(input("Digite a idade: "))
def verifica_idade(idade):    
    if idade < 18:
        raise ValueError("Idade deve ser maior ou igual a 18.")
    else:
        print("Entrada permitida.")
try:
    verifica_idade(idade)
except ValueError as e:
    print(e)
'''

class SaldoInsuficienteError(Exception):
    """Exceção levantada quando o saldo é insuficiente para realizar uma transacao"""
    pass
def sacar(valor, saldo):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para sacar o valor solicitado.")
    saldo -= valor
    return saldo

try:
    saldo_atual = sacar(100, 1000)
except SaldoInsuficienteError as e:
    print(e)