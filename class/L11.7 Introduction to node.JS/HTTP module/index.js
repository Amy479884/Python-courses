var http = require('http')

//ceate a serevr object:
http.createServer(function (req, res) {
    res.write('This is my first Node.js project');
    //write a response to the client
    res.end(); // end the response
}).listen(8080); //the server object listens to port 8080