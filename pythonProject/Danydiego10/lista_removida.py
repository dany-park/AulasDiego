def lista_removida():
    elif selecao == 4:
        for indice, tarefa in enumerate(lista_removidas):
            print(f"- {indice} - {tarefa["titulo_tarefa"]} | {tarefa["descricao_tarefa"]} | {tarefa["categoria_tarefa"]}")

    elif selecao == 5:
        categoria_escolhida = input("Digite a categoria que deseja consultar")
        for tarefa in lista_tarefas:
            if categoria_escolhida == tarefa["categoria_tarefa"]:
                print(f"- {tarefa["titulo_tarefa"]} | {tarefa["descricao_tarefa"]} - {tarefa["categoria_tarefa"]}")

    elif selecao ==0:
        print("até logo!")

    else:
        print("digite uma opção válida")


""""ver lista de tarefas removidas
adicionar data nas tarefas - ordem crescente e decrescente (sort) - fica pra depois!
organizar as tarefas em listas ou categorias, mostrar somente de determinada categoria"""
