import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#1.打开CSV文件
fileNameStr = 'sy8.csv'
df_date = pd.read_csv(fileNameStr,encoding='utf-8')

print("--------------head--------------")
print(df_date.head())
print("--------------describe--------------")
print(df_date.describe())
print("--------------info--------------")
print(df_date.info())
print("================================")
#2.查看是否有缺失值
print(df_date.isnull().sum().sort_values(ascending=False))

#3.生成画布和子图
fig = plt.figure()
#ax1 = fig.add_subplot()

ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)


#去掉ave列中最大的两个异常值
print('--------------------------------')
print(type(df_date),type(df_date['ave']))

mean = df_date['ave'].mean()

max=df_date["ave"].max()
df_date.loc[df_date["ave"]==max,"ave"] = mean

max=df_date["ave"].max()
df_date.loc[df_date["ave"]==max,"ave"] = mean
print('--------------------------------')



#归一化
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

#将ave列归一化
x_reshape = df_date["ave"].values.reshape(-1, 1)
ave = scaler.fit_transform(x_reshape)  #调用MinMaxScaler的fit_transform转换方法

#将DEWP_new列归一化
x_reshape = df_date["DEWP_new"].values.reshape(-1, 1)  #变成n行1列的二维矩阵形式
DEWP = scaler.fit_transform(x_reshape)  #调用MinMaxScaler的fit_transform转换方法

#将HUMI_new列归一化
x_reshape = df_date["HUMI_new"].values.reshape(-1, 1)
HUMI = scaler.fit_transform(x_reshape)  #调用MinMaxScaler的fit_transform转换方法

#将PRES_new列归一化
x_reshape = df_date["PRES_new"].values.reshape(-1, 1)
PRES = scaler.fit_transform(x_reshape)  #调用MinMaxScaler的fit_transform转换方法


#显示4条曲线
'''
ax1.plot(np.arange(1095), ave)
ax1.plot(np.arange(1095), DEWP)
ax1.plot(np.arange(1095), HUMI)
ax1.plot(np.arange(1095), PRES)
ax1.legend(["ave",'DEWP','HUMI','PRES'],loc='best')
'''


#分成3个子图显示
dis=0
dis = DEWP.mean()-ave.mean()
ax1.plot(np.arange(1095), ave+dis)
ax1.plot(np.arange(1095), DEWP)
#ax2.plot(np.arange(1095), df_date["DEWP_new"])
ax1.set_title("DEWP")
ax1.legend(["ave",'DEWP'],loc='best')

dis = HUMI.mean()-ave.mean()
ax2.plot(np.arange(1095), ave+dis)
ax2.plot(np.arange(1095), HUMI)
ax2.set_title("HUMI")
ax2.legend(["ave",'HUMI'],loc='best')

dis = PRES.mean()-ave.mean()
ax3.plot(np.arange(1095), ave+dis)
ax3.plot(np.arange(1095), PRES)
ax3.set_title("PRES")
ax3.legend(["ave",'PRES'],loc='best')

plt.show()