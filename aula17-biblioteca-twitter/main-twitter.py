from twitter import Twitter

#Esse código em especifico não vai rodar, já que ele precisa de uma key entregue na API do twitter
consumer_key = ''
consumer_secret = ''
token_key = ''
token_secret = ''


twitter = Twitter(consumer_key, consumer_secret, token_key, token_secret)

#twitter.tweet('Vamos testar nossa lib') Postando um tweet através da LIB

pesquisa = twitter.search('Corinthians', 'pt')
for tweet in pesquisa:
    print(tweet['user']['screen_name']) #O @ do twitter do usuario
    print(tweet['text']) #O corpo do tweet
    print('\n')