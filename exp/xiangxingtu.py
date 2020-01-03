import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

#打开CSV文件
fileNameStr = 'result.csv'
df = pd.read_csv(fileNameStr,encoding='gbk')
print("------------describe---------------")
print(df.describe())  #查看统计信息

df.boxplot(column='unitprice')  #生成箱型图

#展示均值线

f = df.boxplot(column='totalprice',meanline=True,showmeans=True,return_type='dict')
print(f)
print(type(f))

for mean in f['means']:
    mean.set(color='r', linewidth=3)

plt.show()