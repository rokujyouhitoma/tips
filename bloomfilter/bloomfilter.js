class BloomFilter {
    constructor(capacity, error=0.005) {
        this.capacity = capacity;
        this.error = error;
        this,number_bits = -capacity * Math.log(error) / Math.log(2);
    }

}
