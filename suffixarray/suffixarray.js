var SuffixArray = function(str) {
  var sa = [];
  var i;
  var l = str.length;
  for (i = 0; i < l; ++i) {
    sa.push(i);
  }
  sa.sort(function(a, b) {
    return str.substr(a) < str.substr(b) ? -1 : 1;
  });
  return sa;
};

exports.SuffixArray = SuffixArray;

function binarySearch(str, sa, key){
  var low = 0;
  var high = sa.length - 1;
  var mid;
  while(low <= high) {
    mid = Math.floor((low + high) / 2);
    var val = str.substr(sa[mid], key.length);
    //console.log("(mid, key, val): " + mid + ", " + key + ", " + val);
    if(val === key) {
      return mid;
    } else if(val < key) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return null;
}

exports.binarySearch = binarySearch;