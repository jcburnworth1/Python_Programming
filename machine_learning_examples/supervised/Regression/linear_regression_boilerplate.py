from sklearn.linear_model import LinearRegression

your_model = LinearRegression()

your_model.fit(x_training_data, y_training_data)

## .coef_: contains the coefficients
## .intercept_: contains the intercept
## .score(): returns the coefficient of determination R²

predictions = your_model.predict(your_x_data)

