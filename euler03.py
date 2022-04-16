#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 12:06:31 2022

@author: dayuan
"""

def isPrime(num):
    if num == 2:
        return True
    for i in range (2, num):
        if num % i == 0:
            return False
    
    return True

lpf = 0
currentF = 2

while currentF < 600851475143:
    if isPrime(currentF) and 600851475143 % currentF == 0:
        lpf = currentF
        print (lpf)
    currentF = currentF + 1
print (lpf)