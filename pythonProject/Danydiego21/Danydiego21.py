class Cofre:
    def __init__(self,senha,item):
        self.__senha = senha
        self.__item = item
        self.i = 0

    def __getItemAbrir(self):
        return self.__item

    def __tentar_abrir(self,senha):
          if senha == self.__senha:
              return self.__getItemAbrir()
          else:
              self.i += 1
              print("senha inválida")

    def tentativas(self):
        while self.i<=3:
            item_final = self.__tentar_abrir(input("digite o código: "))
            return item_final

        else:
            print("tentativas esgotadas")

    def alterar_senha(self,senha_atual,senha_nova):
        if senha_atual == self.__senha: #sempre perguntar: é o atributo (self.) ou o (parametro)
            self.__senha = senha_nova
            print("senha alterada com sucesso")
        else:
            print("senha inválida")

cofre = Cofre("1234","dinheiros")
#print(cofre.tentar_abrir("12345"))
#cofre.alterar_senha("1234","12345")
print(cofre.tentativas())

#DESAFIO
#senha incorreta 3x. tentativas restantes. se errar, bloqueia o cofre, mesmo com a senha certa