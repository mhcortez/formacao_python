#x = 15
#print ("par" if x % 2 == 0 else "impar")
#x = 10
#print (x % 2 == 0 and "par" or "impar")

valorSalario = int(input("Digite o valor do salário: "))
valorEmprestimo = int(input("Digite o valor do emprestimo: "))

if (valorEmprestimo <= (valorSalario * 0.5 )):
    print("Emprestimo aprovado!") 
elif ((valorEmprestimo > (valorSalario * 0.5 )) and (valorEmprestimo <= (valorSalario * 0.75))):
    print("Ficará em análise!")
else:
    print("Emprestimo não aprovado")