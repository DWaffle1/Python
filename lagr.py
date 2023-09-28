import csv
import matplotlib.pyplot as plt


#перенос информации из файла в массив

data = []
with open("18_Сургут.csv" , encoding = 'utf-8') as r_file:
    f_reader = csv.reader(r_file, delimiter = ",")
    for i in f_reader:
        data.append(i)
                      
        
#создание осей для графика        

x_v=[]
for i in range(12):
    i += 1
    x_v.append(i)
    
y=[] #Значения температуры
for i in range(12): 
    y.append(data[i+2][1])
    

#функции для интерполяции

def l(x,i):
    res=1
    for j in range(len(x_v)):
        if i!=j :
            res *= (x-x_v[j]) / (x_v[i]-x_v[j])
    return res

def L(x,y):
    f=0
    for i in range(len(x_v)):
        if y[i] != 999.9:
            f += float(y[i])*l(x,i)
        elif y[i] == 999.9:
            continue
    return f

#Построение графика

a=[]
intp=[]

for i in range(7,127):
    a.append(float(i/10))
for i in range(120):
    intp.append(L(a[i],y))
plt.plot(a,intp)
for i in range(12):
    plt.scatter(x_v[i],y[i],color="black")
plt.show
        
