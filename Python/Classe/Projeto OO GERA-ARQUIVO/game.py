class Game:
    nome = ''
    genero = ''
    plataforma = ''
    ano = 0

    def converter_texto(self):
        return self.nome + ';' + self.genero + ';' + self.plataforma + ';' + str(self.ano) + ';'

    def converter_objeto(self, linha):
        # split - para quebrar linha
        informacoes = linha.split(';')
        print(informacoes)
        self.nome = informacoes[0]
        self.genero = informacoes[1]
        self.plataforma = informacoes[2]
        self.ano = informacoes[3]