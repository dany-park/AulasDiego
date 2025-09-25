'''class Piloto:
    def __init__(self,nome):
        self.nome = nome

    def usar_habilidade(self):
        print(f"{self.nome} tenta usar sua habilidade especial!")

class DickVigarista(Piloto):
    def __init__(self):
        super().__init__("dick vigarista")
    def usar_habilidade(self):
        print(f"{self.nome} espalha uma armadilha na pista!")

class PenelopeCharmosa(Piloto):
    def __init__(self):
        super().__init__("penelope charmosa")

    def usar_habilidade(self):
        print(f"{self.nome} acelera com charme e ganha velocidade extra!")

dick_vigarista = DickVigarista()
penelope_charmosa = PenelopeCharmosa()

dick_vigarista.usar_habilidade()
penelope_charmosa.usar_habilidade()

# lição = sai pra lá com esse streaming'''

class Midias:
    def __init__(self,titulo,artista,duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao

    def reproduzir(self):
        print("a midia está sendo reproduzida")

class FitaCassete(Midias):

    def __init__(self,titulo,artista,duracao):
        super().__init__(titulo,artista,duracao)
        self.rebobinada = True
    def rebobinar(self):
        self.rebobinada = True
        print("rebonidado com sucesso")
    def reproduzir(self):
        if self.rebobinada == True:
            print (f"tocando cassete: {self.titulo}")
            self.rebobinada = False
        else:
            print(f"A fita {self.titulo} precisa ser rebobinada.")

class Vinil(Midias):
    def __init__(self,titulo,artista,duracao,lado,rpm):
        super().__init__(titulo,artista,duracao)
        self.lado = lado
        self.rpm = rpm

    def reproduzir(self):
        print(f"Girando vinil {self.titulo} - lado {self.lado} - RPM {self.rpm}")

    def virar_disco(self):
        if self.lado == "a":
            self.lado = "b"

        else:
            self.lado = "a"
        print(f"virado o disco - agora no {self.lado}")

class CD(Midias):

    def __init__(self,titulo,artista,duracao,arranhoes):
        super().__init__(titulo,artista,duracao)
        self.arranhoes = arranhoes

    def reproduzir(self):
        if self.arranhoes <= 50:
            print(f"Tocando CD: {self.titulo}")
        else:
            print("Pode haver arranhões")

midias = [
  CD("Greatest Hits", "Queen", 50, arranhoes=80),
  Vinil("Dark Side of the Moon", "Pink Floyd", 42, "a",rpm=33),
  FitaCassete("Thriller", "Michael Jackson", 40),
]

for m in midias:
  m.reproduzir()

vinil = midias[1]
vinil.virar_disco() # 🔄 Virando disco... agora no lado B
vinil.reproduzir()  # 🎵 Girando Vinil: Dark Side of the Moon — lado B a 33 RPM

fita = midias[2]
fita.reproduzir()   # ⚠️ A fita 'Thriller' precisa ser rebobinada antes de tocar.
fita.rebobinar()    # 🔄 Rebobinando a fita 'Thriller'...
fita.reproduzir()   # 📼 Tocando cassete: Thriller



