class Games():
  nome = ''
  genero = ''
  plataforma = ''
  ano = 0

  nomes = []
  generos = []
  plataformas = []
  anos = []

  def confirmar():
    nomes.append(nome)
    generos.append(genero)
    plataformas.append(plataforma)
    anos.append(ano)

  def getLista():
      print()  