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
    df = get_historical_intraday(stk, day, token="sk_290f4ad121254d7696a9a00c48748bb4")
    data = []
    for minAver in df:
        data.append(minAver.get(key))
    return data

# DESC:  returns an array of all the minutes in between startDate and endDate
#      -stk -> stock abbreviation
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

# DESC:  replaces missing stock prices with averages of surrounding prices
#      -data -> list of stock prices
def fixData(data):
    x = data
    for i in range(len(x)):
        if x[i] is None:
            noneCounter = 1
            while x[i+noneCounter] is None:
                noneCounter+=1
            for j in range(i,i+noneCounter):
                x[j] = (x[i-1] + x[i+noneCounter])/2
    return data


startDate = datetime(2019, 6, 1)
endDate = datetime(2019, 6, 7)

stk = 'AMZN'
# print(GetAverages(stk, "average", endDate))
# print(len(GetAverages(stk, "average", endDate)))
data = GetMultipleIntradayData(stk, "average", startDate, endDate)
print(data)
data = fixData(data)
print(data)
print(len(data))

model.compile(optimizer='adam', loss=keras.losses.binary_crossentropy)


