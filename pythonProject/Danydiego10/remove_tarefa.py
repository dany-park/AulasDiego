def remover_tarefa():
        numero_tarefa = int(input("Digite o numero da tarefa que deseja remover"))
        lista_removidas.append({"titulo_tarefa": titulo_tarefa, "descricao_tarefa": descricao_tarefa, "categoria_tarefa": categoria_tarefa})
        lista_tarefas.pop(numero_tarefa)
        print("tarefa removida com sucesso")
