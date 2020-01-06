## Import libraries
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime

## Read in the data - Source - https://archive.ics.uci.edu/ml/datasets/census+income
income_data = pd.read_csv("Python_Programming/machine_learning_examples/supervised/Random_Forest/income_random_forest/income.csv", header=0, delimiter=', ')

##### Explore the data #####
## Print the head
print(income_data.head(10))

## Print first row
print(income_data.iloc[0])

income_columns = income_data.columns
income_data_types = income_data.dtypes

## Print columns
for i in range(len(income_columns)):
    print("Column Name: {0} - {1}".format(income_columns[i], income_data_types[i]))

## Clean up
del(i, income_columns, income_data_types)

##### Prep the data for the model #####
## Segment off our target labels
income_labels = income_data['income']

## Segment off the features
income_features = income_data[['age','capital-gain','capital-loss','hours-per-week','sex', 'native-country']]

## Convert sex to 1=Male, 0=Female
income_features['sex'] = [0 if i == 'Female' else 1 for i in income_features['sex']]

## Convert native country to 1=United States, 0=Other
income_features['native-country'] = [1 if i=='United States' else 0 for i in  income_features['native-country']]

## Split in train and test
train_data, test_data, train_labels, test_labels = train_test_split(income_features, income_labels, random_state=1)

##### Build the model #####
## Create the classifier object
classifier = RandomForestClassifier(random_state=1, n_estimators=2000)

## Fit the model
model_fit_start = datetime.now()
classifier.fit(train_data, train_labels)
model_fit_end = datetime.now()

## Print model fitting time
print("Fitting Time: {0}".format(model_fit_end - model_fit_start))

## Capture scoring results
train_score = classifier.score(train_data, train_labels)
test_score = classifier.score(test_data, test_labels)

## Print scoring results
print("Train Score: {0}".format(train_score))
print("Test Score: {0}".format(test_score))