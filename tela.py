import tkinter as tk
from inicio import get_cotacoes, mostrar_cotacoes

# Função para atualizar as cotações quando o botão é clicado
def atualizar_cotacoes():
    mostrar_cotacoes(escolha, nome_label, valor_label)

get_cotacoes()  # Obtém as cotações quando o programa começa

# Cria a janela principal
janela = tk.Tk()
janela.geometry("400x500")
janela.title("Api")
janela.iconbitmap("logo.ico")

# Cria uma variável para guardar a escolha do usuário
escolha = tk.StringVar()
escolha.set("Selecione uma moeda")

# Rótulo para instrução
instrucao_label = tk.Label(janela, text="Escolha uma moeda:")
instrucao_label.pack()

# Opções de escolha
opcoes = ["Dólar", "Euro", "Bitcoin"]
opcoes_menu = tk.OptionMenu(janela, escolha, *opcoes)
opcoes_menu.pack()

# Botão para mostrar cotações
mostrar_button = tk.Button(janela, text="Mostrar Cotação", command=atualizar_cotacoes)
mostrar_button.pack()

# Rótulos para exibir as cotações
nome_label = tk.Label(janela, text="Moeda: ")
nome_label.pack()

valor_label = tk.Label(janela, text="Valor: ")
valor_label.pack()

janela.mainloop()
