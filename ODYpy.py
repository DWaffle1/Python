import numpy as np
import matplotlib.pyplot as plt
import math as m
import scipy
h=0.5
y0=1
dy=0
xend=2
x0=0
ite=int((xend-x0)/h)
x=[0]*ite
y=[0]*ite

for i in range(ite-1):
    x[i+1]=x[i]+h


def f(x,yzw):
    y,z = yzw
    dy = z
    dz = x*m.exp(-x)-(8./5.)*z-(4./5.)*y
    return (dy,dz)

yzw=[0]*ite
yzw[0]=(y0,dy)
prib=()
for i in range(ite-1):
   prib = yzw[i]+h*np.array(f(x[i],yzw[i]))
   yzw[i+1] = yzw[i] + (h/2)*np.array((np.array(f(x[i],yzw[i])) + np.array(f(x[i+1],prib))))


for i in range(ite):
    y[i]=yzw[i][0]
#print(y)

while True:
    h=h/2
    ite = int((xend-x0)/h)
    x=[0]*ite
    y1=[0]*ite
    for i in range(ite-1):
        x[i+1]=x[i]+h
    yzw=[0]*ite
    yzw[0]=(y0,dy)
    prib=()
    for i in range(ite-1):
       prib = yzw[i]+h*np.array(f(x[i],yzw[i]))
       yzw[i+1] = yzw[i] + (h/2)*np.array((np.array(f(x[i],yzw[i])) + np.array(f(x[i+1],prib))))
    for i in range(ite):
        y1[i]=yzw[i][0]
    y2=[]
    for i in range(0,len(y1),2):
        y2.append(y1[i])
    y3=np.array(y2)
    if np.linalg.norm(y-y3)<0.01:
        break
    y=y1
print("Оптимальный шаг:",h)
plt.plot(x,y1)
plt.show()
    