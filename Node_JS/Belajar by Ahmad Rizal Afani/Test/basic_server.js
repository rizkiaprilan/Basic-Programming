var http = require('http') //modul

http.createServer(function(request, response) { //buat server
        if (request.url != '/favicon.ico') { //untuk menghilangkan url request /favicon.ico, itu ada lah gambar icon html
            // console.log(request.url) //untuk melihat url request yang masuk
            response.writeHead(200, { "Content-Type": "text/html" }) //contentnya dalam bentuk html
                // response.write("hello world") //write in html
            response.write("url request :" + request.url) //write into html
            response.end() //akhiri response
        }

    }).listen(8888) //port

console.log('Server is running....')