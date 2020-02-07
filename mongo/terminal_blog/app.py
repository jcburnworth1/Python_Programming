## Import libraries
import pymongo

## Connect to local mongoDB
uri = "mongodb://127.0.0.1:27017"

## Initilized mongoDB client
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']
students = collection.find({})

## Print students with for loop
# for student in students:
#     print(student)

## Add students to list with list comprehension
students = [student for student in collection.find({})]
students_marks = [student['mark'] for student in collection.find({})]
print(students)
print(students_marks)