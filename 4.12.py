# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 17:25:24 2020

@author: rosie
"""

import random

RACE_END = 70

def move_tortoise (tortoise) :
    """Move tortoise's position."""
    move = random.randrange(1,11)

    if 1 <= move <= 5:
        tortoise += 3
    elif move in (6,7):
        tortoise -= 6
    else: 
        tortoise += 1
    
    if tortoise < 1:
        tortoise = 1
    elif tortoise > RACE_END:
        tortoise = RACE_END
    
    return tortoise

def move_hare (hare):
    """Move hare's position."""
    move = random.randrange(1,11)
    
    if move in (3,4) :
        hare += 9
    elif move == 5:
        hare -= 12
    elif 6 <= move <= 8:
        hare += 1
    elif move > 8:
        hare -= 2
        
    if hare < 1:
        hare = 1
    elif hare > RACE_END:
        hare = RACE_END
    
    return hare

def print_positions (tortoise,hare) :
    """display positions of tortoise and hare.
    
    Goes through all 70 squares, printing H if hare
    on position and T for tortoise"""
    
    for count in range(1, RACE_END + 1) :
        if count == tortoise and count == hare:
            print('OUCH!!!', end='')
        elif count == hare:
            print('H', end='')
        elif count == tortoise: 
            print('T', end= '')
        else:
            print('', end = '')
        
    print()
    
tortoise = 1
hare = 1
timer = 0 

print('ON YOU MARK, GET SET')
print('BANG!!!!!')
print("AND THEY'RE OFF!!!!!")

while tortoise < RACE_END and hare < RACE_END :
    hare = move_hare(hare)
    tortoise = move_tortoise(tortoise)
    print_positions(tortoise, hare)
    timer += 1

if tortoise >= hare:
    print('\nTORTOISE WINS!!! YAY!!!')
else:
    print('\nHare wins. Yuch!')
print(f'TIME ELAPSED = {timer} seconds')
