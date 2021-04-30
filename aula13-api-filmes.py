import requests
import json

#Esse código em especifico não vai rodar, já que ele precisa de uma key entregue na API do OMDB
apikey = ''

def requisicao(titulo):

    try:
        req = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=' + apikey +'&t=' + titulo + '&type=movie')
        dicionario = json.loads(req.text)
        return dicionario   
    except:
        print('Erro na conexão')
        return None

def printar_detalhes(filme):
    print('\nTitulo: ', filme['Title'])
    print('Ano: ', filme['Year'])
    print('Diretor: ', filme['Director'])
    print('Atores: ', filme['Actors'])
    print('Nota: ', filme['imdbRating'])
    print('Premios: ', filme['Awards'])
    print('Poster', filme['Poster'], '\n')

sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar: ')

    if op == 'SAIR':
        sair = True
        print('Saindo do programa')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado\n')
        else:
            printar_detalhes(filme)
