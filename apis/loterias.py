import requests
import openpyxl 

# URL da API
"https://loteriascaixa-api.herokuapp.com"
url = "https://loteriascaixa-api.herokuapp.com/api"

# Fazendo a requisição GET para a API
response = requests.get(url)

if response.status_code == 200:
    loterias = response.json()
    jogos_list= []
    
    for jogo in loterias:
        jogos_list.append(jogo)
    
    print(jogos_list)    
else:
    print("Erro ao acessar a API. Código de status:", response.status_code)