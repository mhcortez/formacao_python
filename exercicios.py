nomeHotel = input("Digite o nome do hotel : ")
cidade = input("Digite a sua cidade : ")
estrelas = float(input("Digite a quantidade de estrelas (1 a 5): "))

print(cidade[0:8])

qtdnome = len(nomeHotel)
qtdcidade = len(cidade)

if qtdnome >= 6 :
    print(nomeHotel[0:6])
else:   
    print(nomeHotel)
    
if qtdcidade >= 8 :
    print(cidade[0:6])
else:   
    print(nomeHotel)   