#definição da variável
def intersecao(A, B):
#função de inerseção entre A e B para retornar os valores sem repetir
    return set(A).intersection(B)
#Valores de A e B e a impressão da resposta.     
A = [ 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(intersecao(A, B))