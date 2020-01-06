## Import libraries
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

## Create data
temperature = np.array(range(60, 100, 2))
temperature = temperature.reshape(-1, 1)
sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]

## Plot the sales ~ temperature
plt.plot(temperature, sales, 'o')
plt.show()

##### Regression Model #####
## Create a regression object
line_fitter = LinearRegression()

## Fit the line
line_fitter.fit(temperature, sales)

## Predict sales
sales_predict = line_fitter.predict(temperature)

## Plot the results
plt.plot(temperature, sales, 'o')
plt.plot(temperature, sales_predict, 'x')
plt.show()