import tkinter as tk

def pegar_nome():
    nome = input.get()
    label1.config(text=f"Seu nome é {nome}")
#janela

janela = tk.Tk()
janela.title("Cadastrar Nome")
janela.geometry("300x200")

#widget
label = tk.Label(janela,text="Insira seu nome")
label.pack()

input = tk.Entry(janela)
input.pack()

botao = tk.Button(janela,text = "Cadastrar",command=pegar_nome)
botao.pack()

label1 = tk.Label(janela,text="Seu nome é ...")
label1.pack()

janela.mainloop()