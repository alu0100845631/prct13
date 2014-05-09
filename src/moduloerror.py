#!/src/bin/python
PI=3.1415926535897931159979634685441852
import sys

#Funcion de aproximacion.

def aproximacion(n):
  n=int (n)
  if(n!=0):
   suma=0
   for i in range(1,n+1):
     x_i=(i-0.5)/float(n)
     fx_i=4/(1+x_i**2)
     b=i/float(n)
     a=b-(1/float(n))
     suma=suma+fx_i
   pi=suma/float(n)
   return pi
   
#Aqui creamos la funcion de error.

def error(n,m,umbral):
  incorrectos=0
  for i in range(m):
    valor_pi=aproximacion(n)
    valor=valor_pi-PI  #Se calcula la diferencia.
    if(abs(valor)>umbral):
      incorrectos=incorrectos+1 #Se va incrementando el numero de incorrectos.
  porcentaje=(incorrectos/float(m))*100
  return porcentaje
      
      
#Creamos un bloque dentro de la funcion.

if __name__ == "__main__":     
 
 if(len(sys.argv)==4):
   n= int(sys.argv[1])
   m=int(sys.argv[2])
   umbral=float(sys.argv[3])
 else:
   print'La forma de uso es: "modulo.py, n, m, umbral", por lo que se utilizaran los valores por defecto.'
   n=10
   m=10
   umbral=0.00001  
   
 #Llamamos a la funcion.
 
 porcentaje=error(n,m,umbral)
 print 'El numero de porcentajes es %f' %porcentaje