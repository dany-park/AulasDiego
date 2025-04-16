import le_num


def somar():
    numero1, numero2 = le_num.ler_numeros()
    print(f"Soma: {numero1 + numero2}")

def subtrair():
    numero1, numero2 = le_num.ler_numeros()
    print(f"Subtração: {numero1 - numero2}")

def dividir():
    numero1, numero2 = le_num.ler_numeros()
    if numero2 == 0:
        print("Divisão impossível")
    else:
        print(f"Divisão: {numero1 / numero2}")

def multiplicar():
    numero1, numero2 = le_num.ler_numeros()
    print(f"Multiplicação: {numero1 * numero2}")