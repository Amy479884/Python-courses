var mysql = require('mysql');

var con = mysql.createConnection({
    host: "remotemysql.com", // Give your host name
    user: "Amelia", // Give your username
    password: "Honeysingh1!", // Give your password
});

con.connect(function(err) {
    if (err) throw err;
    console.log("Connected");
});



