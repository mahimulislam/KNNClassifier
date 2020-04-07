import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import os
random.seed(1234)

df=pd.read_csv('train.txt',sep=",",header=None,dtype='Float64')
df_arr=df.values


df1=pd.read_csv('test.txt',sep=",",header=None,dtype='Float64')
df_arr1=df1.values

os.remove('prediction.txt')
xtrain=df_arr[:,0]
ytrain=df_arr[:,1]

xtest=df_arr1[:,0]
ytest=df_arr1[:,1]

classtrain=df_arr[:,2]
flagc1=0
flagc2=0

for i in range(0,len(xtrain)):
    if classtrain[i] == 1:
        if flagc1==0:
            plt.scatter(xtrain[i],ytrain[i],s=20,c='r',marker='o',label='class1 train')
            flagc1=1
        else:
            plt.scatter(xtrain[i], ytrain[i], s=20, c='r', marker='o')
    if classtrain[i] == 2:
        if flagc2==0:
            plt.scatter(xtrain[i], ytrain[i], s=20, c='g', marker='x', label='class2 train')
            flagc2=1
        else:
            plt.scatter(xtrain[i], ytrain[i], s=20, c='g', marker='x')


k = int(input('Enter value of k'))
for llld in range(0,len(xtest)):
    pointx = xtest[llld]
    pointy = ytest[llld]

    px = str(pointx)
    py = str(pointy)

    ins = 'Test Point: ' + px + ' , ' + py
    print(ins, file=open("prediction.txt", "a", encoding='utf8'))
    sqdforpoint = []
    sqdpointx = []
    sqdpointy = []
    sqdpointtrain = []


    for i in range(0,len(xtrain)):
        sqd=(xtrain[i]-pointx)**2+(ytrain[i]-pointy)**2
        sqdforpoint.append(sqd)
    sortindices=np.argsort(sqdforpoint)
    print(sortindices)
    sorteds=sorted(sqdforpoint)
    newsort=[]
    for ls in range(0,k):
        val=ls+1
        dmsg="Distance "+str(val)+': '+str(sorteds[ls])+'   '
        classmsg='Class = '
        ind=sortindices[ls]
        classassigned=classtrain[ind]
        classmsg+=str(classassigned)
        dmsg+=classmsg
        print(dmsg, file=open("prediction.txt", "a", encoding='utf8'))
        newsort.append(sorteds[ls])
    newclass1=0
    newclass2=0

    for i in range(0,len(xtrain)):
        sqd=(xtrain[i]-pointx)**2+(ytrain[i]-pointy)**2
        if(sqd in newsort):
            if(classtrain[i]==1):
                newclass1+=1
            if (classtrain[i] == 2):
                newclass2+=1

    if(newclass2>newclass1):
        print('2')
        plt.scatter(pointx, pointy, s=20, c='g', marker='s')
    else:
        print('1')
        plt.scatter(pointx, pointy, s=20, c='r', marker='s')


plt.legend(loc='best')
plt.show()