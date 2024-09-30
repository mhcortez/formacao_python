#numeros_pares = [i for i in range(1,10)] # if i % 2 == 0]
#print(numeros_pares)

palavra =  "python"
count = 0
for letra in palavra:    
    print(letra, str(count))
    count = count + 1
print("*"*40)

palavra = "python"
for i in palavra:
    print(f"A letra {i} tem indice {palavra.index()}")
print("*"*40)

it = ['p','y','t']
for indice, item in enumerate(it):
    print(indice, item)
print("*"*40)   

itens = ['maçã', 'banana', 'cereja']
for indice, item in enumerate(itens):
    print(indice, item)
print("*"*40)

palavra = "python"
for i in enumerate(palavra):
    print(f"A letra {i} tem indice {enumerate(palavra)}")
print("*"*40)  