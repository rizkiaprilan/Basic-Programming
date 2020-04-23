const express = require('express')
const body_parser = require('body-parser') //middleware / software tambahan (input http request ke dalam express)
const app = express() //buat object express nya
const port = 8080

const MongoClient = require('mongodb').MongoClient
const ObjectId = require('mongodb').ObjectID
const DBurl = `mongodb://127.0.0.1:27017/`
const DBname = "arkademy"

let dbo = null
MongoClient.connect(DBurl, (error, result) => { //koneksinya
    if (error) throw error //error diarahkan ke node js/ke terminal

    dbo = result.db(DBname)
})

//BASIC
// app.get('/',(req,res) => res.send('hello world')).listen(port,() => console.log(`Server is running at http://localhost:${port}`))

app.use(body_parser.urlencoded({ extended: false }))

app.get('/mahasiswa', (request, response) => {
    // res.send('HELLO GUYS')  //kaya nge write di web
    //res.end("hello")  //loading web di akhri
    dbo.collection("mahasiswa").find().toArray((err, res) => { //ubah ke array dulu
        if (err) throw err  //jika ada error
        response.json(res)
    })
})

app.get('/siswa', (req, res) => {
    // res.json({ name: 'rizki' })
})

app.get('/mahasiswa/:id', (request, response) => {
    let id_mahasiswa = request.params.id
    // console.log(`nama saya adalah ${nama}`)
    let id_object = new ObjectId(id_mahasiswa)
    dbo.collection("mahasiswa").findOne({ "_id": id_object }, (err, res) => {
        if (err) throw err
        response.json(res)
    })
    // res.json({ name: nama })

})

app.post('/mahasiswa', (request, response) => {   //buka postman, ganti method post > body > x-www-form-urlencoded
    let namaMahasiswa = request.body.nama           //dari body/dari form yang encytype = application/x-www-form-urlencoded
    let alamatMahasiswa = request.body.alamat
    let umurMahasiswa = request.body.umur

    dbo.collection("mahasiswa").insertOne({
        nama: namaMahasiswa,
        umur: umurMahasiswa,
        alamat: alamatMahasiswa
    }, (err, res) => {
        if (!err) {
            response.json(res)
        } else {
            throw err
        }
    })
    // res.json({
    //     nama: namaSiswa,
    //     alamat: alamatSiswa
    // })
})

app.put('/mahasiswa/:id', (request, response) => {   //buka postman, ganti method post > body > x-www-form-urlencoded
    // let id = req.params.id           //dari body/dari form yang encytype = application/x-www-form-urlencoded
    let id_object = new ObjectId(request.params.id)
    let namaMahasiswa = request.body.nama           //dari body/dari form yang encytype = application/x-www-form-urlencoded
    let alamatMahasiswa = request.body.alamat
    let umurMahasiswa = request.body.umur

    dbo.collection("mahasiswa").updateOne({ "_id": id_object }, {
        $set    : {  //atomic operator
            "nama": namaMahasiswa,
            "alamat": alamatMahasiswa,
            "umur": umurMahasiswa
        }
    }, (err, res) => {
        if (!err) {
            response.status(200).json(res)
        } else {
            if (err) throw err
            response.status(500).json({
                "error": "cannot update",
                "message": err
            })
        }
    })
    // res.json({
    //     id: id,
    //     nama: namaSiswa,
    //     alamat: alamatSiswa
    // })
})


app.delete('/mahasiswa/:id', (request, response) => {
    let id_mahasiswa = request.params.id
    let id_object = new ObjectId(id_mahasiswa)
    dbo.collection("mahasiswa").deleteOne({ "_id": id_object }, (err, res) => {
        if (err) throw err
        response.json(res)
    })

    // console.log(`nama sudah di delete adalah ${nama}`)
    // res.json({ name: nama })
})

app.listen(port, () => console.log(`Server is running at http://localhost:${port}`))