# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 21:03:07 2022

@author: PRANEETH
"""

f = open('firsttext.text','r')
flag = False
while(s!=''):
    s=f.readline()
    
    if s =='plz':
        print('the plz is found in the file')
        flag = True
        break
if flag == False:
    print('the word plz is not found in the file')