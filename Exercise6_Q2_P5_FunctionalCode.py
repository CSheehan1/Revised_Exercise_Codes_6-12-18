#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 13:06:01 2018

@author: ColinSheehan
"""
##Used .count previously but that did not work the 2nd time around, fixed by using output from .shape###
virginica = iris[iris.Species=="virginica"]
virginicaPL = virginica.iloc[:,2]
max(virginicaPL)
min(virginicaPL)
blerp = virginicaPL.shape
flerg = sum(virginicaPL)
results=(flerg)//(blerp[0])
results #final line prints the mean value
