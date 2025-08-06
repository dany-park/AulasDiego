#fazer exercicio da impressora e tinta - tema composição
class Cartucho:
    def __init__(self,cor,nivel):
        self.cor = cor
        self.nivel = nivel

class Impressora:
    def __init__(self,marca,cartucho):
        self.marca = marca
        self.cartucho = cartucho

    def imprimir(self,texto):
        if cartucho.nivel > 10:

            cartucho.nivel -= 10
            print(f"imprimindo: {texto}")
            print(f"tinta restante: {cartucho.nivel}")
        else:
            print("Atençao nível de tinta abaixo de 10")

cartucho = Cartucho("preto", 100)
epson = Impressora("hp", "cartucho")
epson.imprimir("Olá, mundo!")
epson.imprimir("Olá, mundo!")
epson.imprimir("Olá, mundo!")
epson.imprimir("Olá, mundo!")
epson.imprimir("Olá, mundo!")
epson.imprimir("Olá, mundo!")
epson.imprimir("Olá, mundo!")
epson.imprimir("Olá, mundo!")
epson.imprimir("Olá, mundo!")
epson.imprimir("Olá, mundo!")
epson.imprimir("Olá, mundo!")
epson.imprimir("Olá, mundo!")