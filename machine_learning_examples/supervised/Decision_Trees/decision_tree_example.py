## Import libraries
from machine_learning_examples.supervised.Decision_Trees.cars import training_points, training_labels, testing_points, testing_labels
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot as plt

## View training data
print("Training Point at Index 0: {0}".format(training_points[0]))
print("Training Label at Index 0: {0}".format(training_labels[0]))

## Create a classifier object
classifier = DecisionTreeClassifier(random_state=0, max_depth=12)

## Fit the model
classifier.fit(training_points, training_labels)

## Print out model score
print("Training Score: {0}".format(classifier.score(training_points, training_labels))) # This will alwasys be 1.0
print("Testing Score: {0}".format( classifier.score(testing_points, testing_labels)))

## Looping over a range to see how max depth impacts test accuracy
training_scores = []
test_scores = []

for i in range(1,101):
    ## Create a classifier object
    classifier = DecisionTreeClassifier(random_state=0, max_depth=i)

    ## Fit the model
    classifier.fit(training_points, training_labels)

    ## Attach scores to proper list
    training_scores.append(classifier.score(training_points, training_labels))
    test_scores.append(classifier.score(testing_points, testing_labels))

## Plot the results
plt.plot(range(1,101), training_scores)
plt.plot(range(1,101), test_scores)
plt.xlabel("Max Tree Depth Allowed")
plt.ylabel("Test Data Score")
plt.title
plt.show()