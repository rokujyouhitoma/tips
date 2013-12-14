describe("require", function(){
  it("binarySearch", function(){
    var SuffixArray = require("./suffixarray").SuffixArray;
    expect(SuffixArray).toBeDefined();
  });
  it("binarySearch", function(){
    var binarySearch = require("./suffixarray").binarySearch;
    expect(binarySearch).toBeDefined();
  });
});

describe("", function(){
  var SuffixArray = null;
  beforeEach(function(){
    SuffixArray = require("./suffixarray").SuffixArray;
  });
  afterEach(function(){
    SuffixArray = null;
  });
  describe("", function(){
    it("", function(){
      var sa = new SuffixArray("abracadabra");
      //console.log(sa);
    });
    it("", function(){
      var s = "Google DriveがGoogle Docsのアップグレードで、ストレージや機能性が増えるだけなら、この移行を気にするユーザはほとんどいないだろう。この前のGmailのデザイン変更や、これまでの、いろんな製品へのGoogle+の統合は、反対意見も多かったが、DriveはDocsの真正のアップグレードと見なされている。とはいえ、前のDocsのほうが良かったと言い出すユーザが、皆無ではないだろう。";
      var sa = new SuffixArray(s);
      //console.log(sa);
    });
  });  
});

describe("", function(){
  var SuffixArray = null;
  var binarySearch = null;
  beforeEach(function(){
    SuffixArray = require("./suffixarray").SuffixArray;
    binarySearch = require("./suffixarray").binarySearch;
  });
  afterEach(function(){
    SuffixArray = null;
    binarySearch = null;
  });
  describe("", function(){
    it("", function(){
      var s = "abracadabra";
      var sa = new SuffixArray(s);
      var r = binarySearch(s, sa, "racadabra");
      //console.log(r);
      //var r = binarySearch([1,2,3,6,7,8,10], 2);
      //expect(r).toEqual(1);
    });
    it("", function(){
      var s = "Google DriveがGoogle Docsのアップグレードで、ストレージや機能性が増えるだけなら、この移行を気にするユーザはほとんどいないだろう。この前のGmailのデザイン変更や、これまでの、いろんな製品へのGoogle+の統合は、反対意見も多かったが、DriveはDocsの真正のアップグレードと見なされている。とはいえ、前のDocsのほうが良かったと言い出すユーザが、皆無ではないだろう。";
      var sa = new SuffixArray(s);
      var index = binarySearch(s, sa, "ユーザ");
      console.log(index);
      //var r = binarySearch([1,2,3,6,7,8,10], 2);
      //expect(r).toEqual(1);
    });
  });  
});
