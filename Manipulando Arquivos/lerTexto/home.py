
def ler(arquivo):
    # Lê o arquivo
    texto = ''  
    arquivo = open(arquivo, 'r')
    texto = arquivo.read()
    arquivo.close()
    return texto
