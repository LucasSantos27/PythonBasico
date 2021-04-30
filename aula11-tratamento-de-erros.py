import time
#Tratamento de erros

#Tratamento de arquivos
def abre_arquiivo(): 
    try:
        open('arquivo_n_existente.txt') #O programa tenta abrir esse arquivo, casso ele não encontre ele vai tentando, até ele existir
        return True
    except Exception as erro:
        print('Aconteceu algo errado: ', erro)
        return False

while not abre_arquiivo():
    print('Tentando abrir o arquivo')
    time.sleep(5) #Tentando a cada 5 segundos

print('Consegui abrir o arquivo')


#Tratamento basico através de erro de divisão com 0
'''
try:
    a = 1220/0
#Except mostrando qual é erro
except Exception as erro:
    print("Aconteceu algo errado:", erro)
'''



#TTIPOS DE EXCEPT

'''
#Except especifico
except ZeroDivisionError:
    print('Divisão por zero, não da para fazer')
'''

'''
#Except geral
except:
    print('Algo deu errado') 
'''