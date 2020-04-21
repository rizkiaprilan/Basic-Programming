var http = require('http') //modul
var filestream = require('fs')

http.createServer(function(request, response) { //buat server
        var statuscode = 0
        var file = ""
        if (request.url == '/') {
            statuscode = 200
            file = '../Template/index.html'
        } else if (request.url == '/contact') {
            statuscode = 200
            file = '../Template/contact.html'
        } else {
            statuscode = 400
            file = '../Template/404.html'
        }
        response.writeHead(statuscode, { "Content-Type": "text/html" }) //contentnya dalam bentuk html
        filestream.createReadStream(file).pipe(response) //untuk baca html dll, pipe itu dia mau response

    }).listen(8888) //port

console.log('Server is running....')