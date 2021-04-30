from conta import Conta
from cliente import Cliente


cliente1 = Cliente('Lucas Santos', '420.815.268-08', 21)
print(cliente1)

conta1 = Conta(cliente1, 1000, 3000)

conta1.depositar(5000)
conta1.depositar(1500)
conta1.consultar_saldo()
conta1.sacar(800)
conta1.consultar_saldo()
conta1.sacar(1700)
conta1.consultar_saldo()
