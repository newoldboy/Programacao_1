from game import Game
import game_arquivo

opcao = -1

lista_games = []

def mostrarMenu():
    print('''
    1 - Cadastrar
    2 - Visualizar
    0 - Sair
    ''')

def cadastrar():
    nome = input('Informe o nome: ')
    genero = input('Informe o genêro: ')
    plataforma = input('Informe a plataforma: ')
    ano = input('Informe o ano: ')
    # Instância um novo objeto Game
    # e armazena as suas informações
    game_novo = Game()
    game_novo.nome = nome
    game_novo.genero = genero
    game_novo.plataforma = plataforma
    game_novo.ano = ano    
    # Adiciona o game na lista
    # lista_games.append(game_novo)
    game_arquivo.salvar(game_novo)


def visualizar():
    lista_games = game_arquivo.ler()
    for game in lista_games:
        print('''
        Nome: %s
        Genêro: %s
        Plataforma: %s
        Ano: %s
        ''' % (game.nome, game.genero,
        game.plataforma, game.ano))

while(opcao != 0):
    mostrarMenu()
    opcao = int(input('Informe uma das opções: '))
    # tratar as opções do menu
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        visualizar()
    elif opcao != 0:
        print('Opção inválida')


