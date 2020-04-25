// const express = require('express')
import express from "express"
const body_parser = require('body-parser')  //conver ke json nya
const todos = require('./routes/todoRoutes') //route nya di inisialisasi
const mongoose = require('mongoose')
const app = express()
const port = 1234

let mongourl = "mongodb://localhost:27017/todoapi"  //todoapi nama database
const mongoDB = mongourl

mongoose.connect(mongoDB)  //connect
mongoose.Promise = global.Promise  //permission
const db = mongoose.connection
db.on('error', console.error.bind(console, "connection error, please check correcly!"))


app.use(body_parser.json())  //convert ke json nya
app.use(body_parser.urlencoded({ extended: false })) //biar ga bisa di inject
app.use('/api', todos)   //berarti bakal jadi localhost:1234/api/<route>


app.listen(port, () => console.log(`localhost running di port ${port}`))
