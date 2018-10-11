class Quadrado():
    tamanho_lado = 3.10
    area = 0
    def trocaLado(self, params):
        self.cor = params

    def  mostraInfoQuadrado(self):
        area = self.tamanho_lado * 4
        print('O lado do quadrado é ' + str(self.tamanho_lado) + ' e sua área é ' + str(self.area))   