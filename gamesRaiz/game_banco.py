from game import Game
from connection import Connection


class GameBanco:

    def __init__(self):
        self.conn = Connection().get_connection()

    def salvar(self, game):
        cursor = self.conn.cursor()
        try:
            sql =''' 
                INSERT INTO games(
                    nome,
                    genero,
                    plataforma,
                    ano,
                    meta_critica,
                    online
                    )
                VALUES(%s, %s, %s, %s, %s, %s)
                '''
            cursor = self.conn.cursor().execute(sql, [game.get_nome(), game.get_genero(), game.get_plataforma(), game.get_ano(), game.get_meta_critic(), game.get_online()])
            self.conn.commit()
        except Exception as e:
            cursor.close()
            print('ERROR: ', e)

    def get_games(self):
        cursor = self.conn.cursor()
        try:
            sql = '''
            select
                id, nome, genero, plataforma, ano, meta_critica, online 
            from games
            '''
            cursor.execute(sql)
            rows = cursor.fetchall()
            lista_games = []
            for row in rows:
                game = Game()
                game.set_id(row[0])
                game.set_nome(row[1])
                game.set_genero(row[2])
                game.set_plataforma(row[3])
                game.set_ano(row[4])
                game.set_meta_critic(row[5])
                game.set_online(row[6])                
                lista_games.append(game)
                print(lista_games)
        except Exception as e:
            cursor.close()
            print('ERROR: ', e)
        cursor.close()
        return lista_games


    def delete_game(self, id):
        cursor = self.conn.cursor()
        try:
            slq = 'DELETE FROM games WHERE id = %s'
            cursor.execute(slq, [id])
            deletados = cursor.rowcount
            self.conn.commit()
            return True
        except Exception as e:
            print('ERRO ', e)
            cursor.close()


    def alter_game(self, game):
        cursor = self.conn.cursor()
        try:
            sql = '''
            UPDATE games SET
                nome = %s,
                genero = %s,
                plataforma = %s,
                ano = %s,
                meta_critica = %s,
                online = %s
            WHERE
                id = %s
            '''
            cursor.execute(sql, [
                game.nome,
                game.genero,
                game.plataforma,
                game.ano,
                game.meta_critica,
                game.online
            ])
            alterados = curso.rowcount
            self.conn.commit()
            return alterados > 0
        except Exception as e:
            cursor.close()
            raise e
            
    def buscar_por_id(self, id):
        cursor = self.conn.cursor()
        try:
            sql = '''SELECT
                id,
                nome,
                genero,
                plataforma,
                ano,
                online,
                meta_critica
            FROM games WHERE id = %s'''
            cursor.execute(sql, [id])
            row = cursor.fetchone()
            game = None 
            if row:
                game= Game()
                game.set_id(row [0])
                game.set_nome(row[1])
                game.set_genero(row[2])
                game.set_plataforma(row[3])
                game.set_ano(row[4])
                game.set_online(row[5])
                game.set_meta_critic(row[6])
                return game
            cursor.close()
        except Exception as e:
            cursor.close()
            print('ERRO ', e)
        