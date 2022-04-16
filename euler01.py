#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:54:08 2022

@author: dayuan
"""

sum = 0
for x in range (1000):
    if x % 3 == 0 or x % 5 == 0:
        sum = sum + x
print (sum)