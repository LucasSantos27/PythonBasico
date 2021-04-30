#LISTA DE CONVIDADOS

qtd_convidados = int(input('Digite quantas pessoas foram convidadas: '))

lista_de_convidados = []

contador = 0

while contador < qtd_convidados:
    convidado = input('Digite o nome do convidado #' + str(contador + 1) + ': ')
    lista_de_convidados.append(convidado)
    contador += 1

print('\nLISTA DE CONVIDADOS PARA FESTA')
print('Serão', qtd_convidados, 'no total.\n')
for convidado in lista_de_convidados:
    print(convidado)