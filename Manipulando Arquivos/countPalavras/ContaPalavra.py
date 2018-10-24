#  LOGICA PARA PEGAR CADA PALAVRA NÃO FUNCIONA AINDA
count = 0
lista = []
palavra = ''
arquivo = open('count.txt', 'r')
for linha in arquivo:
    linha = linha.rstrip()
    palavra = linha.split(" ")
    lista += palavra
# print(lista)
arquivo.close()

for palavra in lista:
    count = 0
    for palavra2 in lista:
        if palavra == palavra2:
            count += 1
    print('"' + palavra + '"' + ' Repetiu: ', count,'\n')

  