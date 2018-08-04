# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 14:27:30 2018

@author: Akshay Jagadale
"""

#lambda function examples
myfunc =  lambda x: x * x 
print (myfunc(2))

myfunc1 = lambda x,y: x+y
print(myfunc1(1,2))

myfunc2 = lambda x,y:x if x > y else y
print(myfunc2(2,1))
print(myfunc2(1,3))


#map function
n = [1,2,3,4]
print(list(map(lambda x:x**2,n)))
 
#using list comprehension
print([x**2 for x in n])


#filter function
print(list(filter(lambda x:x>2,n)))

#using list comprehension
print([x for x in n if x > 2])

from functools import reduce

#reduce function
print(reduce(lambda x,y : x*y,n))

