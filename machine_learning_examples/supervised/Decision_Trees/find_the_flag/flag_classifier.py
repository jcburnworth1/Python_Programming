# Attribute Information:
# 1. name: Name of the country concerned
# 2. landmass: 1=N.America, 2=S.America, 3=Europe, 4=Africa, 4=Asia, 6=Oceania
# 3. zone: Geographic quadrant, based on Greenwich and the Equator; 1=NE, 2=SE, 3=SW, 4=NW
# 4. area: in thousands of square km
# 5. population: in round millions
# 6. language: 1=English, 2=Spanish, 3=French, 4=German, 5=Slavic, 6=Other Indo-European, 7=Chinese, 8=Arabic,
#              9=Japanese/Turkish/Finnish/Magyar, 10=Others
# 7. religion: 0=Catholic, 1=Other Christian, 2=Muslim, 3=Buddhist, 4=Hindu, 5=Ethnic, 6=Marxist, 7=Others
# 8. bars: Number of vertical bars in the flag
# 9. stripes: Number of horizontal stripes in the flag
# 10. colours: Number of different colours in the flag
# 11. red: 0 if red absent, 1 if red present in the flag
# 12. green: same for green
# 13. blue: same for blue
# 14. gold: same for gold (also yellow)
# 15. white: same for white
# 16. black: same for black
# 17. orange: same for orange (also brown)
# 18. mainhue: predominant colour in the flag (tie-breaks decided by taking the topmost hue, if that fails then
#     the most central hue, and if that fails the leftmost hue)
# 19. circles: Number of circles in the flag
# 20. crosses: Number of (upright) crosses
# 21. saltires: Number of diagonal crosses
# 22. quarters: Number of quartered sections
# 23. sunstars: Number of sun or star symbols
# 24. crescent: 1 if a crescent moon symbol present, else 0
# 25. triangle: 1 if any triangles present, 0 otherwise
# 26. icon: 1 if an inanimate image present (e.g., a boat), otherwise 0
# 27. animate: 1 if an animate image (e.g., an eagle, a tree, a human hand) present, 0 otherwise
# 28. text: 1 if any letters or writing on the flag (e.g., a motto or slogan), 0 otherwise
# 29. topleft: colour in the top-left corner (moving right to decide tie-breaks)
# 30. botright: Colour in the bottom-left corner (moving left to decide tie-breaks)

##### Import libraries #####
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

##### Bring in the flag data #####
flags_data = pd.read_csv('Python_Programming/machine_learning_examples/supervised/Decision_Trees/find_the_flag/flags.csv', header=0)

##### Data Exploration #####
flag_columns = flags_data.columns
flag_columns_data_types = flags_data.dtypes

## Print out the types
for i in range(len(flag_columns)):
    print("Column Name - Type: {name} - {type}".format(name=flag_columns[i], type=flag_columns_data_types[i]))

## Clean up
del(i, flag_columns, flag_columns_data_types)

## Print out head
print(flags_data.head(10))

##### Data preparation #####
## Section off the labels
flag_labels = flags_data['Landmass']

## Section off the color columns
flag_colors = flags_data[['Red','Green','Blue','Gold','White','Black','Orange']]

## Split into train and test
train_data, test_data, train_labels, test_labels = train_test_split(flag_colors, flag_labels, random_state=1)

##### Model Fitting #####
## Create a decision tree classifier
classifier = DecisionTreeClassifier(random_state=1)

## Fit model
classifier.fit(train_data, train_labels)
train_score_color_model = classifier.score(train_data, train_labels)
test_score_color_model = classifier.score(test_data, test_labels)

## Print score of the training fit
print("Train Score: {0}%".format(round(train_score_color_model * 100, 2)))

## Print score of the test prediction
print("Test Score: {0}%".format(round(test_score_color_model * 100, 2)))

##### Can we improve classification accuracy by varying tree depth? #####
## Varying depth does not materially improve accuracy - No improvement over initial model
train_score = []
test_score = []

## Loop over and change depth of tree to see if varying depth changes accuracy
for i in range(1,21):
    ## Create a decision tree classifier
    loop_classifier = DecisionTreeClassifier(random_state=1, max_depth=i)

    ## Fit model
    loop_classifier.fit(train_data, train_labels)

    ## Append score results to appropriate lists
    train_score.append(loop_classifier.score(train_data, train_labels))
    test_score.append(loop_classifier.score(test_data, test_labels))

## Plot results of max_depth varying
plt.plot(range(1,21), train_score)
plt.plot(range(1,21), test_score)
plt.axhline(classifier.score(train_data, train_labels)) ## Base score - Training Data
plt.axhline(classifier.score(test_data, test_labels)) ## Base score - Test Data
plt.show()

## Clean up
del(classifier, flag_colors, flag_labels, i, loop_classifier, test_data, test_labels,
    train_data, train_labels)

##### Can we improve classification accuracy by adding more features? #####
## Setup new data / labels with color & shape
flag_labels = flags_data['Landmass']
flag_colors_shapes = flags_data[['Red','Green','Blue','Gold','White','Black','Orange', 'Colors', ## Colors
                                 'Bars','Stripes','Circles','Crosses','Saltires','Quarters','Sunstars', 'Crescent','Triangle']] ## Shapes

## Split into train and test
train_data, test_data, train_labels, test_labels = train_test_split(flag_colors_shapes, flag_labels, random_state=1)

## Setup classifier
classifier_color_shapes = DecisionTreeClassifier(random_state=1)

## Fit model
classifier_color_shapes.fit(train_data, train_labels)
train_score_color_shape_model = classifier_color_shapes.score(train_data, train_labels)
test_score_color_shape_model = classifier_color_shapes.score(test_data, test_labels)

## Print score of the training fit
print("Train Score: {0}%".format(round(train_score_color_model * 100, 2)))

## Print score of the test prediction
print("Test Score: {0}%".format(round(test_score_color_model * 100, 2)))

##### Plot new results to original plot #####
## Plot results of max_depth varying
plt.plot(range(1,21), train_score, c='blue')
plt.plot(range(1,21), test_score, c='orange')
plt.axhline(train_score_color_model, c='red') ## Base score - Training Data
plt.axhline(test_score_color_model, c='red') ## Base score - Test Data
plt.axhline(train_score_color_shape_model, c='purple')
plt.axhline(test_score_color_shape_model, c='purple')
plt.show()