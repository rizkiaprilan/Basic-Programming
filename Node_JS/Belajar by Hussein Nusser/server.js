const { Client } = require('pg')
//sama maknanya
// const Client = require('pg').Client
const express = require('express')
const path = require('path');
const app = express()
const port = 8080

app.use(express.json())  //parse ke json
app.use(express.urlencoded({ extended: false })) //query string biar ga bisa di inject

const client = new Client({
    user: "sde",
    password: "47HAz123",
    host: "gis105-db.udata.id",
    port: 5432,
    database: "gis"
})

start()

app.get('/',(req,res)=> res.sendFile(path.resolve(`${__dirname}/views/home.html`))) //__dirname -> untuk path yang lokasi skrg

app.get("/employees", async (req, res) => {
    const results = await readEmployees()
    // res.writeHead(200,{
    //     "Content-Type": "application/json"
    // }).end(JSON.stringify(results))

    //OR

    res.setHeader("Content-Type", "application/json")
    res.send(JSON.stringify(results.rows)) //JSON.stringify -> convert object to json string
})

app.post("/employees", async (req, res) => {
    let result = {}
    try {
        const reqJson = req.body
        await createEmployees([reqJson.name, reqJson.activity])
        result.success = true
    } catch (error) {
        result.success = false
    } finally {
        res.setHeader("Content-Type", "application/json")
        res.status(200).send(JSON.stringify(result)) //JSON.stringify -> convert object to json string
    }
})

app.delete("/employees/:id", async (req, res) => {
    let result = {}
    try {
        // req.setHeader("Content-Type", "application/json")
        const reqJson = req.params.id
        await deleteEmployees(reqJson)
        result.deleted = "DELETED"
    } catch (error) {
        result.deleted = "FAILED"
    } finally {
        res.setHeader("Content-Type", "application/json")
        res.send(JSON.stringify(result)) //JSON.stringify -> convert object to json string
    }
})

app.put("/employees/:id", async (req, res) => {
    let result = {}
    try {
        // req.setHeader("Content-Type", "application/json")
        const id = req.params.id
        const content = req.body
        await updateEmployees(id,content)
        result.update = "UPDATED"
    } catch (error) {
        result.update = "FAILED"
    } finally {
        res.setHeader("Content-Type", "application/json")
        res.send(JSON.stringify(result)) //JSON.stringify -> convert object to json string
    }
})


app.listen(port, () => console.log(`web server is listening on port ${port}`))


async function start() {
    await connect()
    // const employees = await readEmployees()
    // console.log(employees)

    // const successCreate = await createEmployees(["jamet","lagi joget"])
    // console.log(`Creating was ${successCreate}`)

    // const successDelete = await deleteEmployees(1)
    // console.log(`deleting was ${successDelete}`)
}

async function connect() {
    try {
        await client.connect()
        console.log('success connect to database')
    } catch (error) {
        console.log(`error : ${error}`)
    }
}

async function readEmployees() {
    try {
        return await client.query("SELECT * FROM employees")
        // return result.rows // mengembalikan menjadi object per row

    } catch (error) {
        // return []
    }
}
async function createEmployees(employees) {
    try {
        await client.query("INSERT INTO employees (name,activity) VALUES($1,$2)", employees)
        // return true

    } catch (error) {
        // return false
    }
}
async function deleteEmployees(id) {
    try {
        await client.query("DELETE FROM employees WHERE id = $1", [id])
        return true

    } catch (error) {
        return false
    }
}
async function updateEmployees(id,body) {
    try {
        await client.query(`UPDATE employees SET name = '${body.name}', activity = '${body.activity}' WHERE id = '${id}'`)
        return true

    } catch (error) {
        return false
    }
}

