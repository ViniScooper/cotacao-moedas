import tkinter as tk
from tkinter import ttk
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

# Define a cor de fundo da janela
janela.configure(bg="orange")  # Cor de fundo laranja



# Cria uma variável para guardar a escolha do usuário
escolha = tk.StringVar()
escolha.set("Selecione uma moeda")



# Rótulo para instrução
instrucao_label = tk.Label(janela, text="Escolha uma moeda:", font=('Arial', 14, 'bold'), bg="orange")
instrucao_label.pack(pady=10)



# Opções de escolha
opcoes = ["Dólar", "Euro", "Bitcoin"]
opcoes_menu = tk.OptionMenu(janela, escolha, *opcoes)
#opcoes_menu.config(font=('Arial', 12))
opcoes_menu.config(font=('Arial', 12), bg="PaleGoldenrod", fg="black")  # Cor de fundo branca e texto preto
opcoes_menu.pack(pady=5)




# Botão para mostrar cotações
mostrar_button = tk.Button(janela, text="Mostrar Cotação", command=atualizar_cotacoes, font=('NEGRITO', 12, 'bold'), bg="#EEE8AA", fg="black")
mostrar_button.pack(pady=20)



# Rótulos para exibir as cotações
nome_label = tk.Label(janela, text="Moeda: ", font=('Arial', 12), bg="Peru")
nome_label.pack()




valor_label = tk.Label(janela, text="Valor: ", font=('Arial', 12), bg="PaleGoldenrod")
valor_label.pack()

janela.mainloop()
