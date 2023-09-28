import math as m
a=0.1
i=0
def func(x):
    return x-((m.tan(0.55*x+0.1)-(x**2))/(-2*x+(0.55)/(m.cos(0.55*x+0.1)*2)))
def func1(x):
    return m.tan(0.55*x+0.1)-(x**2)
while True:
     b=func(a)
     if abs(a-b)<0.0001:
        print(a)
        print(b)
        print(func1(a)," ",func1(b))
        print(i)
        break
     a=b
     i+=1
