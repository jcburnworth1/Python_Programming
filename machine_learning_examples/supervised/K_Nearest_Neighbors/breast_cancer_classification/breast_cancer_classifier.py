## Import libraries
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

## Load data
breast_cancer_data = load_breast_cancer()

## Print example data & features
# print(breast_cancer_data.data[0])
# print(breast_cancer_data.feature_names)
# print(breast_cancer_data.target)
# print(breast_cancer_data.target_names)

## Split the data into train, test, and validation sets
training_data, validation_data , training_labels, validation_labels = train_test_split(breast_cancer_data.data,
                                                                                       breast_cancer_data.target,
                                                                                       test_size = 0.2,
                                                                                       random_state = 100)

## Check that training items are same length
print("Training Data Length: {0}".format(len(training_data)))
print("Training Label Length: {0}".format(len(training_labels)))

## Create the classifier
classifier = KNeighborsClassifier(n_neighbors=3)

## Fit the data using the training data
classifier.fit(training_data, training_labels)

## Check the score
print("Classifier Score: {0}".format(classifier.score(validation_data, validation_labels)))

## Loop to test k accruracy from 1 to 100
score_results = []

for i in range(1,101):
    ## Create the classifier
    classifier = KNeighborsClassifier(n_neighbors=i)

    ## Fit the data using the training data
    classifier.fit(training_data, training_labels)

    ## Score the result
    score_temp = classifier.score(validation_data, validation_labels)

    ## Append score and iteration to score_results
    score_results.append(score_temp)

## Clean up
del(i, score_temp)

## Plot the scoring results
plt.plot(range(1,101), score_results)
plt.title('Breast Cancer Classifier Accuracy for K: 1-100')
plt.xlabel('K-Values')
plt.ylabel('Score')
plt.axhline(max(score_results), c='r')
plt.show()