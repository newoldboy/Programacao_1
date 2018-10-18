class Quadrado():
    tamanho_lado = 3.10
    area = 0

    def trocaLado(self, params):
        self.tamanho_lado = params
        self.area = self.tamanho_lado * 4

    def mostraInfoQuadrado(self):        
        print('O lado do quadrado é ', self.tamanho_lado, ' e sua área é ', self.area)   