import requests
import json

#Esse código em especifico não vai rodar, já que ele precisa de uma key entregue na API do OMDB
apikey = ''

def requisicao(titulo):
    filmes = []
    page = 1
    response = 'True'
    while response == 'True':
        try:
            #req = faz uma requisição escolhendo o nome do filme e a pagina dele
            req = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=' + apikey + '&s='+ titulo + '&type=movie&page=' + str(page))
            pagina_filmes = json.loads(req.text)
            #Verifica se o response ainda é 'True', caso ele for 'False', quer dizer que já pode sair da repetição, pois acabou as paginas
            response = pagina_filmes['Response']
            if(response == 'True'):
                filmes.append(pagina_filmes)
            page += 1
        except:
            print('Erro na conexão')
            response = 'False'
    #retorna uma lista com o tamanho de numero de pagina e dentro dela tem outra lista com os filmes
    return filmes


def printar_detalhes(filmes):
    n_filme = 1
    for lista_filme in filmes:
        for filme in lista_filme['Search']:
            print(str(n_filme), '- Filme:', filme['Title'])
            n_filme += 1

sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar: ')

    if op == 'SAIR':
        sair = True
        print('Saindo do programa')
    else:
        filme = requisicao(op)
        printar_detalhes(filme)
