# -*- coding:utf-8 -*-
import math

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
    >>> cantorParingFunction(1,1)
    4
    >>> cantorParingFunction(0,2)
    5
    >>> cantorParingFunction(2,1)
    7
    """
    z = ((x + y) * (x + y + 1) / 2) + y
    return z

def invertedCantorParingFunction(z):
    """
    @see http://en.wikipedia.org/wiki/Pairing_function
    >>> invertedCantorParingFunction(0)
    (0, 0)
    >>> invertedCantorParingFunction(1)
    (1, 0)
    >>> invertedCantorParingFunction(2)
    (0, 1)
    >>> invertedCantorParingFunction(3)
    (2, 0)
    >>> invertedCantorParingFunction(4)
    (1, 1)
    """
    w = int(math.floor((math.sqrt(8*z + 1) - 1) / 2))
    t = (w**2 + w) / 2
    y = z - t
    x = w - y
    return (x,y)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
