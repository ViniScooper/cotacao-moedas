import requests

# Função para obter cotações
def get_cotacoes():
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacoes = cotacoes.json()
    return cotacoes

# Função para mostrar cotações
def mostrar_cotacoes(escolha, nome_label, valor_label):
    cotacoes = get_cotacoes()

    dolar = cotacoes['USDBRL']
    euro = cotacoes['EURBRL']
    bitcoin = cotacoes['BTCBRL']

    moeda_escolhida = escolha.get()

    if moeda_escolhida == "Dólar":
        nome_moeda = dolar['name']
        valor_moeda = dolar['bid']
    elif moeda_escolhida == "Euro":
        nome_moeda = euro['name']
        valor_moeda = euro['bid']
    elif moeda_escolhida == "Bitcoin":
        nome_moeda = bitcoin['name']
        valor_moeda = bitcoin['bid']
    else:
        nome_moeda = ""
        valor_moeda = ""

    # Atualiza os rótulos com as cotações
    nome_label.config(text=f"Moeda: {nome_moeda}")
    valor_label.config(text=f"Valor: {valor_moeda}")
