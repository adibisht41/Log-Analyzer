# -*- coding: utf-8 -*-
"""
Created on Thu May 17 21:49:50 2018

@author: Aditya
"""

filer = open('log.txt','r')
text = filer.read()
file = open('logbig1GB.txt','w')
for i in range(1000000):
    file.write(text)
    file.write('\n')
file.close()
filer.close()