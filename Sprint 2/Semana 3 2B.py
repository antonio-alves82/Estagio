#Lista da questão
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Função para buscar números impares
impar = list(filter(lambda x: (x % 2 != 0), a))
  
print("Numeros impáres da lista:  ", impar) 