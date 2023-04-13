let console = {
    "log": (msg) => { java.lang.System.out.println(msg); }
};

print("Hello World! by print");
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
//console.log()

//TODO: Google Apps Script APIs
//PropertiesService
//PropertiesService.getScriptProperties()
//PropertiesService.getScriptProperties().getProperty(name)
//PropertiesService.getScriptProperties().setProperty(key, value)

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

console.log(Object.keys);
let f1 = (x) => x;

//OAuth2
//see: https://github.com/googleworkspace/apps-script-oauth2
