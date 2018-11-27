class Menus:

    def __init__(self):
        self.opcao = 0


    def mostrar_menu(self):
        self.opcao = 0
        print('''
            Menu da lista N2!

        ===========Funçoes=============  
                1 - Potencia
                2 - Impar Par
                0 - Sair
        ===============================
        ''')
        self.opcao = int(input('Selecionar: '))
        self.validar_opcao()

    def validar_opcao(self):
        try:
            # self.opcao = self.opcao
            if (self.opcao not in (0, 1, 2)):
                print('Opcão inválida! \n')
                self.mostrar_menu()
                              
        except ValueError as e:
            print('Opcão inválida! \n')
            self.mostrar_menu()
        

