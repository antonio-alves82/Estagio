from itertools import chain

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

juntos = list(chain(primeirosNomes, sobreNomes, idades))

frase = ''.join(juntos)
print = (frase)