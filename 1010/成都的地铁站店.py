# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/10/15 16:31'
import pandas
import requests,time
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from math import radians, sin, cos, asin, sqrt
import time
from numpy import linspace
from matplotlib import cm

r=open(r'chengdupoint.csv','r+',encoding='utf-8')
tmp=pd.read_csv(r,header=None)
r.close()
print(tmp)
tmp=tmp.iloc[:,:]
print(tmp.shape)

r=open(r'裁剪.csv','r+',encoding='utf-8')
tmp2=pd.read_csv(r,header=None)
r.close()
tmp2=tmp2.iloc[1:,:]
print(tmp2.shape)

subwayo={}
subwayd={}
for i in range(tmp.shape[0]):
    # 30.58,144.3 a = np.array([2,3,4])
    o_=tmp.iloc[i, 0]
    d_=tmp.iloc[i, 1]
    if o_!=-1:
        subwayo[o_] = subwayo.get(o_,0) + 1
    else:
        pass#弱不存在返回

    if d_!=-1:
        subwayd[d_] = subwayd.get(d_,0) + 1
    else:
        pass#弱不存在返回

subwayo=list(subwayo.items())#counts.items()
subwayd=list(subwayd.items())

print(subwayd)

with open('subwayo.csv', 'w') as f:
    for i in range(len((subwayo))):
        f.write(str(subwayo[i][0]))
        f.write(',')
        f.write(str(subwayo[i][1]))
        f.write('\n')

with open('subwayd.csv', 'w') as f:
    for i in range(len((subwayd))):
        #print(sortf[i])
        #print(type(sortf[i]))
        print(subwayd[i][0])
        f.write(str(subwayd[i][0]))
        f.write(',')
        f.write(str(subwayd[i][1]))
        f.write('\n')