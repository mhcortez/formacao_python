mensagem = "hello, world!"
maiuscula = mensagem.upper()
minuscula = mensagem.lower()
print(maiuscula)
print(minuscula)

mensagem = "Hello, World!"
palavras = mensagem.split(",")
print(palavras)

mensagem = "Hello, World!"
if "World" in mensagem:
    print("A substring 'world' esta presente na mensagem")

mensagem = "Hello, World!"
mensagem = mensagem.replace("Hello", "Python")
print(mensagem)

mensagem = " Hello, World ! "
print(mensagem.strip())