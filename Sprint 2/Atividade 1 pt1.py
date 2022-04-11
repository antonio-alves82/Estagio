print ('Qual é a sua idade ?')
#pegando a informação da idade
idade = int(input())
#verificando se a idade é maior que 100 anos ou não
if idade < 100: 
    print ('falta ' + str(100 - idade) + ' anos para você completar 100 anos')
else:
    print ('você possui mais de 100 anos')