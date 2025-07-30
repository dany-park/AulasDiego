#playlist

class Musica:

    def __init__(self,titulo,artista,duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.duracao})"

class Playlist:

    def __init__(self,nome):
        self.nome = nome
        self.musicas = []

    def adicionar(self,musica):
        self.musicas.append(musica)

    def __str__(self):
        print(f"Playlist {self.nome} com {len(self.musicas)} musica(s)")
        for musica in self.musicas:
            print(musica)
        return ""

    def __len__(self):
        return len(self.musicas)

    def __add__(self, outra_playlist):
        nova = Playlist(f"{self.nome} + {outra_playlist.nome}") # mera string formatada
        nova.musicas = self.musicas + outra_playlist.musicas
        return nova


musica1 = Musica("abc","pele",300)
musica2 = Musica("eduardo e monica","legião",500)
musica3 = Musica("faroeste caboclo","legião",450)
playlist1 = Playlist("jingles")
playlist1.adicionar(musica1)
print(playlist1)
playlist2 = Playlist("rock")
playlist2.adicionar(musica2)
playlist2.adicionar(musica3)
print(playlist2)
print(len(playlist2))
print(playlist2 + playlist1)
# --add
# len
# mistura de playlist

