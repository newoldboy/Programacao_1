from menus import Menus

menu = Menus()

print('''
    MENU da 
''')




def calcular ():    
    print('Calcular potencia!!!') 
    num = int(input('Informe um numero: '))
    potencia = int(input('Informe a potencia: '))   
    result = (num ** potencia)
    print('Resultado: ',result)

def par_impar():
    print('É par ou impar???')
    num = int(input('informe um numero: '))