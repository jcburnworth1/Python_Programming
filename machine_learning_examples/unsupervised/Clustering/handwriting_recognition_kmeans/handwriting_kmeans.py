## Import libraries
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

## Load digits dataset
digits = datasets.load_digits()

## Print digits
print(digits)

## Get data descriptions
print(digits.DESCR)

## Capture digits data
digits_data = digits.data
print(digits_data)

## Capture the targets
digits_target = digits.target
print(digits_target)

## Visualize a single image from the dataset
plt.gray()
plt.matshow(digits.images[100])
plt.xlabel("Image: {0}".format(digits.target[100]))
plt.show()
plt.close('all')

## Cluster the data
model = KMeans(n_clusters = 10, random_state=42)

## Fit the model
model.fit(digits_data)

## Visualize all of the centroids
fig = plt.figure(figsize=(8, 3))
fig.suptitle('Cluser Center Images', fontsize=14, fontweight='bold')

for i in range(10):

  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)

  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
plt.show()