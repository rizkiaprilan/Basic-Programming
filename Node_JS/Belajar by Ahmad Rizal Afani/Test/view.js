var http = require('http') //modul
var url = require('url') //modul
var routes = require('routes')() //modul dan class
var handlebars = require('handlebars') //modul dan class
var filestream = require('fs')

routes.addRoute('/', function(req, res) {
    filestream.readFile('../Template/index.html', function(err, data) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
    });
})
routes.addRoute('/contact', function(req, res) {
    filestream.readFile('../Template/contact.html', function(err, data) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
    });
})
routes.addRoute('/form', function(req, res) {
    filestream.readFile('../Template/form.html', function(err, data) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
    });
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