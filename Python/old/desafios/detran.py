print('Detran Paraná')
print('Estes questionamentos são anonimos. Sua indetidade será preservada.')
print('''
Responda esse questionamento apenas com S para Sim e N para Não''')
vColidiuVeiculo = input('''
    Já colidiu contra outra veículo?
        ''')
vMultaVeiculo = input('''
    Já recebeu mais de uma multa?
        ''')
vDesrespeita = input('''
    Desrespeita algumas leis de trânsito? 
        ''')
vXingar = input('''
    Costuma xingar no trânsito?
        ''')
vPontuacao = 0
if ((vColidiuVeiculo == 'S') or (vColidiuVeiculo == 's')):
    vPontuacao = vPontuacao + 1
if ((vXingar == 'S') or (vXingar == 's')):
    vPontuacao = vPontuacao + 1
if ((vMultaVeiculo == 'S') or (vMultaVeiculo == 's')):
    vPontuacao = vPontuacao + 1
if ((vDesrespeita == 'S') or (vDesrespeita == 's')):
    vPontuacao = vPontuacao + 1

if vPontuacao == 2:
    print('Sua avaliação mostro que você é um Motorista ruim!')
if vPontuacao == 3:
    print('Sua avaliação mostro que você é um Motorista péssimo!')
if vPontuacao > 3:
    print('Você deve entregar seu CNH na saida, sim o programa não é anonimo!')
if vPontuacao < 2:
    print('Você é um otimo motorista, continue assim!')


