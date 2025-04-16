'''Primeira forma de manipular arquivos
lista = open("lista_compras.txt", "r", encoding="utf-8") - - lista = é o streaming do arquivo
itens = lista.read()
print(itens)
lista.close() - - fechar o streaming para nao vazar memória'''


try:
    with open("lista_compras.txt", "r", encoding="utf-8") as lista:
         itens = lista.read()
         itens_separados = itens.split(", ")
         for i in itens_separados:
            print(f"- {i}")
except:
    Print("erro!")

#adição e remoção pela palavra