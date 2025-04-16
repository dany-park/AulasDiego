def listar_categoria():
        categoria_escolhida = input("Digite a categoria que deseja consultar")
        for tarefa in lista_tarefas:
            if categoria_escolhida == tarefa["categoria_tarefa"]:
                print(f"- {tarefa["titulo_tarefa"]} | {tarefa["descricao_tarefa"]} - {tarefa["categoria_tarefa"]}")
