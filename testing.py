from datetime import datetime, timedelta
from iexfinance.stocks import Stock, get_historical_data, get_historical_intraday # https://addisonlynch.github.io/iexfinance/devel/index.html
import tensorflow as tf
from tensorflow import keras
import numpy as np

model = tf.keras.Sequential()
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(1, activation='softmax'))

# DESC:  returns an array of all the minute
#      -stk -> stock abbreiviation
#      -key -> field of data i.e. average, high, low
#      -day -> day of minute stock data
def GetIntradayPrices(stk, key, day):
    df = get_historical_intraday(stk, day)
    data = []
    for minAver in df:
        data.append(minAver.get(key))
    return data

# DESC:  returns an array of all the minutes in between startDate and endDate
#      -stk -> stock abbreiviation
#      -key -> field of data i.e. average, high, low
#      -startDate -> first day to take stock data from
#      -endDate -> last day to take stock data from
def GetMultipleIntradayData(stk, key, startDate, endDate):
    dateIncrement = startDate
    dayDelta = timedelta(days=1)
    data =[]
    while dateIncrement != endDate:
        data += GetIntradayPrices(stk, key, dateIncrement)
        dateIncrement = dateIncrement+dayDelta
    return data



startDate = datetime(2019, 1, 1)
endDate = datetime(2019, 3, 1)

stk = 'AMZN'
# print(GetAverages(stk, "average", endDate))
# print(len(GetAverages(stk, "average", endDate)))

data = GetMultipleIntradayData(stk, "average", startDate, endDate)
print(data)
print(len(data))

