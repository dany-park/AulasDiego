#composicao

class Advogado:
    def __init__(self,nome_adv,oab):
        self.nome_adv = nome_adv
        self.oab = oab

    def __str__(self):
        return f"{self.nome_adv}, oab nº {self.oab}"


class Parte:
    def __init__(self,nome,tipo,advogado):
        self.nome = nome
        self.tipo = tipo
        self.advogado = advogado

class Processo:
    def __init__(self,numero,descricao,partes):
        self.numero = numero
        self.descricao = descricao
        self.partes = partes

    def exibir_dados(self):
        print(f"Processo nº: {self.numero}")
        print(f"Descrição: {self.descricao}")
        print(f"Partes envolvidas:")
        for parte in self.partes:
            print(f"- {parte.nome} ({parte.tipo}), representado por {parte.advogado}")


advogado1 = Advogado("dany",123)
advogado2 = Advogado("carla",234)
parte1 = Parte("João Silva", "autor",advogado1)
parte2 = Parte("Empresa XYZ", "réu",advogado2)

processo = Processo("0100", "Indenização por danos morais", [parte1, parte2])

processo.exibir_dados()

#class advogado (nome,oab)