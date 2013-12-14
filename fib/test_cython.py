import unittest
import pyximport
pyximport.install()
import fib
import test


class TestFib(test.TestFib):
    pass

if __name__ == '__main__':
    unittest.main()
