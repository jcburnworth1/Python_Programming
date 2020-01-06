## LaunchCode
## Code for the HelloWorld Exercises
##### Chapter 1 - What is Code? Beg #####
### Your first program Beg ###
print("Hello, World!")

## Can I print a message that itself contains quote marks, such as Quoth the Raven "Nevermore"?
print('Quoth the Raven "Nevermore"')
### Your first program End ###
##### Chapter 1 - What is Code? End #####

##### Chapter 2 - Working with data Beg #####
### Printing Beg ###
print("hey!")
print("hey", "yourself!")
print("LaunchCode was founded in", 2013)
print("2 + 2 =", 2 + 2)
print("Launch" + "Code") ## String concatenation

print("LaunchCode Hubs, Circa Fall 2016:")
## Printing with markup - \n stands for newline
print("St. Louis\nMiami\nRhode Island\nKansas City")
### Printing End ###

### Values and data types Beg ###
## Types
print(type("Hello, World!")) ## String
print(type(17)) ## Integer
print("Hello, World")
print(type(3.2)) ## Float
print(type("17")) ## String
print(type("3.2")) ## String
print(type('This is a string.')) ## String
print(type("And so is this.")) ## String
print(type("""and this.""")) ## String
print(type('''and even this...''')) ## String
print('''"Oh no", she exclaimed, "Ben's bike is broken!"''') ## Fun with apostrophes and quotes

## Triple Quoting Strings
message = """This message will
span several
lines."""
print(message)
print("""This message will span
several lines
of the text.""")

## Doesn't matter what you use
print('This is a string.')
print("""And so is this.""")

## Type Conversions
print(3.14, int(3.14))
print(3.9999, int(3.9999)) ## This doesn't round to the closest int!
print(3.0, int(3.0))
print(-3.999, int(-3.999)) ## Note that the result is closer to zero
print("2345", int("2345")) ## parse a string to produce an int
print(17, int(17)) ## int even works on integers
print(int("23bottles")) ## Throws an error
print(float("123.45"))
print(type(float("123.45")))
print(str(17))
print(str(123.45))
print(type(str(123.45)))
### Values and data types End ###

### Storing data in variables Beg ###
## Establish and print a few variables
message = "What's up, Doc?"
n = 17
pi = 3.14159

print(message)
print(n)
print(pi)

## Check the variables types
print(type(message)) ## String
print(type(n)) ## Integer
print(type(pi)) ## Float
### Storing data in variables End ###

### Operators and Operands Beg ###
## Legal operators
# 20 + 32
# hour - 1
# hour * 60 + minute
# minute / 60
# 5 ** 2
# (5 + 9) * (15 - 7)

## Operators Examples
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 ** 3)
print(3 ** 2)

## Operators using variables
## Minutes to Hours
minutes = 645
hours = minutes / 60
print(hours)

## Modulus to get remainder
remainder = 7 % 3
print(remainder)
### Operators and Operands End ###

### Prompting for user input Beg ###
## Basic Function to add two numbers
first_number = 6
second_number = 7
sum = first_number + second_number
print("The sum of the two numbers is:", sum)

## User Input example
n = input("Please enter your name: ")
print("Hello", n)

## Seconds to Hours, Minutes, etc.
str_seconds = input("Please enter the number of seconds you wish to convert")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)

## Add two numbers based on user input - Python3 requires explicit type conversion
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
sum = first_number + second_number
print("The sum of the two numbers is:", sum)
### Prompting for user input End ###

### Chapter 2 Practice Beg ###
## 1.) Hello! Given a name, say hello to that person as shown in the example below:
name = input("What is your name?")
print("Hello!", name)

## 2.) Book Reviews We are going to build a “Siri” that asks users for a book title,
## then gives the user its opinion on that book. However our Siri changes its mind a lot -
## so it initially responds positively, then changes its mind. See the example below:
book = input("What's your favorite book?")
print("I love", book, "!")
print("..actually,", book, "is kind of meh. You need a better taste in books!")

## 3.) Fastforward This program calculates your ages five years in the future and prints the result.
name = input("What is your name?")
age = int(input("What is your age?"))
print("In five years,", name, "will be", int(age) + 5, "years old! Wow!")
print("In five years, {0} will be {1} years old! Wow!".format(name, age + 5))

