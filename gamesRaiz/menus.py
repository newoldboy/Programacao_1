#coding=cp1252
class Menus:

    def __init__(self):
        self.opcao = 0


    def mostrar_menu(self):
        print('Selecione uma das opções do menu')
        print('''
            1 - Cadastrar
            2 - Visualizar
            3 - Deletar
            0 - Sair''')

        self.opcao = input('Selecionar: ')
        self.validar_opcao()

    def validar_opcao(self):
        try:
              self.opcao = int(self.opcao)
              if (self.opcao not in (0, 1, 2, 3)):
                    print('Opcão inválida! \n')
                    # Se a opçao digitada nao for um numero ele cai no excpetion 
                    self.mostrar_menu()
              
        except ValueError as e:
            print('Opcão inválida! \n')
            # Se a opçao digitada nao for um numero ele cai no excpetion 
            self.mostrar_menu()
        

