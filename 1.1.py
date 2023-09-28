a=0
b=10
c=a
d=0
i=0
def func(x):
    return (x**3)-18*x-10

while True :
    if func(a)*func(b)<0:
        d=c-((func(c)*(b-c))/(func(b)-func(c)))
        if abs(d-c)<0.0001:
            print(d," ",i," ", func(d))
            break
        else:
            c=d
            i+=1
    elif func(a)*func(b)>=0:
        print("Плохой интервал")
        break
        