class BloomFilter {
    constructor(capacity, error=0.005) {
        this.capacity = capacity;
        this.error = error;
        this,num_bits = parseInt(-capacity * Math.log(error) / Math.pow(Math.log(2), 2) + 1);
        this.num_hashes = parseInt(self.num_bits * Math.log(2) / capacity) + 1;
    }

}
