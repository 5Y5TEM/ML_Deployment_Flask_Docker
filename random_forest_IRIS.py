# Created by MeltemSubasioglu at 2/16/2022
# Source udemy vivekkalyanarangan

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle #saving models as binary files
import os
dirname = os.path.dirname(__file__)



# Loading the dataset
iris = load_iris()
X = iris.data
y = iris.target

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42, test_size=0.5)

# Building the model
model = RandomForestClassifier(n_estimators = 10)

# Training the classifier
model.fit(X_train, y_train)

# Predictions
predicted = model.predict(X_test)

# Check accuracy
print(accuracy_score(predicted, y_test))
# path = (dirname+ r"/rf.pkl")

# Saving the model
with open(dirname+ r"/rf.pkl", 'wb') as model_pkl:
    pickle.dump(model, model_pkl)