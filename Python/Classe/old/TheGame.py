from ClassGame import Games
    
game = Games()
print('''
    Cadatro de jogos!
''')

opcao = 999

while opcao != 0:

    opcao = int(input('''
        1 - para cadastrar;
        2 - para visualizar cadastros;
        0 - para sair ;
    Qual a opção: ''')) 

    if opcao == 1:

        game.nome = input('Título: ')
        game.genero = input('Gênero: ')
        game.plataforma = input('Plataforma: ')
        game.ano = input('Ano: ')
        game.confirmar   
    elif opcao == 2:
        for n in game.nomes:
         print('''
            Nome: %s
            Genero: %s
            Plataforma: %s
            ano: %s
         ''' % (game.nome, game.genero, game.plataformas, game.anos))
        break
    
