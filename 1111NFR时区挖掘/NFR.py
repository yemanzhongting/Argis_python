# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/11/11 14:57'
import numpy as np
import pandas as pd
from math import radians, sin, cos, asin, sqrt
import time

def haversine(latlon1, latlon2):
    """
    计算两经纬度之间的距离
    """
    # print(type(latlon1))

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


# 计算点是否在缓冲区域内,point为np后的
def cal_in_out(point1, area_list, length):
    r_index = -1
    for i in area_list:
        tmp = np.array(i)
        result = haversine(point1, tmp)
        if result < length:
            r_index = area_list.index(i)
            break
    return r_index


Y1 = 30.529114
Y2 = 30.809326
X1 = 103.894287
X2 = 104.234131
N = 20
x_gap = (X2 - X1) / N
y_gap = (Y2 - Y1) / N

# 经度间隔 0.4767285017325457km
# 纬度间隔  0.6220706399999973km

index_all = N * N


# def get_mn(X,Y):
#     #利用地板除，刚好返回他们的索引，这样就可以,索引以0开始
#     m=(X-X1)//x_gap
#     n=(Y-Y1)//y_gap
#     #print(m,n)
#     index=(n)*50+m+1
#     return index

def grid_id(point):
    # 利用地板除，刚好返回他们的索引，这样就可以,索引以0开始
    # print(point[1]) lng
    m = (point[1] - X1) // x_gap
    n = (point[0] - Y1) // y_gap
    # print(m,n)
    index = (n) * 20 + m + 1
    return index

def timestamp(stamp):
    time_local = time.localtime(stamp)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%H", time_local)
    #“%Y-%m-%d %H:%M:%S” 小时从0到23
    return dt

def NFR(o_,d_):
    if (d_ + o_)>10:
        NFR_=(d_ - o_) / (d_ + o_)
    else:
        NFR_=None
    return NFR_

if __name__ == '__main__':
    with open(r'C:\Users\hp\Desktop\成都\Argis_python\order_20161101.csv', 'r+', encoding='utf-8') as f:
        df=pd.read_csv(f,header=None)
    #headers=['ID','ST','CT','LNG1','LAT1','LNG2','LAT2']
    #８：００－９：００、１２：００－１３：００、１８：００－１９：００、２３：００－２４：００
    #8-10,12-14,18-20,21-23
    time_Section=[12,13]
    N=20
    df_grid = pd.DataFrame(np.zeros((N*N,2)))
    print(df_grid)
    print(df_grid.shape)
    print(df_grid.head())
    count=0
    for index, row in df.iterrows():
        tmp=int(timestamp(row[1]))
        if tmp in time_Section:
            o_point=np.array([row[4],row[3]])
            o_grid=int(grid_id(o_point))
            try:
                df_grid.iloc[o_grid,0] =df_grid.iloc[o_grid,0]+ 1
            except:
                print(o_grid)
            d_point=np.array([row[6],row[5]])
            d_grid=int(grid_id(d_point))
            try:
                df_grid.iloc[d_grid,1] =df_grid.iloc[d_grid,1]+ 1
            except:
                print(d_grid)
            count+=1
    print(count)

    #df_grid
    # for index, row in df_grid.iterrows():
    #     tmp = int(timestamp(row[1]))
    df_grid["NFR1213"] = df_grid[[0, 1]].apply(lambda x:NFR(x[0],x[1]), axis=1)

    df_grid.rename(columns={0: 'O_', 1: 'D_'}, inplace=True)

    df_grid.to_csv('NFR1213.csv', encoding='utf-8')  # columns=['ID','O_','D_'])


    # ############切记经纬度转换，出现了计算过程就需要30前面120后面
    # # 30.65964089,104.0743877 #读入聚类点
    # # for i in tmp_point:
    # #     ttmp=i.split(',')
    # #     area_list.append([float(ttmp[0]),float(ttmp[1])])
    # # print(area_list)
    #
    # # 新建od矩阵，输入点数
    #
    # df = pd.DataFrame(np.zeros((index_all, index_all)))
    # print(index_all)
    # # N = len(area_list)
    # # df = pd.DataFrame(np.zeros((N, N)))
    # # length = 500
    # #
    # # print(N)
    #
    # for i in tmp:
    #     # dfjnCh,1478003896,1478005484,104.06576,30.6686,104.062,30.72307
    #     try:
    #         tmp_list = i.split(',')
    #         tmp_oX = float(tmp_list[3])
    #         tmp_oY = float(tmp_list[4])
    #         tmp_dX = float(tmp_list[5])
    #         tmp_dY = float(tmp_list[6])
    #
    #         ## arr2=np.array([30.58,144.3])
    #         point_o = np.array([tmp_oY, tmp_oX])
    #         point_d = np.array([tmp_dY, tmp_dX])
    #
    #         o_ = return_cell_grid_id(point_o)
    #         d_ = return_cell_grid_id(point_d)
    #
    #         print(o_, d_)
    #
    #         if o_ > 0 and o_ <= 400:
    #             if d_ > 0 and d_ <= 400:
    #                 df.iloc[int(o_ - 1), int(d_ - 1)] = df.iloc[int(o_ - 1), int(d_ - 1)] + 1
    #     except:
    #         pass
    #         # print('处理'+str(o_)+str(d_))
    #
    #     # cal_in_out(point1,area_list,length):
    #     # tmp_a=cal_in_out(point_o,area_list,length)
    #     # tmp_b=cal_in_out(point_d,area_list,length)
    #
    #     # if tmp_a!=-1 and tmp_b!=-1:
    #     #     df.iloc[tmp_a,tmp_b]=df.iloc[tmp_a,tmp_b]+1
    #     #     print(tmp_a,tmp_b,'这里加1')
    #
    # # df.to_csv('od矩阵400.csv')
    # #
    # # # r2 = open(r'800200最终.csv', 'r+', encoding='utf-8')
    # # # tmp2 = pd.read_csv(r2, header=None)
    # #
    # # r=open(r'od矩阵400.csv','r+',encoding='utf-8')
    # # tmp=pd.read_csv(r)
    # # r.close()
    #
    # tmp=df
    #
    # print(tmp.shape)
    #
    # #tmp=tmp.iloc[:,1:]
    # print(tmp.shape)
    #
    # sumdd=0
    #
    # with open(config.get('environment', 'outfilename'),'w+',encoding='utf-8') as f:
    #     f.write('o,d,weight,label')
    #     f.write('\n')
    #     for row in range(tmp.shape[0]):
    #         tmp_x=tmp.iloc[row,0]
    #         tmp_y=tmp.iloc[row,1]
    #         for col in range(tmp.shape[1]):
    #             #print(getattr(row, 'c1'), getattr(row, 'c2'))  # 输出每一行
    #             if tmp.iloc[row,col]!=0:
    #                 f.write(str(row))
    #                 f.write(',')
    #                 f.write(str(col))
    #                 f.write(',')
    #                 sumdd=sumdd+tmp.iloc[row,col]
    #                 f.write(str(tmp.iloc[row,col]))
    #                 #f.write(',')
    #                 #detail, id, name =geocode(str(tmp_x)+','+str(tmp_y))
    #                 #print(detail)
    #                 #f.write(detail)
    #                 f.write('\n')
    #                 #print(getattr(row,col))
    # print(tmp.iloc[0,0])
    # print(sumdd)