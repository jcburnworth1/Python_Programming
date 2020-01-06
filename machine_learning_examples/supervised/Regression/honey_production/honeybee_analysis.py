## Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


## Read in the data
## Original data - https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv
honey_data = pd.read_csv("honey_production/honeyproduction.csv")

## Get a sense of the df structure
print(honey_data.head())
print(honey_data.columns)
print(honey_data.shape)

## Roll up yearly production
prod_per_year = honey_data.groupby('year').totalprod.mean().reset_index()

## Start setting the regression
X = prod_per_year.year.values.reshape(-1,1)
y = prod_per_year.totalprod.values.reshape(-1,1)

## Scatter plot of relationship
plt.scatter(x=X, y=y)
plt.show()

## Build the regression
regr = LinearRegression()
regr.fit(X, y)

## Print out line stats
print('Model Coefficient: {0}'.format(round(regr.coef_[0][0], 2)))
print('Model Intercept: {0}'.format(round(regr.intercept_[0], 2)))

## Get y predictions for the given value of x in the original data
y_predict = regr.predict(X)

## Plot original data & predicted data
plt.plot(X, y, 'o')
plt.plot(X, y_predict, 'x')
plt.show()

## Predict production out to 2050
X_future = np.array(range(2013, 2051)).reshape(-1,1)

future_predict = regr.predict(X_future)

## Plot original data & predicted data through 2050
plt.plot(X, y, 'o')
plt.plot(X, y_predict, 'x')
plt.plot(X_future, future_predict, '1')
plt.axvline(2012.5, c='r')
plt.text(2012, 0, 'Training Cut Off',rotation=90)
plt.show()