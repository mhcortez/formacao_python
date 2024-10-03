global_var = 100

def exemplo_escopo():
    local_var = "Estou dentro da função"
    print(local_var)
    print(global_var)
    
exemplo_escopo()
print(global_var)
print("-"*90)

def pessoa(nome,idade):
    print(f"Nome: {nome}, Idade: {idade}")

def pessoa2(nome,idade,altura):
    print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}")

pessoa("Marcelo", 48)
pessoa2("Marcelo", 48, 1.65)
