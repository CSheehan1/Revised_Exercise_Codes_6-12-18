#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:10:34 2018

@author: ColinSheehan
"""

ls
import pandas as pd
import numpy
import matplotlib.pyplot as plt
from plotnine import *
GAME=pd.read_csv('UWvMSU_1-22-13.csv', delim_whitespace=True)
UW=GAME[GAME.team=="UW"]
MSU=GAME[GAME.team=="MSU"]
UWlength=len(UW)
UWlength
MSUlength=len(MSU)
UWlist=[]
UWnewsum = 0
for num in range(0,UWlength):
    UWnewsum = UWnewsum + UW.iloc[num, 2]
    UWlist.append(UWnewsum)
UWdata=pd.DataFrame(data=UWlist, columns=['score'])
UWtime=numpy.array(UW.iloc[:,0])
UWdata.insert(1, 'times', UWtime)
MSUlist=[]
MSUnewsum = 0
for num in range(0,MSUlength):
    MSUnewsum = MSUnewsum + MSU.iloc[num, 2]
    MSUlist.append(MSUnewsum)
MSUdata=pd.DataFrame(data=MSUlist, columns=['score'])
MSUtime=numpy.array(MSU.iloc[:,0])
MSUdata.insert(1, 'times', MSUtime)
UWdata
MSUdata
UWPLOT=ggplot(UWdata, aes(x="times", y="score"))
MSUPLOT=ggplot(MSUdata, aes(x="times", y="score"))
plot1 = ggplot(UWdata, aes(x="times", y="score"))+geom_step(data=UWdata, color="green")+geom_step(data=MSUdata, color="red")+theme_classic()
ggsave(plot = plot1, file="UWgreen_MSUred.pdf", path = "/Users/ColinSheehan/Desktop/Colin_Coding/ICB_EX8")