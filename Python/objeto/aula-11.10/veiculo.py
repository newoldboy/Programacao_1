class Veiculo:
    cor = ''
    num_portas = 0
    nivel_tanque = 0
    capacidade_tanque = 0

    # Construtor da classe
    # def __init__(self, corNova = 'Branca'): CASO CorNova possa ser null
     def __init__(self, corNova = 'Branca'):   
        print('Chamou método construtor')
        self.cor = 