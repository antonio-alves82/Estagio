texto = open("arquivo_texto.txt")
linhas = texto.readlines()
for linha in linhas:
    print(linha)
import os
os.system("pause")