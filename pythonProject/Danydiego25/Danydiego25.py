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
        if self.cartucho.nivel > 10:

            self.cartucho.nivel -= 10
            print(f"imprimindo: {texto}")
            print(f"tinta restante: {self.cartucho.nivel}")
        else:
            print("Atençao nível de tinta abaixo de 10")

cartucho1 = Cartucho("preto", 100)
epson = Impressora("hp", cartucho1)
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