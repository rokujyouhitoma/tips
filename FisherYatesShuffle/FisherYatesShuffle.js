
var FisherYatesShuffle = function(array){
    // Fisher–Yates shuffle
    var result = array.slice();
    for(var i = array.length - 1; 0 < i; i--){
        var r = Math.floor(Math.random() * (i + 1));
        var tmp = result[i];
        result[i] = result[r];
        result[r] = tmp;
    }
    return result;
};
