import psycopg2

class Connection:

    def __init__(self):
        self.conn = None

    def get_connection(self):
        try:
            if self.conn == None:
                self.conn = psycopg2.connect(
                    dbname='gamePY',
                    user='postgres',
                    password='masterkey',
                    host='localhost',
                    port='5432')
            return self.conn
        except Exception as e:
            print('ERRO: ', e)
            return None