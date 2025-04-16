import random
def obter_numero_valido():
    valor_maximo = int(input("digite o valor máximo?"))
    while (valor_maximo < 100):
        print("valor deve ser maior ou igual a 100")
        valor_maximo = int(input("digite o valor máximo?"))
    return valor_maximo

def alterna_palpites_validos():
    anterior = 0
    numero = 0
    soma = 0
    i = 1
    while (soma<=valor_aleatorio):
        if i % 2 != 0:
            jogador = "P1"
        else:
            jogador = "P2"
        numero = int(input(f"{jogador}- Digite um numero:"))
        if numero >= anterior:
            soma = soma + numero
            anterior = numero
            i = i + 1
        else:
            print("numero invalido")
        return soma


'''refatorar arquivo anterior
soma = 0
anterior = 0
numero1= 0
numero2= 0
valor_maximo = obter_numero_valido()
valor_aleatorio = random.randint(100,valor_maximo)
print(valor_aleatorio)'''


valor_maximo = obter_numero_valido()
valor_aleatorio = random.randint(100,valor_maximo)

jogo = alterna_palpites_validos()


print("fim de jogo")
print(valor_aleatorio)
print(soma)
print(anterior)
print(numero)
print(jogo)

