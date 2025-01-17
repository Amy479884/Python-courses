var mysql = require("mysql");

var connection = mysql.createConnection({
    host: "sql12.freesqldatabase.com",
    user: "sql12758131",
    password: "",
    database: "sql12758131"
});
connection.connector((err)=>{
    if(err) throw err
    console.log("connected");

    var sql = "ALTER TABEL Students ADD Student_Grade INT";
    connection.query(sql,function(err, result){
        if(err) throw err;
        console.log("Tabel Altered DB");
    });
});