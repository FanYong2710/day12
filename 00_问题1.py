import numpy as np

data = np.array([6,6,6,6,6,6])

#平均值
mean = (np.mean(data))
print(mean)

#标准差
std = np.std(data)

#标准化公式
print((data - mean) / std)