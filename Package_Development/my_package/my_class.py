## Define a minimal class with an attribute
class MyClass:
    """
    Example class

    :param value: value set to as the ``attribute`` attribute
    :ivar attribute: contains the contents of ``value`` passed in init
    """

    def __init__(self, value):
        self.atrribute = value
        self.atrribute_2 = self._test_function()

    def __repr__(self):
        return '{attribute:' + self.atrribute + '}'

    def _test_function(self):
        return 'Test 2'