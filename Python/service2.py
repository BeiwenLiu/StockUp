# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 00:12:43 2016

@author: evankaplan
"""

import pandas as pd
import quandl as quandl
import matplotlib.pyplot as plt

def service2(stockName, percentchange):
    df = quandl.get("YAHOO/{}".format(stockName), authtoken="p69UHReX9R_5Gr1hKavd")
    df.drop(df.columns[[0,1,2,3,4]], axis=1, inplace=True)
    
    df['Daily Return'] = (df / df.shift(1)) - 1
    
    drvalues = df['Daily Return'].values
    drvalues = drvalues[1:]
    
    adjCloseValues = df['Adjusted Close'].values
    adjCloseValues = adjCloseValues[1:]
    
    neverEnd = 0
    instanceOfEqualPerc = 0
    numberOfDays = 0
    array = []
    for x in range(len(drvalues)):
        if percentchange <= drvalues[x] + .0025 and percentchange >= drvalues[x] - .0025:
            instanceOfEqualPerc = instanceOfEqualPerc + 1
            currentCloseValue = adjCloseValues[x - 1]
            dayNumber = x
            runner = True
            while(dayNumber < len(adjCloseValues) and adjCloseValues[dayNumber] < currentCloseValue and runner):
                dayNumber = dayNumber + 1
                if dayNumber == len(adjCloseValues) - 1:
                    neverEnd = neverEnd + 1
                    runner = False
                    dayNumber = x
            array.append(dayNumber - x)
            print "number of days:  " + str(dayNumber - x)
            numberOfDays = dayNumber - x + numberOfDays
            
    avgDays = numberOfDays/(instanceOfEqualPerc - neverEnd)
    
    plt.hist(array, 500)
    
    print avgDays    
    print numberOfDays
    print instanceOfEqualPerc
    print neverEnd
    
service2("NVAX", -.01)
            