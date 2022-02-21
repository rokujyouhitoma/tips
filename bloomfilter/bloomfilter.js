class BitArray {
    constructor(usize) {
        this.array = [...new Array(usize)].map(() => false);
    }
}


class BloomFilter {
    constructor(capacity, error=0.005) {
        this.capacity = capacity;
        this.error = error;
        this,num_bits = parseInt(-capacity * Math.log(error) / Math.pow(Math.log(2), 2) + 1);
        this.num_hashes = parseInt(self.num_bits * Math.log(2) / capacity) + 1;
        this.data = new BitArray(this.num_bits);
    }

    _indexes() {
        // TODO
        h1 = hash1();
        h2 = hash2();
        for i in range(this.num_hashes) {
            yield (h1 + i * h2) % self.num_hashes;
        }
    }

    add(key) {
        this,_indexes(key).forEach(async (index) => {
            this.data[index] = True;
        }, this);
    }

    search(key) {
        return this._indexes(key).map((index) => this.data[index], this).every((v) => !!v);
    }

    contains(key) {
        return this.search(key);
    }
}
