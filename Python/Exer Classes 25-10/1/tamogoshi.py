class Bixo:
    nome =  '' 
    fome = 100
    saude = 100
    idade = 0

    def alteraBixo(self, params):
        print(params)
        self.nome = params.nome
        self.fome = params.fome
        print('''
            Novo nome:
        ''' + self.nome)
