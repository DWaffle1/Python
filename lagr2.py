import csv
import matplotlib.pyplot as plt
import numpy as np


#перенос информации из файла в массив

data = []
with open("18_Сургут.csv" , encoding = 'utf-8') as r_file:
    f_reader = csv.reader(r_file, delimiter = ",")
    for i in f_reader:
        data.append(i)
                      
        
#создание осей для графика        

x_v=[]   
y=[]
i=0
while True:
    i += 1
    print (data[i][3])
    if len(y) < 12 :
        if float(data[i][3]) == 999.9 :
            continue
        elif float(data[i][3]) != 999.9:
            y.append(float(data[i][3]))
            x_v.append(i)
    elif len(y) >= 12:
        break
print(y)    
print(x_v)
#функции для интерполяции

def l(x,i):
    res=1
    for j in range(len(x_v)):
        if i!=j :
            res *= float((x-x_v[j]) / (x_v[i]-x_v[j]))
    return res

def L(x,y):
    f=0
    for i in range(len(x_v)):
        f += y[i]*l(x,i)

    return f

#Построение графика
intp=[]
print(L(x_v[5],y))
x1 = np.arange(1,x_v[11]+0.3,0.1)
for i in range(len(x1)):
   # print(L(x1[i],y))
    intp.append(L(x1[i],y))
#print(intp)

plt.plot(x1,intp)
for i in range(len(x_v)):
    plt.scatter(x_v[i],y[i],color = "black")




