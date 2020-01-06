## Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

## Load the passenger data
passengers = pd.read_csv('Python_Programming/machine_learning_examples/supervised/Regression/titanic_survival_logistic_regression/titanic_data.csv')

## Update sex column to numerical
passengers['Sex'] = [1 if sex == 'female' else 0 for sex in passengers['Sex']]

## Fill the nan values in the age column
age_mean = np.mean(passengers.Age)
passengers['Age'].fillna(value=age_mean, inplace=True)

## Create a first class column
passengers['FirstClass'] = [1 if pclass == 1 else 0 for pclass in passengers['Pclass']]

## Create a second class column
passengers['SecondClass'] = [1 if pclass == 2 else 0 for pclass in passengers['Pclass']]

## Select the desired features
features = passengers[['Sex', 'Age', 'FirstClass', 'SecondClass']]
survival = passengers['Survived']

## Perform train, test, split
train_features, test_features, train_labels, test_labels = train_test_split(features, survival, test_size=0.2)

## Scale the feature data so it has mean = 0 and standard deviation = 1
scaler = StandardScaler()

train_features = scaler.fit_transform(train_features)
test_features = scaler.fit_transform(test_features)

## Create and train the model
model_1 = LogisticRegression(solver='lbfgs')
model_1.fit(train_features, train_labels)

## Score the model on the train data
train_score = model_1.score(train_features,train_labels)
print("Model 1 Score: {0}".format(train_score))

## Score the model on the test data
test_score = model_1.score(test_features,test_labels)
print("Model 1 Test Score: {0}".format(test_score))

## Analyze the coefficients
print("##### Model Coefficients Beg #####")
print("Sex Coefficient: {0}".format(model_1.coef_[0][0]))
print("Age Coefficient: {0}".format(model_1.coef_[0][1]))
print("First Class Coefficient: {0}".format(model_1.coef_[0][2]))
print("Second Class Coefficient: {0}".format(model_1.coef_[0][3]))
print("##### Model Coefficients End #####")

## Sample passenger features
Jack = np.array([0.0,20.0,0.0,0.0])
Rose = np.array([1.0,17.0,1.0,0.0])
You = np.array([0.0,32,1.0,0.0])

## Combine passenger arrays
unknown_passengers = np.array([Jack, Rose, You])

## Scale the sample passenger features
unknown_passengers = scaler.transform(unknown_passengers)

## Make survival predictions!
unknown_passengers_predict_probs =  model_1.predict_proba(unknown_passengers)

## Print results
print("Jack Survival Probability: {0}%".format(round(unknown_passengers_predict_probs[0][1] * 100,2)))
print("Rose Survival Probability: {0}%".format(round(unknown_passengers_predict_probs[1][1] * 100,2)))
print("My Survival Probability: {0}%".format(round(unknown_passengers_predict_probs[2][1] * 100,2)))