import home

opcao = -1

lista_games = []


def mostrarMenu():
    print('''
    1 - Visualizar texto;
    0 - Sair;
    ''')

def visualizar():
    arquivo = input('Informe o nome do arquivo com sua estensão para ser lido: ')
    texto = home.ler(arquivo)
    print('''1
    
    ''' +texto)
    print('''
        By Guilherme and Lucas W.
    ''')


while(opcao != 0):
    mostrarMenu()
    opcao = int(input('Informe uma das opções: '))
    # tratar as opções do menu
    if opcao == 1:
        visualizar()
    elif opcao != 0:
        print('Opção inválida')


