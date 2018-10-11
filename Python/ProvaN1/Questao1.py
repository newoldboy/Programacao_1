# Pokemon Go Fight 
UPpokemon1 = 100
UPpokemon2 = 100

# Info Players and Pokemons
print('Player 1')
NomePoke1 = input('Qual o nome do seu pokemon: ')
print('Player 2')
NomePoke2 = input('Qual o nome do seu pokemon: ')

print('Player 1')
Tipo1 = int(input('''Digite 1 para seu pokemon ser do tipo Água e 
Digite 2 para seu pokemon ser do tipo Fogo;
    -> '''))

print('Player 2')

Tipo2 = int(input('''Digite 1 para seu pokemon ser do tipo Água e
Digite 2 para seu pokemon ser do tipo Fogo;
    -> '''))

print('Player 1')
Poder1 = int(input('Digite o valor do poder do seu pokemon: '))
print('Player 2')
Poder2 = int(input('Digite o valor do poder do seu pokemon: '))

print('Iniciando batalha')
# Batalha
Resultado = '';
def luta(player1, player2):
    if ((player1 == 1) and (player2 == 1) or (player1 == 2) and (player2 == 2)):
        Resultado =  'Empate!'
    else:
        if (player1 == 2) and (player2 == 1):
            Poder1 = (Poder1 * 5) / 100
            Poder2 = (Poder2 / 10) / 100
            Resultado = NomePoke1 + ' Ganhou!'  
        else:
            Resultado = NomePoke2 + ' Ganhou!'      
    return Resultado
print('A grande luta começa!!!')
print(luta(Tipo1, Tipo2))





