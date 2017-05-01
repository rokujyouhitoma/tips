var Random = function(opt_generator) {
    this.generator = opt_generator || new Xorshift();
};
 
Random.prototype.srand = function(seed) {
    return this.generator.srand(seed);
};
 
Random.prototype.rand = function() {
    return this.generator.rand();
};
 
exports.Random = Random;
 
//Algorithm is coming from http://www.jstatsoft.org/v08/i14/paper Xorshift.                                                                                                          
var Xorshift = function() {
    this._reset(Date.now());
};
 
Xorshift.prototype.srand = function(seed){
    this._reset(seed);
};
 
Xorshift.prototype.rand = function() {
    var tmp = this._x ^ (this._x << 11);
    this._x = this._y >>> 0;
    this._y = this._z >>> 0;
    this._z = this._w >>> 0;
    this._w = (this._w ^ (this._w >>> 19)) ^ (tmp ^ (tmp >>> 8));
    return this._w; /* 0 to 0xFFFFFFFF */
};
 
Xorshift.prototype.calcProbability = function(prob) {
    var dice = (this.rand() % 100);
    return (dice < prob);
};
 
Xorshift.prototype._reset = function(seed) {
    this._x = (seed & 0x66666666) >>> 0;
    this._y = (seed ^ 0xffffffff) >>> 0;
    this._z = ((seed & 0x0000ffff << 16) | (seed >> 16) & 0x0000ffff) >>> 0;
    this._w =seed >>> 0;
    this._seed = seed >>> 0;
};
