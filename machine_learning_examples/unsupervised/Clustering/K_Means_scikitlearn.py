## n_clusters: number of clusters to form and number of centroids to generate
## init: method for initialization
## k-means++: K-Means++ [default]
## random: K-Means
## random_state: the seed used by the random number generator [optional]
# your_model = KMeans(n_clusters=4, init='random')
# your_model.fit(x_training_data)
# predictions = your_model.predict(your_x_data)
## Import libraries
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

## Load iris data
# Column 0: Sepal length
# Column 1: Sepal width
# Column 2: Petal length
# Column 3: Petal width
iris = datasets.load_iris()

## Iris data
samples = iris.data
samples = samples[:, 0:2]

# Use KMeans() to create a model that finds 3 clusters
model = KMeans(n_clusters = 4) ## using K-means++ by default for better centroids
# model = KMeans(n_clusters = 4, inti='random') ## using random initial centroids

# Use .fit() to fit the model to samples
model.fit(samples)

# Use .predict() to determine the labels of samples
labels = model.predict(samples)

# Print the labels
print(labels)

## Plot the results including the clusters
plt.scatter(samples[:,0], samples[:, 1], c = labels)
plt.show()