class Funcoes:


    def aplcicacao(self):
        resposta = input('Deseja sair da aplicação?(S/N): ')
        if resposta.upper() == 'N':
            return True
        else:
            return False

    def calcular (self):    
        print('Calcular potencia!!!') 
        num = int(input('Informe um numero: '))
        potencia = int(input('Informe a potencia: '))   
        result = (num ** potencia)
        print('Resultado: ',result)
        return True

    def par_impar(self):
        print('É par ou impar???')
        num = int(input('informe um numero: '))
        result = num % 2
        if result == 0:
            print('Este número é Par')
            print('=================')
        else:
            print('Este número é Impar')
            print('===================')
