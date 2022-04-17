import os
a = ['Ana', 'Lucas', 'Carlos', 'Priscila',
     'Felipe', 'João', 'Rafael', 'Vinicios', 'Erika']


def fatiamento(list):
    for i in range(0, len(list), 3):
        print(list[i:i+3])


fatiamento(a)
os.system("pause")
