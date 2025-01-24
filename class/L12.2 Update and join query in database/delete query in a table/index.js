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

var sql = "DELETE FROM Students WHERE Student_ID = 101";
connection.query(sql,function(err,result){
    if(err) throw err;
    console.log("Data Deleted From Tabel DB");
});
});