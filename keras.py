# Create first network with Keras
import os
import tensorflow
from tensorflow import keras
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

#from keras.models import Sequential
#from keras.layers import Dense
import numpy
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load pima indians dataset

training_dataset = numpy.loadtxt("/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/MORPHEOME/PPI/morpheome_final-1-23-19-crispra_huttlin_trimmed_v2.csv", delimiter=",")
#test_dataset = numpy.loadtxt("/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/MORPHEOME/PPI/morpheome_final-1-23-19-crispra_test_trimmed.csv", delimiter=",")

#dataset = numpy.loadtxt(os.path.dirname(os.path.realpath(__file__)) + "/pima-indians-diabetes.data.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = training_dataset[:,0:14]
Y = training_dataset[:,14]
# create model
model = Sequential()
model.add(Dense(20, input_dim=14, activation='relu'))
model.add(Dense(14, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=5, batch_size=10,  verbose=2)

# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# calculate predictions
predictions = model.predict(Y)
# round predictions
rounded = [round(x[0]) for x in predictions]
print(rounded)