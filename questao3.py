import time
  #Recursividade, é quando uma função chama a sí próprio dentro de seu escopo, a função "contagemRegressiva" na linha 2, chama a sí mesma na linha 9 do programa
def contagemRegressiva(n):
  if n == 0 :
    print("Fogo")
  else:
    print(n)
    time.sleep(1)
    contagemRegressiva( n - 1)


n = int(input('informe um numero---> '))
contagemRegressiva(n)
