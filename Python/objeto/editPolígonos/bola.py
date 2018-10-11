class Bola():
    cor = 'branco'
    circunferencia = 3.10
    material = 'papelon'

    def trocaCor(self, params):
        self.cor = params

    def  mostrarCor(self):
        print('A cor da bola agora é ' + (self.cor))   