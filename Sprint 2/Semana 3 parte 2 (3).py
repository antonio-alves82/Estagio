print ('Escreva uma palavra')
palavra = str(input())
letras = ''.join (palavra)
inverso = ''
for letra in range(len(letras)-1, -1, -1):
    inverso += letras[letra]
if inverso == letras :
    print ('É um palidromo')
else:
    print ('Não é um palindromo')
import os
os.system("pause")