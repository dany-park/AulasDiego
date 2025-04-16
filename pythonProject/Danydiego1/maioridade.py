
import input_idade
def maioridade():
    idade = input_idade.input_idade()
    if idade>=18:
        print("A bebida está liberada")
    else: print("cai fora!")