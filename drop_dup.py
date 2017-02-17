# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 13:57:13 2017

@author: shangguanxf
"""
import cv2
import os
import numpy as np
import re
import csv
#去点重复的图片，path为去重文件所在路径,路径下只能有图片格式
#path需要/左斜线，windows路径复制是右斜线
def drop_duplicated(path):
    res=set()
    for root,dirs,files in os.walk(path):
        for file in files:
        #去除非图片类型的文件
        #if not file.endswith('.txt'):
            p=os.path.join(root,file)
            im = cv2.imread(p,0)
            im=cv2.resize(im,(8,8))         
            #将im转换成array
            c=np.array(im)
            #将大于平均值的为1，小于为0
            c[c<np.mean(c)]=0
            c[c>0]=1
            '''
            #计算汉明距离
            a=np.array([(1,1,0),(1,0,0)])
            b=np.array([(1,0,1),(1,1,0)])
            print(np.sum((a-b)!=0))
            a1=''.join(re.findall('[0-9]*',np.array2string(a, precision=2, separator='',suppress_small=True)))
            b1=''.join(re.findall('[0-9]*',np.array2string(b, precision=2, separator='',suppress_small=True)))
            bin(int(a1,2)^int(b1,2)).count('1')
            '''
            #去重
            c1=''.join(re.findall('(\w*[0-9]+)\w*',str(c.tolist())))
            if c1 in res:
                os.remove(p)
            else:
                res.add(c1)

    with open('e:/pic_list.txt', 'w') as f:
      for i in res:
          f.writelines(i+'\n')
      