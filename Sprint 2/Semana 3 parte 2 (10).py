import os


class Lampada:
    def __init__(self, a):
        self.a = a

    def esta_ligada(self):
        if (self.a == True):
            print('Está ligada?')
        else:
            print('Está desligada!')

    def liga(self):
        if self.a == False:
            self.a = True
            print('Ligou!')
        else:
            print(self.a)

    def desliga(self):
        if self.a == True:
            self.a = False
            print('Desligou!')
        else:
            print(self.a)


lampada = Lampada(True)
lampada.esta_ligada()
lampada.desliga()
lampada.liga()
os.system("pause")
