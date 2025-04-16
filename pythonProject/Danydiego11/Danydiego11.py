import operacoes_mat

def menu():
    print("""
    Que operação você deseja fazer?

    1 - Soma
    2 - Subtração
    3 - Divisão
    4 - Multiplicação
    0 - Sair
    """)

opcao = -1

while opcao != 0:
    menu()
    try:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            operacoes_mat.somar()
        elif opcao == 2:
            operacoes_mat.subtrair()
        elif opcao == 3:
            operacoes_mat.dividir()
        elif opcao == 4:
            operacoes_mat.multiplicar()
        elif opcao == 0:
            print("A aplicação será encerrada.")
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número.")

print("Fim.")