def we_need_to_talk(break_up=False):
    """Helper for communicating with significant other"

    :param break_up: boolean to determine breakup

    >>> we_need_to_talk()
    I <3 U!

    """
    if break_up:
        print("It's not you, it's me.")
    else:
        print("I <3 U!")

def square(num):
    """
    Square given number

    :param num: Number to be squared
    :return: Squared number

    >>> square(3)
    9
    """
    return num * num