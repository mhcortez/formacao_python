frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)
    
print("*"*40)

notas = {
    'Potuguês': 7, 
    'Matemática': 9, 
    'Lógica': 7, 
    'Algoritmo': 7
}
print("*"*40)

for chave, valor in notas.items():
    print(f"{chave}: {valor}")

for i in range(1,5):
 print(i)

teste = [i for i in range(1,5)]
print(teste)
print("*"*40)


for i in range(0,10, 2):
 print(i)