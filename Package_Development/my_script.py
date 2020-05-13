##### Playing with packages #####
## Direct import
import Python_Programming.Package_Development.my_package.utils as utils
utils.we_need_to_talk()

## Relative from __init__.py
import Python_Programming.Package_Development.my_package as mp
mp.we_need_to_talk()

## Class import and instance of class
my_instance = mp.MyClass('Test')

##### doctest example #####
def square(num):
    """
    Square given number

    :param num: Number to be squared
    :return: Squared number

    >>> square(3)
    9
    """
    return num * num

import doctest
doctest.testmod()

## Look into
# Sphinx
# Travis CI
# Codecov
# Code Climate
