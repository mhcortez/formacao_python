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
try:
    resultado = 10/0
except ZeroDivisionError:
    print("Erro: Não é permitido divisão por 0")
else:
    print(f"O resultado é {resultado}")
finally:
    print("Bloco finaly")
'''