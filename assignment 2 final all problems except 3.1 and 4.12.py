# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:09:41 2020

@author: rosie
"""

2.8

print("number\t square\t cube\t")
for number in range(0,6):
    print("{:<10d}".format(number),"{:<10d}".format(number**2),"{:<10d}".format(number**3))



2.12

print('10 years:', 1000 * (1 + .07) **10)
print('20 years:', 1000 * (1 + .07) **20)
print('30 years:', 1000 * (1 + .07) **30)


For 3.1 see file fig 3_03 practice

3.6

input('What is your problem? ')

answer = input('Have you had this problem before (yes or no)? ')

if answer == 'yes' :
    print('Well, you have it again.')
if answer == 'no' :
    print('Well, you have it now.')
    
3.10

p = 1000
r = 0.07

for year in range (1,31):
    print(f'{year} years: {p * (1+r) ** year:.1f}')
    

3.16

largest = int(input('Enter number: '))
second_largest = int(input('Enter number: '))
number = int(input('Enter number: '))
 
if number > largest:
    second_largest = largest 
    largest = number
else: 
    second_largest = number
for counter in range (2,9):
    number = int(input('Enter number: '))
    if number > largest: 
        second_largest = largest
        largest = number
    elif number > second_largest: 
        second_largest = number

"""find the two largest integers""" 

print(f'largest is {largest}')
print(f'second largest is {second_largest}')


4.9

def fahrenheit (celsius): 
    return (9/5) * celsius + 32

print("Celsius\t Fahrenheit\t")

for celsius in range(101) :
    print(f'{celsius:10}{fahrenheit(celsius):10.1f} ')
    


4.12 see file 

























