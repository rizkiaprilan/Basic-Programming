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

execute()
async function execute() {
    try {
        await client.connect() //bakal pause dulu, gak lanjut ke next line, kalo uda selesai baru lanjut
        console.log("Connected Successfully")
        await client.query('BEGIN')
        await client.query('INSERT INTO employees(name,activity) VALUES($1,$2)',['rizki',"makan nasi"])
        
        const {rows} =  await client.query('SELECT * FROM employees')
        console.table(rows)
        console.log("Inserted")
        await client.query('COMMIT') //harus di commit dulu klo mau ada perubahan
    } catch (error) {
        console.log(`something error happend ${error}`)
        await client.query('ROLLBACK') //klo terjadi kesalahan bisa di rollack
    } finally {
        await client.end()
        console.log("Client disconnected Successfully")
    }
}

