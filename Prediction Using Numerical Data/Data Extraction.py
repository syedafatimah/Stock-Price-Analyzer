# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 01:30:02 2022

@author: Syeda Fatima Zahid
"""

import time
import datetime
import pandas as pd

ticker = 'MSFT'
period1 = int(time.mktime(datetime.datetime(2020, 12, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2020, 12, 31, 23, 59).timetuple()))
interval = '1d' # 1d, 1m

url = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

data = pd.read_csv(url)
print(data)
data.to_csv('MSFT.csv')