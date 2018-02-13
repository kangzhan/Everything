import pandas as pd
import numpy as np
from scipy.stats import mvn,norm

BBB=[0.18,0.12,1.17,5.30,86.93,5.95,0.33,0.02]
A  =[0.06,0.01,0.26,0.74,5.52,91.05,2.27,0.09]
D1=[0]
for i in BBB:
    D1.append(D1[-1]+i)    
D2=[0]
for i in A:
    D2.append(D2[-1]+i)
    
ppf1=np.array([norm.ppf(i/100,0,1) for i in D1])
ppf2=np.array([norm.ppf(i/100,0,1) for i in D2])
ppf1[0]=ppf2[0]=-9999999999999999999999
ppf1[-1]=ppf2[-1]=9999999999999999999999
rslt=np.zeros(shape=(len(ppf1)-1,len(ppf2)-1)) 
mu=[0,0]
S = [[1,0.3],[0.3,1]]
    
for i in range(len(ppf1)-1):
    uu=[]
    for j in range(len(ppf2)-1):
        low=[ppf1[i],ppf2[j]]
        up=[ppf1[i+1],ppf2[j+1]]
        p,k = mvn.mvnun(low,up,mu,S)
        rslt[len(ppf1)-2-i,len(ppf2)-2-j]=p*100

pd.DataFrame(rslt).to_csv('C:/Users/DELL/Desktop/rslt.csv')