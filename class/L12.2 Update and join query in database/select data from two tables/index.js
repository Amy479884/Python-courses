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

connection.query("SELECT Student_Detail.FirstName, Student_Height.Height FROM Students_Detail JOIN Student_Height ON Students_Detail.Reg_ID = Student_Height.Reg_ID", function(err,result,fields)
{
    if(err) throw err;
    console.log("Selected from Tables");
});
});