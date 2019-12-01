## 北京空气质量数据预处理
> 本次作业使用jupyter notebook进行数据的处理
### 汇总计算 PM 指数年平均值的变化情况
#### 导入csv文件
```python
import pandas as pd
df = pd.read_csv('BeijingPM20100101_20151231.csv')
```
导入结果预览

![image-20191201202725068](C:\Users\speci\AppData\Roaming\Typora\typora-user-images\image-20191201202725068.png)

#### 保留和PM值相关的列，并汇总计算平均值
```python
import numpy as np
s_col = df.columns[1:3].append(df.columns[6:10])
org_data = df.loc[:, s_col].copy()    #选取需要的列
org_data
# 清除指定的列全为空的行，dropna参数中axis = 0表示删除行，how = 'all' 表示全为空才删，subset表示针对那几列判空，inplace为真表示是否在原数据上操作，此处要复制到新的dataframe中去，故设为假
cln_data = org_data.dropna(axis = 0, how = 'all', subset = ['PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US Post']).copy()
cln_data.loc[:, 'PM_AVG'] = np.nan
for i in cln_data.index:
    cnt_not_null = 0
    PM_sum = 0
    for j in cln_data.columns[2:6]:
        if not np.isnan(cln_data.loc[i, j]):
            cnt_not_null += 1
            PM_sum += cln_data.loc[i, j]
    cln_data.loc[i, 'PM_AVG'] = PM_sum / cnt_not_null
```
结果

![image-20191201202929913](C:\Users\speci\AppData\Roaming\Typora\typora-user-images\image-20191201202929913.png)

#### 将清理后得到的数据按照年汇总得到每年的PM平均值
```python
grouped = cln_data['PM_AVG'].groupby(cln_data['year']).mean()
```

![image-20191201203055998](C:\Users\speci\AppData\Roaming\Typora\typora-user-images\image-20191201203055998.png)

#### 将结果绘制成折线图
```python
%matplotlib notebook
import matplotlib.pyplot as plt
plt.plot(grouped)
```

![image-20191201203232183](C:\Users\speci\AppData\Roaming\Typora\typora-user-images\image-20191201203232183.png)

### 汇总计算每年中1-12月的PM指数数据变化情况
对于每年的数据按照月分组，计算出每月的PM平均值，之后将六年的数据绘制成折线图
```python
fig = plt.figure()
fig_list = []
for x in range(1, 7):
    ax = fig.add_subplot(2, 3, x)
    fig_list.append(ax)

def monthly(year, data):
    data = data[data['year'] == year]
    monthly_grouped = data['PM_AVG'].groupby(data['month']).mean()
    return monthly_grouped
year = 2010
month_tick = []
for x in range (1, 13):
    month_tick.append(x)
# month_label = filter(str, month_tick)
for x in fig_list:
    x.plot(monthly(year, cln_data))
    x.set_title(str(year))
    x.set_xticks(month_tick)
    x.set_xticklabels(month_tick, rotation = 30, fontsize = 'small')
    
    year += 1
```
结果如下

![image-20191201203511527](C:\Users\speci\AppData\Roaming\Typora\typora-user-images\image-20191201203511527.png)
六年各自的汇总数据如下
##### 2010年
```
month
1      90.403670
2      97.239940
3      94.046544
4      80.072423
5      87.071913
6     109.038938
7     123.426075
8      97.683432
9     122.792735
10    118.784367
11    138.384036
12     97.115747
```
##### 2011年
```
month
1      44.873700
2     150.290179
3      57.991987
4      91.720670
5      65.108146
6     108.794655
7     107.386486
8     103.733800
9      94.969402
10    145.556818
11    109.434965
12    108.721400
```
##### 2012年
```
month
1     118.922388
2      84.442029
3      96.474324
4      87.835883
5      90.966715
6      96.634181
7      80.649709
8      81.165329
9      59.952247
10     94.951351
11     87.436963
12    109.187296
```
##### 2013年
```
month
1     183.195270
2     113.566468
3     114.572693
4      63.047801
5      89.148522
6     111.354861
7      74.932839
8      67.923611
9      85.717824
10    102.208781
11     85.146296
12     90.317764
```
##### 2014年
```
month
1     107.911738
2     160.513889
3     103.183244
4      92.160648
5      64.958557
6      59.154630
7      91.799955
8      65.668237
9      68.232639
10    135.269713
11    106.337500
12     76.622536
```
##### 2015年
```
month
1     110.022737
2     103.445561
3      94.483423
4      79.396991
5      61.167563
6      60.332407
7      60.229503
8      45.896057
9      50.924769
10     77.257841
11    125.803125
12    162.178987
```
