class Game:
        def __init__(self):
                self.id = None
                self.nome  = ' '
                self.genero = ' '
                self.plataforma = ' '
                self.ano = ' '
                self.meta_critic = 0.0
                self.online = False

        def set_id(self, cod):
                self.id = cod   

        def get_id(self, id):
                return self.id

        def set_nome(self, nome):
                self.nome = nome

        def get_nome(self):
                return self.nome

        def set_genero(self, genero):
                self.genero = genero

        def get_genero(self):
                return self.genero

        def set_plataforma(self, plataforma):
                self.plataforma = plataforma

        def get_plataforma(self):
                return self.plataforma

        def set_ano(self, ano):
                self.ano = ano

        def get_ano(self):
                return self.ano

        def set_meta_critic(self, meta_critic):
                self.meta_critic = meta_critic

        def get_meta_critic(self):
                return self.meta_critic

        def set_online_string(self, params):
                if params.upper() == 'S':
                      self.online = True
                else:
                      self.online = False

        def set_online(self, online):
                self.online = online    

        def get_online(self):
                return self.online
