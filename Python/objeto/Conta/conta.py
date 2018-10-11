class Contas():

    numero = 0
    cliente = ''
    limite = 0
    saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self,valor):
        pass
    
    def imprimirSaldo(self):
        print('O saldo da conta %d é %.2f' %
        (self.numero, self.saldo))