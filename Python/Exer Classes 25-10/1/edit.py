from tamogoshi import Bixo


print('''
    Editar tamogoshi!
''')

new_bixo = Bixo()
new_bixo.nome = input('Informe o nome: ')
new_bixo.fome = int(input('''
    Informe o alimento que ira dar para seu bixo;

    1 - carne;
    2 - bolacha;
    3 - banana;
    4 - Não dar comida;

    Informe uma das opções do cardapio: 
'''))
new_bixo.idade = int(input('Informe a idade: '))
new_bixo.alteraBixo(new_bixo)
