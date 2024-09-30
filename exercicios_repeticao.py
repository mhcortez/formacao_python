numero = [i for i in range(1,11)]
print(numero)
print("Letra A  " + "*"*40)

soma = 0
for i in range(1,51):
    soma += i 
print(soma)
print("Letra B  " + "*"*40)

numeros_pares = [i for i in range(1,20)  if i % 2 == 0]
print(numeros_pares)
print("Letra C  " + "*"*40)

frase = "Python é divertido"
contador = 0
frase = frase.strip()
for i in frase:
     contador += 1
print(f"Existem {contador} letras na frase")
print("Letra D  " + "*"*40)


number = int(input("Verificar numeros primos ate: "))
cont = 0
for i in range(2, number):
        if number % i != 0:
            cont += 1
print(cont)
print("Letra D  " + "*"*40)
