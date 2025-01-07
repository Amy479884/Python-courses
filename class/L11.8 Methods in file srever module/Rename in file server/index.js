var fs = require('fs');

//Rename the file "mynewfile1.txt" into "myrenamedfile.txt":

fs.rename('crystal.txt', 'Amelia.txt', function (err) {
    if (err) throw err;
    console.log('File renamed successfully!');
});
