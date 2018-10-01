# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 15:27:40 2018

@author: Akshay Jagadale
"""

from collections import Counter

l = [1,2,1,1,2,3,3,4,4,4,4,4]
c = Counter(l)
#print(c)

print(*c.elements())
print(c.most_common())
x = sorted(c, key = c.get)
print(x)
x = sorted(c.items(), key = lambda x: x[1])
print(x)


y = [0]
m = y * 10
print(m)

s = 'a'
x = s * 10
print(x)