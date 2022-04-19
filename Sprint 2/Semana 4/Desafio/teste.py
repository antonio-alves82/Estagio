import csv

with open('actors.csv', 'r') as actors_csv:
    leitor = csv.reader(actors_csv)
    next(leitor)
    resposta1 = max(leitor, key=lambda column: int(column[2]))
    print(resposta1)
    str1 = '|'.join(resposta1)
with open('Atividade_1.txt', 'w') as a1:
    a1.write(str1)

'''with open('actors.csv', 'r') as actors_csv:
    leitor = csv.reader(actors_csv)
    next(leitor)
    resposta '''

with open('actors.csv', 'r') as actors_csv:
    leitor = csv.reader(actors_csv)
    next(leitor)
    resposta5 = max(leitor, key=lambda column: float(column[1]))
    print(resposta5)
    str5 = '|'.join(resposta5)
with open('Atividade_5.txt', 'w') as a5:
    a5.write(str5)
