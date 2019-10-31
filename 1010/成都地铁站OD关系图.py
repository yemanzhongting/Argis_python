# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/10/15 20:04'
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

# r=open(r'裁剪.csv','r+',encoding='utf-8')
# tmp2=pd.read_csv(r,header=None)
# r.close()
# tmp2=tmp2.iloc[1:,:]
# print(tmp2.shape)
#
# subwayo={}
# subwayd={}

# with open('subway28.csv', 'w') as f:
#     for i in range(tmp.shape[0]):
#         # 30.58,144.3 a = np.array([2,3,4])
#         o_=tmp.iloc[i, 0]
#         d_=tmp.iloc[i, 1]
#         if o_==28:
#             f.write(str(tmp.iloc[i, 4])+','+str(tmp.iloc[i, 5])+','+'0')
#             f.write('\n')
#         else:
#             pass#弱不存在返回
#
#         if d_==28:
#             f.write(str(tmp.iloc[i, 6])+','+str(tmp.iloc[i, 7])+','+'1')
#             f.write('\n')
#         else:
#             pass#弱不存在返回

with open('subway骡马市OD.csv', 'w') as f:
    for i in range(tmp.shape[0]):
        # 30.58,144.3 a = np.array([2,3,4])
        o_=tmp.iloc[i, 0]
        d_=tmp.iloc[i, 1]
        if d_==28:
            f.write(str(tmp.iloc[i, 6])+','+str(tmp.iloc[i, 7])+','+'0')
            #0为这里出发的点
            f.write('\n')
        else:
            pass#弱不存在返回

        if o_==28:
            f.write(str(tmp.iloc[i, 4])+','+str(tmp.iloc[i, 5])+','+'1')
            #为1则为到这里的点
            f.write('\n')
        else:
            pass#弱不存在返回