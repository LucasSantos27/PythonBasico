import oauth2
import urllib.parse
import json

class Twitter:

    def __init__(self, consumer_key, consumer_secret, token_key, token_secre):
        self.conexao(consumer_key, consumer_secret, token_key, token_secre)

    def conexao(self, consumer_key, consumer_secret, token_key, token_secret):
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.client = oauth2.Client(self.consumer, self.token)
    
    def tweet(self, novo_tweet):
        post = urllib.parse.quote(novo_tweet, safe='')
        requisicao = self.client.request('https://api.twitter.com/1.1/statuses/update.json?status=' + post, method='POST')

        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        return objeto

    def search(self, tweet_pesquisa, lang):
        pesquisa = urllib.parse.quote(tweet_pesquisa, safe='')
        requisicao = self.client.request('https://api.twitter.com/1.1/search/tweets.json?q=' + pesquisa + '&lang=' + lang)
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        tweets = objeto['statuses']
        return tweets