## 4.) It’s your birthday!! Write a program that takes the name of a person and “sings” Happy Birthday to them.
lyric = "Happy Birthday to you"
middle_lyric = "Happy Birthday dear"
name = input("What is the name of the birthday person?")
print(lyric, "\n", lyric, "\n", middle_lyric, name, "\n", lyric)

## 5.) Area of a Triangle Create a program that calculates the area of a triangle and prints the result.
## Note: the area of a triangle = 1/2 * base * height.
height = input("What is the height of the triangle?")
base = input("What is the base of a triangle?")
area = .5 * float(base) * float(height)
print("Area of Triangle with base, {0}, and height, {1}: ".format(base, height), area)

## 6.) Interest Calculator Let the user calculate the amount of money they will have in the bank
## after their interest has compounded for a certain number of years. Note: A = P(1+r)^t where
## A = total amount, P = principal, r = rate, and t = time. The interest rate must be in decimal
## format (e.g. 10% in decimal format is 0.1).
principal = input("How much money do you currently have in the bank?")
rate = input("What is your interest rate?")
time = input("Over how many years is the interest compounded?")
amount = float(principal) * (1 + float(rate)) ** float(time)
print("Value of {0} in {1} years with {2} interest: ".format(principal, time, rate), amount)

## 7.) Marathon You are in the middle of a marathon, but need to be finished in time to make it to a concert
## tonight! This program asks for the number of miles you have run so far in the race, and how many hours you
## have spent running. It then tells the user how many hours it will take them to finish the marathon at their
## current pace. Note: a marathon is 26.2 miles.
current_dist = float(input("How many miles have you run so far?"))
elapsed_time = float(input("How many hours ago did you start?"))
current_pace = current_dist / elapsed_time
remaining_dist = 26.2 - current_dist
remaining_time =  remaining_dist / current_pace
print("At this rate, you have {0} hours to go. Yikes... best of luck".format(remaining_time))

## 8.) Time Traveler!! You got a new time traveler - rock on! It needs a little programming to set up.
## You must write a program asking for the current time (hours only) and an amount of hours in the future.
## Use the modulo % operator to tell the time traveler the future hour to which they will be traveling.
## Use a 24-hour clock and do not worry about AM/PM. For instance, if the current time is 20 and it is 6
## hours in the future, it would be 2.
current_time = int(input("What is the current time?"))
hour_to_travel = int(input("How many hours in the future would you like to travel?"))
future_time = current_time % hour_to_travel
print("You will be traveling to", '%02d:%02d' %(int(future_time), int("00")))
### Chapter 2 Practice End ###
##### Chapter 2 - Working with data End #####

##### Chapter 3 - Making decisions with conditionals Beg #####
### Introduction to conditionals Beg ###
## Prompt the user for a number and convert the string to an int
user_submission = input("Enter an integer: ")
user_submission = int(user_submission)

if user_submission % 2 == 0:    # user_submission is even
    print("whiz!")
else:                           # user_submission is odd
    print("bang!")
### Introduction to conditionals End ###

### Boolean values and expressions Beg ###
## Boolean types
print(True)
print(type(True))
print(type(False))

## Booleans are not strings
print(type(True))
print(type("True"))

## Operands Example
print(5 == 5)
print(5 == 6)

## Comparison Operators
# x != y               # x is not equal to y
# x > y                # x is greater than y
# x < y                # x is less than y
# x >= y               # x is greater than or equal to y
# x <= y               # x is less than or equal to y
### Boolean values and expressions End ###

### Conditional syntax Beg ###
## Basic example
x = 15

if x % 2 == 0:
    print(x, "is even")
else:
    print(x, "is odd")
### Conditional syntax End ###

### Nested conditionals Beg ###
## Even & Positive Example
user_input = input("Enter an integer:")
number = int(user_input) # user_input is a string, convert it

if number % 2 == 0:

    print("EVEN!")

    if number > 0:
        print("POSITIVE!")
### Nested conditionals End ###

### Chapter 3 practice Beg ###
## 1.) Number Fun Create a program that asks the user for a number, then tells the
## user if that number is even or if it is divisible by 5. If neither is true, do not print anything.
number = int(input("Please enter a number: "))
if number % 2 == 0:
    print("This number is even!")

