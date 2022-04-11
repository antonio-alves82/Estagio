#pegando o valor de um número qualquer
print ('Digite um número')
numero = int (input())
#calculo para saber se a divisão termina em 0 ou 1
resultado = numero % 2
if resultado == 0: 
    print ('Esse número ' + str(numero) + ' é par')
else:
    print ('Esse número ' + str(numero) + ' é impar' )