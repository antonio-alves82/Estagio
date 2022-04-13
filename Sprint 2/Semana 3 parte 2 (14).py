import random
import numpy as md

def Avarage(randomlist):
    return sum(randomlist)/len(randomlist)
    
#Gerar 50 numeros aleatórios entre 0 e 500

randomlist = random.sample(range(0, 500), 50)

avarage = Avarage(randomlist)

valor_maximo = max(randomlist)

valor_minimo = min(randomlist)



print("A média dos 50 numeros é " + str(avarage) )
print("O valor máximo dos 50 numeros é " +str(valor_maximo))
print("O valor minímo dos 50 numeros é " +str(valor_minimo))
print ("o valor da mediana é: " +str (md.median(randomlist)))
print (randomlist)