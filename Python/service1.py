# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 18:57:12 2016

@author: Beiwen Liu
"""

import pandas as pd
import quandl as quandl
import matplotlib.pyplot as plt

def service1(stockName, percentchange, dayrange): 
    df = quandl.get("YAHOO/{}".format(stockName), authtoken="p69UHReX9R_5Gr1hKavd")
    df.drop(df.columns[[0,1,2,3,4]], axis=1, inplace=True)
    
    df['Daily Return'] = (df / df.shift(1)) - 1
    
    
    drvalues = df['Daily Return'].values
    drvalues = drvalues[1:]
    total = []
    counter = 0
    for x in range(len(drvalues)):
        if percentchange == round(drvalues[x], 2):
            if (x + dayrange < len(drvalues)):
                counter = counter + 1
                tempSum = []
                for y in range(1,dayrange + 1):
                    tempSum.append(drvalues[x + y])
                total.append(sum(tempSum))
                
    avg = sum(total)/len(total)
    print avg, counter
    
service1("TWTR", -.01, 50)