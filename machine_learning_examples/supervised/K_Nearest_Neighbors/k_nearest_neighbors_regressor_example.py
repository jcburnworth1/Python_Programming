## Import libraries
import pickle
from sklearn.neighbors import KNeighborsRegressor

## Establish movie_dataset & movie_ratings from pickle files
## Dataset
file = open('Python_Programming/machine_learning_examples/supervised/K_Nearest_Neighbors/movie_dataset.pkl', 'rb')

movie_dataset = pickle.load(file)

## Ratings
file = open('Python_Programming/machine_learning_examples/supervised/K_Nearest_Neighbors/movie_ratings.pkl', 'rb')

movie_ratings = pickle.load(file)

## Clean up
del(file)

## Convert dicts to lists so we can use KNN
## Movie Dataset
movie_dataset_list = []

for key, value in movie_dataset.items():
    movie_dataset_list.append(value)

## Movie List
movie_ratings_list = []

for key, value in movie_ratings.items():
    movie_ratings_list.append(value)

## Clean up
del(key, value, movie_dataset, movie_ratings)

## Run the KNN using scikit-learn
regressor = KNeighborsRegressor(n_neighbors=5, weights='distance')

## Fit model based on movie data
regressor.fit(movie_dataset_list, movie_ratings_list)

## Predict the rating of our unknown movie
unknown_movies = [[0.016, 0.300, 1.022],
                  [0.0004092981, 0.283, 1.0112],
                  [0.00687649, 0.235, 1.0112]]

print(regressor.predict(unknown_movies))