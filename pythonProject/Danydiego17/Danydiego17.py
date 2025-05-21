class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.desconto = 10

produtos=[]
total = 0

quantidade_produtos = int(input("Digite a quantidade de produtos para cadastrar: "))

for i in range(quantidade_produtos):
    nome = input("Digite o nome do produto: ")
    preco = int(input("Digite o preço do produto: "))
    produto = Produto(nome,preco)
    produtos.append(produto)
    total = total+preco

print("Nota Fiscal: ")

for item in produtos:
    print(f"- {item.nome} - {item.preco}")

print(f"Total: {total} ")

"""desconto funcionar

digite o desconto
******NOTA FISCAL*******
- SABAO (R$12.9)
- CAFÉ (R$ 11.9) POR (9.0)
TOTAL: 21.9

E FAZER OS EXERCICIOS DO NOTION"""




