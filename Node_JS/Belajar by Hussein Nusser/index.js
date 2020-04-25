const {Client} = require('pg')
//sama maknanya
// const Client = require('pg').Client

const client = new Client({
    user: "sde",
    password : "47HAz123",
    host: "gis105-db.udata.id",
    port: 5432,
    database: "gis"
})

client.connect()
.then(()=>console.log("Connected Succesfully")) //jika benar, catch finally tidak dijalankan
.then(()=>client.query('SELECT category,insight_type,creator FROM dx_metadata_visualisation where category = $1 and creator = $2 limit 10',['WFH','Wina']))
.then(results => console.table(results.rows)) //buat nampilin data di console dengan visualisasipip
.catch((error)=> console.log(error))  //kalo error
.finally(()=>client.end()) //maka lakukan ini 
