def tabela(valor):
  print('   ' + '0' + '   ' + '1' + '   ' + '2')
  print('0', end=' ')
  print(' ' + valor[0][0] + ' ' + '|' + ' ' + valor[0][1] + ' ' + '|' + ' ' + valor[0][2])
  print('  ' + '-'*11)
  print('1', end=' ')
  print(' ' + valor[1][0] + ' ' + '|' + ' ' + valor[1][1] + ' ' + '|' + ' ' + valor[1][2])
  print('  ' + '-'*11)
  print('2', end=' ')
  print(' ' + valor[2][0] + ' ' + '|' + ' ' + valor[2][1] + ' ' + '|' + ' ' + valor[2][2])
  # Criar o desenho que é mostrado no Shell

def coordenadas(valor, linha, coluna, jogador, valorx):
  if valor[linha][coluna] == ' ':
    valor[linha][coluna] = jogador
    valorx[linha][coluna] = jogador
    # substituindo o local 'vazio' com o X ou O
  else:
    if jogador == 'X':
      print('Coordenada já escolhida!')
      rodadax() # reiniciar o turno do jogador X
    else:
      print('Coordenada já escolhida!')
      rodadao() #reiniciar o turno do jogador O
  # se estiver ocupado refazer as coordenadas
  # não consegui pensar em como fazer de uma vez.
  # possivelmente teria que criar uma variavel universal que seria o jogador, um por turno
  # ai então eu substituiria
  return valor # a matriz 3x3 atualizada

def rodadax():
  print('Vez do jogador X')
  linha = int(input('Escolha uma linha: '))
  coluna = int(input('Escolha uma coluna: '))
  coordenadas(valor, linha, coluna, 'X', valorx)
  # turno do jogador X

def rodadao():
  print('Vez do jogador O')
  linha = int(input('Escolha uma linha: '))
  coluna = int(input('Escolha uma coluna: '))
  coordenadas(valor, linha, coluna, 'O', valorx)
  # turno do jogador O

def resultado(valor):
  vencedor = ' '
  for linha in range(3):
    if valor[0][linha] == valor[1][linha] == valor[2][linha]:
      vencedor = valor[0][linha]
      print('O vencedor foi o jogador {}'.format(vencedor))
      # se existe linhas com mesmo valor
  for coluna in range(3):
    if valor[coluna][0] == valor[coluna][1] == valor[coluna][2]:
      vencedor = valor[coluna][0]
      print('O vencedor foi o jogador {}'.format(vencedor))
      # se existe coluna com o mesmo valor
  if valor[0][0] == valor[1][1] == valor[2][2]:
    vencedor = valor[0][0]
    print('O vencedor foi o jogador {}'.format(vencedor))
    # se a diagona principal tem valores iguais
  if valor[2][0] == valor[1][1] == valor[0][2]:
    vencedor = valor[1][1]
    print('O vencedor foi o jogador {}'.format(vencedor))
    # se a diagonal secundaria tem valores iguais
  return vencedor == ' ' # expressão booleana

valor = [[' ' for _ in range(3)]for _ in range(3)]
# a matriz que será o jogo da velha

numeros = list(range(1, 10))
valorx = [numeros[i:i+3] for i in range(0, 9, 3)]
# uma matriz 3x3 para ser substituida junto com a matriz principal do jogo da velha
# eu criei essa matriz, pq o meus resultados estavam dando errado, ja que a matriz
# originalmente tme todos os valores igual = ' '
# entção criei uma cópia só para a pontuação

tabela(valor)
turnos = 0
# os turnos servem para avaisar que deu velha
# novamente não consegui implementar isso no resultado()

while resultado(valorx):
  if turnos == 9 and resultado(valorx):
    print('Deu velha!')
    break
  rodadax()
  turnos += 1
  tabela(valor)
  if not resultado(valorx):
    break
  if turnos == 9 and resultado(valorx):
    print('Deu velha!')
    break
  rodadao()
  turnos += 1
  tabela(valor)
  # loop while, que se baseia no resultado()
  # quando se acha o vencedor o loop para, caso o contrario
  # chega no limite de turnos e da velha.