from random import randint

usuario = []
sistema = []

print('''
    Loteria do Azar!!!
*Atenção para jogar digite 6 numeros de 0 a 20!*
''')


for i  in range (0,6):
    num = int(input('Digite um numero: '))
    usuario.append(num)
    sis = randint(0,20)
    sistema.append(sis)

print('''
    Seus numeros:      %s
    Numeros sorteados: %s ''' %(usuario, sistema)
    )

acertos = 0
for n in usuario:
    for m in sistema:
        if n == m:
            acertos += 1
            break

print('''
       ============================
        Quantidade de acertos: %s 
       ============================
        ''' %(acertos))