import tkinter as tk

'''def pegar_nome():
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

janela.mainloop()'''

def calcula_imc():
    imc = float(input.get())/(float(input1.get())*float(input1.get()))
    label2.config(text=f"Seu IMC é {imc}")


janela = tk.Tk()
janela.title("IMC")
janela.geometry("500x500")

label = tk.Label(janela,text="Peso(kg):", padx=100, pady=100)
label.grid(row=0,column=0)

input = tk.Entry(janela)
input.grid(row=0,column=1)

label1 = tk.Label(janela,text="Altura(metros):")
label1.grid(row=1,column=0)

input1 = tk.Entry(janela)
input1.grid(row=1,column=1)

botao = tk.Button(janela,text = "Calcular IMC",command=calcula_imc)
botao.grid(row=3,column=1)

label2 = tk.Label(janela,text="Seu IMC é ...")
label2.grid(row=4,column=0,columnspan=2,ipady=10)

janela.mainloop()

