import numpy as np


###########################################


# Задание СЛАУ



n=12
x=np.zeros(n)
a=np.zeros([n,n])
b=np.zeros([n,n])
f=np.zeros(n)
f1=np.zeros(n)
vych = 0
ai=np.zeros([n,n])
t=np.zeros(n)

for i in range(1,n+1):
    f[i-1]=1/i
#print (f)

for i in range (1,n+1):
    for j in range(1,n+1):
        if i != j :
            a[i-1][j-1] =( (1) / ((i*i)+j))
        elif i == j :
            a[i-1][j-1] = 1


###########################################

#Метод Якоби
for i in range(0,len(a)):
    t[i]=f[i]
    for j in range(0,len(a)):
        if i != j:
            t[i] -=(a[i][j]*x[i])
    t[i] /=(a[i][i])
norm=abs(x[0]-t[0])
for i in range(0, len(a)):
    if abs(x[i]-t[i])>norm:
        norm = abs(x[i]-t[i])
    x[i]=t[i]
while norm > 0.001:
    for i in range(0,len(a)):
        t[i]=f[i]
        for j in range(0,len(a)):
            if i != j:
                t[i] -=(a[i][j]*x[i])
        t[i] /= (a[i][i])
    norm=abs(x[0]-t[0])
    for i in range(0, len(a)):
        if abs(x[i]-t[i])>norm:
            norm = abs(x[i]-t[i])
        x[i]=t[i]



for j in range(0,len(a)):
    s=0
    for i in range(0,len(a)):
        s += a[j][i]*x[i]
    #print(i,') ',s,a[1][i],x[i],f[1])
    print(s-f[j])

        