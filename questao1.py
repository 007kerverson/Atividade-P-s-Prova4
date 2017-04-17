import random
numeros =[1, 2, 3, 4, 5]
alunos = {20161:'kleber', 20162:'clovis', 20163:'claiton' }
mensagemProva4 = []
print('''
i. ‘Seja bem vindo(a) ao Programa da Prova 4’;

ii. Defina o que é uma lista e imprima na tela;

iii. Defina o que é um dicionário e imprima na tela;

iv. ‘Estou pronto para manipular listas e dicionários na prova!’;

''')
sorteados = []
for repetir in range(0,20):
  val_aleatorio = random.randint(1, 100)
  sorteados.append(val_aleatorio)
  print('O Valor Da Linha ',repetir,'È',sorteados[repetir])

mensagemProva4.append('Prova sobre manipulação de listas e dicionários')  
contar = len(mensagemProva4[0])
mensagemProva4.append('Prova de número 4.')
