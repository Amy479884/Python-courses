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

    var sql = "INSERT INTO Students(Student_ID, Student_FirstName, Student_LastName, Student_City, Student_Grade) VALUES(1, 'Amelia', 'Singh', 'Bangalore', '12')";

    var sql = "INSERT INTO Students(Student_ID, Student_FirstName, Student_LastName, Student_City, Student_Grade) VALUES(1, 'Rahul', 'Malhotra', 'Delhi', '6')";

    var sql = "INSERT INTO Students(Student_ID, Student_FirstName, Student_LastName, Student_City, Student_Grade) VALUES(1, 'Aryan', 'Khan', 'Mumbai', '8')";

    var sql = "INSERT INTO Students(Student_ID, Student_FirstName, Student_LastName, Student_City, Student_Grade) VALUES(1, 'Pavan', 'Kumar', 'Kanpur', '11')";
    connection.query(sql, function (err, result) {
        if (err) throw err;
        console.log("Data inserted in DB")
    });
});