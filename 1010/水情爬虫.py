# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/11/11 11:54'
import  requests
from lxml import etree
from  lxml import etree
heaeder={"Accept":"*/*",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.8",
"Connection":"keep-alive",
"Content-Length":"263",
"Content-Type":"text/plain",
"Cookie":"zhuzhan=79852665; wdcid=0134cd31ee26342c; JSESSIONID=92174DBCD61964D5D44894827B16AA55.tomcat1; wdlast=1540946108",
"Host":"xxfb.hydroinfo.gov.cn",
"Origin":"http://xxfb.hydroinfo.gov.cn",
"Referer":"http://xxfb.hydroinfo.gov.cn/ssIndex.html",
    "User-Agent":"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"}
data={"callCount":"1",
"page=":"/ssIndex.html",
"httpSessionId":"92174DBCD61964D5D44894827B16AA55.tomcat1",
"scriptSessionId":"CB88A92E5324CD72009FD446BDFBB4DB876",
"c0-scriptName":"IndexDwr",
"c0-methodName":"getSreachData",
"c0-id":"0",
"c0-param0":"string:hd",
"c0-param1":"string:",
"c0-param2":"string:",
"batchId":"0"}
url="http://xxfb.hydroinfo.gov.cn/dwr/call/plaincall/IndexDwr.getSreachData.dwr"
response=requests.post(url,headers =heaeder,data=data)
response.raise_for_status()


data1 =response.text
print(type(data1))
data2=data1.encode('utf-8').decode('unicode_escape')
html=etree.HTML(data2)
tr=html.xpath("//tr")
print(data2)
heliudata=[]
for td in tr:
    liuyu=td.xpath("./td[1]/text()")
    xingzhenqu=td.xpath("./td[2]/text()")
    heming=td.xpath("./td[3]/text()")
    zhanming=td.xpath("./td[4]//text()")
    riqi=td.xpath("./td[5]/text()")
    shuiwei=td.xpath("./td[6]//text()")
    liuliang=td.xpath("./td[7]/text()")
    jingjieshuiwei=td.xpath("./td[8]/text()")
    print(str(liuyu)+","+str(xingzhenqu)+","+str(heming)+","+str(zhanming)+","+str(riqi)+","+str(shuiwei)+","+str(liuliang)+","+str(jingjieshuiwei))
    heliudata.append(str(liuyu)+","+str(xingzhenqu)+","+str(heming)+","+str(riqi)+","+str(shuiwei)+","+str(liuliang)+","+str(jingjieshuiwei))



print("#"*30)
print(heliudata)