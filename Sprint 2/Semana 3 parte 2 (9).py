def teste(*arg, **args):
    for i in arg:
        print(i)
    for a, b in args.items():
        print(a,b)
# teste
teste('Fulano da Silva', 27, endereço=': Rua Sem fim, Nº 99',CEP=': 99999-999',Cidade = ': Inexistente')