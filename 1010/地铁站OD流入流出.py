# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/10/16 22:09'
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

r=open(r'subwayo.csv','r+',encoding='utf-8')
tmp=pd.read_csv(r,header=None)
r.close()
print(tmp)
print(tmp.shape)

r=open(r'subwayd.csv','r+',encoding='utf-8')
tmp2=pd.read_csv(r,header=None)
r.close()
print(tmp2)
print(tmp2.shape)

with open('resultod.csv','w+',encoding='utf-8') as f:
    for i in range(tmp.shape[0]):
        o_ = tmp.iloc[i, 0]
        for j in range(tmp2.shape[0]):
            d_ = tmp2.iloc[j, 0]
            if o_==d_:
                if tmp.iloc[i, 1]>tmp2.iloc[j, 1]:
                    f.write(str(o_)+','+'流出型'+','+str(tmp.iloc[i, 1])+','+str(tmp2.iloc[j, 1]))
                    f.write('\n')
                else:
                    f.write(str(o_) + ',' + '流入型' + ',' + str(tmp.iloc[i, 1]) + ',' + str(tmp2.iloc[j, 1]))
                    f.write('\n')

#流入型 金沙博物馆
#流出型 公交站
