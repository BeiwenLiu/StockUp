# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 00:34:28 2016

@author: Beiwen Liu
"""

import pandas as pd
import quandl as quandl
import matplotlib.pyplot as plt
import numpy as np

def service3(stockName): 
    df = quandl.get("YAHOO/{}".format(stockName), authtoken="p69UHReX9R_5Gr1hKavd")
    df.drop(df.columns[[0,1,2,3,4]], axis=1, inplace=True)
    
    df['Daily Return'] = (df / df.shift(1)) - 1
    
    drvalues = np.array(df['Daily Return'])
    
    drvalues = drvalues[1:]
    
    plt.hist(drvalues, bins=50)
    plt.show()
    
    
service3("CHK")