## Import libraries
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
from itertools import product

## AND gate points
data = [[0,0],[0,1],[1,0],[1,1]]
labels = [0,0,0,1]

## Get x & y values
x = [point[0] for point in data]
y = [point[1] for point in data]

## Scatter plot the data
plt.scatter(x, y, c = labels)
plt.show()

## Create perceptron object
classifier = Perceptron(max_iter = 40)

## Fit the data
classifier.fit(data, labels)

## Look at the score
classifier.score(data, labels)

## Investigate decision function - This will help us determine how far we are from the boundary
classifier.decision_function([[0, 0], [1, 1], [0.5, 0.5]])

## Begin heat mapping our decision boundary
x_values = np.linspace(0, 1, 100)
y_values = np.linspace(0, 1, 100)

## Get all possible values of the x & y values
point_grid = list(product(x_values, y_values))

## Recall .decision_function with our point grid - This will get us distances around the boundary
distances = classifier.decision_function(point_grid)

## Get only positive distances
abs_distances = [abs(point) for point in distances]

## Reshape for heat mapping
distances_matrix = np.reshape(abs_distances, (100, 100))

## Plot the heatmap
heatmap = plt.pcolormesh(x_values, y_values, distances_matrix)
plt.colorbar(heatmap)
plt.show()

## XOR Gate Points
# data = [[1,0],[0,1],[2,0],[2,1]]
# labels = [1,1,2,3]
#
# ## Get x & y values
# x = [point[0] for point in data]
# y = [point[1] for point in data]
#
# ## Scatter plot the data
# plt.scatter(x, y, c = labels)
# plt.show()
#
# ## Create perceptron object
# classifier = Perceptron(max_iter = 40)
#
# ## Fit the data
# classifier.fit(data, labels)
#
# ## Look at the score
# classifier.score(data, labels)

## OR Gate Points
# data = [[1,0],[0,1],[2,0],[2,1]]
# labels = [1,1,2,1]
#
# ## Get x & y values
# x = [point[0] for point in data]
# y = [point[1] for point in data]
#
# ## Scatter plot the data
# plt.scatter(x, y, c = labels)
# plt.show()
#
# ## Create perceptron object
# classifier = Perceptron(max_iter = 40)
#
# ## Fit the data
# classifier.fit(data, labels)
#
# ## Look at the score
# classifier.score(data, labels)