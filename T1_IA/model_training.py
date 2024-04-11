from pathlib import Path

import pandas as pd

from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import StratifiedShuffleSplit

import tkinter as tk
from tkinter import messagebox

separator = ','
names = ['1','2','3','4','5','6','7','8','9','result']
#reading the dataset using the separator
db = pd.read_csv('tic-tac-toe.data', sep=separator, names=names)

#separating the data in features and target
X = db.drop(columns=['result'])
y = db['result']

#transforming the data from string to number using one-hot encoding
X = pd.get_dummies(X)

#separating the data in training, test and validation (80% for training, 20% for testing, 10% for validation)
X_train_test, X_val, y_train_test, y_val = train_test_split(X, y, test_size=0.1, stratify=y, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X_train_test, y_train_test, test_size=0.2, stratify=y_train_test, random_state=0)

#training a knn model and testing
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)
predictions = knn.predict(X_test)

print('KNN EVALUATION ON TEST')
print('Accuracy:', accuracy_score(y_test, predictions))
print('----------------------------------')

#training a decison_tree model and testing
decison_tree = DecisionTreeClassifier()
decison_tree.fit(X_train,y_train)
predictions = decison_tree.predict(X_test)

print('DECISION TREE EVALUATION ON TEST')
print('Accuracy:', accuracy_score(y_test, predictions))
print('----------------------------------')

#training a mlp model and testing
mlp = MLPClassifier(hidden_layer_sizes=(50, 25), activation='relu', solver='adam')
mlp.fit(X_train,y_train)
mlp = decison_tree.predict(X_test)

print('MLP TREE EVALUATION ON TEST')
print('Accuracy:', accuracy_score(y_test, predictions))
print('----------------------------------')

#training a naive_bayes model and testing
naive_bayes = GaussianNB()
naive_bayes.fit(X_train,y_train)
naive_bayes = decison_tree.predict(X_test)

print('NAIVE BAYES EVALUATION ON TEST')
print('Accuracy:', accuracy_score(y_test, predictions))
print('----------------------------------')


