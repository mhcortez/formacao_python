import os
conta = {}  # Define um dicionário vazio

def desenha_tela():
    print("_"*60)
    print("|  MENU "+" "*51+"|")
    print("|"+" "*59+"|")
    print("|         Escolha uma opção: "+" "*40+"|")
    print("|         1 - CRIAR CONTA: "+" "*56+"|")
    print("|         2 - LISTAR CONTA: "+" "*56+"|")
    print("|         3 - DEPOSITAR: "+" "*58+"|")
    print("|         4 - SACAR: "+" "*61+"|")
    print("|         5 - ENCERRAR: "+" "*69+"|")
    print("|"+" "*88+"|")
    print("-"*90)
    
desenha_tela()
while True:      
    opcao = int(input("DIGITE OPÇÃO : "))

    if opcao == 5:  
        break  # Encerra o laço
    elif opcao == 1:
        cliente = input("Nome do Cliente: ")  
        numero_da_Conta = float(input("Numero da Conta: "))
        valor_saldo = float(input("Digite o Saldo: "))
        
        conta[cliente] = cliente
        conta[numero_da_Conta] = numero_da_Conta
        conta[valor_saldo] = valor_saldo                
        os.system("cls")
        desenha_tela()
    elif opcao == 3:
        nome_do_produto = input("Nome do Cliente: ")        
        #if (nome_do_produto in compras):
        #    del compras[nome_do_produto]
        #    os.system("cls")
        #    desenha_tela()
        #else:
        #    print("Não existe o produto" + nome_do_produto + " na lista")
    elif opcao == 2:
        for chave, valor in conta.items():             
            print(f"{chave}: {valor}")      
            print("")      
    else:
        print("Opção Não existe no MENU")
        break
        os.system("cls")
    
    