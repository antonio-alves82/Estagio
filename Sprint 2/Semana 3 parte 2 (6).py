import os
texto = open("arquivo_texto.txt")
linhas = texto.readlines()
for linha in linhas:
    print(linha)
os.system("pause")
