# nem eu sei o contexto desde exercicio, eu apenas queria colocar em prática algumas coisas
# ignorem que não existe nenhuma lógica kdkdksdkasdkda
import random as rd
import matplotlib.pyplot as plt

time1=[]
time2=[]

def relatorioTime():
    
  nomeTime1 = input('Informe o nome do Time 1: ')
  nomteTime2 = input('Informe o nome do Time 2: ')

  print('Jogou começou a rolar!')

  for jogo in range(10):
      gol1 = rd.randrange(0,10)
      gol2 = rd.randrange(0,10)
      
      time1.append(gol1)
      time2.append(gol2)

  print('acabou')
  print(time1[0:])
  print(time2[0:])
  grafico = input('deseja imprimir um gráfico do game?: ')

  if grafico == 'Sim':

      plt.plot(time1,time2, marker = ('o') )
      plt.show()
relatorioTime()
