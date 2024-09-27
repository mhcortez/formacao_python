capitais = {}  # Define um dicionário vazio

while True:
    nome_do_estado = input("Nome do estado: ")  # Nome do estado
    nome_da_capital = input("Nome da capital deste estado: ")  # Nome da capital do estado

    capitais[nome_do_estado] = nome_da_capital  # Insere o conjunto no dicionário

    opcao = int(input("DIGITE '1' PARA CADASTRAR OUTRO CONJUNTO E '0' PARA ENCERRAR: "))

    if opcao == 0:  # Verifica se o usuário deseja encerrar
        break  # Encerra o laço

print(capitais)
# {'Tocantins': 'Palmas', 'São Paulo': 'São Paulo'}
print("*"*40)

for chave, valor in capitais.items():
    print(f"{chave}: {valor}")
print("*"*40)

for valor in capitais.keys():
    print(valor)
print("*"*40)

for valor in capitais.values():
    print(valor)
print("*"*40)
        