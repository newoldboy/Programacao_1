from game import Game

def salvar(game):
    # Grava no arquivo
    arquivo = open('games.txt', 'a+')
    texto_game = game.converter_texto()

    arquivo.write(texto_game)
    arquivo.write('\r')
    arquivo.close()

def ler():
    # Lê o arquivo
    lista_games = []
    arquivo = open('games.txt', 'r')

    for linha in arquivo:
        game = Game()
        game.converter_objeto(linha)
        lista_games.append(game)

    arquivo.close()
    return lista_games