# polimorfismo - tem a ver com herança (não muito com composição)
# pega comportamento de uma classe, copia em outra e sobrescreve o que quer que mude

class Midia:
    def __init__(self,titulo,duracao):
        self.titulo = titulo
        self.duracao = duracao

    def reproduzir(self):
        print(f"Reproduzindo mídia {self.titulo} ({self.duracao})")

class Dvd(Midia):

    def __init__(self,titulo,duracao,regiao):
        super().__init__(titulo,duracao)
        self.regiao = regiao

    def reproduzir(self):
        print(f"Reproduzindo Dvd - {self.titulo} ({self.duracao}) | Região {self.regiao}")

class Vhs(Midia):
    def __init__(self,titulo,duracao):
        super().__init__(titulo,duracao)
        self.rebobinada = True

    def reproduzir(self):
        if self.rebobinada == True:
            print(f"Reproduzindo Vhs - {self.titulo} ({self.duracao})")
            self.rebobinada = False
        else:
            print("Por favor, rebobinar")
    def rebobinar(self):
        if self.rebobinada == True:
            print("A fita ja está rebobinada")
        else:
            self.rebobinada = True
            print("A fita foi rebobinada com sucesso")


dvd = Dvd("matrix",300,2)
dvd.reproduzir()
vhs = Vhs("Loucademia de policia",120)
vhs.reproduzir()
vhs.reproduzir()
vhs.rebobinar()
vhs.rebobinar()
vhs.reproduzir()

#blueray - reproduzir bonus
#exercicio 2 - lição de casa