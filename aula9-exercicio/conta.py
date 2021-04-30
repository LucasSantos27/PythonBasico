class Conta:
    
    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def sacar(self, dinheiro):
        if self.saldo - dinheiro >= 0:
            self.saldo -= dinheiro
        else:
            print('Saldo insuficiente')
    
    def depositar(self, dinheiro):
        if self.limite >= self.saldo + dinheiro:
            self.saldo += dinheiro
        else:
            print('O seu limite já foi atingido')

    def consultar_saldo(self):
        if self.saldo > 0:
            print('Seu saldo é igual a:', self.saldo)
        else:
            print('Saldo zerado')