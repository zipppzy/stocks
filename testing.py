from datetime import datetime
from iexfinance.stocks import Stock, get_historical_data, get_historical_intraday  #https://addisonlynch.github.io/iexfinance/devel/index.html
import tensorflow as tf
from tensorflow import keras
import numpy as np

model = tf.keras.Sequential()
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(1, activation='softmax'))

#DESC:  returns an array of all the minute
#       averages throughout the day
#      -stk -> stock abbreiviation
#      -key -> field of data i.e. average, high, low
#      -day -> day of minute stock data
def GetAverages(stk, key, day):
    #Todo: rename list from averages
    df = get_historical_intraday(stk, day)
    averages = []
    for minAver in df:
        averages.append(minAver.get(key))
    return averages



startDate = datetime(2018, 1, 27)
endDate = datetime(2019, 3, 1)

stk = 'AMZN'
print(GetAverages(stk,"average", endDate))


