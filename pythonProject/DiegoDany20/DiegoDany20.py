#AULA SOBRE ATRIBUTOS __PRIVADOS
'''class Pessoa:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.__cpf = cpf

    def get_cpf(self):
        print(self.__cpf)

pessoa = Pessoa("dany","29444089843")
print(pessoa.get_cpf())
print(pessoa.__cpf)'''

class Estoque:
    def __init__(self):
        self.__itens = []

    def adicionar_item(self,item):
        self.__itens.append(item)

    def listar_itens(self):
        print(self.__itens)

estoque = Estoque()
estoque.adicionar_item("maça") #chamar os métodos ou comportamentos a partir do objeto (letra minuscula)
estoque.adicionar_item("banana")# e nao chamar a partir da classe (letra maiuscula)
estoque.listar_itens()

#lição de casa - exercicio cofre






