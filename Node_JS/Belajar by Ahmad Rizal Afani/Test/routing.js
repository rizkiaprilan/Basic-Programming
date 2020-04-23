var http = require('http') //modul
var url = require('url') //modul
var routes = require('routes')() //modul dan class

routes.addRoute('/', function(req, res) {
    res.writeHead(200, { 'content-type': 'text/html' })
    res.end('home page')
})
routes.addRoute('/profile/:nama?/:kota?', function(req, res) { //:nama =>parameter wajib, :nama? => optional parameter
    res.writeHead(200, { 'content-type': 'text/html' })
    res.end('profile page ===> ' + this.params.nama + ' dari ' + this.params.kota)
})

routes.addRoute('/contact', function(req, res) { //:nama =>parameter wajib, :nama? => optional parameter
    res.writeHead(200, { 'content-type': 'text/html' })
    res.end('Contact page')
})
http.createServer(function(req, res) { //buat server
        var path = url.parse(req.url).pathname //ambil pathnya
        var match = routes.match(path) //check apa sudah terdaftar routenya
        if (match) {
            match.fn(req, res) //tampilkan isi dari route
        } else {
            res.writeHead(404, { 'content-type': 'text/html' }) //jika tidak sesuai route maka not found
            res.end('page not found')
        }
    }).listen(8888) //port

console.log('Server is running....')