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

    var sql = "INSERT INTRO Students(Student_ID, Student_FirstName,Student_LastName,Student_City,Student_Grade) VALUES ?";
    var values = [
        [101,'Teena', 'Raj', 'Mumbai','12'],
        [103,'Simran','Rohan', 'Bangalore','11'],
        [107,'Rahul', 'Malhotra','Chennai','13'],
        [109, 'Anjali','Smith','Dehradun','10'],
        [102, 'Kajol', 'Gupta','Hyderbad', '9']
    ];
    connection.query(sql,[values],function(err,result){
        if(err) throw err;
        console.log("Multiple Data inserted in DB");
    });
});