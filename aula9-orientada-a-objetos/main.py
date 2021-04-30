from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('Rosa', 6, 'Ford', 10)

print('Cor:', caminhao_rosa.cor)
print('Marca:', caminhao_rosa.marca)
print('Tanque:', caminhao_rosa.tanque, 'litros')

carro_azul = Carro('Azul', 4, 'bmw', 30)

print('\nCor:', carro_azul.cor)
print('Marca:', carro_azul.marca)
print('Tanque:', carro_azul.tanque, 'litros')

carro_azul.abastecer(15)

print('Tanque apos abastecer:', carro_azul.tanque, 'litros')

carro_azul.abastecer(10)