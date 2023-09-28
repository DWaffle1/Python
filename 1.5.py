import numpy as np
import math as m
def f(x):
    return np.array([[m.sin(x[0]-0.6)-x[1]-1.6],[3*x[0]-m.cos(x[1])-0.9]])
def p1x(x):
    return m.cos(x-0.6)
def p1y(x):
    return -1
def p2x(x):
    return 3
def p2y(x):
    return m.sin(x)

x0=np.array([1.,1.])
Y=np.array([[p1x(x0[0]),p1y(x0[1])],[p2x(x0[0]),p2y(x0[1])]])
xn=np.array([15.,15.])
xpg=abs(xn[0]-x0[0])
ypg=abs(xn[1]-x0[0])
e=0.0001

while (xpg > e) and (ypg > e):
    newt= np.transpose(np.matmul(np.linalg.inv(Y) ,f(x0) ))
    c=np.array([newt[0][0],newt[0][1]])
    xn=x0-c
    Y=np.array([[p1x(x0[0]),p1y(x0[1])],[p2x(x0[0]),p2y(x0[1])]])
    xpg=abs(xn[0]-x0[0])
    ypg=abs(xn[1]-x0[0])
    x0=xn
print (xn)

print(m.sin(xn[0]-0.6)-xn[1]-1.6)
print(3*xn[0]-m.cos(xn[1])-0.9)
