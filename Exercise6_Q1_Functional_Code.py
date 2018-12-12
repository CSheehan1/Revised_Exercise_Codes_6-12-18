#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:52:47 2018

@author: ColinSheehan
"""
##used the findRuns file as an example of its use, need to convert it to pandas dataframe##
data=pd.read_csv("findRuns.txt",header=None,sep="\t")
def headscript(X,dataframe): #Usage: X is an argument for the desired number of lines, dataframe is the datafram
    newframe=[]
    for Q in range(0,X+1):
        line=data.iloc[Q,:]
        nums=line.values
        newframe.append(nums)
    newdataframe=pd.DataFrame(data=newframe)
    print(newdataframe)
data
headscript(5,data)

    