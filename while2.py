while True: 
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação: (+ , - , * , /) ou 'sair' para parar: ")
    
    if operacao == "sair":
        break
    
    if operacao == "+":
        print(f"Resultado: { num1 + num2}")
    elif operacao == "-":
        print(f"Resultado: { num1 - num2}")
    elif operacao == "*":
        print(f"Resultado: { num1 * num2}")
    elif operacao == "/":
        if num2 != 0:
            print(f"Resultado: { num1 / num2}")
        else:
            print("Erro: divisão por zero.")
    else:
        print("operação inválida!")
        