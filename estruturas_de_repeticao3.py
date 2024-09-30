frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
contador = 0

for letra in frase:
    if letra not in vogais:
        contador += 1

print(f"Há {contador} consoantes na frase: {frase}")
