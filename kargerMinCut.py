#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 18:23:54 2016

@author: karl
"""

import pandas as pd
import numpy as np
import random
import copy

##Read txt file and put in in a dict form vertex: edge
with open('kargerMinCut.txt') as f:
    lines = f.readlines()
    
dict = {}
for (i,line) in enumerate(lines):
    a = line.split("\t")[1:]
    a.pop()
    dict[i+1] = [int(edge) for edge in a]

#contract function take a dict and two node as an input and do inplace transformation
def contract(dict, u, v):
    dict[u][:] = (value for value in dict[u] if value != v)
    dict[v][:] = (value for value in dict[v] if value != u)
    dict[u].extend(dict[v])
    del dict[v]
    for vertex in dict:
        for index, neighbor in enumerate(dict[vertex]):
            if neighbor == v:
                dict[vertex][index] = u

#%%
countMin = 3000
for i in range(1000):
    if (i % 30 == 0):
        print(str(i))
    dictCopy = copy.deepcopy(dict)
    while (len(dictCopy) > 2):
        u = random.choice(dictCopy.keys())
        v = dictCopy[u][np.random.randint(0,len(dictCopy[u])-1)]
        contract(dictCopy, u, v)
    count = len(dictCopy.values()[0])
    if count < countMin:
        print("coupeMin is " + str(count))
        countMin = count

