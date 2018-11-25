from game import Game
from game_banco import GameBanco

class GameRegra:

    def solicitar_cadastro(self):
        game = Game()
        banco = GameBanco()
        nome = input('Informe o nome: ')
        game.set_nome(nome)
        genero = input('informe o genêro: ')
        game.set_genero(genero)
        plataforma = input('informe a plataforma: ')
        game.set_plataforma(plataforma)
        ano = input('Informe o ano: ')
        game.set_ano(int(ano))
        online = input('O game é online? (S ou N): ')
        game.set_online_string(online)
        meta_critic = input('Informe a nota no meta critica: ')
        game.set_meta_critic(float(meta_critic))
        try:
            banco.salvar(game)
            print('O Game foi Salvo com Sucesso!!')
        except Exception as e:
            print('Erro ao salvar cadastro!')
            print('ERRO', e)
        


    def visualizar_cadastro(selft):
        try:
            lista = GameBanco().get_games()
            print('=' *15)
            for game in lista:
                print('ID: ', game.get_id())
                print('Nome: ',game.get_nome())
                print('Gênero: ',game.get_genero())
                print('Plataforma: ',game.get_plataforma())
                print('Ano: ',game.get_ano())
                print('Online: ',game.online())
                print('Meta Critica: ',game.get_meta_critic())
                print('')
            print('=' *15)
        except Exception as e:
            print('ERRO', e)


    def deletar(self):
        try:
            banco = GameBanco()
            codigo = int(input('Informe o codigo do jogo a ser deletado: '))
            if (banco.delete_game(codigo)):
                print('Game deletado com sucesso!')
        except Exception as e:
            print('ERRO', e)

    def alterar(self):
        try:
            game = Game()
            banco = GameBanco()
            sql = '''
                ALTER TABLE
            '''
        except Exception as e:
            print('ERRO ', e)