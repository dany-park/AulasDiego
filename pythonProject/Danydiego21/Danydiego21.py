class Cofre:
    def __init__(self,senha,item):
        self.__senha = senha
        self.__item = item
        self.tentativa = 0

    def __getItemAbrir(self):
        return self.__item

    def __tentar_abrir(self,senha):
          if senha == self.__senha:
              return self.__getItemAbrir()
          else:
              self.tentativa += 1
              print(f"senha incorreta {3-self.tentativa} restantes")

    def tentativas(self):
        while True:
            item_final = self.__tentar_abrir(input("digite o código: "))
            if self.tentativa < 3 and item_final!= None:
                print(item_final)
            elif self.tentativa < 3 and item_final== None:
                print("tente novamente")
            else:
                print("Cofre Bloqueado")

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