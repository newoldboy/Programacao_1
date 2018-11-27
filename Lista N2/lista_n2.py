from menus import Menus
from funcoes import Funcoes


menu = Menus()
funcao = Funcoes()


def verificaMenus():
    if menu.opcao == 1:
        funcao.calcular()
        if funcao.aplcicacao() == True:    
            getMenu()       
    elif menu.opcao == 2:
        funcao.par_impar()
        if funcao.aplcicacao() == True:    
            getMenu()
    else:
        print('Bye!')
        exit(0)

def getMenu():
    menu.mostrar_menu()
    verificaMenus()

if menu.opcao == 0:
    getMenu()

