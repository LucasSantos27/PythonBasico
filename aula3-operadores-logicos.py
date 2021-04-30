#Variavel booleana
'''
var_verdade = True 
var_falso = False

print(type(var_verdade), type(var_falso))
'''

#Comparações: == != > < >= <=
#Comparações 2: and or not
'''
a = 2
b = 20

if a > b:
    print(a, 'eh maior do que', b)
else:
    print(b, 'eh maior do que', a)
'''

#criando um menu aleatorio
print('Opcoes: \n1 = Futebol Lucas\n2 = Formula 1\n3 = Basquete\n')

opcao = input('Escolha uma opcao: ')

print('\n')

if opcao == '1':
    print('Assistindo futebol')
elif opcao == '2':
    print('Assistindo F1')
elif opcao == '3':
    print('Assistindo basquete')
else:
    print('Opção invalida')
