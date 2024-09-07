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

def coordenadas(valor, linha, coluna, jogador):
  if valor[linha][coluna] == ' ':
    valor[linha][coluna] = jogador
  else:
    if jogador == 'X':
      print('Coordenada já escolhida!')
      rodadax()
    # o bot não precisa da correção de erro por aqui
    # na própria jogada do bot existe a possivel correção
  return valor

def rodadax():
  print('Vez do jogador X')
  linha = int(input('Escolha uma linha: '))
  coluna = int(input('Escolha uma coluna: '))
  coordenadas(valor, linha, coluna, 'X')

def verificar_coluna(valor):
  for j in range(3): # j = coluna
    coluna = [valor[i][j] for i in range(3)] # verifica elemento por elemento de cada coluna
    if coluna.count('X') == 2 and coluna.count(' ') == 1:
      # se tiver 2 'x' ele retorna a coordenada no elementop vazio, para ser preencido pelo O
      return coluna.index(' '), j
  return None # caso contrário, retorna nada e segue para a próxima verificação

def verificar_linha(valor):
  for i in range(3): # i =linha
    # como é por linha, não precisa contrar os elementos das colunas
    if valor[i].count('X') == 2 and valor[i].count(' ') == 1:
      # o mesmo que acontece no verificar_coluna()
      return i, valor[i].index(' ')
  return None

def verificar_diagonais(valor):
  if [valor[i][i] for i in range(3)].count('X') == 2 and [valor[i][i] for i in range(3)].count(' ') == 1:
    # aqui ja foi feito de forma junta a comtagem dos elementos 'x' e ' ', além de rodar por toda a diagonal principal
    return [valor[i][i] for i in range(3)].index(' '), [valor[i][i] for i in range(3)].index(' ')
    # retorna a coordenada que tem o elemento ' ' na diagonal principla para ser preenchido pelo O
  if [valor[i][2 - i] for i in range(3)].count('X') == 2 and [valor[i][2 - i] for i in range(3)].count(' ') == 1:
    # aqui verifica a diagonal secundária
    return [valor[i][2 - i] for i in range(3)].index(' '), 2 - [valor[i][2 - i] for i in range(3)].index(' ')
    # retorna a coordenada do elemtno ' ' na diagonal secundária
  return None

def rodadao():
  jogada = verificar_linha(valor) or verificar_coluna(valor) or verificar_diagonais(valor)
  # o bot tem como prioridade as jogadas mais vantajosas para ele
  # pela ordem de prioridade
  # se não tiver vantagem, ele joga aleatório
  if jogada:
    linha, coluna = jogada
    # se alguma verificação der certa, ela irá retornar 2 valores
    # a linha e a coluna, então isso é absorvido do elemento jogada
  else:
    linha, coluna = random.randint(0, 2), random.randint(0, 2)
    # se não tiver jogadas vantajosas, os números são aleatórios
    while valor[linha][coluna] != ' ': # verificar se a vaga está liberada
      linha, coluna = random.randint(0, 2), random.randint(0, 2)
  coordenadas(valor, linha, coluna, 'O')

def resultado(valor):
  vencedor = ' '
  for linha in range(3):
    if valor[0][linha] == valor[1][linha] == valor[2][linha] != ' ':
      # adicionei o != ' ' para excluir o valorx, pois assim fica com menos uso de memória
      vencedor = valor[0][linha]
      print('O vencedor foi o jogador {}'.format(vencedor))
  for coluna in range(3):
    if valor[coluna][0] == valor[coluna][1] == valor[coluna][2] != ' ':
      vencedor = valor[coluna][0]
      print('O vencedor foi o jogador {}'.format(vencedor))
  if valor[0][0] == valor[1][1] == valor[2][2] != ' ':
    vencedor = valor[0][0]
    print('O vencedor foi o jogador {}'.format(vencedor))
  if valor[2][0] == valor[1][1] == valor[0][2] != ' ':
    vencedor = valor[1][1]
    print('O vencedor foi o jogador {}'.format(vencedor))
  return vencedor == ' '

valor = [[' ' for _ in range(3)]for _ in range(3)]

numeros = list(range(1, 10))

tabela(valor)
turnos = 0

while resultado(valor):
  if turnos == 9 and resultado(valor):
    print('Deu velha!')
    break
  rodadax()
  turnos += 1
  tabela(valor)
  if not resultado(valor):
    break
  if turnos == 9 and resultado(valor):
    print('Deu velha!')
    break
  print('Vez do jogador O')
  rodadao()
  turnos += 1
  tabela(valor)