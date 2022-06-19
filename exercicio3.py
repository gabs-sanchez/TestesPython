import matplotlib.pyplot as plt
import numpy as np

def Grafico():
      
      x = np.array([10,20], dtype = int)
      y = np.array([10,200], dtype = int)

      print(x)
      print(y)
      
      #plt.plot(x,y,marker=('o'))
      plt.bar(x,y,color=('green','blue'))
      plt.title('Gráfico Legal')
      plt.xlabel('valor x')
      plt.ylabel('valor y')

      plt.show()

Grafico()
