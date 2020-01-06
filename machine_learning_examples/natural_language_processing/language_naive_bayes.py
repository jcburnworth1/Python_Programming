# from reviews import counter, training_counts
import pickle
counter = pickle.load( open( "Python_Programming/machine_learning_examples/natural_language_processing/count_vect.p", "rb" ) )
training_counts =  pickle.load( open( "Python_Programming/machine_learning_examples/natural_language_processing/count_vect.p", "rb" ))

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Add your review:
review = "this was amazing"
review_counts = counter.transform([review])

classifier = MultinomialNB()
training_labels = [0] * 1000 + [1] * 1000

classifier.fit(training_counts, training_labels)

neg = (classifier.predict_proba(review_counts)[0][0] * 100).round()
pos = (classifier.predict_proba(review_counts)[0][1] * 100).round()

if pos > 50:
    print("Thank you for your positive review!")
elif neg > 50:
    print("We're sorry this hasn't been the best possible lesson for you! We're always looking to improve.")
else:
    print("Naive Bayes cannot determine if this is negative or positive. Thank you or we're sorry?")

print(
    "\nAccording to our trained Naive Bayes classifier, the probability that your review was negative was {0}% and the probability it was positive was {1}%.".format(
        neg, pos))