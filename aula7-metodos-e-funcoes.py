##Função de somar numeros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

retorno = soma(10, 30)

print(retorno)


#Função que retorna um valor booleano
def tem_sete_itens(argumento):
    if(len(argumento) == 7):
        return True
    else:
        return False

#Metodo: não tem retorno/ Função: tem retorno