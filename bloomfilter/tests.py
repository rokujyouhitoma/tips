import unittest

from bloomfilter import BloomFilter

class TestBloomFilter(unittest.TestCase):

    def test_bloomfilter(self):
        bloom = BloomFilter(100)
        for i in xrange(50):
            bloom.add(str(i))
        assert "20" in bloom
        assert "25" in bloom
        assert "49" in bloom
        assert "50" not in bloom


if __name__ == '__main__':
    unittest.main()
