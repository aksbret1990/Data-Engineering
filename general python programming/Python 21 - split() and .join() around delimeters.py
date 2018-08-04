# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 16:52:43 2018

@author: Akshay Jagadale
"""


stringOfStuff = 'egg,milk,cheese,coffee'
listOfStuff = stringOfStuff.split(',')    
print(listOfStuff)

newstring = ';'.join(listOfStuff)
print(newstring)

anotherstring = 'my cat dog cat has cat fleas'
anotherlist = anotherstring.split()
print(anotherlist)


anotherlist = anotherstring.split(" cat ")
print(anotherlist)