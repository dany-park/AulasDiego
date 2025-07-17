#@property

#@x.setter

#olhar a resolucao do caso do cofre - tentar resetar as tentativas se acertar uma tentativa
# desafio do aquario no notio

class Aquario:

    def __init__(self,temperatura,nivel_o2):
        self.__temperatura = temperatura
        self.__nivel_o2 = nivel_o2

    @property
    def temperatura(self):
        return self.__temperatura

    @property
    def nivel_o2(self):
            return self.__nivel_o2

    @temperatura.setter
    def temperatura(self,nova_temp):
        if  20>= nova_temp <=30:
            self.__temperatura = nova_temp
        else:
            print("Temperatura inválida")

    @nivel_o2.setter
    def nivel_o2(self,novo_nivel):
        if  5>= novo_nivel <=10:
            self.__nivel_o2 = novo_nivel
        else:
            print("Nível inválido")

    def status(self):
        print(f"temperatura: {self.temperatura}C e Nível de O2: {self.nivel_o2}mg/L")

aquario = Aquario(25,7)


aquario.status()
print(aquario.temperatura)
print(aquario.nivel_o2)
aquario.temperatura = 27
aquario.nivel_o2 = 8
aquario.status()

