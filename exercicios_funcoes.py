def obter_detalhes_do_pedido():
    pedido = {
        "item": "Notebook",
        "preco": 1200.00,
        "quantidade": 2
    }
    print("Detalhes do pedido obtido.")
    return pedido   

def calcular_preco_total(pedido):
    preco_total = pedido['preco'] * pedido['quantidade']
    print(f"Preco total calculado: R${preco_total}")
    return preco_total

def enviar_confirmacao(pedido, preco_total):
    print(f"Confirmacao enviada para {pedido['quantidade']} {pedido['item']}(s).")
    print(f"Valor total a ser pago: R${preco_total}")

def processar_pedido():
    pedido = obter_detalhes_do_pedido()
    preco_total = calcular_preco_total(pedido)    
    enviar_confirmacao(pedido,preco_total)


processar_pedido()