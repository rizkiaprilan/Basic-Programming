const mongoose = require('mongoose')  //panggil library/dependency

const schema = mongoose.Schema  //panggil fungsi schema

let todoSchema = schema({
    name: {type : String},
    activity: {type : String},
    done: {type: Boolean}
})

module.exports = mongoose.model("Todos",todoSchema)  //Todos nama collection