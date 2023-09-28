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
    if len(y) < 40 :
        if float(data[i][3]) == 999.9 :
            continue
        elif float(data[i][3]) != 999.9:
            y.append(float(data[i][3]))
            x_v.append(i)
    elif len(y) >= 40:
        break
    
##############################
sumx = 0
sumy = 0
sumxs = 0
sumxy = 0
for i in range (len(x_v)):
    sumxy += x_v[i]*y[i]
    sumx += x_v[i]
    sumy += y[i]
    sumxs += x_v[i]*x_v[i]
    
def a ():
    res = (len(x_v)*sumxy - sumx*sumy) / (len(x_v)*sumxs - (sumx*sumx))
    return res

def b ():
    r = (sumy - a()*sumx)/len(x_v)
    return r

def mnk(x):
    result = a()*x + b()
    return result       

##############################
intp=[]

x1 = np.arange(1,x_v[39]+0.3,0.1)
for i in range(len(x1)):
   # print(L(x1[i],y))
    intp.append(mnk(x1[i]))
#print(intp)

plt.plot(x1,intp)

for i in range(len(x_v)):
    plt.scatter(x_v[i],y[i],color = "black")
