# -*- coding:utf-8 -*-
def cantorParingFunction(x, y):
    """
    @see http://en.wikipedia.org/wiki/Pairing_function
    >>> cantorParingFunction(0,0)
    0
    >>> cantorParingFunction(1,0)
    1
    >>> cantorParingFunction(0,1)
    2
    >>> cantorParingFunction(2,0)
    3
    """
    z = ((x + y) * (x + y + 1) / 2) + y
    return z

if __name__ == "__main__":
    import doctest
    doctest.testmod()
