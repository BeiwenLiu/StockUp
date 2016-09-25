# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 00:12:43 2016

@author: evankaplan
"""

import pandas as pd
import quandl as quandl
import matplotlib.pyplot as plt

def service2(stockName):
    df = quandl.get("YAHOO/{}".format(stockName), authtoken="p69UHReX9R_5Gr1hKavd")
    df.drop(df.columns[[0,1,2,3,4]], axis=1, inplace=True)
    
    df['Daily Return'] = (df / df.shift(1)) - 1
    
    drvalues = df['Daily Return'].values
    drvalues = drvalues[1:]
    
    adjCloseValues = df['Adjusted Close'].values
    adjCloseValues = adjCloseValues[1:]
    
    mx = ma.masked_array(x, mask=[0, 0, 0, 1, 0])