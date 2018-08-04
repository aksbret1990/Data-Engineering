# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 10:28:52 2018

@author: Akshay Jagadale
"""

x = [1,2,3,4]
y = [7,6,2,1]
z = ['a','b','c','d']

print()
for a,b in zip(x,y):
    print(a,b)

print()    
for a,b,c in zip(x,y,z):
    print(a,b,c)
        
print()   
print(zip(x,y,z))

#this will print the tuples
print()
for i in zip(x,y,z):
    print(i)
    
print()
print(list(zip(x,y,z)))

print()
print(dict(zip(x,y)))

print()
[print (a,b,c) for a,b,c in zip(x,y,z)]



print()
# x,y are temporary variables here
[print(x,y) for x,y in zip(x,y)]


print()
# this will still print [1,2,3,4] becuase x, y were temporary variables in list comprehension
print(x)


#be careful about below scenario and try using different variables
print()
for x,y in zip(x,y):
    print(x,y)
    
#x get overwritten and hence won't print [1,2,3,4]    
print()
print(x)