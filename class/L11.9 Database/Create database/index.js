var mysql = require('mysql');

var con = mysql.createConnection({
    host: "remotemysql.com", // Give your host name
    user: "Amelia", // Give your username
    password: "Honeysingh1!", // Give your password
    database: "sql6437074"
});
connection.connect((err) =>{
if(err) throw err
console.log("connected");
var sql = "CREATE TABLE Student(Student_ID INT, Student_FirstName VARCHAR(255),Student_LastName VARCHAR(255), sTUDENT_City VARCHAR(255))";
connection.query(sql,function(err,result){
    if(err) throw err;
    console.log("Tabel created in DB");
});
});









