## Import libraries
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np

## Load data
hours_studied = np.array([[-1.64750894], [-1.47408695], [-1.30066495], [-1.12724296], [-0.95382097], [-0.78039897],
                          [-0.60697698], [-0.43355498], [-0.26013299], [-0.086711], [0.086711], [0.26013299],
                          [0.43355498], [0.60697698], [0.78039897], [0.95382097], [1.12724296], [1.30066495],
                          [1.47408695], [1.64750894]])

passed_exam = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1])

## Create LogisticRegression object and fit model
model_1 = LogisticRegression(solver='lbfgs')

model_1.fit(hours_studied, passed_exam)