## See https://www.codecademy.com/paths/data-science/tracks/dspath-supervised/modules/dspath-classification/lessons/knn/exercises/choosing-k
## Import libraries
import pickle

## Establish movie_dataset & movie_labels
## Dataset
file = open('machine_learning_examples/supervised/K_Nearest_Neighbors/movie_dataset.pkl', 'rb')

movie_dataset = pickle.load(file)

## Labels
file = open('machine_learning_examples/supervised/K_Nearest_Neighbors/movie_labels.pkl', 'rb')

movie_labels = pickle.load(file)

## Clean up
del(file)

# print(movie_dataset['Bruce Almighty'])
# print(movie_labels['Bruce Almighty'])

## Distance Function
def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

## Classification Function
def classify(unknown, dataset, labels, k):
  distances = []
  num_good = 0
  num_bad = 0
  # Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    # Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  # Taking only the k closest points
  neighbors = distances[0:k]

  for movie in neighbors:
    title = movie[1]

    if labels[title] == 0:
      num_bad += 1
    else:
      num_good += 1

    if num_good > num_bad:
      return 1
    else:
      return 0

## K-Mean Classification Example
unclassified_movie = [.4, .2, .9]
classify_result = classify(unclassified_movie, movie_dataset, movie_labels, 5)

## Classify a different movie
## Check if movie is already in dataset
print('Call Me By Your Name' in movie_dataset)

my_movie = [350000, 132, 2017]

normalized_my_movie = [2.8634276635608227e-05, 0.3242320819112628, 1.0112359550561798]

print(classify(normalized_my_movie, movie_dataset, movie_labels, 5))