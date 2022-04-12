print ('Qual é a sua idade ?')
idade = int(input())
if idade < 100: 
    print ('falta ' + str(100 - idade) + ' anos para você completar 100 anos')
else:
    print ('você possui mais de 100 anos')

import os
os.system("pause")