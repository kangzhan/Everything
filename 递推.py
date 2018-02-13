import numpy as np
import pandas as pd

lamda=10
i=0
def factorial(n):
    if(n<=1):
        return 1
    return (n*factorial(n-1))
def fx(j):
    return (lamda**j/factorial(j)*np.exp(-1*lamda))

fs={}
fs[i]=np.exp(lamda*(np.exp(-1*lamda)-1))
while(fs[i]>=0.0000000000001):
    i=i+1
    fs[i]=0
    for j in range(1,i+1):
        fs[i]=fs[i]+lamda*j/i*fx(j)*fs[i-j]
aa=pd.DataFrame(pd.Series(fs),columns=['fs'])
aa.to_csv('C:/Users/DELL/Desktop/result.csv',float_format = '%.10f')