if number % 5 == 0:
    print("This number is divisible by 5!")

## 2.) Mystery Validation This program only accepts certain numbers. Figure out what numbers
## the program is letting go through, and then add descriptive error messages on lines 2, 4, and
## 7 telling the user why their number does not fit the criteria.
a = int(input("Please enter a number: "))

if a < 30:
    print("Please enter a number greater than 30!")
if a > 100:
    print("Please enter a number less than 100!")
else:
    if a % 2 == 0:
        print("Please enter an odd number!")
    else:
        print("That's a great number. Thanks!")

## 3.) Are you legal? This program asks the user for their age, then outputs the things this person
## is legally able to do. As a reminder, at 16 you are allowed to drive, at 18 you are allowed to
## vote, and at 21 you are allowed to drink. If the person is under 16, your program should print: Some day, kid...
age = int(input("What is your age?"))
if age > 21:
    print("You are allowed to drink!")
if age > 18:
    print("You are allowed to vote!")
if age > 16:
    print("You are allowed to drive!")
else:
    print("Some data, kid...")

## 4.) Donut worry, be happy! The donut shop offers discounts on their surprise dozen special on
## even-numbered Sundays (for example, Sunday the 24th and not Sunday the 17th). Normally,
## donuts cost 99 cents a piece and there is no discount for buying a dozen. On even-numbered
## Sundays, you get 25% off the total price if you buy a dozen. Write a program that calculates
## the price of a dozen donuts on a given day.
day = input("What day of the week is it?")
date = int(input("What day of the month is it?"))

if day == "Sunday" and date % 2 == 0:
    print("1 Dozen Donuts:", 12 * .99 * .75)
else:
    print("1 Dozen Donuts:", 12 * .99)

## 5.) Latte Special - Starbucks is offering a new secret drink to celebrate St. Patrick’s day.
## You can only order this drink on Tuesdays during the month of March. Create a program that
## asks the user for the day, then notifies them if they can get the secret drink.
month = input("What month is it?")
day = input("What day is it?")

if month == "March" and day == "Tuesday":
    print("There is a secret drink today, in celebration of St. Patrick's Day!")
else:
    print("Sorry, this drink is only offered in March!")

## 6.) “It’s Friday, Friday...” - TGIF, finally! On Friday nights during June, the local art museum
## hosts a concert. If it is not raining, the concert will be held outside in the adjacent park.
## If it is raining, the concert will be held in the museum. Create a program that asks the user
## for the month, the day of the week, and the weather (rain or sun) then outputs whether if there
## will be a concert, and if so where it will be held. Hint: First, try creating the program without
## worrying about the weather. Then try adding the weather.
month = input("What month is it?")
day = input("What day is it?")
weather = input("Is it rainy or sunny?")

if month == "June":
    if day == "Friday":
        if weather == "sunny":
            print("There is a concert tonight! It will be held in the park.")
        else:
            print("There is a concert tonight! It will be held inside the art museum.")
    else:
        print("Sorry, concerts are only held on Fridays!")
else:
    print("Sorry, concerts are only held during June!")

## 7.) Olympics! The fun at Rio may have just ended, but the countdown is on for the Winter Olympics!
## This program takes an input year and tells the user whether that year is a year for the
## Olympics, either summer or winter.
## The general rule for the Olympic schedule is as follows: the Summer Olympics occur every four years
## on years that are divisible by four (2012, 2016, 2020...). The Winter Olympics occur on even years
##  that are not divisible by four (2010, 2014, 2018...).
year = int(input("Please input a year:"))

if year % 4 == 0:
    print("Summer Olympics!")
elif year % 4 != 0 and year % 2 == 0:
    print("Winter Olympics!")
else:
    print("Sorry, no Olympics this year.")
### Chapter 3 practice End ###
##### Chapter 3 - Making decisions with conditionals End #####

##### Chapter 4 - Repeating with loops Beg #####
### Introduction to loops Beg ###
## Example loop
for name in ["Luke", "Sheila", "Justin", "Mary", "Samantha"]:
    print("Good morning, " + name + "!")

## Example Loop 2 with list variable
coworker_names = ["Luke", "Sheila", "Justin", "Mary", "Samantha"]

