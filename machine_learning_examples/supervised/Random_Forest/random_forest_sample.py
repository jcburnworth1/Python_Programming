## Import libraries
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
from machine_learning_examples.supervised.Random_Forest.cars import training_points, training_labels, testing_points, testing_labels
from sklearn.ensemble import RandomForestClassifier

## Create our random forest classifier
classifier = RandomForestClassifier(n_estimators = 2000, random_state=0)

## Fit the model
classifier.fit(training_points, training_labels)

## Print scores for training and testing
print("Training Score: {0}".format(classifier.score(training_points, training_labels)))
print("Testing Score: {0}".format( classifier.score(testing_points, testing_labels)))