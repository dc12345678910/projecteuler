#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:09:25 2022

@author: dayuan
"""
import math

def isPrime(num):
    if num == 2:
        return True
    for i in range (2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
        
count = 1
bp = 3

while count <= 10001:
    if isPrime(bp):
        count = count + 1
        print (bp, count)
    bp = bp + 1
    
print (bp)