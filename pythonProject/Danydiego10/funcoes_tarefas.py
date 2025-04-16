lista_de_tarefas = []
lista_removidas = []

def cadastrar_tarefa():
       titulo_tarefa = input("Digite um título para a nova tarefa")
       descricao_tarefa = input("Digite uma descrição para a nova tarefa")
       categoria_tarefa = input("Digite a categoria da tarefa")
       lista_de_tarefas.append({
           "titulo_tarefa": titulo_tarefa,
           "descricao_tarefa": descricao_tarefa,
           "categoria_tarefa": categoria_tarefa})
       print("adicionado com sucesso")

def listar_tarefa():
    for indice, i in enumerate(lista_de_tarefas):
       print(f"- {indice} - {i["titulo_tarefa"]} | {i["descricao_tarefa"]} - {i["categoria_tarefa"]}")

def remover_tarefa():
    numero_tarefa = int(input("Digite o numero da tarefa que deseja remover"))
    lista_removidas.append(lista_de_tarefas[numero_tarefa])
    lista_de_tarefas.pop(numero_tarefa)
    print("tarefa removida com sucesso")

def listar_removida():
    for indice, tarefa in enumerate(lista_removidas):
       print(f"- {indice} - {tarefa["titulo_tarefa"]} | {tarefa["descricao_tarefa"]} | {tarefa["categoria_tarefa"]}")

def listar_categoria():
    categoria_escolhida = input("Digite a categoria que deseja consultar")
    for tarefa in lista_de_tarefas:
        if categoria_escolhida == tarefa["categoria_tarefa"]:
            print(f"- {tarefa["titulo_tarefa"]} | {tarefa["descricao_tarefa"]} - {tarefa["categoria_tarefa"]}")


