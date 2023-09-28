import numpy as np

def jacobi(A, b, x0, eps=1e-17, max_iter=100):
    c = len(A)
    x = x0.copy()
    for k in range(max_iter):
        x_new = np.zeros(c)
        for i in range(c):
            s = 0
            for j in range(c):
                if i != j:
                    s += A[i][j] * x[j]
            x_new[i] = (b[i] - s) / A[i][i]
        if np.linalg.norm(x_new - x) < eps:
            return x_new
        x = x_new.copy()
        
n=12
x=np.zeros(n)
A=np.zeros([n,n])
b=np.zeros(n)

for i in range(0,n):
    b[i]=1/(i+1)
#print (f)

for i in range (0,n):
    for j in range(0,n):
        if i != j :
            A[i][j] =( (1) / (((i+1)*(i+1))+(j+1)))
        elif i == j :
            A[i][j] = 1
x0 = np.zeros(n)
x = jacobi(A, b, x0)
print(x)

for i in range(n):
    s=0
    for j in range(n):
        s += A[i][j]*x[j]
    res = abs(s-b[i])
    print(res)