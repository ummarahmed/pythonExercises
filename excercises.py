#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 17:01:27 2021

@author: ummarahmed
"""

print("My Excercises Files")# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
import time


def extract_func_names(func):
    def internal_func(*args, **kwargs):
        print(f"Method {func.__name__} is called.")
        returned_value = func(*args, **kwargs)
        print("Methode execution is completed")
        return returned_value
    return internal_func
        
    
@extract_func_names
def sum_numbers(a, b):
    print("this is inside sum_numbers function")
    return a+b

@extract_func_names
def product_numbers(a, b):
    print("this is inside product_number function")
    return a*b

a,b = 3,4
print(f"Sum of numbers: {sum_numbers(a, b)}")
print(f"Product of numbers: {product_numbers(a, b)}")


/////////////////////////////////
working with numpy


import numpy as np

mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Shape of Matrix is: ",mat.shape)

new_mat = mat.reshape(1,9)
print("Shape of new_mat is: ", new_mat.shape)

trans_new_mat = new_mat.T
print("Transpose of new_mat is: ",trans_new_mat.shape)


diag = np.diag(1,2,3,4)
identity = np.identity(10)


seq = np.arange(start=0, stop=100, step=5)


"EXERCISE # 1"
name = input("What is yout name?")
age = input("What is yout age?")
yearToBe100 = 2021 + (100 - int(age))
print(f"{name} you will be of 100 in {yearToBe100}.\n"*50)



"EXERCISE # 2"
number = int(input("Enter number to check."))
solve = number%2
if solve == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")
    
if ((number%4) == 0 ):
    print(f"{number} is multiple of 4.")
    
        
"EXERCISE # 3"
 numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 for i in numbers:
     if i < 5:
         print(i)

"Exercise # 4"

number = int(input("Enter number..."))
for i in range(1, 100):
    if number%i == 0:
        print(i)

"EXERCISE # 5"


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for i in a:
    for j in b:
        if i == j:
            print(i)

import random
arr1 = []
arr2 = []
for i in range(15):
    arr1.append(random.randint(1,30))
    arr2.append(random.randint(1,30))
    
print(arr1)
print(arr2)

for i in arr1:
    for j in arr2:
        if i == j:
            print(i)

word = input("Enter Word...")
print(len(word))

rvs = word[::-1]
print(rvs)
if word == rvs:
     print("True")
else:
    print("False")




"EXERCISE # 7"
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

arrEve = []

[arrEve.append(i) for i in a if i%2 == 0 and 10<i<50] 
print(arrEve)
"""























