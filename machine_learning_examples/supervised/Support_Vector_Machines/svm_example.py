## Import Libraries
from sklearn.svm import SVC
import matplotlib.pyplot as plt

## Create our data
points = [[0.5, 2], [1.0, 6], [1.5, 8],
          [2.0, 1], [2.0, 7], [2.5, 2]]

labels = [1,0,0,1,0,1]

## Create classifier object and fit model
classifier = SVC(kernel= 'linear')
classifier.fit(points, labels)

## Predict two points
print(classifier.predict([[3,2], [6,7]]))