var http = require('http') //modul
var url = require('url')
var filestream = require('fs')
var querystring = require('querystring')

http.createServer(function(request, response) { //buat server
        if (request.url != '/favicon.ico') {
            var access = url.parse(request.url) //menghasilkan string query, sperti informasi tentang urlnya yang berupa object
            if (access.pathname == '/') {
                var data = querystring.parse(access.query) //pecah string menjadi object ex: access.query => http://localhost:8888/?nama=rizki&umur=21
                response.writeHead(200, { "Content-Type": "text/plain" })
                response.end(JSON.stringify(data)) //convert json/object menjadi string
            } else if (access.pathname == "/form") {
                if (request.method.toUpperCase() == "POST") { //post
                    var data_post = ""
                    request.on('data', function(chunck) {
                        data_post += chunck
                    })

                    request.on('end', function() {
                        data_post = querystring.parse(data_post)
                        response.writeHead(200, { "Content-Type": "text/plain" })
                        response.end(JSON.stringify(data_post)) //convert json/object menjadi string
                    })

                } else { //get

                    response.writeHead(200, { "Content-Type": "text/html" })
                    filestream.createReadStream('../Template/form.html').pipe(response)
                }

            } else {
                response.writeHead(404, { "Content-Type": "text/plain" })
                response.end("page not found") //convert json/object menjadi
            }
        }
    }).listen(8888) //port

console.log('Server is running....')