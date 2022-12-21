# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 10:29:19 2022

@author: PRANEETH
        print(x *y)
"""

t = int(input())

for i in range(t):
    x,y,z = map(int,input().split(' '))
    if y%z ==0:
        print(x*int(y/z))
    else:
        print(x* int(y/z + 1))
    