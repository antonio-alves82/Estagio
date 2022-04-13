print ("Escreva uma sequência de numeros e separe eles por virgulas")
a = input()
b = a.split(',')
soma = 0
for i in b:
    soma += int(i)
print ('A soma do resultado é : '+  str(soma))