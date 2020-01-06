#  ---------------------- Hello -------------------------
# INSTRUCTIONS
# In this program, you must ask the user:
#	"What is your name?"
# And then respond by printing out a personalized greeting.
# GENERAL RULE
# For a person named Maria, respond by printing:
#	Hello Maria :)
# For a person named Wally, respond by printing:
#	Hello Wally :)
# ...etc.
# In general, for a person named <NAME>, respond by printing:
#	Hello <NAME>
# SPECIAL NAMES
# Two people are special: Amar and Brandy.
# A person named Amar or Brandy should receive an additional comment after you say hello
# For a person named Amar, respond by saying:
#	Hello Amar :)
#	I like your shoes
# For a person named Brandy, respond by saying:
#	Hello Brandy :)
#	You seem like a cool person
# Note that the robot grader will only mark your solution correct if your
# print statements match EXACTLY what was specified above.
#	Spelling, spacing, punctuation... all that stuff matters.
#	Your input statement also matters. You must say it exactly like this:
#		What is your name?
# --------------------------------------------------------------------
# Put your Python code here:
## Capture name input
name = input("What is your name? ")

## Logic for what to output
if name.lower() == "amar":
    print("Hello {0} :)".format(name.title()))
    print("I like your shoes")
elif name.lower() == "brandy":
    print("Hello {0} :)".format(name.title()))
    print("You seem like a cool person")
else:
    print("Hello {0}".format(name.title()))