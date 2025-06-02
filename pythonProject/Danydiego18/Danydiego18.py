"""class Produto:
    def __init__(self, nome, preco, desconto):
        self.nome = nome
        self.preco = preco
        self.desconto = desconto
        self.preco_desconto = 0

    def calcula_desconto(self):
        self.preco_desconto = self.preco - int(self.preco * self.desconto / 100)

class NotaFiscal:
    def __init__(self, produtos):
        self.produtos = produtos
    def imprimir():
        print("*********Nota Fiscal*********")
        for item in produtos:
            if  item.desconto == 0:
                print(f"- {item.produtos(nome)} - {item.preco}")
            else:
                print(f"- {item.nome} - {item.preco} - por {item.preco_desconto}")
        print(f"Total: {total} ")

produtos=[]
total = 0

quantidade_produtos = int(input("Digite a quantidade de produtos para cadastrar: "))

for i in range(quantidade_produtos):
    nome = input("Digite o nome do produto: ")
    preco = int(input("Digite o preço do produto: "))
    desconto = int(input("Digite o desconto: "))
    produto = Produto(nome,preco,desconto)
    produto.calcula_desconto()
    produtos.append(produto)
    total = total+produto.preco_desconto

produtos.imprimir()"""





"""criar class nota fiscal com função imprimir

class NotaFiscal:
    def __init__(self, produtos)
    def imprimir():

E FAZER OS EXERCICIOS DO NOTION """

class Produto:
    def __init__(self, nome, preco, desconto):
        self.nome = nome
        self.preco = preco
        self.desconto = desconto
        self.preco_desconto = 0

    def calcula_desconto(self):
        self.preco_desconto = self.preco - int(self.preco * self.desconto / 100)

class NotaFiscal:
    def __init__(self, produtos):
        self.produtos = produtos

    def imprimir(self):
        print("********* Nota Fiscal *********")
        total = 0
        for item in self.produtos:
            if item.desconto == 0:
                print(f"- {item.nome} - R$ {item.preco}")
                total += item.preco
            else:
                print(f"- {item.nome} - R$ {item.preco} - por R$ {item.preco_desconto}")
                total += item.preco_desconto
        print(f"Total: R$ {total}")

# Programa principal
produtos = []

quantidade_produtos = int(input("Digite a quantidade de produtos para cadastrar: "))

for i in range(quantidade_produtos):
    nome = input("Digite o nome do produto: ")
    preco = int(input("Digite o preço do produto: "))
    desconto = int(input("Digite o desconto (em %): "))
    produto = Produto(nome, preco, desconto)
    produto.calcula_desconto()
    produtos.append(produto)

nota_fiscal = NotaFiscal(produtos)
nota_fiscal.imprimir()