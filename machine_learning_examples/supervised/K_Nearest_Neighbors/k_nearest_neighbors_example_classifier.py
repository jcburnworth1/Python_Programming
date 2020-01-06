## Import libraries
import pickle
from sklearn.neighbors import KNeighborsClassifier

## Establish movie_dataset & movie_labels from pickle files
## Dataset
file = open('machine_learning_examples/supervised/K_Nearest_Neighbors/movie_dataset.pkl', 'rb')

movie_dataset = pickle.load(file)

## Labels
file = open('machine_learning_examples/supervised/K_Nearest_Neighbors/movie_labels.pkl', 'rb')

movie_labels = pickle.load(file)

## Clean up
del(file)

## Convert dicts to lists so we can use KNN
## Movie Dataset
movie_dataset_list = []

for key, value in movie_dataset.items():
    movie_dataset_list.append(value)

## Movie List
movie_labels_list = []

for key, value in movie_labels.items():
    movie_labels_list.append(value)

## Clean up
del(key, value, movie_dataset, movie_labels)

## Run the KNN using scikit-learn
classifier = KNeighborsClassifier(n_neighbors = 5)

classifier.fit(movie_dataset_list, movie_labels_list)

## Predict the unknown points
unknown_points = [[.45, .2, .5],
                 [.25, .8, .9],
                 [.1, .1, .9]]

print(classifier.predict(unknown_points))