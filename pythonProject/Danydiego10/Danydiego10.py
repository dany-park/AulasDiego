import funcoes_tarefas



selecao = -1

while selecao != 0:
    try:
        print('''Selecione uma opção:
        1 - Cadastrar nova tarefa
        2 - Listar todas tarefas
        3 - Remover tarefa
        4 - Listar removidas
        5 - Listar tarefas de uma categoria
        0- Sair''')
        selecao = int(input("Digite a opção desejada?"))
    except ValueError:
        print("Digite número válido")
    if selecao == 1:
       funcoes_tarefas.cadastrar_tarefa()

    elif selecao == 2:
        funcoes_tarefas.listar_tarefa()

    elif selecao == 3:
        funcoes_tarefas.remover_tarefa()

    elif selecao == 4:
        funcoes_tarefas.listar_removida()

    elif selecao == 5:
        funcoes_tarefas.listar_categoria()

    elif selecao ==0:
        print("até logo!")

    else:
        print("digite uma opção válida")


""""ver lista de tarefas removidas
adicionar data nas tarefas - ordem crescente e decrescente (sort) - fica pra depois!
organizar as tarefas em listas ou categorias, mostrar somente de determinada categoria"""
