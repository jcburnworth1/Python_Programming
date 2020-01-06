## Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

## Read in the data
streeteasy = pd.read_csv("Python_Programming/machine_learning_examples/supervised/Regression/rental_data.csv")

## Copy the streeteasy data
df = pd.DataFrame(streeteasy)

## Create x & y data frames to build the regression
## Can select n-columns for x
x = df[['size_sqft','building_age_yrs']]
y = df[['rent']]

## Split data into test & train
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

## Create regression object and train model - Note uses same LinearRegression() method as simple
ols = LinearRegression()
ols.fit(x_train, y_train)
ols.score(x_train, y_train)

## Plot the figure with 3D view of the data
fig = plt.figure(1, figsize=(6, 4))
plt.clf()

## Create 3D axes
elev = 43.5
azim = -110

ax = Axes3D(fig, elev=elev, azim=azim)
ax.scatter(x_train[['size_sqft']], x_train[['building_age_yrs']], y_train, c='k', marker='+')
ax.plot_surface(np.array([[0, 0], [4500, 4500]]), np.array([[0, 140], [0, 140]]),
                ols.predict(np.array([[0, 0, 4500, 4500], [0, 140, 0, 140]]).T).reshape((2, 2)), alpha=.7)
ax.set_xlabel('Size (ft$^2$)')
ax.set_ylabel('Building Age (Years)')
ax.set_zlabel('Rent ($)')
ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])
plt.show()

## Predict an apartment with 1500 sqft in a 34 year old building
sonny_apartment = [[1500, 34]]
predict = ols.predict(sonny_apartment)
print("Predicted rent: $%.2f" % predict)