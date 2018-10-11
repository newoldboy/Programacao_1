from bola import Bola
from quadrado import Quadrado
from bola import Bola

# ----Bola -----------------
print('Configuração para a Bola!')

cor_nova = Bola()
cor_nova.cor = input('Digite a nova cor para a bola: ')

cor_nova.trocaCor(cor_nova.cor)

cor_nova.mostrarCor()

print('Configuração para a Bola!')

# ----Quadrado------------------
print('Configuração para a Quadrado!')

tamanho_novo = Quadrado()
tamanho_novo.tamanho_lado = input('Digite o lado para o quadrado: ')

tamanho_novo.trocaLado(tamanho_novo.tamanho_lado)

tamanho_novo.mostraInfoQuadrado()

# print('Configuração para a Bola!')