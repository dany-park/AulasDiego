'''soma = 0
anterior = 0
numeros_aceitos = []

while (soma<=100):
    numero = int(input("Digite um numero:"))
    if numero > anterior:
         soma = soma + numero
         anterior = numero
         numeros_aceitos.append(numero)
    else:
        print("numero invalido")
print("fim de jogo")
print(numeros_aceitos)'''

'''soma<=100 DIGITE O VALOR MAXIMO: - NUMERO ALEATORIO ENTRE 100 E O MAX
(PROGRAMA NAO DEVE COMERCAR ATÉ QUE INSIRA VALOR MAIOR QUE 100)
IMPORT Random (MINISCULO)
VARIAVEL = RANDOM.RANDINT(MIN,MAX)

DESAFIO
DIGITE O P1
DIGITE O P2
QUEM ESTOURAR PERDEU'''

import random


soma = 0
anterior = 0
numero1= 0
numero2= 0
valor maximo = obter_valor_valido()
valor_aleatorio = random.randint(100,valor_maximo)



i = 1
while (soma<=valor_aleatorio):
    if i % 2 != 0:
        jogador = "P1"
    else:
        jogador = "P2"
    numero1 = int(input(f"{jogador}- Digite um numero:"))
    if numero1 >= anterior:
        soma = soma + numero1
        anterior = numero1
        i = i + 1
    else:
        print("numero invalido")




    '''if i % 2 != 0 and numero1 >= anterior:
         numero1 = int(input("P1 - Digite um numero:"))
         soma = soma + numero1
         anterior = numero1
         i = i+1
    elif i % 2 == 0 and numero2 >= anterior:
         numero1 = int(input("P2 - Digite um numero:"))
         soma = soma + numero2
         anterior = numero2
         i = i+1
    else:
       print("numero invalido")'''


print("fim de jogo")
print(valor_aleatorio)
print(soma)
print(anterior)
print(numero1)
print(numero2)

