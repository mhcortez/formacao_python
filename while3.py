import os
compras = {}  # Define um dicionário vazio

def desenha_tela():
    print("_"*90)
    print("|  MENU "+" "*81+"|")
    print("|"+" "*88+"|")
    print("|         Escolha uma opção: "+" "*60+"|")
    print("|         1 - ADICIONAR PRODUTO: "+" "*56+"|")
    print("|         2 - REMOVER PRODUTO: "+" "*58+"|")
    print("|         3 - EXIBIR LISTA: "+" "*61+"|")
    print("|         4 - Sair: "+" "*69+"|")
    print("|"+" "*88+"|")
    print("-"*90)
    
desenha_tela()
while True:      
    opcao = int(input("DIGITE OPÇÃO : "))

    if opcao == 4:  
        break  # Encerra o laço
    elif opcao == 1:
        nome_do_produto = input("Nome do Produto: ")  
        valor_do_produto = float(input("Valor do Produto: "))
        compras[nome_do_produto] = valor_do_produto  
        os.system("cls")
        desenha_tela()
    elif opcao == 2:
        nome_do_produto = input("Nome do Produto: ")        
        if (nome_do_produto in compras):
            del compras[nome_do_produto]
            os.system("cls")
            desenha_tela()
        else:
            print("Não existe o produto" + nome_do_produto + " na lista")
    elif opcao == 3:
        for chave, valor in compras.items():             
            print(f"{chave}: {valor}")      
            print("")      
    else:
        print("Opção Não existe no MENU")
        break
        os.system("cls")
    
    