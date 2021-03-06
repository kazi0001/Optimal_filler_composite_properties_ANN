# -*- coding: utf-8 -*-
"""Artificial Neural Network

# This code is generated by Dr. Kazi Monzure Khoda

### Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import mean_squared_error
from keras.callbacks import EarlyStopping 
import pyrenn
from scipy.io import savemat


tf.__version__

"""## Part 1 - Data Preprocessing

### Importing the dataset
"""

dataset = pd.read_excel('PP_params.xlsx')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Taking care of missing data
from sklearn.impute import SimpleImputer 
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(X[:, 0:7])
X[:, 0:7] = imputer.transform(X[:, 0:7])

"""### Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


## Part 2 - Building the ANN
ann = tf.keras.models.Sequential()
ann.add(tf.keras.layers.Dense(units=200, activation='relu', input_dim = 8))
ann.add(tf.keras.layers.Dense(units=200, activation='relu'))
ann.add(tf.keras.layers.Dense(units=200, activation='relu'))
ann.add(tf.keras.layers.Dense(units=200, activation='relu'))
ann.add(tf.keras.layers.Dense(units=1))
ann.compile(optimizer = 'adam', loss = 'mean_squared_error')

"""### Training the ANN model on the Training set"""

#ann.fit(X_train, y_train, batch_size = 32, epochs = 10000)

"""### Training the ANN model on the Training set"""
early_stopping_monitor = EarlyStopping(monitor='val_loss', patience=5000)  # ignored
history_mse = ann.fit(X_train, y_train, batch_size = 32, epochs = 10000, callbacks = [early_stopping_monitor], verbose = 0, validation_split = 0.2)

print('Loss:    ', history_mse.history['loss'][-1], '\nVal_loss: ', history_mse.history['val_loss'][-1])

# EVALUATE MODEL IN THE TEST SET
score_mse_test = ann.evaluate(X_test, y_test)
print('Test Score:', score_mse_test)

# EVALUATE MODEL IN THE TRAIN SET
score_mse_train = ann.evaluate(X_train, y_train)
print('Train Score:', score_mse_train)


ann.save('my_model_PP3')
#net = ann.save('my_model_PP3.h5')
#net1 = ann.get_config()
#pyrenn.saveNN(net,r'C:\Users\KK14839\Dropbox\4. Toufiq & Mimi\Dr. Elsadig\Cotton filler\Python Code\Cotton Filler\ANN\ANN_PP\Final Code\Optimal design\mynetwork.csv')
#pyrenn.saveNN(net,r'C:\nn\mynetwork.csv')
#savemat("matlab_matrix.mat", net1)

"""### Predicting the results of the Test set"""

# y_pred = ann.predict(np.array([[0.07, 0.06, .139, 0.765, 28, 440, 15.7, 0.1390, 39.6 ]]))
y_pred = ann.predict(np.array([[0.015, 0.05, 0.065, 0.08, 25, 400, 0.8, 30 ]]))
#y_pred = ann.predict(np.array([[0.0165, 0.055, 0.0715, 0.088, 27.5, 440, 0.88, 33 ]]))
#y_pred = ann.predict(np.array([[0.0135, 0.045, 0.0585, 0.072, 22.5, 360, 0.72, 27]]))
#y_pred = ann.predict(np.array([[0.0165, 0.05, 0.065, 0.08, 25, 400, 0.8, 30 ]]))
#y_pred = ann.predict(np.array([[0.015, 0.05, 0.065, 0.08, 25, 400, 0.8, 33]]))
# Initiation Eng, Propagation Eng,Total Eng, Ductility, Tensile Strength, Mod of Elas,	Elong, Nt wt