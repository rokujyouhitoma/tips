# Ref: http://shop.oreilly.com/product/0636920028963.do
# Ref: http://d.hatena.ne.jp/nishiohirokazu/20080213/1202912207

import bitarray
import math
import mmh3

class BloomFilter(object):
    def __init__(self, capacity, error=0.005):
        """
        Initialize a Bloom filter with given capacity and false positive rate
        """
        self.capacity = capacity
        self.error = error
        self.num_bits = int(-capacity * math.log(error) / math.log(2)**2) + 1
        self.num_hashes = int(self.num_bits * math.log(2) / float(capacity)) + 1
        self.data = bitarray.bitarray(self.num_bits)

    def _indexes(self, key):
        h1, h2 = mmh3.hash64(key)
        for i in xrange(self.num_hashes):
            yield (h1 + i * h2) % self.num_bits

    def add(self, key):
        for index in self._indexes(key):
            self.data[index] = True

    def search(self, key):
        return all(self.data[index] for index in self._indexes(key))

    def __contains__(self, key):
        return self.search(key)

    def __len__(self):
        num_bits_on = self.data.count(True)
        return -1.0 * self.num_bits * math.log(1.0 - num_bits_on / float(self.num_bits)) / float(self.num_hashes)

    @staticmethod
    def union(bloom_a, bloom_b):
        assert bloom_a.capacity == bloom_b.capacity, "Capacities must be equal"
        assert bloom_a.error == bloom_b.error, "Error rates must be equal"
        bloom_union = BloomFilter(bloom_a.capacity, bloom_a.error)
        bloom_union.data = bloom_a.data | bloom_b.data
        return bloom_union
