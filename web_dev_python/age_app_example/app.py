__author__ = 'jcb'


def age_program():
    user_age = input("Enter your age:")
    age_seconds = int(user_age) * 365 * 24 * 60 * 60
    print("Your age in seconds is {}".format(age_seconds))

if __name__ == '__main__':
    age_program()