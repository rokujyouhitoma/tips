import unittest
import fib


class TestFib(unittest.TestCase):
    def setup(self):
        pass

    def test_fib(self):
        self.assertEqual(0, fib.fib(0))
        self.assertEqual(1, fib.fib(1))
        self.assertEqual(1, fib.fib(2))
        self.assertEqual(2, fib.fib(3))
        self.assertEqual(3, fib.fib(4))
        self.assertEqual(55, fib.fib(10))

if __name__ == '__main__':
    unittest.main()
