#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 17:36:06 2018

@author: Marcelo
"""

import numpy as np

Wi = np.random.normal(0,0.01,3)

Wo = np.random.normal(0,0.01,2)

X = np.array([
        [-2,-1,0,1],
        [-1,0,1,2],
        [1,1,1,1]
        ])

Tar = np.array([-1.5,-1,1,1.5])

Zin = np.dot(np.transpose(Wi),X)

Zt = np.tanh(Zin)

XX = np.array([1,1,1,1])

Z = np.vstack((Zt,XX))

Wt = np.dot(np.transpose(Wo),Z)

#print Wi
#print Wo
#print Zin
#print Zt
#print Z

print Wt