dict = {"Sport": 41, "Santa Cruz": 29, "Nautico":21}

print(dict)
print("-"*30)

#Adiciona um valor
dict["Salgueiro"] = 20
print(dict)
print("-"*30)

#Lista as chaves
print(list(dict))
print("-"*30)

#Ordena as chaves
print(sorted(dict))
print("-"*30)

#Delete uma chave / valor
del dict["Nautico"]
print(dict)
print("-"*30)

dict["Nautico"] = 21
print(dict)
print("-"*30)
#buscando um valor pela chave
time = input("Digite um time :")
if (time in dict):
    print("Existe " + time +" no dicionario")
else:
    print("Não existe " + time + " no dicionario")
print("-"*30)

#listando as chaves
print("Listando as chaves :")
print(list(dict.keys()))

#buscando um indice numa lista
busca = list(dict.keys())
print(busca[0])
print("-"*30)

#listando os valores
print("Listando os valores :")
print(list(dict.values()))
print("-"*30)

#deletanto um item pela chave
popado = dict.pop("Salgueiro")
print(dict)
