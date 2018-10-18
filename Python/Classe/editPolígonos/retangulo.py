class Retangulo():
    lado_a = 0
    lado_b = 0
    perimetro = 0
    area = 0

    def setaLados(self, ladoA, ladoB):
        self.lado_a = ladoA
        self.lado_b = ladoB
        self.perimetro = ((self.lado_a * 2) + (self.lado_b * 2))
        self.area = ladoA * ladoB

    def mostraInfoRetangulo(self):
        print('O lado do A é: ',self.lado_a,
             ' O lado do B é: ',self.lado_b,
        ' Sua área é: ', self.area, ' Seu perimetro é ', self.perimetro)   