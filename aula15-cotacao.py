import requests
import json
import time
import datetime

while True:
    requesicao = requests.get('https://economia.awesomeapi.com.br/json/all')
    cotacao = json.loads(requesicao.text)

    print('##COTAÇÃO DAS MOEDAS##', datetime.datetime.now())
    print('Dólar: R$', cotacao['USD']['bid'])
    print('Euro: R$', cotacao['EUR']['bid'])
    print('Bit coin: R$', cotacao['BTC']['bid'])
    time.sleep(10)

