from bola import Bola
from quadrado import Quadrado
from retangulo import Retangulo

print('''
    Edição de Polígonos!
''')

# ----Bola -----------------

print(' Configuração para a Bola!')

cor_nova = Bola()
cor_nova.cor = input('Digite a nova cor para a bola: ')

cor_nova.trocaCor(cor_nova.cor)

cor_nova.mostrarCor()

print('''
    Bola configurada!
''')

# ----Quadrado------------------

print(' Configuração para a Quadrado!')

vquadrado = Quadrado()
vquadrado.tamanho_lado = int(input('Digite o lado para o quadrado: '))

vquadrado.trocaLado(vquadrado.tamanho_lado)

vquadrado.mostraInfoQuadrado()

print('''
    Quadrado configurado!
''')

# -----Retangulo----------------

print(' Configuração para Retangulo!')

vretangulo = Retangulo()
vretangulo.lado_a = int(input('Informe o lado A: '))
vretangulo.lado_b = int(input('Informe o lado B: '))

vretangulo.setaLados(vretangulo.lado_a, vretangulo.lado_b)

vretangulo.mostraInfoRetangulo()

print('''
    Retangulo configurado!
''')