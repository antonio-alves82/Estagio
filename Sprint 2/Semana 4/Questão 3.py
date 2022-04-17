import os


class calculo:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def subtracao(self):
        self.a = self.x - self.y
        print(f'A subtração do número {self.x} e o núemro {self.y} é {self.a}')

    def soma(self):
        self.b = self.x + self.y
        print(f'A soma do numéro {self.x} e o número {self.y} é {self.b}')


input_x = input('Escreva o primeiro núemro: ')
input_y = input('Escreva o segundo núnero: ')
x = int(input_x)
y = int(input_y)
teste = calculo(x=x, y=y)
teste.soma()
teste.subtracao()
os.system("pause")
