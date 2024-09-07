import random

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

def coordenadas(valor, linha, coluna, jogador, valorx):
  if valor[linha][coluna] == ' ':
    valor[linha][coluna] = jogador
    valorx[linha][coluna] = jogador
  else:
    if jogador == 'X':
      print('Coordenada já escolhida!')
      rodadax()
    else:
      # tirei o print de erro, pois o erro do bot eh concertado sozinho
      # o usuário não precisa saber
      rodadao()
  return valor

def rodadax():
  print('Vez do jogador X')
  linha = int(input('Escolha uma linha: '))
  coluna = int(input('Escolha uma coluna: '))
  coordenadas(valor, linha, coluna, 'X', valorx)

def rodadao():
  # o jogador 'O' é feito pela máquina
  #tirei o print, pois se acontecer um erro o print e repetia todas as vezes
  linha = random.randint(0, 2)
  # a máquina escolhe a linha
  coluna = random.randint(0, 2)
  # a máquina escolhe a coluna
  coordenadas(valor, linha, coluna, 'O', valorx)

def resultado(valor):
  vencedor = ' '
  for linha in range(3):
    if valor[0][linha] == valor[1][linha] == valor[2][linha]:
      vencedor = valor[0][linha]
      print('O vencedor foi o jogador {}'.format(vencedor))
  for coluna in range(3):
    if valor[coluna][0] == valor[coluna][1] == valor[coluna][2]:
      vencedor = valor[coluna][0]
      print('O vencedor foi o jogador {}'.format(vencedor))
  if valor[0][0] == valor[1][1] == valor[2][2]:
    vencedor = valor[0][0]
    print('O vencedor foi o jogador {}'.format(vencedor))
  if valor[2][0] == valor[1][1] == valor[0][2]:
    vencedor = valor[1][1]
    print('O vencedor foi o jogador {}'.format(vencedor))
  return vencedor == ' '

valor = [[' ' for _ in range(3)]for _ in range(3)]

numeros = list(range(1, 10))
valorx = [numeros[i:i+3] for i in range(0, 9, 3)]

tabela(valor)
turnos = 0

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
  print('Vez do jogador O')
  # coloquei o print aqui para só se repetir um vez durante a rodada.
  rodadao()
  turnos += 1
  tabela(valor)