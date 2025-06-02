class Contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def listar_informacoes(self):
        print(f"nome: {self.nome}, número: {self.numero}")

class Agenda:
    def __init__(self, contatos):
        self.contatos = contatos

    def listar_contatos(self):
        print("Contatos na Agenda: ")

        for contato in self.contatos:
            print(f"nome: {contato.nome}, número: {contato.numero}")



contato = Contato("dany", "13089123")
contato1 = Contato("diego", "0981235")
#contato.listar_informacoes()

agenda = Agenda([contato, contato1])
agenda.listar_contatos()

#programa principal

# CRIAR MENU - LIÇÃO DE CASA