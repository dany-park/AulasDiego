def selecao_operacao():
    selecao = int(input("""
        Que operação você deseja fazer?

        1 - soma
        2 - subratração
        3 - divisão
        4 - multiplicação
        0 - sair
      """))
    return selecao

def input_n1_n2():
    numero1 = int(input("Primeiro valor: "))
    numero2 = int(input("Segundo valor: "))
    return numero1,numero2

def soma(n1,n2):
    return n1 + n2

def subtracao():
    n1, n2 = input_n1_n2()
    return n1 - n2

def divisao():
    n1, n2 = input_n1_n2()
    if (n2 == 0):
        print("Divisão impossível")
    else:
        return n1/n2

def multiplicacao():
    n1, n2 = input_n1_n2()
    return n1 * n2

'''opcao = -1

while (opcao != 0):
    opcao = selecao_operacao()

    if (opcao == 1):
        num1, num2 = input_n1_n2()
        resultado_soma = soma(num1,num2)
        print(f"O resultado da soma é: {resultado_soma}")

    elif (opcao == 2):
        resultado_subtracao = subtracao()
        print(f"O resultado da subtração é: {resultado_subtracao}")

    elif (opcao == 3):
        resultado_divisao = divisao()
        print(f"O resultado da divisao é: {resultado_divisao}")

    elif (opcao == 4):
        resultado_multiplicacao = multiplicacao()
        print(f"O resultado da multiplicacao é: {resultado_multiplicacao}")
    else:
        print("A aplicação será encerrada.")
print("Fim.")'''


