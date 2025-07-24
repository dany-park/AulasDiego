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



musica1 = Musica("abc","pele",300)
playlist1 = Playlist("jingles")
playlist1.adicionar(musica1)
print(playlist1)

# --add
# len
# mistura de playlist

