'''qtd_produtos = int(input("Quantidade de produtos?"))
produtos = []
soma_precos = 0

for i in range(qtd_produtos):
    produto = input("Qual o produto?")
    preco = input("Qual o preço?")
    soma_precos = soma_precos + int(preco)
    produto_informado = {"produto": produto,"preco": preco}
    produtos.append(produto_informado)

print("nota fiscal")
for prod in produtos:
    print(f"- {prod["produto"]} {prod["preco"]}")

print("Total")
print(soma_precos)


#incluir desconto - nota sai com valor calculado - proxima aula'''

qtd_produtos = int(input("qual a quantidade de produtos?"))
produtos = []
soma_precos = 0

for i in range(qtd_produtos):
    produto = input("qual o produto?")
    preco = input("qual o preço?")
    desconto = float(input("qual o desconto em porcentagem?"))
    preco_desconto = float(preco) * float(1-((desconto)/100))
    produto_preco = {"produto":produto,"preco":preco_desconto}
    produtos.append(produto_preco)
    soma_precos = soma_precos + float(preco_desconto)


print("nota fiscal")
for item in produtos:
    print(f"- {item["produto"]} {item["preco"]}")

print("Total")
print(soma_precos)

