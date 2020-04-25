const { Client } = require('pg')
//sama maknanya
// const Client = require('pg').Client

const client = new Client({
    user: "sde",
    password: "47HAz123",
    host: "gis105-db.udata.id",
    port: 5432,
    database: "gis"
})

async function execute() {
    try {
        await client.connect() //bakal pause dulu, gak lanjut ke next line, kalo uda selesai baru lanjut
        console.log("Connected Successfully")
        const results = await client.query('SELECT category,insight_type,creator FROM dx_metadata_visualisation')
        console.table(results.rows)
    } catch (error) {
        console.log(`something error happend ${error}`)
    } finally {
        await client.end()
        console.log("Client disconnected Successfully")
    }
}

execute()
