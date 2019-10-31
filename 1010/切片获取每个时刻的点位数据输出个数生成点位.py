# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/10/29 20:47'
import configparser
import os, sys
import pandas,time
import numpy as np
import pandas as pd

parent_dir = os.path.dirname(os.path.abspath(__file__))

#  实例化configParser对象
config = configparser.ConfigParser()
config.read(parent_dir + "/config.init", encoding='utf-8')  # 读取配置文件采用绝对路径

#(config.get('environment', 'filename')


df = pd.read_csv(config.get('setting', 'input_file'), encoding='utf-8')
print(df.head())
a = df['START']#['a']   # a 这一列是时间戳
b = [time.gmtime(i) for i in a]

#b = [time.gmtime(i) for i in a]  # time.gmtime() 接收时间戳（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
Y = []
M = []
D = []
H = []
MIN = []
S = []
for i in b:
    a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9 = i
    Y.append(a_1)
    M.append(a_2)
    D.append(a_3)
    H.append(a_4)
    MIN.append(a_5)
    S.append(a_6)

S_Y = pd.Series(Y, name='Year')
S_M = pd.Series(M, name='Month')
S_D = pd.Series(D, name='Day')
S_H = pd.Series(H, name='Hour')
S_MIN = pd.Series(MIN, name='Minute')
S_S = pd.Series(S, name='s')

time_df = pd.concat([df, S_Y, S_M, S_D, S_H, S_MIN, S_S], axis=1)

select_point=[]

time_df = time_df[(time_df['Hour']>=int(config.get('setting', 'timeseriess')) )&(time_df['Hour']<=int(config.get('setting', 'timeseriesc')))]

# time_df.drop(0, axis=1)
# # #.iloc[:, 0]
#time_df[:0].reset_index(index=list(range(1, time_df.shape[0])))

# （1）首先把df1中的要加入df2的一列的值读取出来，假如是'date'这一列
#     date = df1.pop('date')
# （2）将这一列插入到指定位置，假如插入到第一列
#     df2.insert(0,'date',date)

time_df.insert(0,'NEW_ID',list(range(time_df.shape[0])))
#time_df['NEW_ID']=list(range(time_df.shape[0]))

time_df.reset_index(drop=True)

#print(time_df.colum())

time_df.to_csv(config.get('setting', 'out_file'), encoding='utf-8')#,header=0是否保留索引

print(time_df.shape)