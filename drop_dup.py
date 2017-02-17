# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 13:57:13 2017

@author: shangguanxf
"""
import cv2
import os
import numpy as np
#去点重复的图片，path为去重文件所在路径,路径下只能有图片格式
#path需要/左斜线，windows路径复制是右斜线
def drop_duplicated(path):
    res={}
    for root,dirs,files in os.walk(path):
        for file in files:
        #去除非图片类型的文件
        #if not file.endswith('.txt'):
            p=os.path.join(root,file)
            im = cv2.imread(p,0)
            im=cv2.resize(im,(8,8))
            
             