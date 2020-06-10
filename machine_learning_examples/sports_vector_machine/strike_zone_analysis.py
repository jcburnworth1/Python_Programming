## Import libraries
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd

## Read in the data
aaron_judge = pd.read_csv('machine_learning_examples/sports_vector_machine/aaron_judge.csv')
jose_altuve = pd.read_csv('machine_learning_examples/sports_vector_machine/jose_altuve.csv')
david_ortiz = pd.read_csv('machine_learning_examples/sports_vector_machine/david_ortiz.csv')

## Explore the data
## Column names
print(aaron_judge.columns)
print(aaron_judge.description.unique()) # Stores outcome of the pitch
print(aaron_judge.type.unique()) # Stores strike, ball, or hit
print(aaron_judge.plate_x.unique()) # Store x position of the pitch - Distance from center
print(aaron_judge.plate_z.unique()) # Store z position of the pitch - Distance off ground

## Map aaron_judge['type'] field to 1 - Strike (S) or 0 - Ball (B) - Will drop X later
aaron_judge['type_num'] = aaron_judge['type'].map({'S':1, 'B':0})

## Drop missing values from aaron_judge for type, plate_x, plate_z
aaron_judge = aaron_judge.dropna(subset=['type_num','plate_x','plate_z'])

## Plot the pitches in a scatter plot
plt.scatter(x=aaron_judge['plate_x'], y=aaron_judge['plate_z'], c=aaron_judge['type_num'],
            cmap=plt.cm.coolwarm, alpha=0.5)
plt.show()

##### Build the SVM for Aaron Judge's strike zone #####
## Split data
training_set, validation_set = train_test_split(aaron_judge[['plate_x', 'plate_z', 'type_num']], random_state=1)

## Create classifier object
aaron_judge_model = SVC(kernel='rbf')

## Fit our model
aaron_judge_model.fit(training_set[['plate_x','plate_z']], training_set[['type_num']])

## Score model against training and validation data
## Initial scores with default gamma and C
# Training Score: 0.8413897280966768
# Test Score: 0.8355957767722474

## Scores when gamma = 100 and C = 100
# Training Score: 0.974320241691843
# Test Score: 0.7933634992458521

print("Training Score: {0}".format(aaron_judge_model.score(training_set[['plate_x','plate_z']],
                                                           training_set[['type_num']])))
print("Test Score: {0}".format(aaron_judge_model.score(validation_set[['plate_x','plate_z']],
                                                       validation_set[['type_num']])))

##### Loop over the above and test different values for gamma #####
gamma_manipulation_results_train = []
gamma_manipulation_results_validation = []

for i in range(1,101):
    ## Create classifier object
    aaron_judge_model = SVC(kernel='rbf', gamma=i)

    ## Fit our model
    aaron_judge_model.fit(training_set[['plate_x', 'plate_z']], training_set[['type_num']])

    gamma_manipulation_results_train.append(aaron_judge_model.score(training_set[['plate_x', 'plate_z']],
                                                                    training_set[['type_num']]))
    gamma_manipulation_results_validation.append(aaron_judge_model.score(validation_set[['plate_x', 'plate_z']],
                                                                         validation_set[['type_num']]))

## Plot the results
plt.plot(range(1,101), gamma_manipulation_results_train)
plt.plot(range(1,101), gamma_manipulation_results_validation)
plt.axhline(max(gamma_manipulation_results_validation))
plt.axvline(gamma_manipulation_results_validation.index(max(gamma_manipulation_results_validation)))
plt.title('Gamma 1-100')
plt.show()

##### Loop over the above and test different values for C #####
c_manipulation_results_train = []
c_manipulation_results_validation = []

for i in range(1,101):
    ## Create classifier object
    aaron_judge_model = SVC(kernel='rbf', C=i)

    ## Fit our model
    aaron_judge_model.fit(training_set[['plate_x', 'plate_z']], training_set[['type_num']])

    c_manipulation_results_train.append(aaron_judge_model.score(training_set[['plate_x', 'plate_z']],
                                                                training_set[['type_num']]))
    c_manipulation_results_validation.append(aaron_judge_model.score(validation_set[['plate_x', 'plate_z']],
                                                                     validation_set[['type_num']]))

## Plot the results
plt.plot(range(1,101), c_manipulation_results_train)
plt.plot(range(1,101), c_manipulation_results_validation)
plt.axhline(max(c_manipulation_results_validation))
plt.axvline(c_manipulation_results_validation.index(max(c_manipulation_results_validation)))
plt.title('C 1-100')
plt.show()

##### Find Optimal values for gamma and C #####
gamma_optimal = gamma_manipulation_results_validation.index(max(gamma_manipulation_results_validation))
c_optimal = 2

## Create classifier object
aaron_judge_model_final = SVC(kernel='rbf', gamma=gamma_optimal, C=c_optimal)

## Fit our model
aaron_judge_model_final.fit(training_set[['plate_x','plate_z']], training_set[['type_num']])

## Score model against training and validation data
print("Training Score: {0}".format(aaron_judge_model_final .score(training_set[['plate_x','plate_z']],
                                                                  training_set[['type_num']])))
print("Test Score: {0}".format(aaron_judge_model_final.score(validation_set[['plate_x','plate_z']],
                                                             validation_set[['type_num']])))