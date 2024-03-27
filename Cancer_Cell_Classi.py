# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10StckLQOyhSjpJc9w_xNTxY3qEr-cy9d
"""

from ipywidgets import interact, widgets  # Import interact and widgets
# Import other libraries you need (e.g., pandas for data manipulation)

import sklearn

# importing the dataset
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']

print(label_names)

print(labels)

print(feature_names)

print(features)

from sklearn.model_selection import train_test_split

# splitting the data
train, test, train_labels, test_labels = train_test_split(features, labels,
									test_size = 0.33, random_state = 42)

from sklearn.naive_bayes import GaussianNB

# initializing the classifier
gnb = GaussianNB()

# training the classifier
model = gnb.fit(train, train_labels)

predictions = gnb.predict(test)

# printing the predictions
print(predictions)

from sklearn.metrics import accuracy_score

# evaluating the accuracy
print(accuracy_score(test_labels, predictions))