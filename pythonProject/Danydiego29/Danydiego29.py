class Piloto:
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

# lição = sai pra lá com esse streaming