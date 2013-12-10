#!-*- coding:utf-8 -*-
"""
Floyd's cycle-finding algorithm
http://en.wikipedia.org/wiki/Cycle_detection
http://www.siafoo.net/algorithm/10
"""

def floyd(top):
    """
    >>> floyd([1,2,3,4])
    False
    >>> floyd([1,2,1,2,1])
    True
    >>> floyd([1,2,3,1,2,3,1])
    True
    >>> floyd([1,2,3,1,2,3,1,2,3,1])
    True
    >>> floyd(["A","B","A","B","A"])
    True
    """
    tortoise = top
    hare = top
    while True:
        # Is Hare at End?
        if not hare[1:]:
            return False # NO LOOP
        hare = hare[1:] # Increment hare
        # Is Hare at End?
        if not hare[1:]:
            return False # NO LOOP
        hare = hare[1:] # Increment Hare Again

        tortoise = tortoise[1:]

        # Did Hare Meet Tortoise?
        if hare[0] == tortoise[0]:
            return True # LOOP!

if __name__ == "__main__":
    import doctest
    doctest.testmod()
