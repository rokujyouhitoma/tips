let console = {
    "log": function(msg) {
        java.lang.System.out.println(Array.prototype.slice.call(arguments).join(" "));
    },
    "assert": function(condition) {
        // see: https://developer.mozilla.org/en-US/docs/Web/API/console/assert
        // spec: https://console.spec.whatwg.org/#assert
        if (condition) {
            return;
        }
        let message = "Assertion failed";
        let args = Array.prototype.slice.call(arguments);
        let data = [];
        if (args.length == 1) {
            data.push(message);
        } else {
            let first = args[1];
            if (typeof first !== 'string') {
                data.unshift(message);
            } else {
                let concated = `${message}: ${first}`;
                data[0] = concated;
            }
        }
        console.log(data);
    }
};


let Store = function(){
    var file = new java.io.FileReader("test.json");
    var sb = new java.lang.StringBuilder();
    while(file.read() != -1) {
        sb.append(file.read());
    }
    var contents = sb.toString();
    file.close();
    console.log(contents);
};
Store.prototype.set = function(key, value){
    var json = JSON.stringify({}, null, 2);
    var file = new java.io.FileWriter("test.json");
    file.write(json);
    file.close();
};
Store.prototype.get = function(key) {
};

console.log("Hello World! by console.log");

let test_let = "test_let";

//const test_const = "test_const";
//->throw java.lang.NullPointerException

(function() {
    // const basic support: https://mozilla.github.io/rhino/compat/engines.html#ES2015-bindings-const-basic-support
    const test_const = "test_const";
    console.log(test_const);

    // https://mozilla.github.io/rhino/compat/engines.html#ES2015-syntax-template-literals-basic-functionality
    console.log(`${test_const}`);

    console.log(new Date());
    console.log(new Date().getTime());
    console.log(`${new Date()}`);
})();

//TODO: GAS JavaScript global object
console.assert(console.log);
console.assert(true);
console.assert(false);
console.assert(false, 1);
console.assert(false, "1");

//TODO: Google Apps Script APIs
let Properties = function() {
    this.store = new Store();
};
Properties.prototype.getProperty = function(key){
    return this.store.get(key);
};
Properties.prototype.setProperty = function(key, value){
    this.store.set(key, value);
    return this;
};

//PropertiesService
//PropertiesService.getScriptProperties()
//PropertiesService.getScriptProperties().getProperty(name)
//PropertiesService.getScriptProperties().setProperty(key, value)
let PropertiesService = {
    "getScriptProperties": function(){
        // TODO
        return new Properties();
    }
};
console.assert(PropertiesService);
console.assert(PropertiesService.getScriptProperties);
console.assert(PropertiesService.getScriptProperties());
console.assert(PropertiesService.getScriptProperties().getProperty);
console.assert(PropertiesService.getScriptProperties().setProperty);
console.assert(PropertiesService.getScriptProperties().setProperty("key", "value"));

//see: https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet-app?hl=ja
/*
  class SpreadsheetApp
  class SpreadsheetApp.openById(id)
*/

//see: https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet?hl=ja
//class Spreadsheet.getSheetByName()

//see: https://developers.google.com/apps-script/reference/spreadsheet/sheet?hl=ja
//class Sheet.getRange()
//class Sheet.getLastRow()
//class Sheet.getLastColumn()

//see: https://developers.google.com/apps-script/reference/spreadsheet/range?hl=ja
//class Range.getValues()

//HtmlService
//HtmlService.createHtmlOutput

let f1 = (x) => x;

//OAuth2
//see: https://github.com/googleworkspace/apps-script-oauth2
