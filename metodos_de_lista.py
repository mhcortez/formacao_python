#Append
lista1 = [1,2,3]
print(lista1)

lista1.append("Python")
lista1.append("java")
lista1.append('php')
lista1.append('c#')
print(lista1)
lista1.reverse()
print(lista1)
print("Tamanho da lista  " + str(len(lista1)))

#insert
#lista1.insert(2, "c++")
#print(lista1)

#lista1.remove(1)
#print(lista1)
#print(2 in lista1)
#print(1 in lista1)

elemento = input("Digite o elemento procurado:")
novo = input("Digite o elemento novo:")
if (elemento in lista1):
    indice = lista1.index(elemento)
    lista1.remove(elemento)
    lista1.insert(indice, novo)
    print(lista1)
else:
    print('elemento não existe na lista')
