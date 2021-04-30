#ESTRUTURA DE DADOS

lista_nomes = ['Futebol', 'Formula 1', 'Futebol Americano', 'Basquete'] #Lista (list)
tupla_nomes = ('Futebol', 'Formula 1', 'Futebol Americano', 'Basquete') #Tupla (tuple), não é mutavel/dinâmico
dicionario_nomes = {'esporte' : 'Futebol', 'time' : 'Corinthians', 'campeonato' : 'Brasileirão'} #Dicionario (dict), lembra um objeto JSON, precisa de uma chave e de um valor
conjunto_nomes = {'Futebol', 'Formula 1', 'Futebol Americano', 'Basquete'} #Conjunto (set), não existe itens repetidos, não é ordenado

#A utilização do for pode usar em qualquer uma dessa estrutura de dados
'''
for nome in tupla_nomes:
    print(nome)
'''

#Pode perguntar através do if se tem algum nome especifico dentro da estrutura de dados
'''
if 'Formula 1' in conjunto_nomes:
    print('F1 esta na lista')

if 'Volei' in dicionario_nomes.values():
    print('Volei esta na lista')
else:
    print('Volei não esta na lista')
'''

#Em qualquer estrutrua de dados pode se usar o tamanho dela através do len
'''
tamanho_conjunto = len(conjunto_nomes)
print(tamanho_conjunto)
'''

#No dicionario precisa colocar a chave no lugar do indice
'''
print(dicionario_nomes['esporte'])

print(dicionario_nomes)

dicionario_nomes['campeonato'] = 'Paulistão'

print(dicionario_nomes)

dicionario_nomes.clear()

print(dicionario_nomes)
'''

#Nos conjuntos, não são ordenados e não pode ser repetido. Utilizado para fazer buscas, é uma tabela Hash
print(conjunto_nomes)

conjunto_nomes.add('Formula 1') #Não adicionou

print(conjunto_nomes)

 #Inicializando as estruturas de dados

lista = []
tupla = ()
dicionario = {} #ou dict()
conjunto = set()