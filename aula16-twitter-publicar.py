#pip install oauth2 instal oauth2 para ajudar na manipulação das APIs do twitter
import oauth2
import json
import urllib.parse #Detecar o texto e fazer um parse dele
import pprint #Singifica "Pretty Print", ou seja, para as impressões sairem mais bonitas

#Esse código em especifico não vai rodar, já que ele precisa de uma key entregue na API do twitter
consumer_key = ''
consumer_secret = ''
token_key = ''
token_secret = ''

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

post = input('Novo tweet: ')
post_codificado = urllib.parse.quote(post, safe='')

requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + post_codificado, method='POST')

#Você recebe do twitter uma tupla com: um response e uma utilizando a classe bytes, para isso precisamos decodificar os bytes em uma string
'''
print(requisicao)
print(type(requisicao[0]))
print(type(requisicao[1]))
'''

#decodificando bytes em string
decodificar = requisicao[1].decode()

#Agora com a requisição em String, vc transforma a requisicação em JSON
objeto = json.loads(decodificar)

print(objeto)