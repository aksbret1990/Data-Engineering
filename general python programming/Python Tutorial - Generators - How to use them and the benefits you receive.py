# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 14:30:10 2018

@author: Akshay Jagadale
"""

def square_numbers(nums):
    for i in nums:
        yield(i*i)
        
my_nums = square_numbers([1,2,3,4,5])

#print(next(my_nums))  
#print(next(my_nums)) 
#print(next(my_nums)) 
#print(next(my_nums)) 
#print(next(my_nums)) 
#print(next(my_nums))     
    

for i in my_nums:
    print(i)
    
    
my_nums = (x*x for x in [1,2,3,4,5])
print(my_nums)
    
    
    
    
    
