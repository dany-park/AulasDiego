'''
#qual o maior numero da lista

precos = [1.9, 3.9, 100, 5.6, 6.9, 10, 57, 99, 50]
maior = 0

for numero in precos:
    if numero>maior:
        maior = numero
print(maior)
'''
'''
qual o menor numero
precos = [1.9, 3.9, 100, 1.8, 5.6, 6.9, 10, 57, 99, 50]
menor=precos[0]

for numero in precos:
    if numero<menor:
        menor=numero
print(menor)
'''

'''precos = [1.9, 3.9, 100, 1.8, 5.6, 6.9, 10, 57, 99, 50]
precos_dentro = []

valor_limite = float(input("qual valor limite para compra?"))
for valor in precos:
    if valor <= valor_limite:
        precos_dentro.append(valor)
print(f"Os valores que voce pode comprar são: {precos_dentro}")'''

#colocar na ordem crescente ou decrescente - bubblesort

'''precos = [1.9, 3.9, 100, 1.8, 5.6, 6.9, 10, 57, 99, 50]
ordem_crescente = []
maior = 0
menor = precos[0]
for valor in precos:
    if float(valor) >= float(maior):
        maior=valor
        ordem_crescente.append(valor)
    else:
        menor=valor
        ordem_crescente.insert(0,valor)

print(ordem_crescente)'''

'''precos = [1.9, 3.9, 100, 1.8, 5.6, 6.9, 10, 57, 99, 50]
precos.pop() #remove o ultimo ou o indice que vc passar'''

