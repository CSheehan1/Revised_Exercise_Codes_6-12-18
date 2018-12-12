#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:37:24 2018

@author: ColinSheehan
"""
#Problem with previous code is that raw_input() must be "read" by the computer 
#with the addition of some other characters. I would run the code and it would 
#get stuck on the while statement. using randint() fixed this issue
ls
nano Number_Game_Script.py
def numbergame():
    import random
    target=random.randint(1,100)
    print("I'm thinking of a number between 1 and 100...")
    thing=int(input("Guess my number: "))
    while thing != target:
        if thing > target:
            print("Sorry, too high!")
        elif thing < target:
            print("Sorry, too low!")
        thing=int(input("Guess again: "))
    print("Well done, persistent master of we...mere machines...")