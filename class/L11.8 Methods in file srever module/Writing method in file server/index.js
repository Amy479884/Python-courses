var fs = require('fs');

//create a file named mynewfile3.txt:

fs.writeFile('Amelia.txt', 'Welcome!!', function (err) {
    if (err) throw err;
    console.log('Content changed!')
});
