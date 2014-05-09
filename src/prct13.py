#!/src/bin/python
import modulo
import time
import matplotlib.pyplot as pl
import numpy as np
import moduloerror

nro_test=100
intervalos=[10, 50, 100, 150, 500, 550, 1000]
umbral=[1e-3, 1e-4, 1e-5, 1e-6, 1e-7]


p=[]
for n in intervalos:
  ci=time.clock() 
  e=modulo.error(n, nro_test,1e-5 )
  cf=time.clock()
  tp=cf-ci 
  p=p+[tp]

#Primera grafica

pl.subplot(2,1,1)

pl.plot(intervalos,p, color="red", linewidth=2.5, linestyle="-")
pl.xticks([10,50,100,150,500,550,1000])
pl.xlim(-10.0,1100.0)
pl.ylim(-0.001,0.14)
pl.xlabel('Intervalos')
pl.ylabel('Tiempo en segundos')
pl.title('Tiempo')
pl.savefig("graficatiempo.eps",dpi=72)
pl.show()


t=[]
for n in intervalos:
  porcentaje=[]
  for i in umbral:
    x=moduloerror.error(n,100,umbral)
    porcentaje=porcentaje+[x]
  t=t+[p]

print t[0]
print t[1]
print t[2]
print t[3]
print t[4]
#Segunda grafica

pl.subplot(2,1,1)

pl.plot(umbral,t[0], color="blue", linewidth=2.5, linestyle="-", label="10")
pl.plot(umbral,t[1], color="red", linewidth=2.5, linestyle="-.", label="50")
pl.plot(umbral,t[2], color="black", linewidth=2.5, linestyle="--", label="100")
pl.plot(umbral,t[3], color="yellow", linewidth=2.5, linestyle="..", label="150")
pl.plot(umbral,t[4], color="green", linewidth=2.5, linestyle="-", label="500")
pl.plot(umbral,t[5], color="violet", linewidth=2.5, linestyle="-", label="550")
pl.plot(umbral,t[6], color="grey", linewidth=2.5, linestyle="-", label="1000")

pl.legend(loc='upper left')
pl.xlim(1e-1,1e-9) #Limite en el eje x
pl.xticks([1e-3, 1e-4, 1e-5, 1e-6, 1e-7]) 
pl.ylim(-2.0,110.0) #Limite en el eje y
pl.title('Porcenatjes')
pl.savefig("graficapor.eps", dpi=72)

pl.show()



