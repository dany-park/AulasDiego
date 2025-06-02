class Produto:
    def __init__(self, nome, preco, desconto):
        self.nome = nome
        self.preco = preco
        self.desconto = desconto
        self.preco_desconto = 0

    def calcula_desconto(self):
        self.preco_desconto = self.preco - int(self.preco * self.desconto / 100)

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

print("*********Nota Fiscal*********")

for item in produtos:
    if item.desconto == 0:
        print(f"- {item.nome} - {item.preco}")
    else:
        print(f"- {item.nome} - {item.preco} - por {item.preco_desconto}")

print(f"Total: {total} ")

"""desconto funcionar

digite o desconto
******NOTA FISCAL*******
- SABAO (R$12.9)
- CAFÉ (R$ 11.9) POR (9.0)
TOTAL: 21.9

E FAZER OS EXERCICIOS DO NOTION """




