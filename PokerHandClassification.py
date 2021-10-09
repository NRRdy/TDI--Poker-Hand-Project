# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 19:30:16 2021

@author: Nicholas Ray

Source of Poker Hand Data:
Robert Cattral (cattral '@' gmail.com)

Franz Oppacher (oppacher '@' scs.carleton.ca)
Carleton University, Department of Computer Science
Intelligent Systems Research Unit
1125 Colonel By Drive, Ottawa, Ontario, Canada, K1S5B6

http://archive.ics.uci.edu/ml/datasets/Poker+Hand
"""

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Working Directory
DataDir = "E:/Work/JobApplications/TDI_CodingChallenge/"

#Load Data
data_train = pd.read_csv(DataDir + "PokerHands_train.csv")

data_test = pd.read_csv(DataDir + "PokerHands_test.csv")

# Create arrays for the features and the response variable
y = data_train['Class'].values
X = data_train.drop('Class', axis=1).values

# Create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors = 6)

# Fit the classifier to the data
knn.fit(X, y)

# Predict the poker hands for the training data X
y_pred = knn.predict(X)

# Predict the poker hands for the test data
new_prediction = knn.predict(data_test)
print("Prediction: {}".format(new_prediction))