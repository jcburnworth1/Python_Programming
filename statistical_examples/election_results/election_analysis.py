## Import libraries
import numpy as np
from matplotlib import pyplot as plt

## Election Survey data
survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos',
                    'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan',
                    'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan',
                    'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan',
                    'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan',
                    'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan',
                    'Kerrigan', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan',
                    'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan',
                    'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

## Calculate Ceballos survey responses
total_ceballos = sum([1 for response in survey_responses if response == 'Ceballos'])

print("Ceballos Responses: {0}".format(str(total_ceballos)))

## Calculate percentage Ceballos
percentage_ceballos = round((total_ceballos / len(survey_responses)) * 100, 2)

print("Ceballos Percentage: {0}%".format(str(percentage_ceballos)))

## Calculate possible outcomes
possible_surveys = np.random.binomial(70, 0.54, size=10000) / 70

## Histogram of possible surveys
plt.hist(possible_surveys, range=(0,1), bins = 20)
plt.show()

## Calculate Ceballos losses
ceballos_loss_surveys = np.mean(possible_surveys < 0.5)

print("Ceballos Loss %: {0}".format(str(round(ceballos_loss_surveys * 100, 2))))

## Simulate a large survey
large_survey = np.random.binomial(7000, 0.54, size=10000) / 7000

## Re-calculate Ceballos losses with larger size
ceballos_loss_new = np.mean(large_survey < 0.5)

print("New Ceballos Loss %: {0}%".format(str(round(ceballos_loss_new * 100, 2))))