lista1 = [1,2,3,4,5]

#Tamanhos
print(lista1)
print("tamanho da lista: " + str(len(lista1)) )
print("-"*40)
#posicao
print("posicao 3 da lista: " + str(lista1[3]))
print("intervalo da lista: " + str(lista1[0:3]))
print("-"*40)
#operacoes
print("Adicionando")
lista1.append(6)
lista1.append(6)
print("novo tamanho da lista: " + str(len(lista1)))
print(lista1)
print("Removendo")
lista1.remove(5)
print("novo tamanho da lista: " + str(len(lista1)))
print(lista1)
print("-"*40)
#ordenar
print("ordenando")
lista1.reverse()
print(lista1)
lista1.sort()
print(lista1)
print("-"*40)
#buscando
print("buscando")
print("O objeto '3' na lista esta no indice: " + str(lista1.index(3)))
print("-"*40)
#contando ocorrencias
print("buscando")
print("O objeto '6' aparece " + str(lista1.count(6))+ " vezes na lista" )
print("-"*40)
#fatiando listas
