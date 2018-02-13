import numpy as np
import pandas as pd
from scipy import stats


Data=pd.read_excel('C:/Users/DELL/Desktop/股票指数数据.xlsx')
Names=['上证综指','创业板指','中证500','沪深300']
Data=Data[Names]
Method=['pearson','kendall','spearman']
Corr={}

for method in Method:
    if(method=='pearson'):
        Corr[method]=pd.DataFrame(np.corrcoef(Data,rowvar=0),columns=Names,index=Names)
        Corr[method].to_csv('C:/Users/DELL/Desktop/all.csv')
        continue
    Corr[method]=pd.DataFrame(columns=Names,index=Names)
    if(method=='kendall'):
            for i in Names:
                for j in Names:
                    Corr[method][i][j]=stats.kendalltau(Data[i], Data[j])[0]
            Corr[method].to_csv('C:/Users/DELL/Desktop/all.csv',mode='a+')
            continue
    if(method=='spearman'):
            for i in Names:
                for j in Names:
                    Corr[method][i][j]=stats.spearmanr(Data[i], Data[j])[0]
            Corr[method].to_csv('C:/Users/DELL/Desktop/all.csv',mode='a+')
            continue