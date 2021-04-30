#Listas
frase = 'Oi, tudo bem?'
print(frase[0]) #Imprime caractere especifico
print(frase[4:8]) #Imprime uma seção de caracteres
print(frase[1:12:2]) #Imprime uma seção de caracteres pulando de 2 a 2

lista_nomes = ['Futebol', 'Formula 1', 'Futebol Americano', 'Basquete']

print(lista_nomes[0]) #Imprime posição especifica da lista
print(lista_nomes[-1]) #Imprime o ultimo da lista (primeiro ao contrario)
print(lista_nomes[0:3]) #Imprime uma seção da lista
print(lista_nomes[0:4:2] ) #Imprime uma seção da lista pulando de 2 a 2

#Adicionar elemntos nas listas
lista_nomes.append('E-sport') #Sempre adicionado no ultimo da lista
print(lista_nomes[-1]) #Imprime o ultimo da lista (primeiro ao contrario)

#Remove elementos nas listas
lista_nomes.remove('Futebol Americano')
print(lista_nomes)

#Limpar a lista
##lista_nomes.clear()

#Adicionar um elemento em uma posição especifica
lista_nomes.insert(0, 'Xadrez')
print(lista_nomes)

#Pega o ultimo elemnto da lista e retira ele da lista
primeiro = lista_nomes.pop()
print(primeiro)
print(lista_nomes)

#Modificar algum elemento da lista
lista_nomes[2] = 'F1'
print(lista_nomes)

#Contar os elemntos repetidos de uma lista
contador_futebol = lista_nomes.count('Futebol')
print(contador_futebol)

#Tamanho de uma strig ou lista
print(len(lista_nomes), len(frase))

#Strings

#Transforma tudo em minusculo
frase_minusculo = frase.lower()
print(frase_minusculo)

#Separa a frase e transforma em uma lista
frase_separada = frase.split(',')
print(frase_separada)

#Concatenação de frases

frase_nova = frase + ' Mae ta bem? G? 3? X?'
print(frase_nova)