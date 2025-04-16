import funcoes

selecao = -1

while selecao != 0:
    try:
        print('''Selecione uma opção:
        1 - Ler
        2 - Add
        3 - Remover
        0- Sair''')
        selecao = int(input("Digite a opção desejada?"))
    except ValueError:
        print("Digite número válido")

    try:
        if selecao == 1:
           funcoes.ler()
        elif selecao == 2:
           funcoes.add()
        elif selecao == 3:
            funcoes.remove()
        elif selecao == 0:
            print("até logo!")
        else:
            print("digite opção válida")

    except:
        Print("erro!")

# melhorar o programa - menu, modulos etc