#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:45:17 2018

@author: ColinSheehan
"""
##realized output from shape is a list itself, with an index to use as input for the next function
ls
iris = pd.read_csv('iris.csv')
Slist=iris.shape
Frow=Slist[0] - 2
Srow=Slist[0]
Fcol=Slist[1] - 2
Scol=Slist[1]
lasttwo=iris.iloc[Frow:Srow, Fcol:Scol]
lasttwo
