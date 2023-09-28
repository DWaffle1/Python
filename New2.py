import csv
import matplotlib.pyplot as plt
import numpy as np


#перенос информации из файла в массив

data = []
with open("18_Сургут.csv" , encoding = 'utf-8') as r_file:
    f_reader = csv.reader(r_file, delimiter = ",")
    for i in f_reader:
        data.append(i)
  
##############################

#создание массивов

x_v=[]
for i in range(6):
    i += 1
    x_v.append(i)  
#print(x_v[5])


y=[] 
for i in range(6): 
    y.append(float(data[i+7][1]))
#print(y)  

  
arr=np.zeros((len(y),len(y)))
#print (arr)


for i in range(len(y)):
    arr[i][0]=y[i]
#print (arr)

##############################

#Заполнение массивов разницами

for i in range(1,len(y)):
    for j in range(0, len(y)-1):
        if arr[j+1][i-1] != 0:
            arr[j][i]=arr[j+1][i-1]-arr[j][i-1]
        elif  arr[j+1][i-1] == 0:
            continue
#print (arr)
#for i in range(1,len(x_v)):
    #print(arr[len(arr)-i-1][i])


#############################

#Второй метод Ньютона
def q(x):
    return x-x_v[len(x_v)-1]


def N(x):
    s = arr[len(arr)-1][0]
    p=1
    for i in range(1,len(x_v)):
        p *= (q(x)+(i-1))/i
        s += arr[len(arr)-i-1][i]*p
    return s
    
##############################

#Построение графика

intp=[]
#print(N(x_v[1]))

x1 = np.arange(0.9,6.1,0.1)
for i in range(len(x1)):
    intp.append(N(x1[i]))

plt.plot(x1,intp)
for i in range(6):
    plt.scatter(x_v[i],y[i],color = "black")
