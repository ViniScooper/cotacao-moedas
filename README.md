Documentação do Programa de Cotações de Moedas
Este programa em Python permite que o usuário visualize as cotações de Dólar, Euro e Bitcoin em relação ao Real (BRL). Ele utiliza a biblioteca tkinter para criar uma interface gráfica simples onde o usuário pode escolher a moeda desejada e clicar em um botão para ver a cotação atualizada.

Módulos
tela.py
Este módulo é responsável por criar a interface gráfica, receber a escolha do usuário e chamar a função para mostrar as cotações.

Funções:
atualizar_cotacoes(): Esta função é chamada quando o botão "Mostrar Cotação" é clicado. Ela chama a função mostrar_cotacoes() com os argumentos necessários.
main(): Esta função inicia a interface gráfica e configura os elementos como rótulos, botões e menus.
inicio.py
Este módulo contém as funções relacionadas às cotações das moedas.

Funções:
get_cotacoes(): Esta função faz uma requisição à API https://economia.awesomeapi.com.br/ para obter as cotações de Dólar, Euro e Bitcoin em relação ao Real. Retorna um dicionário com as cotações.
mostrar_cotacoes(escolha, nome_label, valor_label): Esta função recebe a escolha do usuário (Dólar, Euro ou Bitcoin) e os rótulos onde as cotações serão exibidas. Com base na escolha, atualiza os rótulos com as cotações correspondentes.
Variáveis
em tela.py
escolha: Uma variável StringVar() que guarda a escolha do usuário.
nome_label: Rótulo para exibir o nome da moeda escolhida.
valor_label: Rótulo para exibir o valor da moeda escolhida.
em inicio.py
dolar, euro, bitcoin: Variáveis que armazenam as cotações individuais de Dólar, Euro e Bitcoin, respectivamente.
