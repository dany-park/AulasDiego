""""#CRIE APP DE SENHA SEGURA
senha=input("Digite sua senha:")
print(len(senha))
print(senha.find("@"))
print(senha.find(" "))
if (len(senha)>=8 and senha.find("@")!=-1 and senha.find(" ")==-1):
    print("Sua senha é segura")
else:
    print("Sua senha é muito fraca!")"""

''' ESTOQUE
estoque = ["computador","grampeador","borracha","lápis",40,12]
tem_produto=False
item=input("Qual item voce busca?")
for produto in estoque:
    if str(produto)==item:
        tem_produto=True
if tem_produto==True:
    print("Produto disponível")
else: print("Produto indisponível")
for indice, produto in enumerate(estoque) - emular o FIND'''



