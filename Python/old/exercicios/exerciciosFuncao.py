# Faça um programa, com uma função que necessite de um parâmetro. A função retorna o valor de caractere
#  ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo

def NumIndentifica(num):
    if (num <= 0):
        result = 'N'
    else:
        result = 'P'
    return (result)
vnum = int(input('Informe um número: '))
print(NumIndentifica(vnum))    

