## Gradebook Project - CodeAcademy
## Last Semester's Grades
last_semester_gradebook = [("politics", 80),
                           ("latin", 96),
                           ("dance", 97),
                           ("architecture", 65)]

## Current Semester Subjects
subjects = ["physics",
            "calculus",
            "poetry",
            "history"]

## Current Semester Grades
grades = [98, 97, 85, 88]

## Append Computer Science subject & grade
subjects.append("computer science")
grades.append(100)

## Combine subjects & grades
gradebook = list(zip(subjects, grades))

## Append visual arts to gradebook
gradebook.append(("visual arts", 93))

## Print gradebook
print(gradebook)

## Create the full gradebook
full_gradebook = last_semester_gradebook + gradebook

## Print out full gradebook
print(full_gradebook)