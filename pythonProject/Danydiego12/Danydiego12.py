#TRATAMENTO DE ERROS


try:
    numero1 = int(input("digite o primeiro numero: "))
    numero2 = int(input("digite o segundo numero: "))
    print(numero1/numero2)
except ValueError: #Exception as e (print o tipo de erro)
                    #print(e)
    print("digite em algarismo numérico")
except ZeroDivisionError:
    print("não é possível dividir por zero. refaça a operação")

'''LIÇÃO: TRATAR ERRO DO PROJETO DA AULA 10'''