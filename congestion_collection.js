var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/actual_raod";	
var requestURL ="https://traffic.longdo.com/api/json/traffic/index?callback=callback_function";
var request = new JSONHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();

function callback_function(){

	var MongoClient = require('mongodb').MongoClient;
	var url = "mongodb://localhost:27017/actual_raod";
	
	MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var output = request.response;
  db.collection("congestion").insertOne(output, function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
});
	
}