
candidatos = ['Bolsonaro', 'Haddadi', 'Ciro', 'Cabo Daciolo', 'Branco', 'Nulo']

bolsonaro = 0
haddadi = 0
ciro = 0
daciolo = 0
branco = 0
nulo = -1
voto = int 
print('\n' * 50)
while voto != 0:
    print('Lista dos candidatos: ')
    for i in range(0, 6):
        print(i +1, '-', candidatos[i])       
    
    voto = int(input('Em qual candidato a presidencia desja votar? '))
    print('\n' * 50)
    
    
    if voto == 1:
        bolsonaro += 1
    elif voto == 2:
        haddadi += 1
    elif voto == 3:
        ciro += 1
    elif voto == 4:
        daciolo += 1
    elif voto == 5:
        branco += 1
    elif voto == 6:
        nulo += 1  
    else:
        print('Número incorreto')  

total_votos =  bolsonaro + haddadi + ciro + daciolo + branco + nulo 

bolsonaro_por = (bolsonaro / total_votos) * 100
haddadi_por = (haddadi / total_votos) * 100
ciro_por = (ciro / total_votos) * 100
daciolo_por = (daciolo / total_votos) * 100
branco_por = (branco / total_votos) * 100
nulo_por = (nulo / total_votos) * 100

print('=' * 75)
print('Bolsonaro recebeu', round(bolsonaro_por, 2), '% do total de votos', 'e recebeu', bolsonaro, 'votos')
print('-' * 75)
print('Haddadi recebeu', round(haddadi_por, 2), '% do total de votos', 'e recebeu', haddadi, 'votos')
print('-' * 75)
print('Ciro recebeu', round(ciro_por, 2) , '% do total de votos', 'e recebeu', ciro, 'votos')
print('-' * 75)
print('Daciolo recebeu', round(daciolo_por, 2), '% do total de votos', 'e recebeu', daciolo, 'votos')
print('-' * 75)
print('A porcentagem de votos Brancos foi', round(branco_por, 2), '%', 'e recebeu', branco, 'votos')
print('-' * 75)
print('A porcentagem de votos Nulos foi', round(nulo_por, 2), '%', 'e recebeu', nulo, 'votos')    
print('=' * 75)    
print('Total: ', total_votos, 'Votos' )
