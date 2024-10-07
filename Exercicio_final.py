import os
conta = {}  # Define um dicionário vazio

def desenha_tela():
    print("_"*60)
    print("|  MENU "+" "*52+"|")
    print("|"+" "*59+"|")
    print("|         Escolha uma opção: "+" "*31+"|")
    print("|         1 - CRIAR CONTA: "+" "*33+"|")
    print("|         2 - LISTAR CONTA: "+" "*32+"|")
    print("|         3 - DEPOSITAR: "+" "*35+"|")
    print("|         4 - SACAR: "+" "*39+"|")
    print("|         5 - ENCERRAR: "+" "*36+"|")
    print("|"+" "*59+"|")
    print("-"*60)
    
#TODO: Desacoplar tudo em funcoes
#TODO: Tentar usar aquivos separados
#TODO: Tentar usar classe para conta
#TODO: fazer documentação
#FIXME:usar tratamento de erros personalizados

desenha_tela()
while True:      
    opcao = int(input("DIGITE OPÇÃO : "))

    if opcao == 5:  # Encerra o programa
        break  
    
    elif opcao == 1: # Cria uma nova conta
        if (len(conta) <= 0 ): 
            cliente = input("Nome do Cliente: ")  
            numero_da_Conta = float(input("Numero da Conta: "))
            valor_saldo = float(input("Digite o Saldo: "))
            
            conta["cliente"] = cliente
            conta["conta"] = numero_da_Conta
            conta["saldo"] = valor_saldo                
            os.system("cls")
            desenha_tela()
        else:
            print("Já existe conta cadastrada.")
        
    elif opcao == 2: #Listar conta
        if (len(conta) > 0 ):           
            for chave, valor in conta.items():             
                print(f"{chave}: {valor}")      
                print("")      
        else:
            print("Não existe conta cadastrada")
            
    elif opcao == 3: #Depositar
        nome_do_cliente = input("Nome do Cliente: ")        
        if (nome_do_cliente in conta.values()):
            valor_deposito = float(input("Valor do Depósito: "))
            saldo = conta.get("saldo")
            novo_saldo = saldo + valor_deposito            
            conta.update({'saldo':novo_saldo})
            print(f"O novo saldo da conta é: {conta['saldo']}")            
        else:
            print("Não existe conta para do correntista :" + nome_do_cliente)
    
    elif opcao == 4: #Sacar        
        nome_do_cliente = input("Nome do Cliente: ")        
        if (nome_do_cliente in conta.values()):
            valor_saque = float(input("Valor do Saque: "))
            saldo = conta.get("saldo")
            if (saldo >= valor_saque):
                novo_saldo = saldo - valor_saque
                conta.update({'saldo':novo_saldo})
                print("Saque efetuado com sucesso!")
                print(f"O novo saldo da conta é: {conta['saldo']}")            
            else:
                print("O valor solicitado é maior que o valor disponível no saldo.")                           
        else:
            print("Não existe conta para do correntista  : " + nome_do_cliente)                
        
    else:
        print("Opção Não existe no MENU")
        break
        os.system("cls")
       
    
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