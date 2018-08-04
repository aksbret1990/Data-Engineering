# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 09:00:45 2018

@author: Akshay Jagadale
"""

example = ['left','right','up','down']
#normal way
for i in range(0,len(example)):
    print(i , example[i])
print('---------------------------------------------------------------')    


#using enumerate
for i,j in enumerate(example):
    print(i,j)
print('------------------------------------------------------------------')    

#using enumerate for dictionary 
my_dict = {'a':0,'b':1,'c':2 }
for i,j in enumerate(my_dict):
    print(i,j)
print('----------------------------------------------------------------------')  


new_dict = dict(enumerate(example))

print(new_dict)