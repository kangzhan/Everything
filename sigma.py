import numpy as np
import pandas as pd
import math
from scipy.optimize import fsolve  
import scipy.stats

I = 0.034788#无风险收益率以短期债券收益率为准
R = np.log(1 + I)/365#计算连续利息力

Data=pd.read_excel('C:/Users/DELL/Desktop/data.xlsx')
Data['V_E']=Data['shares']*Data['close']
Data['logretn']=np.log(Data['V_E']/Data['V_E'].shift(1))
Sigma_E=Data['logretn'].std()#计算Sigma_E
X=Data['liab'][0]#计算X
result=[]
for i in range(110):
    def f(x):
        V_E= Data['V_E'][i]
        delta_t=(Data['date'][118]-Data['date'][i]).days
        V_A = float(x[0])  
        Sigma_A = float(x[1])  
        return [  
            V_E-V_A*scipy.stats.norm.cdf((np.log(V_A/X)+(R+Sigma_A*Sigma_A/2)*delta_t)/(Sigma_A*np.sqrt(delta_t)),0,1)-math.exp(-R*delta_t)*X*scipy.stats.norm.cdf((np.log(V_A/X)+(R-Sigma_A*Sigma_A/2)*delta_t)/(Sigma_A*np.sqrt(delta_t)),0,1),  
            Sigma_E - V_A * scipy.stats.norm.cdf((np.log(V_A/X)+(R+Sigma_A*Sigma_A/2)*delta_t)/(Sigma_A*np.sqrt(delta_t)),0,1)*Sigma_A/V_E  
        ]  
    result.append(fsolve(f, [Data['V_E'][118]+X, 0.01]))
result=pd.DataFrame(result,index=Data['date'][:110],columns=['V_A','Sigma_A'])
result.to_csv('C:/Users/DELL/Desktop/result.csv',float_format = '%.10f')
    