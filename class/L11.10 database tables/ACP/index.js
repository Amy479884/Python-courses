var mysql = require("mysql");

var connection = mysql.createConnection({
    host: "sql12.freesqldatabase.com",
    user: "sql12758131",
    password: "",
    database: "sql12758131"
});
connection.connector((err) => {
    if (err) throw err
    console.log("connected");

    var sql = "INSERT INTO Students(Student_ID, Student_FirstName, Student_LastName, Student_City, Student_Grade, Student_favcar, Student_favcolor) VALUES(1, 'Crystal', 'Singh', 'Mumbai', '12', 'Ferraie', 'red' )";
    connection.query(sql, function (err, result) {
        if (err) throw err;
        console.log("Data inserted in DB")
    });
});