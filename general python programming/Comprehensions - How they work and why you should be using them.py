# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:57:32 2018
@author: Akshay Jagadale
"""
nums = [1,2,3,4,5,6,7,8,9,10]
######################################################################################################################
#I want n * n for each n in nums

my_list = []
#using for loop
for i in nums:
    my_list.append(i*i)
print('using for loop',my_list)
    
#using list comprehension
my_list = [i*i for i in nums]
print('using list comprehension',my_list)

#using map
my_list = list(map(lambda x:x*x, nums) )
print('using map function',my_list)


######################################################################################################################
#i want a list of numbers that are divisible by 2
my_list = []

#using for loop
for i in nums:
    if(i % 2 ==0):
        my_list.append(i)
print('using for loop',my_list)

#using list comprehension
my_list = [n for n in nums if n%2==0]
print('using list comprehension',my_list)

#using filter
my_list = list(filter(lambda x : x%2==0, nums))
print('using filter',my_list)

######################################################################################################################
#i want a (letter,number) pair for each letter in 'abcd' and number in '0123'
my_list = []

#using for loop
for letter in 'abcd':
    for number in range(0,4):
        my_list.append((letter,number))
print(my_list)

#using list comprehension
my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)

#using map
list(map(lambda letter,number : (letter,number), 'abcd',range(0,4)))
print(my_list)

######################################################################################################################
#Dictionary comprehension

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman','Superman','Spiderman','Wolverine','Deadpool']
print(list(zip(names,heros)))

#I want a dict{'name':'hero'} for each name,hero in zip(names,hero)
my_dict = {}

for name,hero in zip(names,heros):
    my_dict[name] = hero
print(my_dict)


my_dict = {name:hero for name,hero in zip(names,heros) if name!='Peter'}
print(my_dict)

######################################################################################################################
#set comprehensions

nums = [1,1,1,2,2,2,3,3,3,3,4,3,1,2,5,5,5,1,1,2,4,4,4,5,6,6,6,6,6,7,7,7,9,8,8,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

my_set = {n for n in nums}
print(my_set)

######################################################################################################################
#generator expressions
#I want to yield n*n for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n
        
my_gen = gen_func(nums)


for i in my_gen:
    print(i)
    
    
my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)
    


######################################################################################################################













