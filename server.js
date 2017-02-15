var fs = require("fs");//module for file system procedures - to act upon files
var express = require("express"); // node module for REST API fast creation
var app = express();
require('shelljs/global');

const hostname = '127.0.0.1';
const port = 8090;

app.get('/getresult', function (req, res) {
  exec('python image_check.py > output.txt');
   fs.readFile( __dirname + "/" + "output.txt", 'utf8', function (err, data) {
       console.log( data );
       res.end( data );
   });
});





app.listen(port, hostname, function(err){
   console.log("Started static resource server at http://%s:%s", hostname, port)
});
