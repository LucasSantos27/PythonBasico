#Função pra achar o maior numero de uma lista
def maiornumero (lista):
    maiornumero = lista[0]
    for i in lista:
        if(i > maiornumero):
            maiornumero = i
    return maiornumero

#Função para achar o menor numero de uma lista
def menornumero (lista):
    menornumero = lista[0]
    for i in lista:
        if(i < menornumero):
            menornumero = i
    return menornumero



lista_numeros = [8,2, 3, 5, 13]

n_maior = maiornumero(lista_numeros)
print('O maior numero eh', n_maior)

n_menor = menornumero(lista_numeros)
print('O menor numero eh', n_menor)