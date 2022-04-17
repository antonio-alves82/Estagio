import os


class Animal:
    def __init__(self, nome: str, voar: str, emitir_som: str):
        self.nome = nome
        self.voar = voar
        self.emitir_som = emitir_som

    def exemplo(self):
        print(f'O {self.nome} {self.voar} e faz {self.emitir_som}')


class Pato (Animal):
    def __init__(self, nome: str, voar: str, emitir_som: str):
        super().__init__(nome, voar, emitir_som)


class pardal (Animal):
    def __init__(self, nome: str, voar: str, emitir_som: str):
        super().__init__(nome, voar, emitir_som)


pato = Pato(nome="Pato", voar="voa", emitir_som="Quack Quack")
pardal = Animal(nome="Pardal", voar="voa", emitir_som="Piu Piu")


pato.exemplo()
pardal.exemplo()
os.system("pause")
