var fs = require("fs");
var express = require("express"); 
require('shelljs/global');
var multer = require('multer');
var bodyParser = require('body-parser');

var app = express();
app.use(express.static('public'));
app.use(bodyParser.urlencoded({extended :false}));

const hostname = '127.0.0.1';
const port = 8090;
var upload = multer({dest: __dirname+'/incomingImages'});

app.get('/getresult', function (req, res) {
  exec('python image_check.py > output.txt');
   fs.readFile( __dirname + "/" + "output.txt", 'utf8', function (err, data) {
       console.log( data );
       res.end( data );
   });
}); 

app.post('/getresult',upload.single('file'), function (req, res) {
console.log(req.file.name);
console.log(req.file.path);
console.log(req.file.type);
var file = __dirname+'/incomingImages/'+req.file.name;
fs.rename(req.file.path, file, function(err){
	if(err){console.log(err);
	res.send(500);
	}else{
		exec('python image_check.py ' + file+' > output.txt');
  	 fs.readFile( __dirname + "/" + "output.txt", 'utf8', function (err, data) {
       console.log( data );
       res.end( data );
   });
	}

});

});

app.get('/', function(req,res){
res.sendFile(__dirname+"/imagesub.htm");
});



app.listen(port, hostname, function(err){
   console.log("Started static tensorflow server at http://%s:%s", hostname, port)
});
