lista = ['arlindo', 'feijao', 'coxinha', 'inteiro', 'vinagre', 'juropinga', 'goole', 'tubo',
    'vermelho', 'creiton', 'pedro', 'neine']

vLetra = input('informe uma letra: ')

for palavra in lista:
    for letra in palavra:
        if letra == vLetra:
            print('  ' + palavra + ';')
            break