#Criando um objeto através de uma classe

class Veiculo:
    #Constrtutor
    def __init__(self, cor, rodas, marca, tanque):
        self.cor = cor 
        self.rodas = rodas     #Atributos /\
        self.marca = marca     #Atributos \/
        self.tanque = tanque
    
    #Metodos
    def abastecer(self, litros):
        self.tanque += litros