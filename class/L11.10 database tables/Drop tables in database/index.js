var mysql = require("mysql");

var connection = mysql.creatorConnection({
    host:"sql12.freesqldatabase.com",
    user:"sql12758131",
    password:"",
    database:"sql12758131"
});
connection.connect((err)=>{
    if(err) throw err;
    console.log("connected");

    var sql = "DROP TABEL Student";
    connection.query(sql,function(err,result){
        if(err) throw err;
        console.log("Table Dropped DB");
    });
});
