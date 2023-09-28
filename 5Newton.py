import numpy as np
import matplotlib.pyplot as plt


x1 = -5.0
x2 = 12.0
x=[[x1],[x2]]

def f(x1,x2):
    return float(2*(x1**2) - 16*x1 + 3*(x2**2) + 51*x2 + 249.75)

def chast_proizx1(x1):
    return float(4.0*x1 - 16.0)
def chast_proizx2(x2):
    return float(6.0*x2 + 51.0)
def gradient(x):
    vector = [[-chast_proizx1(x[0][0])],[-chast_proizx2(x[1][0])]]
    return vector

def chast_proizx12():
    return float(4)
def chast_proizx22():
    return float(6)
def gradient2():
    vector = [[chast_proizx12(),0],[0,chast_proizx22()]]
    return vector

xn=[[],[]]
p=[]
array=[]
while True:
    array.append(x)
    p=np.linalg.solve(gradient2(),gradient(x))
    xn=x+p
    if np.linalg.norm(xn-x)<0.001:
        break
    x=xn
print(x)
listx=[]
listy=[]
for i in range (len(array)):
    listx.append(array[i][0])
for i in range (len(array)):
    listy.append(array[i][1])
    
list_of_x = np.arange(-10, 20, 0.1)
list_of_y = np.arange(-20, 10, 0.1)
list_of_z = np.arange(-10, 10, 0.1)
xgrid, ygrid, zgrid = np.meshgrid(list_of_x, list_of_y, list_of_z)
zgrid = 2*xgrid**2-16*xgrid+3*ygrid**2+51*ygrid+249.75+500

X, Y = np.meshgrid(list_of_x, list_of_y)
Z = zgrid[:,:,0].reshape(X.shape)

C = plt.contour(X, Y, Z, levels=10)
plt.clabel(C, inline=1)

plt.plot(listx,listy)
plt.scatter(x[0], x[1], color = "Orange")

fig = plt.figure()
axes = fig.add_subplot(projection='3d')
axes.plot_surface(X, Y, Z,  linewidth=0.3)
axes.scatter(x[0],x[1],  color="red")
plt.show()


    