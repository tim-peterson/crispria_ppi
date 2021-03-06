# Create first network with Keras
import os
'''from random import random
import pandas
from pandas import concat
from pandas import DataFrame'''

import tensorflow
from tensorflow import keras
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
'''from tensorflow.python.keras.layers import LSTM
from tensorflow.python.keras.layers import Masking'''

#from keras.models import Sequential
#from keras.layers import Dense
import numpy
from numpy import array
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load pima indians dataset

training_dataset = numpy.loadtxt("/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/MORPHEOME/PPI/morpheome_final-1-27-19-crispria_huttlin_trimmed_v11d.csv", delimiter=",")

#training_dataset = numpy.loadtxt("/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/MORPHEOME/PPI/morpheome_final-1-25-19-crispria_huttlin_trimmed_v8.csv", delimiter=",")
# skiprows=1,
#, usecols = (1,15)
#dataset = numpy.loadtxt(os.path.dirname(os.path.realpath(__file__)) + "/pima-indians-diabetes.data.csv", delimiter=",")
# split into input (X) and output (Y) variables

#X, Y = training_dataset[:, :-1], training_dataset[:, -1] # works the same as the commands below
X = training_dataset[:,0:16]
#X = training_dataset[:,0:14]
Y = training_dataset[:,16]
#Y = training_dataset[:,14]
# create model
model = Sequential()
#model.add(Masking(mask_value=0, input_shape=(:,0:16)))
#model.add(LSTM(5))
model.add(Dense(20, input_dim=16, activation='relu'))
#model.add(Dense(20, input_dim=14, activation='relu'))
model.add(Dense(16, activation='relu'))
#model.add(Dense(14, activation='relu'))
'''model.add(Dense(14, activation='relu'))
model.add(Dense(14, activation='relu'))
model.add(Dense(14, activation='relu'))
model.add(Dense(14, activation='relu'))
model.add(Dense(14, activation='relu'))
model.add(Dense(14, activation='relu'))
model.add(Dense(14, activation='relu'))
model.add(Dense(14, activation='relu'))
model.add(Dense(14, activation='relu'))
model.add(Dense(14, activation='relu'))
model.add(Dense(14, activation='relu'))'''
model.add(Dense(1))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=5, batch_size=10,  verbose=2)

# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

test_dataset = numpy.loadtxt("/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/MORPHEOME/PPI/morpheome_final-1-27-19-crispria_test_mtor_atraid_v11d.csv", delimiter=",")
#, usecols = (1,14)
#test = training_dataset[:,0:13]
# calculate predictions
predictions = model.predict(test_dataset)
# round predictions
rounded = [round(x[0]) for x in predictions]
print(rounded)

#rounded.astype(numpy.int64)

rounded = numpy.array(rounded, dtype=numpy.int64)

test_dataset_v2 = test_dataset
#[a[:,:j] for j in i]
for i in range(int(test_dataset.shape[0])):
	test_dataset_v2[i] = numpy.append(test_dataset_v2[i], rounded[i])
#dictA = dict(zip(list1, rounded))

#print(test_dataset_v2)

#x = numpy.arange(20).reshape((4,5))
numpy.savetxt('/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/MORPHEOME/PPI/test_predictions_v4.txt', test_dataset_v2) #, fmt='%s'
