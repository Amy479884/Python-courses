var mysql = require("mysql");

var connection = mysql.createConnection({

    host: "sql12.freesqldatabase.com",

    user: "sql12758131",

    password: "rEhwYw1qJC",

    database: "sql12758131"

});

connection.connector((err) => {

    if (err) throw err

    console.log("connected");

    connection.query("SELECT Student_FirstName, Student_LastName FROM Student WHERE Student_FirstName = 'Dharani'" , function(err,result,fields){
        if(err) throw err;
        console.log(result);
    });
});