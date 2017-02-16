# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 13:57:13 2017

@author: shangguanxf
"""
from PIL import Image
import os
#去点重复的图片，path为去重文件所在路径,路径下只能有图片格式
#path需要/左斜线，windows路径复制是右斜线
def drop_duplicated(path):
    res={}
    size=8,8
    for root,dirs,files in os.walk(path):
        for file in files:
        #去除非图片类型的文件
        #if not file.endswith('.txt'):
             im = Image.open(os.path.join(root,file))
             im.thumbnail(size, Image.ANTIALIAS)