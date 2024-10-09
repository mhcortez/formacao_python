import requests 
import openpyxl

# URL da API
url = "https://jsonplaceholder.typicode.com/users"

#Fazendo a requisição GET para a API
response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    
    #criando um novo arquivo Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    
    #Adiconando os cabeçalhos das colunas
    sheet.append(["ID", "Nome", "Email", "Empresa"])
    
    #Adiconando dados da API ao Excel
    for user in users:
        if user["name"] == "Glenna Reichert":
            sheet.append([user["id"], user["name"], user["email"], user["company"]["name"]])
    
    #Salvando o arquivo Excel
    workbook.save("usuarios_api.xlsx")
    print("Dados salvos com sucesso no arquivo Excel!")
    
else:
    print("Erro ao acessar a API. Código de status:", response.status_code)
