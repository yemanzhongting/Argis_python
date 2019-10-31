# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/10/31 13:45'
import sys,pprint
from gexf import Gexf


# test helloworld.gexf
gexf = Gexf("Gephi.org","A Web network")
graph=gexf.addGraph("directed","static","A Web network")

atr1 = graph.addNodeAttribute('url',type='string')
atr2 = graph.addNodeAttribute('indegree',type='float')
atr3 = graph.addNodeAttribute('frog',type='boolean',defaultValue='true')

tmp = graph.addNode("0","Gephi")
tmp.addAttribute(atr1,"http://gephi.org")
tmp.addAttribute(atr2,'1')

tmp = graph.addNode("1","Webatlas")
tmp.addAttribute(atr1,"http://webatlas.fr")
tmp.addAttribute(atr2,'2')

tmp = graph.addNode("2","RTGI")
tmp.addAttribute(atr1,"http://rtgi.fr")
tmp.addAttribute(atr2,'1')

tmp = graph.addNode("3","BarabasiLab")
tmp.addAttribute(atr1,"http://barabasilab.com")
tmp.addAttribute(atr2,'1')
tmp.addAttribute(atr3,'false')

graph.addEdge("0","0","1",weight='1')
graph.addEdge("1","0","2",weight='1')
graph.addEdge("2","1","0",weight='1')
graph.addEdge("3","2","1",weight='1')
graph.addEdge("4","0","3",weight='1')


output_file=open(".\data.gexf","w")
gexf.write(output_file)