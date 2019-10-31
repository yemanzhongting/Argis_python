# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/10/10 11:29'
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

def haversine(latlon1, latlon2):
    """
    计算两经纬度之间的距离
    """
    if (latlon1 - latlon2).all():
        lat1, lon1 = latlon1
        lat2, lon2 = latlon2
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6370996.81  # 地球半径
        distance = c * r
    else:
        distance = 0
    return distance

#计算点是否在缓冲区域内,point为np后的
def cal_in_out(point1,area_list,length):
    r_index=-1
    for i in area_list:
        tmp=np.array(i)
        result=haversine(point1,tmp)
        if result<length:
            r_index=area_list.index(i)
            break
    return r_index

r=open(r'裁剪.csv','r+',encoding='utf-8')
tmp=pd.read_csv(r,header=None)
r.close()
print(tmp)
tmp=tmp.iloc[1:,:]
print(tmp.shape)

area_list=[]
for i in range(tmp.shape[0]):
    # 30.58,144.3 a = np.array([2,3,4])
    tmp_i_=np.array([ float(tmp.iloc[i,6]),float(tmp.iloc[i,5]) ])#([ float(tmp.iloc[i,6]),float(tmp.iloc[i,5]) ])

    area_list_ = tmp_i_.tolist()
    area_list.append(area_list_)#返回他的index

print(area_list)

f=open('order_20161101_w.csv', 'r+', encoding='utf-8')
data=pd.read_csv(f)
f.close()
#data=data.iloc[1:,:]
#data = np.array(data)
print(type(data))
print(data.shape)

#tmp=tmp.iloc[:,1:]

# with open('order_20161101_w.csv', 'r+', encoding='utf-8') as f:
#     tmp = f.readlines()
# for i in tmp:
#     tmp_list = i.split(',')
#     tmp_oX = float(tmp_list[3])
#     tmp_oY = float(tmp_list[4])
#     tmp_dX = float(tmp_list[5])
#     tmp_dY = float(tmp_list[6])
#     data.append([tmp_oY,tmp_oX])

#此时进行筛选！！！
#30.695°N-30.660°N，104.040°E-104.110°E

length=300

with open(r'chengdupoint.csv','w+',encoding='utf-8') as f:
# f.write('o,d,weight,label')
# f.write('\n')
#104.1228,30.71106,104.18364,30.69343
    for row in range(data.shape[0]):
        data_dx=float(data.iloc[row,6])
        data_dy=float(data.iloc[row,5])
        data_ox=float(data.iloc[row, 4])
        data_oy=float(data.iloc[row, 3])

        point_o = np.array([data_ox, data_oy])
        point_d = np.array([data_dx, data_dy])

        indexo=cal_in_out(point_o,area_list,length)
        indexd=cal_in_out(point_d, area_list, length)
        #1478002563,1478003504
        f.write(str(indexo)+','+str(indexd)+','+str(data.iloc[row,1])+','+str(data.iloc[row,2])+','+str(data_ox)+
                ','+str(data_oy)+','+str(data_dx)+','+str(data_dy))
        f.write('\n')

