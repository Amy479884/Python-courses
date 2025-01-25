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

var sql = "UPDATE Students SET Student_City='Mumbai' WHERE Student_ID = 102";
connection.query(sql, function (err, result) {
    if (err) throw err;
    console.log("Data Updated in Table");
});
});