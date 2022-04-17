import os


class ordenadora:
    def __init__(self, listabaguncada):
        self.listabaguncada = listabaguncada

    def ordenacaoCrescente(self):
        listabaguncada = x
        listabaguncada.sort()
        print(
            f'A ordem crescente dos números da primeira lista são {listabaguncada}')

    def ordenacaoDecrescente(self):
        listabaguncada = y
        listabaguncada.sort(reverse=True)
        print(
            f'A ordem decrescente dos números da segunda lista são {listabaguncada}')


x = [3, 4, 2, 1, 5]
crescente = ordenadora(x)
crescente.ordenacaoCrescente()
y = [9, 7, 6, 8]
decrescente = ordenadora(y)
decrescente.ordenacaoDecrescente()
os.system("pause")
