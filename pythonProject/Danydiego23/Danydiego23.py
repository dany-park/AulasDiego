# dunder methods

# def __init__

# def __str__ (é o que altera a função padrão do print)

#def __eq__ (é o que altera a função padrão de comparação == que da false pq compara o endereço de memória e não os valores que atribuimos

'''class Processo:

    def __init__(self,numero,autor,reu,valor_causa):
        self.numero = numero
        self.autor = autor
        self.reu = reu
        self.valor_causa = valor_causa

    def __str__(self):
        return f"Processo nº{self.numero} - Autor: {self.autor} x reu: {self.reu} - valor: {self.valor_causa}"

    def __eq__(self,processo2):
        return ((self.autor == processo2.autor) and
                (self.reu == processo2.reu) and
                (self.valor_causa == processo2.valor_causa))

processo = Processo(1,"dany","diego",100)
processo2 = Processo(2,"dany","diego",100)

print(processo)
print(processo2)
print(processo == processo2)

#taxas, taxas'''

class Produto:

    def __init__(self,nome,valor,taxas):
        self.nome = nome
        self.valor = valor
        self.taxas = taxas

    def total(self):
        total_taxas = 0
        for i in self.taxas:
            total_taxas = total_taxas + i

        valor_total = self.valor + total_taxas
        return valor_total

    def __str__(self):
        return f"Produto: {self.nome} - Total: R$ {self.total()}"

    def __add__(self, other):
        return self.total() + other.total()

    def __lt__(self, other):
        return self.total() < other.total()

produto = Produto("notebook",100,[10,2])
produto2 = Produto("tablet",90,[9])

print(produto)
print(produto2)
print(produto + produto2)
print(produto2 < produto)








