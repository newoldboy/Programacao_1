class MyCar():
    def __init__(self):
        self.gasolina = 0
        self.tanque = 100
        self.consumo = 10

    def abastecer(self, gasolina):
        if ((self.gasolina + gasolina) > self.tanque):
            return False
        else:
            self.gasolina = self.gasolina + gasolina
            return True
        
    def dirigir(self, distancia):
        if self.gasolina == 0:
            return False
        else:
            gasto = self.gasolina / self.consumo
            if ((gasto - self.gasolina) <= 0):
                self.gasolina = self.gasolina - distancia
                return True
            else :
                return False

    def infoGasolina(self):
        return self.gasolina
