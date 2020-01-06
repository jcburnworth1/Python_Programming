## Import libraries
import matplotlib.pyplot as plt

## Create data
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

##### Create line of best fit manually #####
## Slope:
m = 10

## Intercept:
b = 55

## Calculate y-values for regression manually
y = [(m * x_value) + b for x_value in months]

## Plot Month vs. Revenue & Revenue line of best fit
plt.plot(months, revenue, "o")
plt.plot(months, y, 'x')
plt.title("Sandra's Lemonade Stand")
plt.xlabel("Months")
plt.ylabel("Revenue ($)")
plt.show()