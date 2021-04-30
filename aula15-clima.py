import requests
import json

#Esse código em especifico não vai rodar, já que ele precisa de uma key entregue na API do Open Weather
idapi = ''

while True:
    cidade = input('Escreva o nome da sua cidade: ')
    try:
        requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?lang=pt_br&q=' + cidade +'&appid=' + idapi)
        tempo = json.loads(requisicao.text)
        print('Condição do tempo:', tempo['weather'][0]['description'])
        print('Temperatura:', float(tempo['main']['temp'] - 273.15))
    except:
        print('Não foi possivel encontrar essa cidade')
        break