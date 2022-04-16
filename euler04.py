#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 18:33:12 2022

@author: dayuan
"""

n = 0
a = 100
b = 100
for a in range(100, 999):
    for b in range(a, 999):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                 n = a * b
print (n)