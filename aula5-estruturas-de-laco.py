#Criando lista para percorrer com o laço
'''
lista_nomes = ['Futebol', 'Formula 1', 'Futebol Americano', 'Basquete']

for nome in lista_nomes:
    print(nome)
'''

#Criação de uma lista numeros
'''
lista_de_numeros = range(4) #Até o número 4, sem contar ele
lista_de_numeros2 = range(5,10) #Intervalo de numeros até o 10, sem contar ele
lista_de_numeros3 = range(0,100,2) #Intervalo de números pulando de 2 a 2

for n in lista_de_numeros:
    print(n)
'''

#Usando a lista de numeros junto a lista de nomes
'''
for  i in lista_de_numeros:
    print(lista_nomes[i])

lista_de_numeros = range(len(lista_nomes)) #Já pega o tamanho exato da lista de nomes
'''

#Também pode utilizar laço nas Strings
'''
palavra = "Lucas Santos"

for letra in palavra:
    print(letra)
'''

#Além de for, poderá usar o While
'''
i = 0

while i < 10:
    print(i, 'é menor do que 10')
    i+= 1

    print('Acabou o while, i é igual a', i)
'''

#Loop infinito
'''
while True:
    print('Loop infinito')
'''

#Lista de frutas
'''
lista_frutas = ['maçã', 'pera', 'laranja', 'melancia', 'uva']
contador = 0

for fruta in lista_frutas:
    contador += 1

print(contador)
print(len(lista_frutas))
'''

#Utilização do break

numero = 0

while True:
    print(numero)
    if(numero == 20):
        print('Break utilizado')
        break
    numero += 1
