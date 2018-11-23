from menus import Menus
from game_regra import GameRegra


menu = Menus()

menu.mostrar_menu()
gameRegra = GameRegra()

if menu.opcao == 1:
    gameRegra.solicitar_cadastro()
elif menu.opcao == 2:
    gameRegra.visualizar_cadastro()
elif menu.opcao == 3:
    gameRegra.deletar()
elif menu.opcao == 4:
    gameRegra.alterar()
else:
    print('Obrigado e volte sempre!')
    exit(0)