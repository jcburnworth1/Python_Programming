## Import libraries
from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

## Import scikit-learn emails dataset
emails = fetch_20newsgroups(categories=['rec.sport.baseball', 'rec.sport.hockey'])

## Print target names
print(emails.target_names)

## Print email 1 for visual purposes
print(emails.data[0])
print(emails.data[1])

## Determine which target describe which target_names
## 0 = baseball, 1 = hockey
print(emails.target[0])
print(emails.target[1])

## Split data to train and test
train_emails = fetch_20newsgroups(categories = ['rec.sport.baseball', 'rec.sport.hockey'], subset = 'train',
                                  shuffle=True, random_state=108)

test_emails = fetch_20newsgroups(categories = ['rec.sport.baseball', 'rec.sport.hockey'], subset = 'test',
                                  shuffle=True, random_state=108)

## Create CountVectorizer to count up words in the emails
counter = CountVectorizer()

counter.fit(train_emails.data + test_emails.data)

## Transform the data into counts
train_counts = counter.transform(train_emails.data)
test_counts = counter.transform(test_emails.data)

## Create our Naive Bayes classifier
classifier = MultinomialNB()

classifier.fit(train_counts, train_emails.target)

## Print classifier score
print(classifier.score(test_counts, test_emails.target))