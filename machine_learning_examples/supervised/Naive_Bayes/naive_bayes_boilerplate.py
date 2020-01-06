from sklearn.naive_bayes import MultinomialNB

your_model = MultinomialNB()

your_model.fit(x_training_data, y_training_data)

# Returns a list of predicted classes - one prediction for every data point
predictions = your_model.predict(your_x_data)

# For every data point, returns a list of probabilities of each class
probabilities = your_model.predict_proba(your_x_data)