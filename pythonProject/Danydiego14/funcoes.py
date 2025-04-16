
def ler():
    with open("lista_compras.txt", "r", encoding="utf-8") as lista:
         itens = lista.read()
         itens_separados = itens.split(", ")
         for i in itens_separados:
            print(f"- {i}")

def add():
    item_add = input("digite o item que quer adicionar: ")
    with open("lista_compras.txt", "a", encoding="utf-8") as lista:
        itens = lista.write(", " + item_add)
    print("item adicionado com sucesso")

def remove():
    item_remove = input("digite o item que deseja remover: ")
    with open("lista_compras.txt", "r", encoding="utf-8") as lista:
        itens = lista.read()
        itens_separados = itens.split(", ")
        itens_separados.remove(item_remove)
        itens_juntos = ", ".join(itens_separados)
    with open("lista_compras.txt", "w", encoding="utf-8") as lista:
        itens = lista.write(itens_juntos)
    print("removido com sucesso")
