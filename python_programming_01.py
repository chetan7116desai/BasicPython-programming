# -*- coding: utf-8 -*-
"""python programming 01

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iqUEUrnY0kYBmMED4AAjnUs_ZcDR3hOI
"""

print('hello world')

"""Code to increase the ram of google colab  (I hope it helps everyone)"""

a =[]
while(1):
  a.append('1')

"""Drawing a shape"""

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

"""Variables and data **types** bold text"""

char_name = "chetan"
date = "10.12"

print("Its been a absolute preveledge for " +char_name+  " to be a part of this course on " +date+ ",")


print ("he " +char_name+ " being so anxious about learning new things finds this course an absolute gem on" +date +".")

"""Working with string"""

print("KATECH \n IDEAS")

print("KATECH/IDEAS")

hey = "chetan"
print(hey.lower().islower())

len(hey)

print(hey[:-1])

print(hey.index('an'))

print(hey.replace("chetan","chetan"))

"""working with numbers"""

print(2**3)

from math import *
a =2
b =2.4
print(pow(a,4))
print(round(3.4))
print(min(2,3))
print(sqrt(b))

"""taking user input"""

name = input("enter your name: ")
print("hello " +name+ " There")
age = input("enter your age: ")
print("your age is " +age+ "thats good")

"""building a calculator"""

num1 = input("enter a first number")
num2 = input("enter a second number")
result = float(num1)+float(num2)

print(result)

"""MAD LIBS"""

earth = input("where do you live")
you = input("who are you")

print("Cover the " +earth+ ",")
print("before")
print("the earth covers " +you+".")

"""Lists function"""

abc= ['chetan','2','3']
print(abc[1])

defe = ['3','5','6']
print(abc+defe)

defe[0] = '7'

abc.extend(defe)

abc

abc.append('10')

abc.append(defe)

abc

abc.insert(0,'1')

abc

abc.remove(1)

abc.remove('chetan')

abc

abc.pop()

abc

abc.clear

abc.clear()

abc

abc =['1', '2', '3', '7', '5', '6', '7', '5', '6', '10']

print(abc.insert(0,'chetan'))

abc

abc.index("chetan")

abc.index("deepak")

abc.sort()

number = ['10','2' ,'34' , '11']

print(number.sort())

print(number)

print(number.sort())

number

number =[1,3,50,4,10]

print(number.sort())

number.sort()

print(number)

number2 = number.copy()

print(number2)

number.reverse()

print(number)

