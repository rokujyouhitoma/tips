class ExDate {
    static now() {
        return Date.now();
    }
}

class Random {
    constructor() {
        this.generator = new Xorshift();
    }

    srand(seed) {
        return this.generator.srand(seed);
    }

    rand() {
        return this.generator.rand();
    }
}

//Algorithm is coming from http://www.jstatsoft.org/v08/i14/paper Xorshift.
class Xorshift {
    static MIN_VALUE = 0;
    static MAX_VALUE = 0xFFFFFFFF;

    constructor(OptDate) {
        let Date = OptDate || Date;
        this.#reset(Date.now());
    }

    srand(seed) {
        this.#reset(seed);
        return this.rand();
    }

    /* @return: 0 to 0xFFFFFFFF */
    rand() {
        let tmp = this._x ^ (this._x << 11);
        this._x = this._y >>> 0;
        this._y = this._z >>> 0;
        this._z = this._w >>> 0;
        this._w = (this._w ^ (this._w >>> 19)) ^ (tmp ^ (tmp >>> 8));
        return this._w;
    }

    #reset(seed) {
        this._x = (seed & 0x66666666) >>> 0;
        this._y = (seed ^ 0xffffffff) >>> 0;
        this._z = ((seed & 0x0000ffff << 16) | (seed >> 16) & 0x0000ffff) >>> 0;
        this._w =seed >>> 0;
        this._seed = seed >>> 0;
    }
}
