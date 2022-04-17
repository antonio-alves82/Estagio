class Pessoa: 
    def __init__(self, nome = str, id = int):
        self.__nome = nome
        self.id = id 
    def exemplo (self):
        return ("Teste do capeta {self.__nome}")

teste1 = Pessoa (nome= "Laxiba")

teste1.exemplo()
print (teste1.exemplo)

