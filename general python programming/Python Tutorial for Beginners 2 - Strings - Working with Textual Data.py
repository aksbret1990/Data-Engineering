# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 18:20:04 2018

@author: Akshay Jagadale
"""
message = 'Bobby\'s World'
message = """Bobby's world 
was a good cartoon 
in 1999


"""

message = "Hello world"
print(message)
print(len(message))
print(message[0])
print(message[0:5])
print(message[:5])
print(message[8:])


print(message.lower())
print(message.upper())
print(message.count('world'))
print(message.count('l'))
print(message.find('world'))
print(message.find('university'))
print(message.find('l'))


message = message.replace('world','universe')
print(message)


greeting = "Hello"
name = 'Michael'

messaage = greeting + name
print(messaage)


messaage = greeting + ', ' + name + '. Welcome!'
print(messaage)



messaage = '{}, {}. Welcome!'.format(greeting,name)
print(messaage)


messaage = f'{greeting}, {name}. Welcome!'.format(greeting,name)
print(messaage)

messaage = f'{greeting}, {name.upper()}. Welcome!'.format(greeting,name)
print(messaage)

print(dir(name))


print(help(str))


print(help(str.lower))


