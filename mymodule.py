""" This is a python module. It can be used to store python functions and other objects """

number = 4


def addOne(number):
    """
        example function to show how functions can be passed into each other

        Parameters
            number:int
            number to incerease by one
    """
    return number + 1


def subtractOne(number):
    """
        example function to show how functions can be passed into each other

        Parameters
            number:int
            number to decerease by one
    """
    return number - 1


if __name__ == '__main__':
    """this part will only get run if the 'mymodule.py' file is call directly. Sometimes it can be
       useful to put some test of the functions down here"""
    print('addOne(1) = ', addOne(1))
    print('subtractOne(1) = ', subtractOne(1))
