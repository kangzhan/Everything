import numpy as np
import pandas as pd
from numpy.linalg import cholesky
import matplotlib.pyplot as plt

  
num = 50;
col=[]
for i in np.arange(num):
    col.append('X'+str(i+1))
    
#二维正态
miu2 = np.array([2, 7])
sigma2 = np.array([[1, 1.5], [1.5, 3]])
r2 = cholesky(sigma2)
s2 = np.dot(np.random.randn(num, 2), r2) + miu2
plt.plot(s2[:,0],s2[:,1],'+')
plt.show()
s2=pd.DataFrame(s2.T,columns=col)
s2.T.to_csv('C:/Users/DELL/desktop/多维正态/二维正态.csv')

#三维正态
miu3 = np.array([2, 5, 8])
sigma3 = np.array([[1, 1.5, 0.9], [1.5, 3,1.7], [0.9,1.7,5]])
r3 = cholesky(sigma3)
s3 = np.dot(np.random.randn(num, 3), r3) + miu3
s3=pd.DataFrame(s3.T,columns=col)
s3.T.to_csv('C:/Users/DELL/desktop/多维正态/三维正态.csv')

#四维正态
miu4 = np.array([2, 5, 8,-5])
sigma4 = np.array([[1, 1.5, 0.9,2.1], [1.5, 3,1.7,1.8], [0.9,1.7,5,3],[2.1,1.8,3,8]])
r4 = cholesky(sigma4)
s4 = np.dot(np.random.randn(num, 4), r4) + miu4
s4=pd.DataFrame(s4.T,columns=col)
s4.T.to_csv('C:/Users/DELL/desktop/多维正态/四维正态.csv')

#五维正态
miu5 = np.array([2, 5, 8,-5,12])
sigma5 = np.array([[1, 1.5, 0.9,2.1,0], [1.5, 3,1.7,1.8,0], [0.9,1.7,5,3,0],[2.1,1.8,3,8,0],[0,0,0,0,4]])
r5 = cholesky(sigma5)
s5 = np.dot(np.random.randn(num, 5), r5) + miu5
s5=pd.DataFrame(s5.T,columns=col)
s5.T.to_csv('C:/Users/DELL/desktop/多维正态/五维正态.csv')