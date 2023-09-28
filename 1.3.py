a=-2
b=-4
с=0
i=0
def func(x):   
    return float((x**3)-(18*x)-10)

while True :
    c=float((a+b)/2)
    if func(a)*func(b)<0:
        if func(a)*func(c)<0:
            b=c
        elif func(c)*func(b)<0:
            a=c
        i+=1
        if abs(b-a)<0.0001:
            print(a," ",b," ",i," ", func(b)," ", func(a))
            break
    elif func(a)*func(b)>=0:
        print("плохой интервал")
        break
#4.4970
#-0.5656
#-3.93






    
    

