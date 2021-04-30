#Procurar padrões regex101.com
import re
import requests

'''
string_de_teste = 'O gato gata gatinho gatoncio é bonito'


#r vem de raw, ou seja para deixar o "arquivo bruto"
padrao = re.search(r'gat.', string_de_teste) #O . vale para qualquer carectere ate mesmo o espaço. O \w apenas para letras ou carecteres especiais, vazio nao
padrao2 = re.findall(r'gat\w+', string_de_teste)

#exemplo da utilização do raw
#print(r'Oi\ntudo bem?')
#Quando utiliza-se o raw, o \n aparece invés de pular linha4

if padrao:
    print(padrao.group())
else:
    print('Padrão não encontrado')

if padrao2:
    print(padrao2)
else:
    print('Padrão não existente')
'''

requisicao = requests.get('https://solyd.com.br/ead/')

padrao = re.findall (r'[\w\.-]+@[\w-]+\.[w\.-]+', requisicao.text) #Raw String

if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')