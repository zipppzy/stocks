from datetime import datetime
from iexfinance.stocks import Stock, get_historical_data, get_historical_intraday
import tensorflow as tf
from tensorflow import keras
import numpy as np

model = tf.keras.Sequential()
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(1, activation='softmax'))





stk = Stock('TSLA')
print(stk.get_price())
