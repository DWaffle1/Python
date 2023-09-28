import matplotlib.pyplot as mp
import math as m
a=-0.5
i=0
xg=[]
yg=[]
for i in range(0,101,1):
    xg.append(0.02*i-0.5)
for i in range (0,101,1):
    yg.append(m.tan(0.55*xg[i]+0.1)-(xg[i]**2))
def func(x):
    return (m.atan(x**2)-0.1)/0.55
def func1(x):
    return m.tan(0.55*x+0.1)-(x**2)
while True:
     b=func(a)
     if abs(a-b)<0.0001:
        print(a)
        print(b)
        print(func1(b)," ", func1(a))
        print(i)
        break
     a=b
     i+=1
mp.plot(xg,yg)
mp.show()
