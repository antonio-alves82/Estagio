import csv


with open('actors.csv', 'r') as actors_csv:
    leitor = csv.reader(actors_csv)
    next(leitor)
    resposta1 = max(leitor, key=lambda column: int(column[2]))
    # print(resposta1)
    str1 = '|'.join(resposta1)
with open('Atividade_1.txt', 'w') as a1:
    a1.write(str1)

with open('actors.csv', 'r') as actors_csv:
    leitor = csv.DictReader(actors_csv)
    Actor = []
    nMoveis = []

    for col in leitor:
        Actor.append(col['Actor'])
        nMoveis.append(col['Number of Movies'])
    #print('Actor: ', Actor)
    #print('Numero de filmes: ', nMoveis)
    ZipResposta2 = zip(Actor, nMoveis)
    Resposta2 = list(ZipResposta2)
    # print(Resposta2)
    str2 = '|'.join(map(str, Resposta2))
with open('Atividade_2.txt', 'w') as a2:
    a2.write(str2)

with open('actors.csv', 'r') as actors_csv:
    leitor = csv.DictReader(actors_csv)
    TGross = []
    nMovies2 = []
    Actor2 = []
    for col in leitor:
        TGross.append(col['Total Gross'])
        nMovies2.append(col['Number of Movies'])
        Actor2.append(col['Actor'])
    #print('Total_Gross', TGross)
    #print('Numero de Filmes: ', nMovies2)
    TGross2 = (list(map(float, TGross)))
    nMovies3 = (list(map(int, nMovies2)))
    média = [m/n for m, n in zip(TGross2, nMovies3)]
    Zipresposta3 = zip(Actor2, média)
    resposta3 = list(Zipresposta3)
    resposta3b = max(resposta3, key=lambda column: int(column[1]))
    str3 = '|'.join(map(str, resposta3b))
with open('Atividade_3.txt', 'w') as a3:
    a3.write(str3)


with open('actors.csv', 'r') as actors_csv:
    leitor = csv.reader(actors_csv)
    next(leitor)
    resposta5 = max(leitor, key=lambda column: float(column[1]))
    # print(resposta5)
    str5 = '|'.join(resposta5)
with open('Atividade_5.txt', 'w') as a5:
    a5.write(str5)