for name in coworker_names:
    print("Good morning, " + name + "!")
### Introduction to loops End ###

### For loop syntax Beg ###
## Nothing of note
### For loop syntax End ###

### Loop flow Beg ###
## Nothing of note
### Loop flow End ###

### For loop examples Beg ###
## Numbers Example
for number in [1, 4, 7, 8]:
    print(number)

## String Example
for item in ["peanut butter", "chocolate chips", "pretzels"]:
    print("I need to remember to buy " + item + " at the grocery store")

## Varied Example
for thing in ["banana", 3.4, 8, 100, -1, "hello"]:
    print(thing)

## Loop with variable list
nums = [14, 15, 18, 21]

for i in nums:
    print(i)

## Loop with multiple lines in body
for num in [3, 4, 5, 6, 7]:
    print("The number is", num);
    print("The square of the number is", num**2)
### For loop examples End ###

### For-loop syntax revisited Beg ###
## Repeat Hello four times
for i in [0, 1, 2, 3]:
    print("Hello!")

for i in ["Ross", "Rachel", "Chandler", "Phoebe"]:
    print("Hello!")

## Using range - Not inclusive
print(range(4))
print(range(10))
print(range(4))
print(range(1, 5))


## Print hello four times using the range function
for i in range(4):
    print("Hello!")

## Print the iterator value
for i in range(10):
    print(i)

## Increment / Decrement Range by some value
print(range(0, 19, 2))
print(range(0, 20, 2))
print(range(10, 0, -1))
### For-loop syntax revisited End ###

### Combining loops and conditionals Beg ###
## Conditional with loop example
max_number = int(input("Print all positive even numbers less than:"))

for candidate in range(max_number + 1):
    ## test for evenness
    if candidate % 2 == 0:
        print(candidate)

## Conditional & Loop to find max
## create a list to check
numbers = [-1, 5, 17, -8, -133, 42, 6]

## keep track of the largest num found so far
largest = -1000

## Loop over list, numbers, and capture larger value
for number in numbers:
    if number > largest:
        largest = number

print("The largest number in the list", numbers,"is", largest)
### Combining loops and conditionals End ###

### Naming loop variables Beg ###
## Nothing of note
### Naming loop variables End ###

### Chapter 4 practice Beg ###
## 1.) Party Time! Let’s say we have some friends, and we’d like to send them each
## an email inviting them to our party. We don’t quite know how to send email yet,
## so for the moment we’ll just print a message for each friend.
friends = ["Elvis", "J.C.", "Mark", "Tamala", "Crystal"]

for friend in friends:
    print("Come to a party", friend)

## 2.) Loop-the-Loop Loops can be built in two ways: using a list or using the range
## function. Create a for loop using range that produces the same output as the for
## loop below (which uses a list).
# for i in [4, 8, 12, 16, 20]:
#     print(i)
for i in range(4, 21, 4):
    print(i)

## 3.) Classic Interview Problem The problem is famously used in job interviews. See
## if you can figure it out! Loop through the numbers between 1 and 20. If a number is
## divisible by 3, print Hip. If the number is divisible by 7, print “Hooray”.
numbers = range(1, 21)

for number in numbers:
    if number % 3 == 0:
        print("Hip")
    if number % 7 == 0:
        print("Hooray")

## 4.) Launch(Code) Create a program where the user inputs a number, and your program
## prints out a countdown from that number. If the user inputs a negative number,
## the program should do nothing.
start_number = int(input("Please enter a number: "))

for number in range(start_number, 0, -1):
    print(number, "...")
    if number == 1:
        print("BLAST OFF!!!")

## 5.) The Owl and the Pussycat This program should iterate through the beginning of the
## poem “The Owl and the Pussycat” and print out all words that are three letters long. List
## through the List of words below, and print out any word that has three letters. To find
## the length of a word, use the function len() as shown below.
word_list = ["the", "owl", "and", "the", "pussycat", "went", "to", "sea", "in", "a",
             "beautiful", "pea", "green", "boat", "they", "took", "some", "honey",
             "and", "plenty", "of", "money", "wrapped", "up", "in", "a", "five", "pound", "note"]

for word in word_list:
    if len(word) == 3:
        print(word)
### Chapter 4 practice End ###
##### Chapter 4 - Repeating with loops End#####