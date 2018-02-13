import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#读入文件名字
name="priceroad(T=1000,s0=100.000000,miu=0.020000,sigma=0.100000)"
#读入txt文件为DataFrame
priceroad=pd.read_csv('F:/C++_WorkSpace/Stockprice_randomwalk/Stockprice_randomwalk/'+name+'.txt', header = None,sep=',', encoding='utf8')
plt.figure(figsize=(30,10)) 
#把100条轨道画在一个图里
for i in priceroad.index:
    plt.plot(priceroad.iloc[i])
#输出图片
plt.savefig("F:/C++_WorkSpace/Stockprice_randomwalk/Stockprice_randomwalk/"+name+".jpg") 