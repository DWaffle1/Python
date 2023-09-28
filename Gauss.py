import numpy as np



###########################################


# Задание СЛАУ



n=12
x=np.zeros(n)
a=np.zeros([n,n])
f=np.zeros(n)

for i in range(0,n):
    f[i]=1/(i+1)
#print (f)

for i in range (0,n):
    for j in range(0,n):
        if i != j :
            a[i][j] =( (1) / (((i+1)*(i+1))+(j+1)))
        elif i == j :
            a[i][j] = 1
       
ad=a.copy()
fd=f.copy()            
            
############################################
for k in range (n-1):
    for i in range (k+1,n):
        c=a[i][k]/a[k][k] #чтобы не занулялся
        for j in range(n):            
            a[i][j] = a[i][j] - a[k][j] * (c)
        f[i] = f[i]-f[k] * (c)
  

         
v = 0
for i in range (n-1,-1,-1):
    v = 0
    for j in range(n-1,i,-1):
        v += a[i][j]*x[j]
    x[i] = (f[i]-v)/a[i][i]
print(x)


s=0
res=5
#print(ad,fd)
for i in range(n):
    s=0
    for j in range(n):
        s += ad[i][j]*x[j]
    res = abs(s-fd[i])
    print(res)

    