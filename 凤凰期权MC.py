import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt
def mc_accumulator(path_num, S, H, E, vol, c_rate, annual_risk_free, d):
    risk_free = annual_risk_free / 252
    real_vol = vol / np.sqrt(252)
    path_ratio = S * np.exp(np.cumsum(risk_free - real_vol * real_vol / 2 + real_vol *
                                        ss.norm.rvs(size=[252, path_num]), axis=0))
    #生成股价路径
    gain = np.array([0.] * path_num)
    not_in = np.array([1] * path_num)
    effect = np.array([1] * path_num)
    monthly_not_in = np.array([1] * path_num)
    for i in range(252):
        monthly_not_in = monthly_not_in * (1 - (path_ratio[i] < H) * effect) # 判断敲入
        if (i+1) % 21 == 0:
            gain += effect * monthly_not_in * np.exp(-risk_free*(i+1)) * S * c_rate
            not_in = not_in * monthly_not_in
            monthly_not_in = np.array([1] * path_num)
            effect = effect * (path_ratio[i] < E)
    gain += (path_ratio[i] < E) * (path_ratio[i] - E) * (1 - not_in) * np.exp(-risk_free* 252)
    #plt.hist(gain, 50)
    #plt.show()
#    return [gain, path_ratio]
    return path_ratio
a=mc_accumulator(1000,100, 70, 100, 0.4, 0.015, 0.06, 1)