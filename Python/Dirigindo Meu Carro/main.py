from menus import Menus
from carro import MyCar

car = MyCar()
menu = Menus()

menu.mostrar_menu()

if menu.opcao == 1:
    gas = int(input('Informe o valor que deseja abastecer: '))
    if (car.abastecer(gas)):
        print('''
            Veiculo abastecido!
                ============================        
                █   Gasolina atual: %sL     █
                ============================''' % car.infoGasolina())
        menu.mostrar_menu()
    else:
        print('Não foi possivel abastecer, quantidade de gasolina superior a capacidade do tanque.')
        menu.validar_opcao(1)
        
elif menu.opcao == 2:
    gas = int(input('Informe a distancia a ser percorrida em KM: '))
    if(car.abastecer()):
        print('Você chegou ao seu destino!')
        menu.mostrar_menu()
    else:
        print('Você não conseguiu chegar ao seu destino e ficou sem carro!')
else:
    print('Obrigado e volte sempre!')
    exit(0)
