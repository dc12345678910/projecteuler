#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:10:39 2022

@author: dayuan
"""

num1 = 1
sum1 = 0

while num1 <= 100:
    sum1 = sum1 + num1*num1
    num1 = num1 + 1
    
num2 = 1
sum2 = 0
sumsq = 0

while num2 <= 100:
    sum2 = sum2 + num2
    num2 = num2 + 1
    
sumsq = sum2*sum2

print (sumsq - sum1)