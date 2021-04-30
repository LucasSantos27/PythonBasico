#Para importar bibliotecas de fora do python, é preciso abrir o cmd e instalar através do "pip install 'nome da biblioteca'"
import requests #Beautiful Soup 4 ou BS4 //pip install bs4. Consegue destrinxar uma pagina

texto = None

cabecalho = {'User-agent': 'Windows 12',
            'Referer' : 'https://google.com'}

meus_cookies = {'Ultima-visita': '10-10-20'}

dados = {'username' : 'Lumi', 'password' : '12345678'}

#requests: .get, .post, .delete
try:
    #requisicao = requests.get('https://putsreq.com/zOWwV8mQylGC1mnRMcL0') 
    requisicao = requests.post('https://putsreq.com/zOWwV8mQylGC1mnRMcL0',
                                headers = cabecalho,
                                cookies = meus_cookies,
                                data = dados)
    texto = requisicao.text
except Exception as e:
    print('Requisição deu errado: ',e)

print(texto)