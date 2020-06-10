## Import libraries
import numpy as np

## Create cupcakes np.array
cupcakes = np.array([2, 0.75, 2, 1, 0.5])

## Read in the data
recipes = np.genfromtxt('basic_python/bettys_bakery_numpy/recipes.csv', delimiter=',')

## Print out recipes
print(recipes)

## Store eggs required for all recipes
eggs = recipes[:,2]

## Recipes with only 1 egg
print("Recipes with 1 Egg: " +  str(len(eggs[eggs == 1])))

## Create cookies array
cookies = recipes[2,]

## Calculate double batch of cupcakes
double_batch = cupcakes * 2

## Create grocery_list
grocery_list = cookies + double_batch