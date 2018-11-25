class Menus:

    def __init__(self):
        self.opcao = 0


    def mostrar_menu(self):
        print('''
            Menu do transporte!

        ===========Funçoes=============  

                1 - Abastecer
                2 - Dirigir
                0 - Sair

        ===============================
        ''')
        self.opcao = input('Selecionar: ')
        self.validar_opcao()

    def validar_opcao(self):
        try:
            self.opcao = int(self.opcao)
            if (self.opcao not in (0, 1, 2)):
                print('Opcão inválida! \n')
                self.mostrar_menu()
              
        except ValueError as e:
            print('Opcão inválida! \n')
            self.mostrar_menu()
        

