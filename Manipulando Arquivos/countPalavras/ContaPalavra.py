arquivo = open('count.txt', 'r')
count = 0
palavra = input('''
    Digite a palavra que deseja verificar sua existencia no texto: ''')
for linha in arquivo:
    linha = linha.rstrip()
    if palavra in linha:
        count = count + 1
        print(palavra + ' está contida em ' + linha)      
print('Tem: ', count)
arquivo.close()


#  LOGICA PARA PEGAR CADA PALAVRA NÃO FUNCIONA AINDA
# count = 0
# pula = 0
# arquivo = open('count.txt', 'r')
# for linha in arquivo:
#     arquivo = open('count.txt', 'r')
#     text = arquivo.readline()
#     palavra = text.split(" ")[pula]
#     arquivo.close()
#     print('''
#     palavra é
#     = ''' + palavra)
#     linha = linha.rstrip()
#     for palavra in linha:  
#         if palavra in linha:
#             count = count + 1
#             pula = pula + 1
#             print(linha)       
# print('Tem: ', count)
# arquivo.close()