#  herança

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def deslocar(self):
        print(f"o {self.nome} está se deslocando")

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos"

class Mamifero(Animal):
    def __init__(self,nome,idade,pelo):
        super().__init__(nome,idade)
        self.pelo = pelo

    def mamar(self):
        print(f"o {self.nome} está mamando")

class Ave(Animal):
    def __init__(self,nome,idade,pena):
        super().__init__(nome,idade)
        self.pena = pena

    def voar(self):
        print(f"a {self.nome} está voando")


mamifero = Mamifero("leao",10,"curto")
ave = Ave("papagaio",100,"verde")
mamifero.deslocar()
ave.deslocar()
mamifero.mamar()
ave.voar()
print(mamifero)
print(ave)

#outro exercício da aula do fazendeiro