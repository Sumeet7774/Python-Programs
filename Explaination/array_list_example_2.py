# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 12:16:32 2022

@author: DELL
"""

arr = ['Tiger','Ostrich','Tortoise','Peacock','Sparrow']

print(arr[0])   #it will display the content which is on array number 0
print(arr[2])   #it will display the content which is on array number 2
print('Length of the array is: ',len(arr))  #it will display the length of the array

str1 = arr[0] + ' ' + arr[2]    #concatenation of tiger and tortoise
print(str1) 
print(len(arr[1]))              #it will display the length of the ostrich

print(arr[0][0])    #the first 0 is for array of string and the second 0 is for the first character of tiger which is T
print(arr[2][2])    #the first 2 is for array of string and the second 2 is for the third character of tortoise which is r 
print(arr[4][6])    #the first 4 is for array of string and the second 6 is for the last character of sparrow which is w

print(arr)          #it will print all the elements of the list or array

print(arr[0:3])     #it will print in range meaning it will rprint from range 0 to 3

print(arr[2:])      #it will print in range meaning it will print from range 2 to last element

print(arr[:2])      #it will print in range meaning it will print from starting to 2nd element

print(arr[:])       #it will print in range meaning it will print all element

print(arr[0][0:3])  #it will print in range. The first 0 represent the tiger and the second 0:3 will print the characters of tiger from 0 to 3 element means it will print Tig

print(arr[1][0:4])

print(arr[4][4:])
      
      