'''
open ('arquivo.txt', 'w') #abrir o arquivo, com argumento 'w',ou seja, "write". Cria arquivo ou sobrescreve se o arquivo já existir.
open ('arquivo.txt', 'r') #abrir o arquivo, com argumento 'r',ou seja, "read". Lê o arquivo que já existe, senão nao funciona.
open ('arquivo.txt', 'a') #abrir o arquivo, com argumento 'a',ou seja, "append". Cria arquivo ou adiciona se o arquivo já existir
open ('arquivo.png', 'b') #abrir arquivo, com argumento 'b', ou seja, "binnary". Pode ser usado com os outros: wb, rb, ab
'''

arquivo = open ('arquivo.txt', 'w')

arquivo.write('Eaí veiiii, beleza?')