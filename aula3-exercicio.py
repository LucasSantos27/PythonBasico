#Programa se é apto entrar no exercito
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

if idade >= 18 and peso >= 60 and altura >= 1.7:
    print ('Parabéns, você está apto á entrar no exercito.')
else:
    print ('Infelizmente você não está apto.')